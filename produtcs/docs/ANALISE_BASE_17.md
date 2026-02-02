# Análise da base de produtos (17) — 2026-02-01

**Arquivo:** `produtcs/imported/187255-products (17).csv`  
**Última versão da base** adicionada ao repositório. Este documento consolida o que temos no projeto e o estado atual do catálogo.

---

## 1. Resumo da base (17)

| Métrica | Valor |
|--------|--------|
| **Produtos (linhas pai)** | 273 |
| **Variações (linhas filho)** | 640 |
| **Total de linhas de dados** | 913 |
| **Colunas** | 36 (formato Bagy) |
| **Encoding** | UTF-8 |

A base segue o padrão Bagy: linha pai com `product_id` sem espaço e `variation_id` vazio; linhas de variação com `product_id` com espaço à esquerda e `variation_id` preenchido. Descrições em HTML podem conter quebras de linha dentro de campos entre aspas.

---

## 2. Classificação Fase 1 (script `analise_master_fase1.py`)

Resultado da análise sobre **187255-products (17).csv**:

| Categoria | Contagem | % | Ação |
|-----------|----------|---|------|
| **padrao_novo** | 266 | 97,4% | Já no padrão (✨ Descrição completa + blocos 🎉/📋/🚚/💡/❤️) — manter |
| **outros** | 7 | 2,6% | Descrição em outro formato (sem ✨) — revisar se quiser uniformizar |
| placeholder | 0 | 0% | — |
| vela_silver_antigo | 0 | 0% | — |
| prato_ajustar | 0 | 0% | — |
| boleira_h3 | 0 | 0% | — |

**Conclusão:** Quase todo o catálogo já está no padrão de descrição adotado (template com emojis e “✨ Descrição completa”). Não há mais placeholder genérico, velas “Silver Festas” antigas, pratos com “– -” ou descrições só com `<h3>`.

---

## 3. Os 7 produtos em “outros”

São produtos com descrição válida mas que **não** seguem o padrão “✨ Descrição completa”:

| product_id | Nome |
|------------|------|
| 9911832 | Chapéu de Festa de Papel – Degradê com dourado |
| 9911818 | Chapéu de Festa de Papel – Liso |
| 9911826 | Chapéu de Festa de Papel – Liso Neon |
| 9911836 | Chapéu de Festa de Papel – Metalizado |
| 9912089 | Kit Chá Revelação (cadastro quase vazio) |
| 9911936 | Vela Vulcão Chá Revelação |
| 9911924 | Vela Vulcão para Festa |

- **Chapéus (4):** descrição em parágrafo único, sem blocos com emojis. Opcional: alinhar ao template completo.
- **Kit Chá Revelação (9912089):** poucos campos preenchidos; provável rascunho ou produto a completar.
- **Vela Vulcão (2):** texto curto e direto; já há delta de Vela Vulcão (arquivo 29) — conferir se esse export (17) já reflete o import.

Listas por categoria em: `produtcs/work/analise_fase1_listas/`.

---

## 4. Produto novo: Leque de Papel Decorativo

Na base (17) o **Leque de Papel Decorativo** está presente e completo:

- **product_id:** 9907906  
- **Nome:** Leque de Papel Decorativo – Kit com 6 Unidades  
- **URL:** /leque-de-papel-decorativo-kit-com-6-unidades-sortido  
- **Descrição:** padrão ✨/📋/🚚/❤️  
- **Variações:** 8 (Rosa Bebê, Rosa, Amarelo, Azul Bebê, Vermelho, Azul, etc.) com `variation_id` e `color` preenchidos  
- **Categoria:** Artigos de Festa > Leque  
- **Imagens:** 7 arquivos  
- **Preço:** preenchido  

Ou seja, o fluxo de cadastro por import (arquivo 40 só-produto + 41 variações, ou 40 com variações) foi aplicado e refletido nesta base.

---

## 5. O que temos no repositório (visão geral)

### 5.1 Bases importadas (`produtcs/imported/`)

- **187255-products (17).csv** — **base atual** (esta análise).
- Versões anteriores: (1), (2), (3), (4), (5), (6), (7), (9), (10), (11), (14), (15) e arquivos datados (20260128, 20260129, 20260130, etc.).
- Uso: (15) foi a “matriz final” dos documentos de análise anteriores; (17) passa a ser a referência mais recente.

### 5.2 Documentação (`produtcs/docs/`)

| Documento | Conteúdo |
|-----------|----------|
| **ANALISE_BASE_17.md** | Este arquivo — análise da base (17). |
| **ANALISE_MASTER_20260130.md** | Análise e plano de ajustes sobre a base (15); status dos deltas 34–38. |
| **IMPORT_NOVO_PRODUTO.md** | Como cadastrar produto novo por CSV (ex.: Leque); formato 36 colunas; script e spec. |
| **IMPORT_TRACKING.md** | Controle de imports (17, 18, 19, 28, 32, 33, etc.). |
| **TODO.md** | Fases de enriquecimento (velas, pratos, outros); itens concluídos e pendentes. |
| **VELA_STRATEGY.md** | Padrões de nome e template para velas. |
| **ENRICHMENT_WORKFLOW.md** | Workflow seguro para enriquecimento em massa. |

### 5.3 Scripts (`produtcs/scripts/`)

| Script | Função |
|--------|--------|
| `analise_master_fase1.py` | Classifica linhas pai em categorias (placeholder, padrao_novo, outros, etc.); gera listas e CSV. |
| `gerar_deltas_fase2.py` | Gera deltas de correção (placeholder, prato, vela silver). |
| `gerar_delta_boleira_h3.py` | Gera delta para produtos com descrição em `<h3>`. |
| `gerar_import_novo_produto.py` | Gera CSV de novo produto (ex.: Leque) a partir de spec. |
| `gerar_import_leque_variacoes.py` | Gera CSV de variações do Leque (41). |
| `fix_prato_dash_delta_33.py` | Corrige “– -” em pratos (delta 33). |
| `gerar_delta_*` (outros) | Diversos deltas por tipo de produto. |

### 5.4 Trabalho em andamento (`produtcs/work/`)

- **Deltas já importados:** 34 (placeholder), 35 (prato), 36 (vela silver), 37 (boleira h3), 38 (h3 restante), 39 (outros), etc.
- **Import novo produto:** 40 (Leque com/sem variações), 41 (variações Leque).
- **Análise Fase 1:** `analise_fase1_resultado.csv`, `analise_fase1_listas/*.txt` (gerados a partir da base (17)).

### 5.5 Templates e specs

- **templates/** — Descrições HTML por tipo (prato, vela design, vela mini, vela neon, vela Disney, etc.).
- **lequePapelDecorativo** — Spec do Leque (nome, descrição, SEO, variações).
- **catalog/** — Mapeamentos (ex.: silverplastic-vela-mapping-v1.json).

---

## 6. Comparativo base (15) vs base (17)

| Aspecto | Base (15) | Base (17) |
|---------|-----------|-----------|
| Produtos (linhas pai) | 263 | 273 |
| padrao_novo | 165 (62,7%) | 266 (97,4%) |
| placeholder | 1 | 0 |
| vela_silver_antigo | 4 | 0 |
| prato_ajustar | 10 | 0 |
| boleira_h3 | 67 | 0 |
| outros | 16 | 7 |

A base (17) incorpora os imports feitos após (15): deltas 34–39, novo produto Leque (40/41) e possíveis outros ajustes. O saldo é **+10 produtos** e **quase 100% do catálogo** no padrão novo de descrição.

---

## 7. Próximos passos sugeridos

1. **Atualizar referência de “master”** nos docs e scripts que ainda apontam para (15) para **187255-products (17).csv**, quando for o caso.
2. **Revisar os 7 “outros”** (4 chapéus, 1 kit chá, 2 velas vulcão): decidir se entram em um delta de uniformização (template com ✨) ou permanecem como estão; Kit Chá (9912089) pode precisar de cadastro completo.
3. **Manter IMPORT_TRACKING.md** com o registro de que (17) é a base atual e, se fizer novo export no futuro, nomear como (18) e atualizar este documento.
4. **TODO.md / VELA_STRATEGY:** manter como estão; os itens pendentes (ex.: Vela Vulcão Chá, “outros” 44) continuam válidos para planejamento.

---

## 8. Checklist rápido (base 17)

- [x] 36 colunas, encoding UTF-8, estrutura Bagy (pai/variação)
- [x] 273 produtos, 640 variações, 913 linhas de dados
- [x] 97,4% no padrão “✨ Descrição completa”
- [x] Leque de Papel Decorativo (9907906) cadastrado com 8 variações
- [ ] 7 produtos em “outros” revisados (opcional)
- [ ] Doc/scripts que citam (15) como master atualizados para (17) se desejado
