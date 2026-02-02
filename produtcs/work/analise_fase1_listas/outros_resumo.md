# Produtos "outros" (16) — o que está fora do padrão

Estes produtos **não** entram em nenhuma das regras da Fase 1 (placeholder, vela_silver_antigo, prato_ajustar, boleira_h3, padrao_novo).  
O padrão do catálogo exige: **nome** em Title Case, **descrição** com cabeçalho `✨ Descrição completa — ...` e blocos 🎉, 📋, ℹ️, 🚚, 💡, ❤️.

---

## 1. Talheres Eco Madeira (4 produtos)

| product_id | Nome |
|------------|------|
| 9834079 | Colher Eco Madeira Estampada – 10 Unidades |
| 9834099 | Colher Sobremesa Eco Madeira Estampada – 10 Unidades |
| 9834059 | Faca Eco Madeira Estampada – 10 Unidades |
| 9834037 | Garfo Eco Madeira Estampado – 10 Unidades |

**Fora do padrão:** Descrição curta (um parágrafo), sem `✨ Descrição completa`, sem blocos (🚚 Frete, 💡 Dica, ❤️ Garanta o seu). Nomes OK (Title Case, hífen).

---

## 2. Cortina (1 produto)

| product_id | Nome |
|------------|------|
| 9833627 | Cortina Metalizada Decorativa 100x200cm |

**Fora do padrão:** Descrição no formato antigo (“A **Cortina...** da Silver Festas...”), sem ✨ e sem blocos padronizados.

---

## 3. Lança Confete (1 produto)

| product_id | Nome |
|------------|------|
| 9840809 | Lança Confete Colorido 30cm |

**Fora do padrão:** Descrição em texto corrido, com “Características:”, “Marca: Silver Festas” solto; sem ✨ e sem estrutura de blocos.

---

## 4. Velas Metalizada Torcida (3 produtos)

| product_id | Nome |
|------------|------|
| 9883299 | Vela Metalizada Torcida - Dourada - 15 CM |
| 9883297 | Vela Metalizada Torcida - Prata - 15 CM |
| 9883298 | Vela Metalizada Torcida - Rose Gold - 15 CM |

**Fora do padrão:**  
- **Descrição:** só uma frase em ALL CAPS (ex.: “VELA METALIZADA TORCIDA DOURADA 15 CM”) — praticamente placeholder.  
- **Nome:** “15 CM” em maiúsculas; o ideal seria “15 cm”.

---

## 5. Vela Mini Design — descrição antiga (6 produtos)

| product_id | Nome |
|------------|------|
| 9825330 | Vela Mini Design - Amarelo Candy |
| 9825230 | Vela Mini Design - Branco |
| 9832758 | Vela Mini Design - Bronze |
| 9825554 | Vela Mini Design - Dourado |
| 9832929 | Vela Mini Design - Lilás |
| 9825131 | Vela Mini Design - Verde Candy |

**Fora do padrão:** Descrição com uma frase só (“A Vela Número Mini Design ... da Silver Festas...”), sem `✨ Descrição completa` e sem blocos. Nomes já no padrão (Vela Mini Design - Cor).

*Nota: O script não os colocou em `vela_silver_antigo` porque o nome não tem “Vela Número” nem “| Silver Festas”; só a descrição menciona Silver Festas.*

---

## 6. Vela Palito Neon Glitter (1 produto)

| product_id | Nome |
|------------|------|
| 9882939 | Vela Palito Neon Glitter |

**Fora do padrão:** Descrição só “VELA PALITO NEON GLITTER” (ALL CAPS, placeholder). Sem conteúdo real.

---

## Resumo por tipo

| Tipo | Qtd | Principais problemas |
|------|-----|----------------------|
| Talheres Eco | 4 | Descrição curta, sem template completo |
| Cortina | 1 | Descrição formato antigo |
| Lança Confete | 1 | Descrição corrida, sem estrutura |
| Vela Metalizada Torcida | 3 | Descrição ALL CAPS / placeholder; “15 CM” no nome |
| Vela Mini Design | 6 | Descrição uma frase, sem template v1 |
| Vela Palito Neon Glitter | 1 | Descrição placeholder ALL CAPS |
| **Total** | **16** | |

---

## Sugestão para “deletar e criar novos”

- **Deletar da base** faz sentido se:
  - Você quer recriar com nome + descrição já no padrão.
  - Evita misturar produtos antigos com novos (menos risco de sobrescrever correções).
- **Manter e só ajustar** faz sentido se:
  - Quiser preservar `product_id` / histórico / vendas (quando aplicável).
  - For pouco volume e der para padronizar em um delta (ex.: talheres, cortina, lança, velas torcidas, Mini Design restantes, palito).

Se optar por deletar, use esta lista de `product_id` para exclusão em lote; depois crie os novos produtos já com o template de nome e descrição definido no projeto.
