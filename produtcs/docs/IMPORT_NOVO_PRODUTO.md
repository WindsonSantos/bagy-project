# Cadastro de novo produto por importação (Bagy)

Este documento descreve como **criar um produto que ainda não existe na base** usando um CSV no mesmo formato do export Bagy (36 colunas).

## Estrutura gerada

- **Cabeçalho:** Idêntico ao export Bagy (`product_id`, `product_external_id`, `variation_id`, … até `sku`).
- **Produto novo:** `product_id` e `variation_id` **vazios** para a Bagy criar novos IDs na importação.
- **Linha pai:** Uma linha com nome, url, peso, dimensões, meta, description, short_description, brand, category_1, category_2, active, etc.
- **Variações:** Uma linha por variação (ex.: por cor), com `color`, `first_attribute_group` (ex.: Cor), `first_attribute_value`, `sku` preenchidos; nome/url/dimensões podem ficar vazios (herdam do pai no export).

## Como a Bagy estrutura produto + variações (export)

No arquivo base `187255-products_20260130.csv`, produtos com variações (ex.: **Vela Palito - Lisa Colorida**, product_id 9840812) seguem este padrão:

- **Linha pai:** `product_id` sem espaço (ex.: `9840812`), `variation_id` vazio, `name` e `url` preenchidos, `price` e dimensões preenchidos.
- **Linhas de variação:** `product_id` **com espaço à esquerda** (ex.: ` 9840812`), `variation_id` preenchido (ex.: 28613441), **`name` e `url` vazios**, `price` e dimensões vazios, `color` preenchido (Rosa, Azul, Colorida).

Ou seja: o **espaço à esquerda em `product_id`** indica “esta linha é variação do produto acima”. O script de import novo produto replica isso: na primeira linha, `product_id` vazio (novo produto); nas linhas seguintes, **`product_id` = um espaço** e **`name`/`url` vazios**, para a Bagy interpretar como variações do produto criado na linha 1. Se a importação ainda exigir `name` em todas as linhas ou não agrupar por espaço, use `--só-produto` e cadastre as variações no painel.

## Erro "The name field is required" (linha 8+)

Se a Bagy exige **name** em todas as linhas ao criar produto, a importação falha nas linhas de variação (name vazio). O script passou a gerar variações no **formato do export** (product_id com espaço, name vazio). Vale testar de novo; se continuar falhando, use `--só-produto` e crie as variações manualmente.

## Como gerar o CSV (Leque de Papel Decorativo)

**Com variações (8 linhas — tente primeiro):**
```bash
python3 produtcs/scripts/gerar_import_novo_produto.py
```
Saída: `produtcs/work/40-import-novo-leque-papel-decorativo.csv` — 1 pai + 7 variações, **name** preenchido em todas.

**Só produto (1 linha — plano B):** se a Bagy não agrupar as 8 linhas como 1 produto com variações, use apenas o produto e crie as variações no painel:
```bash
python3 produtcs/scripts/gerar_import_novo_produto.py --só-produto
```
Saída: `produtcs/work/40-import-novo-leque-papel-decorativo-só-produto.csv` — 1 linha (produto pai).

## Pré-requisitos na Bagy

1. **Importar como “criar novos”**  
   No fluxo de importação da Bagy, use a opção que **cria novos produtos** quando `product_id` (e/ou identificador único) estiver vazio. Se a Bagy só permitir “atualizar” por ID, pode ser necessário criar primeiro um produto manualmente e depois ajustar o processo com a equipe Bagy.

2. **Arquivo**  
   - Encoding: **UTF-8**.  
   - Delimitador: **vírgula** (`,`).  
   - Mesmas 36 colunas e mesma ordem do export.

3. **Preço e imagens**  
   - O CSV do Leque deixa `price` e `images` vazios (preço “a definir”, imagens a enviar depois).  
   - Após importar, preencha preço e fotos no painel se necessário.

4. **Variações**  
   - A Bagy deve interpretar: primeira linha = produto pai; linhas seguintes com `color` / `first_attribute_*` / `sku` = variações do mesmo produto.  
   - Se a Bagy agrupar por outro critério (ex.: `product_external_id`), podemos adaptar o script para preencher um identificador temporário comum.

## Próximos produtos (N em massa)

Para cadastrar mais produtos por importação:

1. **Criar uma “spec” por produto**  
   No mesmo estilo de `produtcs/lequePapelDecorativo`: nome, descrição HTML, SEO, categorias, dimensões, variações (SKU + Cor/modelo).

2. **Estender o script**  
   - Opção A: Adicionar no script uma spec embutida por produto (como o Leque) e um argumento, ex.: `python3 gerar_import_novo_produto.py leque-papel-decorativo` ou `nome-do-outro`.  
   - Opção B: Fazer o script **ler um arquivo de spec** (ex.: formato markdown ou YAML com seções Nome, Descrição, SEO, Variações, Dimensões) e gerar o CSV. Assim você mantém um arquivo por produto e o script gera todos os CSVs de uma vez.

3. **Importar em lote**  
   - Um CSV por produto novo (como o 40) ou um único CSV com vários produtos (vários “pais” + suas variações), conforme o que a Bagy aceitar.

## Validação antes de importar

- [ ] Cabeçalho com exatamente 36 colunas e nomes iguais ao export Bagy.  
- [ ] Todas as linhas com 36 campos.  
- [ ] `product_id` e `variation_id` vazios nas linhas de novo produto/variação.  
- [ ] Descrição HTML em uma única linha (sem quebras no meio do campo).  
- [ ] Número decimal de peso no formato da base (ex.: `0,150` com vírgula, se for o padrão do export).

## Cadastro em duas etapas (produto já criado → adicionar variações)

Quando o produto foi criado com **1 registro só** (sem variações), a Bagy cria uma **variação padrão única**. Para adicionar as demais variações por import:

1. **Export** do produto (ex.: `187255-products (16).csv`) mostra: linha pai (product_id sem espaço) + linha de variação (product_id **com espaço** à esquerda, variation_id preenchido, name/url vazios).
2. **Import de novas variações:** CSV com linhas no mesmo formato da variação, mas com **product_id = " " + id_do_produto** (ex.: ` 9907906`) e **variation_id vazio** (Bagy cria). Preencher **color** e **sku** por variação; name/url vazios.
3. Após importar, no painel exclua a variação padrão única que a Bagy criou; ficam as variações (cores) desejadas.

**Leque (product_id 9907906):**  
Script: `produtcs/scripts/gerar_import_leque_variacoes.py`  
Saída: `produtcs/work/41-import-leque-variacoes.csv` (7 linhas: Rosa, Rosa Bebê, Amarelo, Azul Bebê, Vermelho, Candy Colors, Sortido).

```bash
python3 produtcs/scripts/gerar_import_leque_variacoes.py
```

## Arquivos relacionados

- **Spec do Leque:** `produtcs/lequePapelDecorativo`  
- **Script novo produto:** `produtcs/scripts/gerar_import_novo_produto.py`  
- **Script variações Leque:** `produtcs/scripts/gerar_import_leque_variacoes.py`  
- **CSV novo produto (1 linha):** `produtcs/work/40-import-novo-leque-papel-decorativo-só-produto.csv`  
- **CSV variações Leque:** `produtcs/work/41-import-leque-variacoes.csv`  
- **Referência de colunas:** primeiro registro de `produtcs/imported/187255-products (15).csv`
