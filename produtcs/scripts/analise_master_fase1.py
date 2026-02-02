#!/usr/bin/env python3
"""
Fase 1 — Análise do master 20260130.
Classifica cada produto (linha pai) em categorias para o plano de ajustes.
Gera contagens e listas por grupo.
"""
import csv
import os
import sys

# Colunas: product_id=0, variation_id=2, name=4, description=13, short_description=14
IDX_PRODUCT_ID = 0
IDX_VARIATION_ID = 2
IDX_NAME = 4
IDX_DESCRIPTION = 13
IDX_SHORT_DESC = 14

# Categorias (prioridade: a primeira que bater ganha)
CAT_PLACEHOLDER = "placeholder"           # desc começa com "- Para decorar e festejar"
CAT_SILVER_ANTIGO = "vela_silver_antigo" # vela com nome/desc Silver Festas, sem ✨
CAT_PRATO_AJUSTAR = "prato_ajustar"      # Prato Papel (sem "de") ou "– -" no nome
CAT_BOLEIRA_H3 = "boleira_h3"            # desc com <h3>Benefícios</h3>, sem ✨
CAT_PADRAO_NOVO = "padrao_novo"          # desc tem ✨ Descrição completa (OK)
CAT_OUTROS = "outros"                    # não classificado acima


def classify(name: str, description: str) -> str:
    """Retorna uma única categoria por produto (prioridade na ordem acima)."""
    name = (name or "").strip()
    desc = (description or "").strip()
    desc_lower = desc.lower()
    desc_start = desc[:200].strip() if desc else ""

    # 1) Placeholder genérico
    if "- para decorar e festejar" in desc_lower[:150]:
        return CAT_PLACEHOLDER

    # 2) Vela formato Silver Festas (nome com "Vela Número" ou "| Silver Festas", desc sem ✨)
    is_vela_silver = (
        ("vela número" in name.lower() or "| silver festas" in name.lower())
        and ("✨ descrição completa" not in desc_lower and "descrição completa —" not in desc_lower)
        and ("silver festas" in desc_lower or "benefícios" in desc_lower or "especificações" in desc_lower)
    )
    if is_vela_silver:
        return CAT_SILVER_ANTIGO

    # 3) Prato a ajustar: "Prato Papel" sem " de " ou "– -" no nome
    if "prato papel" in name.lower() and "prato de papel" not in name.lower():
        return CAT_PRATO_AJUSTAR
    if "– -" in name or "\u2013 -" in name:  # en-dash + hyphen
        return CAT_PRATO_AJUSTAR

    # 4) Boleira (ou outro) com <h3> e sem ✨
    if "<h3>benefícios</h3>" in desc_lower or "<h3>especificações</h3>" in desc_lower:
        if "✨ descrição completa" not in desc_lower:
            return CAT_BOLEIRA_H3

    # 5) Já no padrão novo
    if "✨ descrição completa" in desc_lower or "descrição completa —" in desc_lower:
        return CAT_PADRAO_NOVO

    return CAT_OUTROS


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    # Aceita caminho por argumento; senão usa a matriz final (14).csv
    if len(sys.argv) > 1:
        master_path = os.path.abspath(sys.argv[1])
    else:
        master_path = os.path.join(base, "imported", "187255-products (15).csv")
    out_dir = os.path.join(base, "work")
    out_csv = os.path.join(out_dir, "analise_fase1_resultado.csv")
    out_list_dir = os.path.join(out_dir, "analise_fase1_listas")

    if not os.path.isfile(master_path):
        print(f"Arquivo não encontrado: {master_path}", file=sys.stderr)
        sys.exit(1)

    os.makedirs(out_dir, exist_ok=True)
    os.makedirs(out_list_dir, exist_ok=True)

    counts = {c: 0 for c in [CAT_PLACEHOLDER, CAT_SILVER_ANTIGO, CAT_PRATO_AJUSTAR, CAT_BOLEIRA_H3, CAT_PADRAO_NOVO, CAT_OUTROS]}
    rows_by_cat = {c: [] for c in counts}

    with open(master_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if len(row) <= max(IDX_NAME, IDX_DESCRIPTION):
                continue
            variation_id = (row[IDX_VARIATION_ID] or "").strip()
            if variation_id:
                continue  # só linhas pai
            product_id = (row[IDX_PRODUCT_ID] or "").strip()
            name = (row[IDX_NAME] or "").strip()
            description = (row[IDX_DESCRIPTION] or "").strip()
            short_desc = (row[IDX_SHORT_DESC] or "").strip()[:80]

            cat = classify(name, description)
            counts[cat] += 1
            rows_by_cat[cat].append((product_id, name[:70], short_desc[:50], cat))

    # Relatório no stdout
    print("=" * 60)
    print("FASE 1 — Diagnóstico do master (matriz final)")
    print("Arquivo:", os.path.basename(master_path))
    print("=" * 60)
    total = sum(counts.values())
    print(f"Total de produtos (linhas pai): {total}\n")
    print("Contagem por categoria:")
    for c in [CAT_PLACEHOLDER, CAT_SILVER_ANTIGO, CAT_PRATO_AJUSTAR, CAT_BOLEIRA_H3, CAT_PADRAO_NOVO, CAT_OUTROS]:
        pct = (100 * counts[c] / total) if total else 0
        print(f"  {c}: {counts[c]} ({pct:.1f}%)")
    print()

    # Gravar CSV com todos (product_id, name, short_desc, categoria)
    with open(out_csv, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f)
        w.writerow(["product_id", "name", "short_description", "categoria"])
        for c in counts:
            for r in rows_by_cat[c]:
                w.writerow(r)
    print(f"Resultado completo (CSV): {out_csv}")

    # Listas por categoria (só product_id, uma por linha)
    for c in counts:
        path = os.path.join(out_list_dir, f"{c}.txt")
        with open(path, "w", encoding="utf-8") as f:
            for r in rows_by_cat[c]:
                f.write(r[0] + "\n")
        print(f"  {c}: {path} ({len(rows_by_cat[c])} IDs)")

    # Amostras das categorias que precisam de ação
    print("\n--- Amostras (primeiros 3 por categoria de ação) ---")
    for c in [CAT_PLACEHOLDER, CAT_SILVER_ANTIGO, CAT_PRATO_AJUSTAR, CAT_BOLEIRA_H3]:
        if rows_by_cat[c]:
            print(f"\n[{c}]")
            for r in rows_by_cat[c][:3]:
                print(f"  {r[0]} | {r[1]}")

    return 0


if __name__ == "__main__":
    sys.exit(main())
