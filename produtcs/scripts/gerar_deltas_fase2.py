#!/usr/bin/env python3
"""
Fase 2 — Gera deltas de correção a partir do master (14).csv.
- placeholder: 1 produto (Bandeja) — nova descrição no padrão
- prato_ajustar: 10 produtos — corrige "– -" → " - " no nome e textos
- vela_silver_antigo: 4 produtos — nome "Vela Mini Design - Cor - Nn" + descrição template v1
"""
import csv
import os
import re
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MASTER = os.path.join(BASE, "imported", "187255-products (15).csv")
LISTAS = os.path.join(BASE, "work", "analise_fase1_listas")
WORK = os.path.join(BASE, "work")

# Colunas
IDX = {
    "product_id": 0, "product_external_id": 1, "variation_id": 2, "variation_external_id": 3,
    "name": 4, "url": 5, "weight": 6, "depth": 7, "width": 8, "height": 9,
    "meta_title": 10, "meta_description": 11, "meta_keywords": 12,
    "description": 13, "short_description": 14, "ncm": 15, "images": 16,
    "price": 17, "price_compare": 18, "model": 19, "gender": 20, "age_group": 21,
    "active": 22, "brand": 23, "category_1": 24, "category_2": 25, "category_3": 26,
    "gtin": 27, "mpn": 28, "stock": 29, "color": 30,
    "first_attribute_group": 31, "first_attribute_value": 32,
    "second_attribute_group": 33, "second_attribute_value": 34, "sku": 35,
}


def load_ids(filename):
    path = os.path.join(LISTAS, filename)
    if not os.path.isfile(path):
        return set()
    with open(path, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())


def fix_dash(s):
    if not s:
        return s
    t = s.replace("– -", " - ").replace("\u2013 -", " - ").replace(" – - ", " - ")
    return re.sub(r"  +", " ", t)


def desc_bandeja(name):
    """Descrição no padrão para Bandeja Prato Retangular."""
    return (
        f'<p><strong>✨ Descrição completa — {name}</strong></p>'
        f'<p>A <strong>{name}</strong> é prática para servir doces, salgados e porções em festas e eventos.</p>'
        f'<p>Material resistente e descartável, ideal para organizar a mesa e facilitar a limpeza.</p>'
        f'<p><strong>🎉 Ideal para diversas ocasiões</strong></p><ul><li>Festas e eventos</li><li>Aniversários</li><li>Reuniões</li></ul>'
        f'<p><strong>📋 Especificações do produto</strong></p><ul><li><strong>Material:</strong> Papel Metalizado</li><li><strong>Quantidade:</strong> 5 unidades</li><li><strong>Dimensões aprox.:</strong> 26,5 x 18,5 cm</li></ul>'
        f'<p><strong>ℹ️ Informações importantes</strong></p><ul><li>Produto descartável.</li></ul>'
        f'<p><strong>🚚 Frete e prazo</strong></p><p>Calcule o frete informando seu CEP antes de finalizar a compra.</p>'
        f'<p><strong>❤️ Garanta o seu</strong></p><p>Garanta agora a <strong>{name}</strong> e deixe sua festa ainda mais prática!</p>'
    )


def short_bandeja(name):
    return f"{name}. Bandeja descartável prática para festas e eventos. Material resistente."


def meta_title_bandeja(name):
    return f"{name} | Descartáveis para Festa"


def meta_desc_bandeja(name):
    return f"{name}. Bandeja descartável para festas e eventos. Prática e resistente."


def desc_vela_mini(name):
    """Descrição template v1 Vela Mini Design (uma linha, minificado)."""
    return (
        f'<p><strong>✨ Descrição completa — {name}</strong></p>'
        f'<p>A <strong>{name}</strong> é perfeita para destacar o bolo e deixar a comemoração ainda mais especial.</p>'
        f'<p>Com visual moderno e acabamento caprichado, valoriza a decoração da mesa e fica linda nas fotos.</p>'
        f'<p><strong>🎉 Ideal para diversas ocasiões</strong></p><ul><li>Aniversários infantis e adultos</li><li>Festas temáticas</li><li>Comemorações especiais</li></ul>'
        f'<p><strong>⭐ Por que escolher este produto?</strong></p><ul><li>Fácil de usar</li><li>Ótimo destaque no bolo</li><li>Valoriza a decoração da mesa</li></ul>'
        f'<p><strong>📋 Especificações do produto</strong></p><ul><li>Tipo: vela decorativa para bolo</li><li>Conteúdo da embalagem: 1 vela (número conforme o modelo)</li></ul>'
        f'<p><strong>ℹ️ Informações importantes</strong></p><ul><li>As cores podem variar levemente conforme a tela do dispositivo.</li><li>Produto indicado para uso decorativo.</li></ul>'
        f'<p><strong>🚚 Frete e prazo</strong></p><p>Calcule o frete e o prazo de entrega informando seu CEP antes de finalizar a compra.</p>'
        f'<p><strong>💡 Dica</strong></p><p>Combine com outros artigos de festa do mesmo tema para montar uma decoração completa e harmoniosa.</p>'
        f'<p><strong>❤️ Garanta a sua</strong></p><p>Garanta agora a <strong>{name}</strong> e deixe sua comemoração ainda mais especial!</p>'
    )


def short_vela(name):
    return f"Vela Mini Design para bolo com visual moderno. {name}. Ideal para aniversários e festas temáticas."


def meta_vela(name):
    return f"{name} | Decoração para Festa"


def meta_desc_vela(name):
    return f"{name} para bolo. Visual moderno e tamanho compacto. Perfeita para destacar a decoração do bolo."


def extrair_cor_nome_vela(name):
    """De 'Vela Número Mini Design Azul' ou 'Vela Número Mini Design Rosa Bebe' extrai a cor."""
    name = (name or "").strip()
    # Padrão: Vela Número Mini Design {Cor}
    m = re.match(r"Vela\s+N[uú]mero\s+(?:Mini\s+Design\s+)?(.+)$", name, re.I)
    if m:
        return m.group(1).strip()
    return ""


def numero_vela(first_attr_val, sku):
    """Obtém o número da vela (0-9 ou ?) a partir de first_attribute_value ou sku."""
    v = (first_attr_val or "").strip()
    if v in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "?"):
        return v
    s = (sku or "").strip()
    if s and "-" in s:
        tail = s.split("-")[-1]
        if tail in ("0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "?"):
            return tail
    return "0"


def main():
    if not os.path.isfile(MASTER):
        print(f"Master não encontrado: {MASTER}", file=sys.stderr)
        return 1

    ids_placeholder = load_ids("placeholder.txt")
    ids_prato = load_ids("prato_ajustar.txt")
    ids_vela = load_ids("vela_silver_antigo.txt")

    # Cor por product_id (vela) — preenchido na primeira passagem com a linha pai
    cor_por_pid = {}

    with open(MASTER, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    # Primeira passagem: para velas, guardar cor do nome da linha pai
    for row in rows:
        if len(row) <= max(IDX["name"], IDX["first_attribute_value"]):
            continue
        pid = (row[IDX["product_id"]] or "").strip()
        vid = (row[IDX["variation_id"]] or "").strip()
        if pid not in ids_vela or vid:
            continue
        name = (row[IDX["name"]] or "").strip()
        cor = extrair_cor_nome_vela(name)
        if cor:
            cor_por_pid[pid] = cor

    # Segunda passagem: montar deltas
    delta_placeholder = []
    delta_prato = []
    delta_vela = []

    for row in rows:
        if len(row) < 36:
            row = row + [""] * (36 - len(row))
        pid = (row[IDX["product_id"]] or "").strip()
        vid = (row[IDX["variation_id"]] or "").strip()
        name = (row[IDX["name"]] or "").strip()

        if pid in ids_placeholder:
            if not vid:
                new_row = list(row)
                new_row[IDX["description"]] = desc_bandeja(name)
                new_row[IDX["short_description"]] = short_bandeja(name)
                new_row[IDX["meta_title"]] = meta_title_bandeja(name)
                new_row[IDX["meta_description"]] = meta_desc_bandeja(name)
                delta_placeholder.append(new_row)
            continue

        if pid in ids_prato:
            new_row = list(row)
            new_row[IDX["name"]] = fix_dash(row[IDX["name"]])
            new_row[IDX["meta_title"]] = fix_dash(row[IDX["meta_title"]])
            new_row[IDX["meta_description"]] = fix_dash(row[IDX["meta_description"]])
            new_row[IDX["description"]] = fix_dash(row[IDX["description"]])
            new_row[IDX["short_description"]] = fix_dash(row[IDX["short_description"]])
            delta_prato.append(new_row)
            continue

        if pid in ids_vela:
            cor = cor_por_pid.get(pid, "")
            num = numero_vela(
                row[IDX["first_attribute_value"]] if len(row) > IDX["first_attribute_value"] else "",
                row[IDX["sku"]] if len(row) > IDX["sku"] else "",
            )
            new_name = f"Vela Mini Design - {cor} - N{num}" if cor else name
            new_row = list(row)
            new_row[IDX["name"]] = new_name
            new_row[IDX["description"]] = desc_vela_mini(new_name)
            new_row[IDX["short_description"]] = short_vela(new_name)
            new_row[IDX["meta_title"]] = meta_vela(new_name)
            new_row[IDX["meta_description"]] = meta_desc_vela(new_name)
            delta_vela.append(new_row)
            continue

    def write_delta(path, delta_rows):
        with open(path, "w", encoding="utf-8", newline="") as out:
            w = csv.writer(out, delimiter=",", quoting=csv.QUOTE_MINIMAL)
            w.writerow(header)
            for r in delta_rows:
                w.writerow(r)

    os.makedirs(WORK, exist_ok=True)
    write_delta(os.path.join(WORK, "34-delta-placeholder.csv"), delta_placeholder)
    write_delta(os.path.join(WORK, "35-delta-prato-ajustar.csv"), delta_prato)
    write_delta(os.path.join(WORK, "36-delta-vela-silver-antigo.csv"), delta_vela)

    print("Fase 2 — Deltas gerados em produtcs/work/")
    print(f"  34-delta-placeholder.csv: {len(delta_placeholder)} linhas")
    print(f"  35-delta-prato-ajustar.csv: {len(delta_prato)} linhas")
    print(f"  36-delta-vela-silver-antigo.csv: {len(delta_vela)} linhas")
    return 0


if __name__ == "__main__":
    sys.exit(main())
