#!/usr/bin/env python3
"""
Gera delta 37 — produtos boleira_h3 (67): alinha descrição ao padrão.
- Adiciona "✨ Descrição completa — {nome}" no início (se não tiver).
- Substitui <h3>Benefícios</h3> → 🎉 Ideal para diversas ocasiões
- Substitui <h3>Especificações</h3> → 📋 Especificações do produto
- Substitui <h3>Variação</h3> → Variação (em <p><strong>)
- Adiciona ao final: 🚚 Frete e prazo, 💡 Dica, ❤️ Garanta o seu (se não tiver).
"""
import csv
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(BASE, "imported", "187255-products (15).csv")
LISTAS = os.path.join(BASE, "work", "analise_fase1_listas")
WORK = os.path.join(BASE, "work")

IDX = {
    "product_id": 0, "variation_id": 2, "name": 4,
    "meta_title": 10, "meta_description": 11,
    "description": 13, "short_description": 14,
}


def load_ids(filename):
    path = os.path.join(LISTAS, filename)
    if not os.path.isfile(path):
        return set()
    with open(path, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())


def extrair_nome_desc(desc):
    """Tenta extrair nome do produto do primeiro <strong> na descrição."""
    if not desc:
        return ""
    m = re.search(r"<strong>([^<]+)</strong>", desc)
    return m.group(1).strip() if m else ""


def bloco_final(nome):
    """Bloco padrão ao final da descrição (frete, dica, garanta)."""
    nome_strong = f"<strong>{nome}</strong>" if nome else "o produto"
    return (
        '<p><strong>🚚 Frete e prazo</strong></p>'
        '<p>Calcule o frete e o prazo de entrega informando seu CEP antes de finalizar a compra.</p>'
        '<p><strong>💡 Dica</strong></p>'
        '<p>Combine com outros artigos de festa para uma mesa completa e harmoniosa.</p>'
        '<p><strong>❤️ Garanta o seu</strong></p>'
        f'<p>Garanta agora {nome_strong} e deixe sua festa ou evento ainda mais especial!</p>'
    )


def transformar_descricao(desc, nome_display):
    """Padroniza títulos h3 e adiciona ✨ no início; adiciona frete/dica/garanta no final se faltar."""
    if not desc:
        return desc
    d = desc.strip()
    nome = nome_display or extrair_nome_desc(d)

    if "✨ Descrição completa" not in d and "Descrição completa —" not in d and nome:
        prefixo = f'<p><strong>✨ Descrição completa — {nome}</strong></p>'
        d = prefixo + d
    d = re.sub(r"<h3>\s*Benefícios\s*</h3>", "<p><strong>🎉 Ideal para diversas ocasiões</strong></p>", d, flags=re.I)
    d = re.sub(r"<h3>\s*Características\s*</h3>", "<p><strong>⭐ Por que escolher este produto?</strong></p>", d, flags=re.I)
    d = re.sub(r"<h3>\s*Especificações\s*</h3>", "<p><strong>📋 Especificações do produto</strong></p>", d, flags=re.I)
    d = re.sub(r"<h3>\s*Variação\s*</h3>", "<p><strong>Variação</strong></p>", d, flags=re.I)

    if "🚚 Frete e prazo" not in d and "Frete e prazo" not in d:
        d = d.rstrip()
        if d and not d.endswith("</p>"):
            d = d + "\n"
        d = d + bloco_final(nome or nome_display or "o produto")
    return d


def main():
    if not os.path.isfile(MASTER):
        print(f"Master não encontrado: {MASTER}", file=sys.stderr)
        return 1

    ids_boleira = load_ids("boleira_h3.txt")
    if not ids_boleira:
        print("Nenhum product_id em boleira_h3.txt", file=sys.stderr)
        return 1

    with open(MASTER, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    # Nome do produto por product_id (linha pai)
    nome_por_pid = {}
    for row in rows:
        if len(row) <= IDX["name"]:
            continue
        pid = (row[IDX["product_id"]] or "").strip()
        vid = (row[IDX["variation_id"]] or "").strip()
        if pid in ids_boleira and not vid:
            nome_por_pid[pid] = (row[IDX["name"]] or "").strip()

    delta = []
    for row in rows:
        if len(row) < 36:
            row = row + [""] * (36 - len(row))
        pid = (row[IDX["product_id"]] or "").strip()
        if pid not in ids_boleira:
            continue
        name = (row[IDX["name"]] or "").strip()
        nome_display = name or nome_por_pid.get(pid, "")
        desc = (row[IDX["description"]] or "").strip()
        if not desc:
            continue
        new_desc = transformar_descricao(desc, nome_display)
        if new_desc == desc:
            continue
        new_row = list(row)
        new_row[IDX["description"]] = new_desc
        delta.append(new_row)

    out_path = os.path.join(WORK, "38-delta-h3-restante.csv")
    os.makedirs(WORK, exist_ok=True)
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        w.writerow(header)
        for r in delta:
            w.writerow(r)

    print(f"Delta gerado: {out_path}")
    print(f"Linhas alteradas: {len(delta)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
