#!/usr/bin/env python3
"""
Gera CSV para adicionar variações (cores) ao produto Leque já existente na Bagy.
Produto: 9907906 (Leque de Papel Decorativo – Kit com 6 Unidades).
Estrutura: igual à linha de variação do export (16) — product_id com espaço + variation_id vazio.
Saída: produtcs/work/41-import-leque-variacoes.csv
"""
import csv
import os

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(BASE, "work")
PRODUCT_ID_LEQUE = "9907906"

# Cabeçalho Bagy (36 colunas)
HEADER = [
    "product_id", "product_external_id", "variation_id", "variation_external_id",
    "name", "url", "weight", "depth", "width", "height",
    "meta_title", "meta_description", "meta_keywords",
    "description", "short_description", "ncm", "images",
    "price", "price_compare", "model", "gender", "age_group", "active",
    "brand", "category_1", "category_2", "category_3",
    "gtin", "mpn", "stock", "color",
    "first_attribute_group", "first_attribute_value",
    "second_attribute_group", "second_attribute_value", "sku",
]

# Conteúdo igual à variação padrão do export (16) — meta, description, short, categories
META_TITLE = "Leque de Papel Decorativo Kit com 6 Unidades | Cor de Papel"
META_DESC = "Leque de papel decorativo com 6 unidades em tamanhos variados. Ideal para festas, painéis e decoração temática. Prático, leve e fácil de montar."
META_KW = "leque decorativo, decoração de festa, leque de papel, painel decorativo, artigos de festa"
DESCRIPTION = (
    "<p><strong>✨ Descrição completa — Leque de Papel Decorativo</strong></p>"
    "<p>O <strong>Leque de Papel Decorativo</strong> é ideal para transformar a decoração de festas e eventos, criando composições alegres, modernas e cheias de charme.</p>"
    "<p>Com tamanhos variados, o kit permite montar painéis decorativos, paredes temáticas e cenários para fotos de forma prática e visualmente impactante.</p>"
    "<p><strong>🎉 Ideal para diversas ocasiões</strong></p><ul><li>Aniversários infantis e adultos</li><li>Festas temáticas</li><li>Chás e comemorações especiais</li><li>Decoração de ambientes e painéis</li></ul>"
    "<p><strong>⭐ Por que escolher este produto?</strong></p><ul><li>Design decorativo e versátil</li><li>Tamanhos variados para composições criativas</li><li>Leve e fácil de montar</li><li>Ótimo destaque na decoração</li></ul>"
    "<p><strong>📋 Especificações do produto</strong></p><ul><li><strong>Tipo:</strong> leque decorativo de papel</li><li><strong>Tamanhos:</strong> 20 cm, 30 cm e 40 cm</li><li><strong>Conteúdo da embalagem:</strong> 6 leques (2 de cada tamanho)</li><li><strong>Material:</strong> papel decorativo</li></ul>"
    "<p><strong>ℹ️ Informações importantes</strong></p><ul><li>As cores podem variar levemente conforme a tela do dispositivo.</li><li>Produto indicado para uso decorativo.</li><li>Uso preferencial em ambientes internos.</li></ul>"
    "<p><strong>🚚 Frete e prazo</strong></p><p>Calcule o frete e o prazo de entrega informando seu CEP antes de finalizar a compra.</p>"
    "<p><strong>💡 Dica</strong></p><p>Combine com outros artigos de festa para criar uma decoração completa e harmoniosa.</p>"
    "<p><strong>❤️ Garanta o seu</strong></p><p>Garanta agora o Leque de Papel Decorativo e deixe sua celebração ainda mais especial!</p>"
)
SHORT_DESC = "Leque de papel decorativo com 6 unidades em tamanhos variados (20 cm, 30 cm e 40 cm). Ideal para painéis e decoração temática."

# 7 variações (a variação padrão criada pela Bagy pode ser deletada no painel depois)
VARIACOES = [
    ("HA536A", "Rosa"),
    ("HA536B", "Rosa Bebê"),
    ("HA536C", "Amarelo"),
    ("HA536D", "Azul Bebê"),
    ("HA536E", "Vermelho"),
    ("HA536F", "Candy Colors"),
    ("HA536G", "Sortido"),
]


def main():
    rows = []
    # product_id com espaço = variação do produto 9907906 (como no export)
    pid_com_espaco = " " + PRODUCT_ID_LEQUE
    for sku, cor in VARIACOES:
        row = [
            pid_com_espaco,
            "",
            "",   # variation_id vazio — Bagy cria nova variação
            "",
            "",   # name vazio
            "",   # url vazio
            "", "", "", "",  # weight, depth, width, height
            META_TITLE,
            META_DESC,
            META_KW,
            DESCRIPTION,
            SHORT_DESC,
            "", "",  # ncm, images
            "", "", "", "", "",  # price, price_compare, model, gender, age_group
            "1",   # active
            "",    # brand (vazio como na linha de variação do export)
            "Artigos de Festa",
            "Decoração & Acessórios",
            "",
            "", "",  # gtin, mpn
            "0",    # stock
            cor,    # color
            "", "",  # first_attribute_group, first_attribute_value
            "", "",  # second_attribute_group, second_attribute_value
            sku,
        ]
        rows.append(row)

    os.makedirs(WORK, exist_ok=True)
    out_path = os.path.join(WORK, "41-import-leque-variacoes.csv")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        w.writerow(HEADER)
        w.writerows(rows)

    print("CSV de variações gerado:", out_path)
    print(f"Linhas: {len(rows)} (product_id = \" {PRODUCT_ID_LEQUE}\", variation_id vazio)")
    print("Após importar: exclua no painel a variação padrão única que a Bagy criou; ficarão as 7 variações (Rosa, Rosa Bebê, Amarelo, Azul Bebê, Vermelho, Candy Colors, Sortido).")
    return 0


if __name__ == "__main__":
    exit(main())
