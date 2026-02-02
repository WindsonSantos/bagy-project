# Workflow seguro — enriquecimento em massa (CSV de produtos)

Este documento descreve um **passo a passo repetível e seguro** para enriquecer o cadastro (texto/SEO/categorias/etc.) **sem quebrar o import**.

## Regras de segurança (não negociáveis)
- **Não alterar** delimiter, encoding, ordem/nomes das colunas.
- **Não adicionar/remover colunas**.
- **Não “normalizar” números** (ex.: `0.00` vs `0,000`) e não converter tipos.
- **Não trimar** espaços (há linhas de variação com whitespace à esquerda em `product_id`).
- **Não reserializar** o CSV “na marra” (Excel/Sheets) quando houver HTML multi-linha.
- **Sempre validar** antes de importar:
  - Cabeçalho idêntico (36 colunas, mesma ordem)
  - Todas as linhas com 36 campos
  - Row count só muda se for intencional
  - IDs preservados (`product_id`, `variation_id`)

## Estrutura de pastas
- `produtcs/imported/`
  - **Arquivos baixados do sistema** (fonte).
- `produtcs/work/`
  - **Arquivos de import** gerados por lote/etapa (01, 02, 03…).
- `produtcs/templates/`
  - Templates de texto/HTML por tipo (ex.: velas).
- `produtcs/docs/`
  - Workflow, TODO e decisões.

## Documento base atual (matriz)
- **Master de trabalho (documento final):** `produtcs/imported/187255-products (15).csv` — matriz baixada do sistema.
- A regra "apenas produtos de integração" foi suspensa por enquanto; ajustes podem ser feitos em todos os produtos. Integração será tratada depois.
- Análise do master e plano de ajustes: `docs/ANALISE_MASTER_20260130.md`

## Estratégia recomendada (por tipo de produto)
1. **Escolher um “tipo”** (ex.: Velas) e uma **subfamília** (ex.: “Vela Neon Glitter”, “Vela Design”, etc.).
2. Definir **alvo exato** (critério objetivo) para selecionar produtos:
   - Ex.: `name` contém “Vela Neon” (linha pai: `variation_id` vazio).
3. Criar um **template v1** (HTML) para:
   - `description` (HTML)
   - `short_description` (curta)
   - opcional: `meta_title`, `meta_description`, `meta_keywords`
4. (Opcional, recomendado) **Padronizar `name`** junto com o template do subtipo, **no mesmo arquivo de import**:
   - Ex.: velas `… Numero - X` → `… - Numero X`
   - Sempre com regra de match (regex) para não afetar outros produtos.
5. Rodar um **piloto pequeno** (10–20 produtos) e importar para validar.
6. Subir para lote maior (50/100/200) mantendo as mesmas validações.
6. Guardar o arquivo importado em `work/` com sequencial.

## Observações práticas do seu dataset atual
- O “master” atual (`187255-products_UpdatedAllProductNames.csv`) está consistente:
  - 36 colunas em todas as linhas
  - delimiter `,`, quotechar `\"`, LF, UTF‑8
- Você já aplicou uma regra útil:
  - `active=0` para quase todos os produtos sem imagem (bom para não exibir incompleto).

