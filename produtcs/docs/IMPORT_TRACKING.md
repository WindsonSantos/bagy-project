# Controle de Imports — Rastreabilidade

## Arquivos Importados

| # | Arquivo | Data | Produtos | Alterações | Status |
|---|---------|------|----------|------------|--------|
| 17 | `17-187255-products_UpdatedAllProductNames-vela-numero-name+color+texts-complete.csv` | 2026-01-26 | 59 (Vela Mini Design) | Nome + textos completos | ✅ Importado |
| 18 | `18-187255-products_UpdatedAllProductNames-vela-design-name+texts-complete.csv` | 2026-01-26 | 77 (59 Mini + 18 Design) | Nome + textos completos | ✅ Importado |
| 19 | `19-187255-products_UpdatedAllProductNames-vela-pick-name+texts-complete.csv` | 2026-01-26 | 18 (Vela Pick) | Nome + textos completos | ✅ Importado |
| 28 | `28-187255-products_UpdatedAllProductNames-velas-lote2-delta-name+texts-complete.csv` | 2026-01-26 | 51 (Espiral, Neon Glitter, Palito Gigante, Dourada Glitter, Palito, Mickey/Minnie) | Nome + textos completos (delta) | ✅ Importado |
| 32 | `32-187255-products_UpdatedAllProductNames-pratos-de-papel-delta-name+texts-complete.csv` | 2026-01-26 | 65 (Pratos de Papel) | Nome + textos (apenas integração a partir de agora) | ✅ Importado |
| 33 | `33-187255-products_UpdatedAllProductNames-pratos-fix-dash-delta.csv` | 2026-01-26 | 0 | Corrige "– -" → " - " **apenas produtos de integração**; no master atual nenhum produto de integração tinha o bug | ⏳ Pronto para import (pode ser vazio) |

---

### Regra: apenas produtos de integração
- **Alterar somente produtos com `product_external_id` preenchido.** Produtos cadastrados manualmente (product_external_id vazio) não entram em delta/import gerados por script.
- Os nomes com "– -" (ex.: Prato de Papel Xadrez Amarelo – - 18cm) no arquivo 32 referem-se a produtos **sem** product_external_id (manuais); por isso o delta 33 não os altera. Para corrigir no sistema, edite manualmente ou reverta o import do 32 para esses itens.

---

## Quando Atualizar a Base Master

### ⚠️ **ATUALIZAR BASE ANTES DE GERAR PRÓXIMO ARQUIVO**

Após importar com sucesso o último arquivo de velas (atualmente o **28**), você deve:

1. **Baixar o arquivo master atualizado** do sistema (ex.: `187255-products (11).csv`)
2. **Substituir** `produtcs/imported/187255-products_UpdatedAllProductNames.csv`
3. **Me avisar** que a base foi atualizada
4. **Só então** eu gero o próximo arquivo (próximos tipos de produto)

### Por quê?

- O arquivo master no sistema agora tem todas as correções do arquivo 18
- Se eu gerar o próximo arquivo usando a base antiga, vou sobrescrever correções já importadas
- Usando a base atualizada, eu preservo tudo que já foi feito

---

## Próximos Arquivos Planejados

- ✅ Velas — Lote 1: Mini Design (17)
- ✅ Velas — Lote 2: Design (18)
- ✅ Velas — Lote 3: Pick (19)
- ✅ Velas — Lote 4: Espiral + Neon Glitter + Palito Gigante + Dourada Glitter + Palito + Mickey/Minnie (28, delta)
- 🔄 **Próximo**: Vela Vulcão (2 produtos)
- 🔄 Depois: Outros tipos (44 produtos)

---

## Checklist Antes de Gerar Novo Arquivo

- [ ] Arquivo anterior foi importado com sucesso
- [ ] Base master foi atualizada (`produtcs/imported/187255-products_UpdatedAllProductNames.csv`)
- [ ] Confirmei que a base tem as correções do arquivo anterior
- [ ] Posso gerar o próximo arquivo

---

## Backup e Versionamento

**Recomendação**: Após cada import bem-sucedido, faça backup do arquivo master atualizado:

```
produtcs/imported/backups/187255-products_UpdatedAllProductNames-pos-import-18.csv
```

Isso permite reverter se necessário.
