# Estratégia — Enriquecimento de Velas

## Status Atual

✅ **Vela Mini Design** (59 produtos) — CONCLUÍDO  
✅ **Vela Design** (18 produtos) — CONCLUÍDO  
✅ **Vela Pick** (18 produtos) — CONCLUÍDO  
✅ **Vela Espiral** (12 produtos) — CONCLUÍDO  
✅ **Vela Neon Glitter** (10 produtos) — CONCLUÍDO  
✅ **Vela Palito Gigante** (5 produtos) — CONCLUÍDO  
✅ **Vela Dourada Glitter** (9 produtos) — CONCLUÍDO  
✅ **Vela Palito** (9 produtos) — CONCLUÍDO  
✅ **Vela Mickey/Minnie** (6 produtos) — CONCLUÍDO  

- Nome padronizado seguindo o padrão geral abaixo
- Templates aplicados no estilo `descricaoVela`
- Arquivos 17, 18, 19 e 28 (delta) usados para atualizar o sistema

---

## Próximo Passo: Vela Design (90 produtos)

### 1. Análise Inicial

**Padrões encontrados:**
- `Vela Design {Cor} {Tipo?} Numero - {num}` (ex.: "Vela Design Branco Perolizada Numero 0")
- `Vela Design {Cor} Numero - {num}` (ex.: "Vela Design Prata Numero 0")
- `Vela Design Parabens {Cor}` (ex.: "Vela Design Parabens Candy Color")

**Classificação necessária:**
- Design com números (padronizar: `Vela Design - {Cor} - N{num}`)
- Design "Parabéns" (padronizar: `Vela Design Parabéns - {Cor}`)
- Design com variações (ex.: "Perolizada")

### 2. Template Base

Já existe: `vela-design-numero-description-v1.md`

**Adaptações necessárias:**
- Para números: usar template existente
- Para "Parabéns": criar variação do template
- Incluir cor no nome quando aplicável

### 3. Processo de Execução

1. **Análise detalhada** (script Python)
   - Identificar todos os padrões de nome
   - Extrair cores e números
   - Classificar por subtipo

2. **Criação/atualização de templates**
   - Design Número (já existe, ajustar se necessário)
   - Design Parabéns (criar novo)

3. **Geração do arquivo de import**
   - Padronizar nomes
   - Preencher textos (description, short_description, meta_title, meta_description)
   - Aplicar regras de segurança (só preencher vazios)

4. **Validação**
   - 36 colunas em todas as linhas
   - Cabeçalho idêntico
   - IDs preservados

---

## Estratégia Geral para Todos os Tipos

### Padrão de Nome (quando aplicável)
- **Com número e cor**: `Vela {Tipo} - {Cor} - N{num}`
- **Com número sem cor**: `Vela {Tipo} - N{num}`
- **Sem número com cor**: `Vela {Tipo} - {Cor}`
- **Especiais**: conforme o tipo (ex.: "Vela Palito Gigante - {Cor} - {Tamanho}")

### Template Base (estilo `descricaoVela`)
```html
<p><strong>✨ Descrição completa — {Nome do Produto}</strong></p>
<p>A <strong>{Nome}</strong> é perfeita para...</p>
<p>Com visual moderno e acabamento caprichado...</p>
<p><strong>🎉 Ideal para diversas ocasiões</strong></p>
<ul><li>Aniversários...</li></ul>
<p><strong>⭐ Por que escolher este produto?</strong></p>
<ul><li>Fácil de usar</li></ul>
<p><strong>📋 Especificações do produto</strong></p>
<ul><li>Tipo: vela decorativa para bolo</li></ul>
<p><strong>ℹ️ Informações importantes</strong></p>
<p><strong>🚚 Frete e prazo</strong></p>
<p><strong>💡 Dica</strong></p>
<p><strong>❤️ Garanta a sua</strong></p>
```

### Regras de Preenchimento
- **Só preencher campos vazios** (ou placeholders curtos sem HTML)
- **Não sobrescrever** descrições manuais completas
- **Preservar** estrutura do CSV (36 colunas, delimiter, encoding)

---

## Ordem de Execução Recomendada

1. ✅ **Vela Mini Design** — CONCLUÍDO
2. ✅ **Vela Design** — CONCLUÍDO
3. ✅ **Vela Pick** — CONCLUÍDO
4. ✅ **Vela Espiral** — CONCLUÍDO
5. ✅ **Vela Neon Glitter** — CONCLUÍDO
6. ✅ **Vela Palito Gigante** — CONCLUÍDO
7. ✅ **Vela Dourada Glitter** — CONCLUÍDO
8. ✅ **Vela Palito** — CONCLUÍDO
9. ✅ **Vela Mickey/Minnie** — CONCLUÍDO
10. 🔄 **Vela Vulcão** (2)
11. 🔄 **Outros** (44) — classificar depois

---

## Checklist por Tipo

Para cada tipo de vela, seguir:

- [ ] Análise de padrões de nome
- [ ] Identificação de cores/números/tamanhos
- [ ] Criação/atualização de template
- [ ] Script de padronização de nome
- [ ] Script de preenchimento de textos
- [ ] Geração de arquivo de import
- [ ] Validação (36 colunas, estrutura)
- [ ] Teste piloto (se necessário)
- [ ] Import e validação visual
