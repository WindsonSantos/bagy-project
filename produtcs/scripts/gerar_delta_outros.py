#!/usr/bin/env python3
"""
Gera delta para os 16 produtos "outros" (analise_fase1_listas/outros.txt).
Aplica nome e descrição no padrão do catálogo (✨, 🎉, 📋, ℹ️, 🚚, 💡, ❤️).
Saída: produtcs/work/39-delta-outros.csv
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


def load_outros_ids():
    path = os.path.join(LISTAS, "outros.txt")
    if not os.path.isfile(path):
        return set()
    with open(path, "r", encoding="utf-8") as f:
        return set(line.strip() for line in f if line.strip())


# --- Talheres Eco (Colher, Colher Sobremesa, Faca, Garfo) ---
def desc_talher_eco(name):
    return (
        f'<p><strong>✨ Descrição completa — {name}</strong></p>'
        f'<p>Os talheres eco de madeira estampada são ideais para quem busca praticidade, beleza e sustentabilidade em festas e eventos.</p>'
        f'<p>Biodegradáveis e resistentes, deixam a mesa bonita e alinhada à preocupação com o meio ambiente.</p>'
        f'<p><strong>🎉 Ideal para diversas ocasiões</strong></p><ul><li>Festas e eventos</li><li>Aniversários</li><li>Comemorações sustentáveis</li></ul>'
        f'<p><strong>📋 Especificações do produto</strong></p><ul><li><strong>Material:</strong> Madeira estampada</li><li><strong>Quantidade:</strong> 10 unidades</li><li>Biodegradável e resistente</li></ul>'
        f'<p><strong>ℹ️ Informações importantes</strong></p><ul><li>Produto biodegradável.</li></ul>'
        f'<p><strong>🚚 Frete e prazo</strong></p><p>Calcule o frete e o prazo de entrega informando seu CEP antes de finalizar a compra.</p>'
        f'<p><strong>💡 Dica</strong></p><p>Combine com pratos e guardanapos do mesmo tema para uma mesa harmoniosa.</p>'
        f'<p><strong>❤️ Garanta o seu</strong></p><p>Garanta agora <strong>{name}</strong> e deixe sua festa ainda mais especial!</p>'
    )


def short_talher_eco(name):
    return f"{name}. Talheres de madeira estampada, biodegradáveis e resistentes. Ideal para festas e eventos sustentáveis."


def meta_talher_eco(name):
    return f"{name} | Sustentável e Biodegradável"


def meta_desc_talher_eco(name):
    return f"{name}. Madeira estampada, biodegradável e resistente. Ideal para festas e eventos."


# --- Cortina Metalizada ---
def desc_cortina(name):
    return (
        f'<p><strong>✨ Descrição completa — {name}</strong></p>'
        f'<p>A <strong>{name}</strong> é ideal para criar um fundo de fotos incrível e dar um toque especial de brilho na decoração.</p>'
        f'<p>Alto brilho, fácil instalação e efeito metalizado para festas e eventos.</p>'
        f'<p><strong>🎉 Ideal para diversas ocasiões</strong></p><ul><li>Fundo para fotos</li><li>Decoração de festas</li><li>Aniversários e eventos</li></ul>'
        f'<p><strong>📋 Especificações do produto</strong></p><ul><li><strong>Dimensões:</strong> 100 x 200 cm</li><li>Alto brilho metalizado</li><li>Fácil instalação</li></ul>'
        f'<p><strong>ℹ️ Informações importantes</strong></p><ul><li>As cores podem variar levemente conforme a tela do dispositivo.</li></ul>'
        f'<p><strong>🚚 Frete e prazo</strong></p><p>Calcule o frete e o prazo de entrega informando seu CEP antes de finalizar a compra.</p>'
        f'<p><strong>💡 Dica</strong></p><p>Use como backdrop para fotos e valorize a decoração da festa.</p>'
        f'<p><strong>❤️ Garanta o seu</strong></p><p>Garanta agora a <strong>{name}</strong> e deixe sua festa ainda mais especial!</p>'
    )


def short_cortina(name):
    return f"{name}. Cortina metalizada para fundo de fotos e decoração. Alto brilho e fácil instalação."


# --- Lança Confete ---
def desc_lanca_confete(name):
    return (
        f'<p><strong>✨ Descrição completa — {name}</strong></p>'
        f'<p>A <strong>{name}</strong> é feita em tubo de papelão reforçado com confetes coloridos, ideal para animar qualquer festa.</p>'
        f'<p>Basta girar a parte indicada e provocar uma linda chuva de confetes em casamentos, noivados, aniversários e muito mais.</p>'
        f'<p><strong>🎉 Ideal para diversas ocasiões</strong></p><ul><li>Aniversários</li><li>Casamentos e noivados</li><li>Comemorações</li></ul>'
        f'<p><strong>📋 Especificações do produto</strong></p><ul><li><strong>Material:</strong> Papelão reforçado e papéis metalizados</li><li><strong>Comprimento:</strong> 30 cm</li><li>Confetes coloridos inclusos</li></ul>'
        f'<p><strong>ℹ️ Informações importantes</strong></p><ul><li>Produto para uso em festas e eventos.</li></ul>'
        f'<p><strong>🚚 Frete e prazo</strong></p><p>Calcule o frete e o prazo de entrega informando seu CEP antes de finalizar a compra.</p>'
        f'<p><strong>💡 Dica</strong></p><p>Use no momento do parabéns ou da entrada dos noivos para um efeito surpresa.</p>'
        f'<p><strong>❤️ Garanta o seu</strong></p><p>Garanta agora a <strong>{name}</strong> e anime suas comemorações!</p>'
    )


def short_lanca_confete(name):
    return f"{name}. Tubo com confetes coloridos para animar festas. Basta girar e soltar a chuva de confetes."


# --- Vela Metalizada Torcida (15 cm) ---
def fix_name_vela_torcida(name):
    """Corrige '15 CM' para '15 cm' no nome."""
    if not name:
        return name
    return re.sub(r"\b15\s*CM\b", "15 cm", name, flags=re.I)


def desc_vela_torcida(name):
    return (
        f'<p><strong>✨ Descrição completa — {name}</strong></p>'
        f'<p>A <strong>{name}</strong> é uma vela decorativa com efeito metalizado e formato torcido, ideal para destacar bolos e mesas de festa.</p>'
        f'<p>Visual moderno e brilhante para aniversários e comemorações.</p>'
        f'<p><strong>🎉 Ideal para diversas ocasiões</strong></p><ul><li>Aniversários</li><li>Festas temáticas</li><li>Comemorações</li></ul>'
        f'<p><strong>📋 Especificações do produto</strong></p><ul><li><strong>Tipo:</strong> vela decorativa</li><li><strong>Altura aprox.:</strong> 15 cm</li><li>Acabamento metalizado torcido</li></ul>'
        f'<p><strong>ℹ️ Informações importantes</strong></p><ul><li>Produto indicado para uso decorativo.</li><li>As cores podem variar levemente conforme a tela do dispositivo.</li></ul>'
        f'<p><strong>🚚 Frete e prazo</strong></p><p>Calcule o frete e o prazo de entrega informando seu CEP antes de finalizar a compra.</p>'
        f'<p><strong>💡 Dica</strong></p><p>Combine com outros artigos de festa para uma decoração completa.</p>'
        f'<p><strong>❤️ Garanta o seu</strong></p><p>Garanta agora a <strong>{name}</strong> e deixe sua comemoração ainda mais especial!</p>'
    )


def short_vela_torcida(name):
    return f"{name}. Vela decorativa metalizada torcida, 15 cm. Ideal para bolos e decoração de festas."


# --- Vela Mini Design (reutiliza padrão do template v1) ---
def desc_vela_mini(name):
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


def short_vela_mini(name):
    return f"Vela Mini Design para bolo com visual moderno. {name}. Ideal para aniversários e festas temáticas."


def meta_vela_mini(name):
    return f"{name} | Decoração para Festa"


def meta_desc_vela_mini(name):
    return f"{name} para bolo. Visual moderno e tamanho compacto. Perfeita para destacar a decoração do bolo."


# --- Vela Palito Neon Glitter ---
def desc_vela_palito_neon(name):
    return (
        f'<p><strong>✨ Descrição completa — {name}</strong></p>'
        f'<p>A <strong>{name}</strong> é perfeita para destacar bolos e deixar a comemoração ainda mais especial.</p>'
        f'<p>Com acabamento em glitter e visual moderno, é ideal para festas infantis e adultas.</p>'
        f'<p><strong>🎉 Ideal para diversas ocasiões</strong></p><ul><li>Aniversários</li><li>Festas temáticas</li><li>Comemorações</li></ul>'
        f'<p><strong>⭐ Por que escolher este produto?</strong></p><ul><li>Acabamento com efeito glitter</li><li>Ótima presença visual no bolo</li><li>Fácil de posicionar e usar</li></ul>'
        f'<p><strong>📋 Especificações do produto</strong></p><ul><li><strong>Tipo:</strong> vela decorativa para bolo</li><li><strong>Conteúdo da embalagem:</strong> 1 unidade</li></ul>'
        f'<p><strong>ℹ️ Informações importantes</strong></p><ul><li>As cores podem variar levemente conforme a tela do dispositivo.</li><li>Produto indicado para uso decorativo.</li></ul>'
        f'<p><strong>🚚 Frete e prazo</strong></p><p>Calcule o frete e o prazo de entrega informando seu CEP antes de finalizar a compra.</p>'
        f'<p><strong>💡 Dica</strong></p><p>Combine com outros artigos de festa da mesma paleta para uma decoração completa.</p>'
        f'<p><strong>❤️ Garanta a sua</strong></p><p>Garanta agora a <strong>{name}</strong> e deixe sua comemoração ainda mais especial!</p>'
    )


def short_vela_palito_neon(name):
    return f"{name}. Vela decorativa com efeito neon e glitter. Ideal para bolos e festas."


def meta_vela_palito_neon(name):
    return f"{name} | Decoração para Festa"


def meta_desc_vela_palito_neon(name):
    return f"{name} para bolo: efeito neon e glitter. Visual moderno e fácil de usar. Ideal para aniversários e festas."


def classify_outros(name):
    """Retorna tipo para escolher template: talher_eco, cortina, lanca_confete, vela_torcida, vela_mini, vela_palito_neon."""
    n = (name or "").strip().lower()
    if "colher" in n and "eco" in n:
        return "talher_eco"
    if "faca" in n and "eco" in n:
        return "talher_eco"
    if "garfo" in n and "eco" in n:
        return "talher_eco"
    if "cortina" in n and "metalizada" in n:
        return "cortina"
    if "lança confete" in n or "lanca confete" in n:
        return "lanca_confete"
    if "vela metalizada torcida" in n:
        return "vela_torcida"
    if "vela palito neon glitter" in n:
        return "vela_palito_neon"
    if "vela mini design" in n:
        return "vela_mini"
    return None


def main():
    if not os.path.isfile(MASTER):
        print(f"Master não encontrado: {MASTER}", file=sys.stderr)
        return 1

    ids_outros = load_outros_ids()
    if not ids_outros:
        print("Nenhum product_id em outros.txt", file=sys.stderr)
        return 1

    with open(MASTER, "r", encoding="utf-8-sig", newline="") as f:
        reader = csv.reader(f)
        header = next(reader)
        rows = list(reader)

    delta = []
    for row in rows:
        if len(row) < 36:
            row = row + [""] * (36 - len(row))
        pid = (row[IDX["product_id"]] or "").strip()
        vid = (row[IDX["variation_id"]] or "").strip()
        if pid not in ids_outros or vid:
            continue
        name = (row[IDX["name"]] or "").strip()
        tipo = classify_outros(name)
        if not tipo:
            print(f"Aviso: tipo não identificado para product_id={pid} name={name!r}", file=sys.stderr)
            continue

        new_name = name
        if tipo == "vela_torcida":
            new_name = fix_name_vela_torcida(name)

        new_row = list(row)
        new_row[IDX["name"]] = new_name

        if tipo == "talher_eco":
            new_row[IDX["description"]] = desc_talher_eco(new_name)
            new_row[IDX["short_description"]] = short_talher_eco(new_name)
            new_row[IDX["meta_title"]] = meta_talher_eco(new_name)
            new_row[IDX["meta_description"]] = meta_desc_talher_eco(new_name)
        elif tipo == "cortina":
            new_row[IDX["description"]] = desc_cortina(new_name)
            new_row[IDX["short_description"]] = short_cortina(new_name)
            new_row[IDX["meta_title"]] = (row[IDX["meta_title"]] or "").strip() or f"{new_name} | Fundo de Festa"
            new_row[IDX["meta_description"]] = (row[IDX["meta_description"]] or "").strip() or short_cortina(new_name)
        elif tipo == "lanca_confete":
            new_row[IDX["description"]] = desc_lanca_confete(new_name)
            new_row[IDX["short_description"]] = short_lanca_confete(new_name)
            new_row[IDX["meta_title"]] = f"{new_name} | Artigos de Festa"
            new_row[IDX["meta_description"]] = short_lanca_confete(new_name)
        elif tipo == "vela_torcida":
            new_row[IDX["description"]] = desc_vela_torcida(new_name)
            new_row[IDX["short_description"]] = short_vela_torcida(new_name)
            new_row[IDX["meta_title"]] = f"{new_name} | Decoração para Festa"
            new_row[IDX["meta_description"]] = short_vela_torcida(new_name)
        elif tipo == "vela_mini":
            new_row[IDX["description"]] = desc_vela_mini(new_name)
            new_row[IDX["short_description"]] = short_vela_mini(new_name)
            new_row[IDX["meta_title"]] = meta_vela_mini(new_name)
            new_row[IDX["meta_description"]] = meta_desc_vela_mini(new_name)
        elif tipo == "vela_palito_neon":
            new_row[IDX["description"]] = desc_vela_palito_neon(new_name)
            new_row[IDX["short_description"]] = short_vela_palito_neon(new_name)
            new_row[IDX["meta_title"]] = meta_vela_palito_neon(new_name)
            new_row[IDX["meta_description"]] = meta_desc_vela_palito_neon(new_name)

        delta.append(new_row)

    os.makedirs(WORK, exist_ok=True)
    out_path = os.path.join(WORK, "39-delta-outros.csv")
    with open(out_path, "w", encoding="utf-8", newline="") as out:
        w = csv.writer(out, delimiter=",", quoting=csv.QUOTE_MINIMAL)
        w.writerow(header)
        for r in delta:
            w.writerow(r)

    print("Delta 'outros' gerado:", out_path)
    print(f"Total de linhas (apenas pais): {len(delta)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
