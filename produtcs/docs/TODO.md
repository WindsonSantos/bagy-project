# TODO — Enriquecimento de catálogo (CSV)

## Fase 0 — Base (concluída)
- [x] Consolidar nomes no arquivo master (`187255-products_UpdatedAllProductNames.csv`)
- [x] Inativar produtos sem imagem (`active=0`) para não exibir na loja

## Fase 1 — Preparação
- [ ] Definir padrão de escrita (tom, estilo HTML, tamanho alvo)
- [ ] Definir regras de preenchimento:
  - [ ] Preencher somente quando o campo estiver vazio?
  - [ ] Sobrescrever manual? (recomendado: **não** sem confirmação)
- [ ] Montar “dicionário” de linhas/coleções (ex.: Silverplastic) para consistência
  - [ ] Criar mapa de subtipos por `product_external_id` (códigos do catálogo)

## Fase 2 — Velas (primeira categoria)

### Status: Em progresso
- [x] **Vela Mini Design** (59 produtos) — ✅ CONCLUÍDO
  - [x] Padronização de nome: `Vela Mini Design - {Cor} - N{num}`
  - [x] Templates criados e aplicados
  - [x] Arquivo 17 gerado com nome + textos completos

### Próximos tipos (prioridade por quantidade):

#### 2.1 — Vela Design (20 produtos) — ✅ CONCLUÍDO
- [x] Analisar padrões de nome (cores, números, variações)
- [x] Template aplicado (baseado em `vela-design-numero-description-v1.md`)
- [x] Padronizar nome: `Vela Design - {Cor} - N{num}` (quando aplicável)
- [x] Arquivo 18 gerado com nome + textos completos

#### 2.2 — Vela Pick (18 produtos) — ✅ CONCLUÍDO
- [x] Analisar padrões (cores, números)
- [x] Template aplicado (baseado em estilo descricaoVela)
- [x] Padronizar nome: `Vela Pick - {Cor} - N{num}` (ou `Vela Pick Metalizada - {Cor}`)
- [x] Arquivo 19 gerado com nome + textos completos

#### 2.3 — Vela Espiral (12 produtos) — ✅ CONCLUÍDO
- [x] Analisar variações (cores, tamanhos, tipos)
- [x] Template aplicado (baseado em estilo descricaoVela)
- [x] Padronizar nome: `Vela Espiral - {Cor}` ou `Vela Espiral Big/Metalizada - {Cor}`
- [x] Arquivo 20 gerado com nome + textos completos

#### 2.4 — Vela Neon Glitter (10 produtos) — ✅ CONCLUÍDO
- [x] Template aplicado (baseado em `vela-neon-glitter-description-v1.md`)
- [x] Analisar padrões de nome
- [x] Padronizar nome: `Vela Neon Glitter - {Cor}` (nomes já estavam corretos, corrigido meta_title/meta_description)
- [x] Arquivo 22 gerado com textos padronizados

#### 2.5 — Vela Palito Gigante (5 produtos) — ✅ CONCLUÍDO
- [x] Analisar padrões (cores, tamanhos)
- [x] Template aplicado (baseado em estilo descricaoVela)
- [x] Padronizar nome: `Vela Palito Gigante - {Cor}`
- [x] Arquivo 23 gerado com nome + textos completos

#### 2.6 — Vela Dourada Glitter (10 produtos)
- [ ] Analisar padrões (números)
- [ ] Criar template v1
- [ ] Padronizar nome: `Vela Dourada Glitter - N{num}`
- [ ] Gerar arquivo de import

#### 2.7 — Vela Palito (9 produtos) — ✅ CONCLUÍDO
- [x] Analisar padrões (cores, tamanhos)
- [x] Template aplicado (baseado em estilo descricaoVela)
- [x] Padronizar nome: `Vela Palito - {Cor}` ou variações especiais
- [x] Arquivo 25 gerado com nome + textos completos

#### 2.8 — Vela Mickey/Minnie (6 produtos) — ✅ CONCLUÍDO
- [x] Template aplicado (baseado em `vela-disney-numero-description-v1.md`)
- [x] Padronizar nome: `Vela {Mickey/Minnie} - N{num}`
- [x] Arquivo 27 gerado com nome + textos completos

#### 2.9 — Vela Vulcão Chá Revelação (2 produtos)
- [ ] Analisar padrões
- [ ] Criar template v1
- [ ] Padronizar nome
- [ ] Gerar arquivo de import

#### 2.10 — Outros tipos (44 produtos)
- [ ] Classificar e agrupar por similaridade
- [ ] Criar templates conforme necessário
- [ ] Processar em lotes

## Fase 3 — Outras categorias
- [ ] Pratos / Copos / Talheres
- [ ] Forminhas / Caixas / Embalagens
- [ ] Decoração (balões, faixas, etc.)

## Fase 4 — Qualidade & SEO
- [ ] Evitar descrições 100% idênticas (mínimo: título + 1–2 frases variáveis)
- [ ] Inserir FAQ/benefícios quando fizer sentido (sem promessas não verificadas)
- [ ] Revisar ortografia e termos (“Parabéns”, acentos, etc.)

## Fase 5 — Documentação e rastreabilidade
- [x] Criar `IMPORT_TRACKING.md` para rastrear imports
- [ ] Registrar cada import (arquivo + data + o que mudou)
- [ ] Manter templates versionados (v1, v2…)

