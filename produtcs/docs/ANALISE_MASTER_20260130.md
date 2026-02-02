# Análise do master 2026-01-30 — Relatório e plano de ajustes

**Documento base (matriz final):** `produtcs/imported/187255-products (15).csv` — arquivo baixado do sistema  
**Objetivo:** Identificar o que está fora do padrão (nomes e descrições) que vínhamos seguindo e propor um plano de ajustes.  
**Contexto:** Estratégia de “apenas produtos integrados” foi abandonada por enquanto; vamos ajustar todos os produtos e depois tratar integração.

---

## 1. Padrões de referência (histórico do projeto)

### 1.1 Nomes

| Categoria | Padrão desejado | Fonte |
|----------|------------------|--------|
| **Vela Mini Design** (número) | `Vela Mini Design - {Cor} - N{num}` (ex.: Vela Mini Design - Rosa Candy - N1) | TODO.md, VELA_STRATEGY.md |
| **Vela Design** (número) | `Vela Design - {Cor} - N{num}` | idem |
| **Vela Pick** | `Vela Pick - {Cor} - N{num}` ou `Vela Pick Metalizada - {Cor}` | idem |
| **Vela Espiral** | `Vela Espiral - {Cor}` ou `Vela Espiral Big/Metalizada - {Cor}` | idem |
| **Vela Neon Glitter** | `Vela Neon Glitter - {Cor}` | idem |
| **Outras velas** (Palito, Mickey/Minnie, etc.) | `Vela {Tipo} - {Cor}` ou com N{num} quando aplicável | idem |
| **Prato de Papel** | `Prato de Papel {Tema} - {Cor} - {tamanho} - {quantidade}` ou `Prato de Papel {Tema} - {tamanho} - {quantidade}`; usar " - " (hífen com espaços), nunca "– -" | prato-de-papel-description-v1.md |
| **Outros** | Title case, sem ALL CAPS; "Prato de Papel" e não "Prato Papel" quando for o caso | convenção geral |

### 1.2 Descrições (HTML)

Padrão “último” que estávamos usando (templates em `produtcs/templates/` e estilo `descricaoVela`):

- **Abertura:** `<p><strong>✨ Descrição completa — {Nome do Produto}</strong></p>`
- **Parágrafos** com `<p>`, `<strong>` para destaque do nome e características
- **Blocos com emojis e títulos claros:**
  - `🎉 Ideal para diversas ocasiões`
  - `⭐ Por que escolher este produto?`
  - `📋 Especificações do produto`
  - `ℹ️ Informações importantes`
  - `🚚 Frete e prazo`
  - `💡 Dica`
  - `❤️ Garanta a sua / Garanta o seu`
- **Especificações** em lista `<ul>/<li>` com `<strong>Material:</strong>`, `<strong>Tamanho:</strong>`, etc.
- **Short description:** frase curta, acentuada, sem placeholder genérico

---

## 2. O que está fora do padrão no master 20260130

### 2.1 Descrições com placeholder genérico

- **Padrão errado:** texto que começa com  
  **"- Para decorar e festejar, encontre aqui os produtos que você precisa. Possuímos uma grande diversidade de balões, suportes e decoração..."**  
  e depois "Detalhes do Produto", "Tamanho do Produto" em formato listado simples.
- **Exemplo no CSV:** primeiro produto (9840811 – Bandeja Prato Retangular - Descartável - 5 Unidades).
- **Ação:** substituir por descrição no padrão completo (por tipo de produto), com ✨/📋/🎉/⭐ etc.

### 2.2 Velas com nome e descrição no formato “Silver Festas” (antigo)

- **Nomes fora do padrão:**
  - "Vela Número Candy Color Amarelo | Silver Festas"
  - "Vela Número Mini Design Lilás | Silver Festas"
  - "Vela Número Azul | Silver Festas"
  - Ou seja: "Vela Número {Cor} | Silver Festas" ou "Vela Número Mini Design {Cor} | Silver Festas", **sem** o padrão `Vela Mini Design - {Cor} - N{num}`.
- **Descrições fora do padrão:**
  - Começam com `<p><strong>A Vela Número Mini Design {Cor}</strong> da Silver Festas é ideal para...`
  - Usam `<p><strong>Benefícios</strong></p>` e `<p><strong>Especificações</strong></p>` **sem** os emojis e **sem** o título "✨ Descrição completa —".
  - Não seguem o bloco 🎉/⭐/📋/ℹ️/🚚/💡/❤️.
- **Exemplos de product_id no CSV:** 9825330 (Candy Color Amarelo), 9832929 (Mini Design Lilás), 9818958 (Número Azul), e outros no mesmo estilo.
- **Ação:** padronizar nome para `Vela Mini Design - {Cor} - N{num}` (ou Design/Pick/etc. conforme o tipo) e reescrever descrição no template v1 (✨ Descrição completa, 📋 Especificações do produto, etc.).

### 2.3 Velas já no padrão (referência positiva)

- **Nomes corretos:** ex. "Vela Mini Design - Rosa Candy - N0", "Vela Mini Design - Rosa - N1" (product_id 9883423, 9883424, 9883403, 9883404, etc.).
- **Descrições corretas:** contêm "✨ Descrição completa —", "📋 Especificações do produto", "🎉 Ideal para diversas ocasiões", "⭐ Por que escolher este produto?", etc., em uma única linha de HTML (minificado).
- **Nenhuma alteração necessária** nesses; servem de modelo para os demais.

### 2.4 Boleiras e outros produtos com <h3> em vez do padrão com emojis

- **Padrão atual no CSV:** descrições com `<h3>Benefícios</h3>`, `<h3>Especificações</h3>`, `<h3>Variação</h3>`, sem "✨ Descrição completa", sem 🎉/⭐/📋/ℹ️/🚚/💡/❤️.
- **Exemplo:** Boleira Desmontável G/M/P (9814477, 9814449, 9814474).
- **Ação (recomendação):** opcional; podemos manter esse estilo para boleiras ou, em fase posterior, alinhar ao padrão com emojis e "✨ Descrição completa" para uniformidade.

### 2.5 Pratos de Papel

- No master 20260130 não foi feita uma varredura linha a linha; em versões anteriores tínhamos:
  - "Prato Papel" em vez de "Prato de Papel".
  - Nomes com "– -" (en-dash + hífen) em vez de " - " (apenas hífen com espaços).
  - Descrições sem o template completo (✨/📋/🎉/⭐, etc.).
- **Ação:** na análise por script ou na próxima etapa, listar todos os "Prato" / "Prato de Papel" e corrigir nome + descrição conforme `prato-de-papel-description-v1.md`.

### 2.6 Outros possíveis desvios

- Nomes em ALL CAPS ou com inconsistência de title case.
- "Prato Papel" em vez de "Prato de Papel".
- meta_title / meta_description vazios onde já temos nome e descrição padronizados (oportunidade de preencher).
- short_description com texto genérico ou placeholder.

---

## 3. Resumo quantitativo — Fase 1 (resultado do script)

**Fonte:** `scripts/analise_master_fase1.py` sobre o master **`187255-products (15).csv`** (matriz final).

| Categoria | Contagem | % | Ação |
|-----------|----------|---|------|
| **placeholder** | 1 | 0,4% | Reescrever descrição no padrão completo |
| **vela_silver_antigo** | 4 | 1,5% | Nome → Vela Mini Design - Cor - Nn; descrição → template v1 |
| **prato_ajustar** | 10 | 3,8% | Corrigir "– -" → " - " no nome; descrição template prato se necessário |
| **boleira_h3** | 67 | 25,5% | Opcional: alinhar ao padrão com emojis |
| **padrao_novo** | 165 | 62,7% | Já no padrão — manter |
| **outros** | 16 | 6,1% | Revisar manualmente ou classificar depois |
| **Total (linhas pai)** | **263** | 100% | |

**Arquivos gerados (Fase 1):**
- `work/analise_fase1_resultado.csv` — todos os produtos com coluna `categoria`
- `work/analise_fase1_listas/{categoria}.txt` — um product_id por linha, por categoria

---

## 4. Plano de ajustes sugerido

### Fase 1 — Diagnóstico preciso (recomendado antes de alterar em massa)

1. **Script de análise** (ou planilha filtrada) sobre `187255-products_20260130.csv`:
   - Listar todas as linhas **pai** (variation_id vazio) com: product_id, name, primeiros 200 caracteres de description, short_description.
   - Classificar:
     - Descrição começa com "- Para decorar e festejar" → **placeholder**.
     - Descrição contém "✨ Descrição completa" → **padrão novo**.
     - Descrição contém "Silver Festas" e "Benefícios"/"Especificações" sem ✨ → **formato Silver antigo**.
     - Nome "Vela Número" mas não "Vela Mini Design -" / "Vela Design -" → **nome fora do padrão**.
     - Nome contém "Prato Papel" (sem "de") ou "– -" → **prato a padronizar**.
2. **Contagens e lista de product_id** por grupo para priorizar e gerar deltas.

### Fase 2 — Correções por grupo

1. **Placeholder "- Para decorar e festejar"**  
   - Identificar todos os product_id afetados.  
   - Para cada um, definir tipo (bandeja, prato, etc.) e gerar description + short_description (e meta se fizer sentido) no padrão completo.  
   - Gerar arquivo de import (delta) só com essas linhas.

2. **Velas "Silver Festas" (nome + descrição)**  
   - Mapear product_id → tipo (Mini Design, Design, etc.), cor e número a partir do nome atual.  
   - Aplicar padrão de nome: `Vela Mini Design - {Cor} - N{num}` (ou Design/Pick conforme o caso).  
   - Aplicar template v1 de descrição (vela-mini-design-numero-description-v1.md ou o correspondente).  
   - Preencher meta_title, meta_description, short_description.  
   - Gerar delta de import.

3. **Pratos de Papel**  
   - Listar todos os pratos; corrigir "Prato Papel" → "Prato de Papel" e "– -" → " - ".  
   - Aplicar template prato-de-papel-description-v1.md onde a descrição não estiver no padrão.  
   - Gerar delta de import.

4. **Boleiras (opcional)**  
   - Se quiser uniformizar: reescrever descrição com "✨ Descrição completa" e blocos 🎉/⭐/📋/ℹ️/🚚/💡/❤️.  
   - Caso contrário, deixar como está.

### Fase 3 — Validação e import

- Todo arquivo de import: manter 36 colunas, mesmo cabeçalho, sem alterar estrutura.  
- Validar em piloto (poucos produtos) antes de import em massa.  
- Após cada import bem-sucedido, atualizar o master local (e backup) conforme `IMPORT_TRACKING.md`.

---

## 5. Referências no repositório

- **Padrão de nomes (velas):** `docs/TODO.md`, `docs/VELA_STRATEGY.md`
- **Templates de descrição:**  
  - `templates/vela-mini-design-numero-description-v1.md`  
  - `templates/prato-de-papel-description-v1.md`  
  - `descricaoVela` (estilo geral)
- **Workflow e segurança:** `docs/ENRICHMENT_WORKFLOW.md`
- **Rastreio de imports:** `docs/IMPORT_TRACKING.md`

---

## 6. Status das fases

| Fase | Status | Observação |
|------|--------|------------|
| **Fase 1 — Diagnóstico** | ✅ Concluída | Script `scripts/analise_master_fase1.py`; listas em `work/analise_fase1_listas/`. Master: `187255-products (15).csv`. |
| **Fase 2 — Correções por grupo** | ✅ Concluída | Deltas gerados: `34-delta-placeholder.csv` (1 linha), `35-delta-prato-ajustar.csv` (20 linhas), `36-delta-vela-silver-antigo.csv` (48 linhas). Script: `scripts/gerar_deltas_fase2.py`. |
| **Fase 3 — Validação e import** | ⏳ Pendente | Após cada delta, validar e atualizar master. |

---

## 7. Deltas — Status de import

Arquivos em `produtcs/work/` (só linhas alteradas; mesmo cabeçalho e 36 colunas do master):

| Arquivo | Conteúdo | Linhas | Status |
|---------|----------|--------|--------|
| `34-delta-placeholder.csv` | Bandeja (9840811): descrição/meta no padrão ✨/📋 | 1 | ✅ Importado |
| `35-delta-prato-ajustar.csv` | 10 pratos: corrige "– -" → " - " no nome e textos | 20 | ✅ Importado |
| `36-delta-vela-silver-antigo.csv` | 4 velas: nome "Vela Mini Design - Cor - Nn" + descrição template v1 | 48 | ✅ Importado |
| `37-delta-boleira-h3.csv` | 67 produtos (boleiras, copos, guardanapos, canudos): descrição com ✨ + 🎉/📋 + 🚚/💡/❤️ | 318 | ✅ Importado |
| `38-delta-h3-restante.csv` | 9 produtos (pratos com descrição em &lt;h3&gt;): mesmo padrão ✨/📋/🚚/💡/❤️ | 18 | ✅ Importado |

**Script para 37/38:** `scripts/gerar_delta_boleira_h3.py` (usa lista `boleira_h3.txt`; master (15).csv)

---

## 8. Próximo passo (opcional)

- **Deltas 34 a 38** — todos importados.
- Revisar os **16 produtos** em **outros** (lista em `work/analise_fase1_listas/outros.txt`) e classificar/ajustar se precisar.
- Master atual: `187255-products (15).csv`. Para reanalisar: `python3 scripts/analise_master_fase1.py "imported/187255-products (15).csv"`.
