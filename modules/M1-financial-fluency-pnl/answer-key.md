# Answer Key — M1

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## A1

### Income statement

| Linha | R$ mil |
|---|---:|
| Revenue | 300 |
| COGS | (90) |
| Gross profit | 210 |
| Cash opex | (90) |
| D&A | (20) |
| Operating income | 100 |
| Interest | (5) |
| Net income | 95 |

### Cash flow

- Net income: `95`
- Add D&A: `+20`
- Increase AR: ending AR = `100 + 120 - 70 = 150`; increase `50`, portanto `-50`
- Increase AP: `+30`
- CFO: `95 + 20 - 50 + 30 = 95`
- CFI: capex `-50`
- CFF: principal `-20`
- Net change cash: `25`
- Ending cash: `525`

### Balance sheet

- Cash `525`
- AR `150`
- Equipment net: `200 + 50 - 20 = 230`
- Assets `905`
- AP `110`
- Debt `100`
- Equity: `600 + 95 = 695`
- Liabilities + equity `905`

Checks: balance `0`; cash flow ending cash equals balance sheet cash.

Fatal errors: interest em financing cash flow; principal como expense; D&A omitida do PPE; AR tratado como cash; balanço ajustado por plug.

## A2 — solução de referência

Valores de M24, R$ mil, tolerância ±0,1:

| Cenário | Revenue | Gross margin | Operating income | Ending cash |
|---|---:|---:|---:|---:|
| Base | 4.670,7 | 72,0% | 2.266,3 | 24.031,1 |
| Upside | 6.974,0 | 73,4% | 3.944,4 | 34.473,1 |
| Downside | 2.269,5 | 67,8% | 505,6 | 11.065,6 |

O arquivo deve mostrar `MODEL STATUS = PASS`. Forecast error usa `(actual − forecast)/forecast`; bias preserva sinal, erro absoluto não. A recomendação não é única, mas precisa usar os resultados acima, explicar drivers da aba Variance e declarar alternativa/trigger.

## A3 — elementos esperados

1. Collection/aging, renewal timing, billing mix, service delivery/revenue recognition, credits/disputes e mudança de payment terms.
2. Pode melhorar CFO temporariamente e piorar supplier risk; separar source de caixa e sustentabilidade.
3. Capacity, ramp, coverage, win rate, ACV/usage, margin, hiring lead time, downside funding e kill criterion.
4. Open não gera payroll; approved cria compromisso/opção; started tem payroll, ramp e custo de reversão.
5. Quando exposure é material, recorrente, fora do appetite/authority local ou exige hedge/funding. Quantificar antes de escalar.

## Rubrica

| Critério | Peso | 4 — forte | 2 — parcial | 0 — falha |
|---|---:|---|---|---|
| Reconciliação | 25 | todas as demonstrações e checks fecham | erro imaterial explicado | mismatch/plug |
| Mecânica financeira | 25 | timing e signs corretos | lacuna localizada | lucro=caixa/erro material |
| Forecast | 20 | drivers, vintages e bridge | cenário superficial | budget mascarado |
| Julgamento | 20 | trade-off, alternativa e trigger | recomendação genérica | decisão sem economics |
| Comunicação | 10 | QBR conciso e decision-ready | excesso de detalhe | risco material omitido |

Nota mínima 80/100 e zero fatal errors.

## Form B — reteste focal

- Reconciliação: repita A1 com cash inicial 620, AR 80, equipment 240, AP 70, debt 150, equity 720; revenue 360 (210 cash/150 prazo), COGS 108 (72 cash/36 AP), cash opex 105, D&A 25, capex 40, collection 55, principal 30 e interest 6. Gabarito: operating income 122; net income 116; ending AR 175; ending AP 106; CFO 82; CFI (40); CFF (30); ending cash 632; PPE 255; assets e liabilities+equity 1.062.
- Forecast: use o cenário Downside já versionado na planilha; reporte M12 e M24, cash minimum e três ações condicionadas. Inputs não podem ser alterados.
- Fatal error original deve ser medido isoladamente e não pode ser compensado por média.
