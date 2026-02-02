#!/usr/bin/env python3
"""
Gera delta 33: corrige " – - " / "– -" -> " - " em name e textos
APENAS para produtos de integração (product_external_id preenchido).
Não altera produtos cadastrados manualmente.
"""
import csv
import os
import sys

# Colunas (índice): product_id=0, product_external_id=1, name=4, meta_title=10, meta_description=11, description=13, short_description=14
NAME_IDX = 4
META_TITLE_IDX = 10
META_DESC_IDX = 11
DESC_IDX = 13
SHORT_DESC_IDX = 14
TEXT_INDICES = (NAME_IDX, META_TITLE_IDX, META_DESC_IDX, DESC_IDX, SHORT_DESC_IDX)

# Padrão errado: en-dash (U+2013) seguido de espaço e hífen -> substituir por " - "
BAD_PATTERNS = ("– -", " – - ", "– - ")
REPLACEMENT = " - "


def fix_dash(s: str) -> str:
    if not s:
        return s
    t = s
    for bad in BAD_PATTERNS:
        t = t.replace(bad, REPLACEMENT)
    return t


def main():
    base = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    master_path = os.path.join(base, "imported", "187255-products_UpdatedAllProductNames.csv")
    out_path = os.path.join(base, "work", "33-187255-products_UpdatedAllProductNames-pratos-fix-dash-delta.csv")

    if not os.path.isfile(master_path):
        print(f"Arquivo master não encontrado: {master_path}", file=sys.stderr)
        sys.exit(1)

    integration_product_ids = set()
    rows_by_line = []
    header = None

    with open(master_path, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        for row in reader:
            if len(row) < 15:
                continue
            pid = (row[0] or "").strip()
            ext_id = (row[1] or "").strip()
            if ext_id:
                integration_product_ids.add(pid)
            rows_by_line.append(row)

    # Corrigir apenas linhas de produtos de integração que contenham o padrão errado
    delta_rows = []
    for row in rows_by_line:
        pid = (row[0] or "").strip()
        if pid not in integration_product_ids:
            continue
        modified = list(row)
        changed = False
        for i in TEXT_INDICES:
            if i >= len(modified):
                continue
            orig = modified[i] or ""
            new_val = fix_dash(orig)
            if new_val != orig:
                modified[i] = new_val
                changed = True
        if changed:
            delta_rows.append(modified)

    with open(out_path, "w", encoding="utf-8", newline="") as f:
        writer = csv.writer(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        for r in delta_rows:
            writer.writerow(r)

    print(f"Delta 33 gerado: {out_path}")
    print(f"Produtos de integração no master: {len(integration_product_ids)}")
    print(f"Linhas corrigidas (apenas integração): {len(delta_rows)}")
    if len(delta_rows) == 0:
        print("Nenhuma linha de produto de integração continha '– -' no master. Se o nome errado está no sistema após import do 32, os afetados são produtos sem product_external_id (manuais); não os alteramos por regra.")


if __name__ == "__main__":
    main()
