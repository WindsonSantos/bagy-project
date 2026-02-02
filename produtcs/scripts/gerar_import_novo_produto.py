#!/usr/bin/env python3
"""
Gera CSV de importação para NOVO produto (cadastro inédito na base Bagy).
Estrutura idêntica ao export Bagy (36 colunas). product_id e variation_id vazios.
Uso: python gerar_import_novo_produto.py [nome_do_produto]
  Sem argumento: gera o Leque de Papel Decorativo (spec embutida).
  Com argumento: carrega spec do arquivo produtcs/<nome_do_produto> (formato futuro).
Saída: produtcs/work/40-import-novo-<slug>.csv
"""
import csv
import os
import sys

BASE = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
WORK = os.path.join(BASE, "work")

# Cabeçalho idêntico ao export Bagy (36 colunas)
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


def make_row(
    product_id="",
    product_external_id="",
    variation_id="",
    variation_external_id="",
    name="",
    url="",
    weight="",
    depth="",
    width="",
    height="",
    meta_title="",
    meta_description="",
    meta_keywords="",
    description="",
    short_description="",
    ncm="",
    images="",
    price="",
    price_compare="",
    model="",
    gender="",
    age_group="",
    active="1",
    brand="",
    category_1="",
    category_2="",
    category_3="",
    gtin="",
    mpn="",
    stock="",
    color="",
    first_attribute_group="",
    first_attribute_value="",
    second_attribute_group="",
    second_attribute_value="",
    sku="",
):
    """Monta uma linha com exatamente 36 campos."""
    return [
        str(product_id),
        str(product_external_id),
        str(variation_id),
        str(variation_external_id),
        str(name),
        str(url),
        str(weight),
        str(depth),
        str(width),
        str(height),
        str(meta_title),
        str(meta_description),
        str(meta_keywords),
        str(description),
        str(short_description),
        str(ncm),
        str(images),
        str(price),
        str(price_compare),
        str(model),
        str(gender),
        str(age_group),
        str(active),
        str(brand),
        str(category_1),
        str(category_2),
        str(category_3),
        str(gtin),
        str(mpn),
        str(stock),
        str(color),
        str(first_attribute_group),
        str(first_attribute_value),
        str(second_attribute_group),
        str(second_attribute_value),
        str(sku),
    ]


# --- Especificação Leque de Papel Decorativo (embutida) ---
LEQUE_NAME = "Leque de Papel Decorativo – Kit com 6 Unidades"
LEQUE_URL = "/leque-de-papel-decorativo-kit-6-unidades"
LEQUE_DESCRIPTION = (
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
LEQUE_SHORT = "Leque de papel decorativo com 6 unidades em tamanhos variados (20 cm, 30 cm e 40 cm). Ideal para painéis e decoração temática."
LEQUE_META_TITLE = "Leque de Papel Decorativo Kit com 6 Unidades | Cor de Papel"
LEQUE_META_DESC = "Leque de papel decorativo com 6 unidades em tamanhos variados. Ideal para festas, painéis e decoração temática. Prático, leve e fácil de montar."
LEQUE_META_KW = "leque decorativo, decoração de festa, leque de papel, painel decorativo, artigos de festa"
LEQUE_WEIGHT = "0,150"
LEQUE_DEPTH = "35.00"
LEQUE_WIDTH = "35.00"
LEQUE_HEIGHT = "5.00"
LEQUE_BRAND = "Silver Festas"
LEQUE_CAT1 = "Artigos de Festa"
LEQUE_CAT2 = "Decoração & Acessórios"
LEQUE_VARIATIONS = [
    ("HA536A", "Rosa"),
    ("HA536B", "Rosa Bebê"),
    ("HA536C", "Amarelo"),
    ("HA536D", "Azul Bebê"),
    ("HA536E", "Vermelho"),
    ("HA536F", "Candy Colors"),
    ("HA536G", "Sortido"),
]


def build_leque_rows():
    """Retorna lista de linhas (listas) para o Leque: 1 pai + 7 variações."""
    rows = []
    # Linha pai (produto novo: product_id e variation_id vazios)
    parent = make_row(
        product_id="",
        product_external_id="",
        variation_id="",
        variation_external_id="",
        name=LEQUE_NAME,
        url=LEQUE_URL,
        weight=LEQUE_WEIGHT,
        depth=LEQUE_DEPTH,
        width=LEQUE_WIDTH,
        height=LEQUE_HEIGHT,
        meta_title=LEQUE_META_TITLE,
        meta_description=LEQUE_META_DESC,
        meta_keywords=LEQUE_META_KW,
        description=LEQUE_DESCRIPTION,
        short_description=LEQUE_SHORT,
        ncm="",
        images="",
        price="",
        price_compare="",
        model="",
        gender="",
        age_group="",
        active="1",
        brand=LEQUE_BRAND,
        category_1=LEQUE_CAT1,
        category_2=LEQUE_CAT2,
        category_3="",
        gtin="",
        mpn="",
        stock="",
        color="",
        first_attribute_group="",
        first_attribute_value="",
        second_attribute_group="",
        second_attribute_value="",
        sku="",
    )
    rows.append(parent)
    # Variações no formato Bagy (como no export 187255-products_20260130): product_id com
    # espaço à esquerda indica "variação do produto acima"; name e url vazios.
    for sku, cor in LEQUE_VARIATIONS:
        var_row = make_row(
            product_id=" ",  # espaço = variação do produto da linha anterior (ver Vela Palito 9840812)
            product_external_id="",
            variation_id="",
            variation_external_id="",
            name="",
            url="",
            weight="",
            depth="",
            width="",
            height="",
            meta_title=LEQUE_META_TITLE,
            meta_description=LEQUE_META_DESC,
            meta_keywords=LEQUE_META_KW,
            description=LEQUE_DESCRIPTION,
            short_description=LEQUE_SHORT,
            ncm="",
            images="",
            price="",
            price_compare="",
            model="",
            gender="",
            age_group="",
            active="1",
            brand=LEQUE_BRAND,
            category_1=LEQUE_CAT1,
            category_2=LEQUE_CAT2,
            category_3="",
            gtin="",
            mpn="",
            stock="",
            color=cor,
            first_attribute_group="",
            first_attribute_value="",
            second_attribute_group="",
            second_attribute_value="",
            sku=sku,
        )
        rows.append(var_row)
    return rows


def build_leque_rows_só_produto():
    """Retorna apenas 1 linha (produto pai), sem variações. Use se a Bagy não aceitar variações no import — crie as variações no painel depois."""
    return build_leque_rows()[:1]


def main():
    args = [a for a in sys.argv[1:] if a.startswith("--")]
    rest = [a for a in sys.argv[1:] if not a.startswith("--")]
    só_produto = "--só-produto" in args or "--so-produto" in args
    product_slug = (rest[0] if rest else "").strip() or "leque-papel-decorativo"

    if "leque" in product_slug.lower():
        rows = build_leque_rows_só_produto() if só_produto else build_leque_rows()
        out_slug = "leque-papel-decorativo"
        if só_produto:
            out_slug += "-só-produto"
    else:
        print("Produto não reconhecido. Use sem argumento para gerar o Leque.", file=sys.stderr)
        return 1

    os.makedirs(WORK, exist_ok=True)
    out_path = os.path.join(WORK, f"40-import-novo-{out_slug}.csv")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        w = csv.writer(f, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        w.writerow(HEADER)
        for row in rows:
            w.writerow(row)

    print("CSV de importação (novo produto) gerado:", out_path)
    if só_produto:
        print("Linhas: 1 (apenas produto pai). Crie as variações no painel depois.")
    else:
        print(f"Linhas: 1 pai + {len(rows) - 1} variações = {len(rows)} total (variações com product_id=' ' e name vazio, formato Bagy).")
    print("Campos product_id e variation_id vazios para a Bagy criar novos IDs.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
