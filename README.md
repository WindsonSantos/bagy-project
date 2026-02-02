# bagy-project

Projeto de **enriquecimento de catálogo** para loja Bagy: bases de produtos em CSV (export/import Bagy, 36 colunas), scripts de análise e geração de arquivos de import, templates de descrição e documentação do workflow.

## Estrutura do repositório

```
bagy-project/
├── produtcs/
│   ├── imported/          # Bases de produtos (CSV export Bagy)
│   │   └── 187255-products (17).csv   # Base atual (273 produtos, 640 variações)
│   ├── work/              # CSVs de import gerados (deltas, novo produto, variações)
│   ├── scripts/           # Scripts Python (análise, deltas, import novo produto)
│   ├── templates/         # Templates de descrição HTML por tipo (vela, prato)
│   ├── docs/              # Documentação (workflow, TODO, import tracking)
│   ├── catalog/           # Mapeamentos (ex.: silverplastic-vela-mapping-v1.json)
│   └── lequePapelDecorativo   # Spec do produto Leque de Papel Decorativo
└── README.md
```

## Requisitos

- **Python 3** (scripts em `produtcs/scripts/` usam apenas biblioteca padrão: `csv`, `os`, `sys`)

## Scripts principais

| Script | Função |
|--------|--------|
| `analise_master_fase1.py` | Classifica produtos (linhas pai) em categorias (padrão novo, placeholder, outros, etc.) e gera listas + CSV. |
| `gerar_import_novo_produto.py` | Gera CSV para cadastrar **novo produto** (ex.: Leque) no formato Bagy 36 colunas. |
| `gerar_import_leque_variacoes.py` | Gera CSV de **variações** do Leque (cores). |
| `gerar_deltas_fase2.py` | Gera deltas de correção (placeholder, prato, vela silver). |
| `gerar_delta_boleira_h3.py` | Gera delta para produtos com descrição em `<h3>`. |
| `gerar_delta_outros.py` | Gera delta para produtos em “outros”. |
| `fix_prato_dash_delta_33.py` | Corrige “– -” em nomes de pratos (delta 33). |

### Exemplos de uso

**Análise da base atual (classificação Fase 1):**
```bash
python3 produtcs/scripts/analise_master_fase1.py "produtcs/imported/187255-products (17).csv"
```
Saída: `produtcs/work/analise_fase1_resultado.csv` e listas em `produtcs/work/analise_fase1_listas/`.

**Gerar CSV para novo produto (Leque) com variações:**
```bash
python3 produtcs/scripts/gerar_import_novo_produto.py
```
Saída: `produtcs/work/40-import-novo-leque-papel-decorativo.csv`.

**Gerar só o produto (sem variações):**
```bash
python3 produtcs/scripts/gerar_import_novo_produto.py --só-produto
```
Saída: `produtcs/work/40-import-novo-leque-papel-decorativo-só-produto.csv`.

**Gerar CSV de variações do Leque:**
```bash
python3 produtcs/scripts/gerar_import_leque_variacoes.py
```
Saída: `produtcs/work/41-import-leque-variacoes.csv`.

## Documentação

| Documento | Conteúdo |
|-----------|----------|
| [ANALISE_BASE_17.md](produtcs/docs/ANALISE_BASE_17.md) | Análise da base atual (17): números, classificação, 7 “outros”, Leque. |
| [ENRICHMENT_WORKFLOW.md](produtcs/docs/ENRICHMENT_WORKFLOW.md) | Workflow seguro para enriquecimento em massa (regras, estrutura, estratégia). |
| [IMPORT_NOVO_PRODUTO.md](produtcs/docs/IMPORT_NOVO_PRODUTO.md) | Como cadastrar produto novo por CSV (formato, Leque, variações, validação). |
| [IMPORT_TRACKING.md](produtcs/docs/IMPORT_TRACKING.md) | Controle de imports (arquivos 17, 18, 19, 28, 32, 33, etc.). |
| [TODO.md](produtcs/docs/TODO.md) | Fases de enriquecimento (velas, pratos, outros) e itens pendentes. |
| [VELA_STRATEGY.md](produtcs/docs/VELA_STRATEGY.md) | Padrões de nome e template para velas. |

## Base atual

- **Arquivo:** `produtcs/imported/187255-products (17).csv`
- **Produtos (linhas pai):** 273
- **Variações:** 640
- **Formato:** CSV Bagy, 36 colunas, UTF-8, vírgula como delimitador.

Quase todo o catálogo está no padrão de descrição adotado (✨ Descrição completa + blocos 🎉/📋/🚚/💡/❤️). Detalhes em [ANALISE_BASE_17.md](produtcs/docs/ANALISE_BASE_17.md).

## Licença

Uso interno / projeto próprio.
