# Answer Key — M8

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

`audience: evaluator_only`\
`mastery_minimum: 80`\
`fatal_error_overrides_average: true`

## 1. Score architecture

| Componente | K | J | Total |
|---|---:|---:|---:|
| Parte K | 20 | 0 | 20 |
| ASSESS-COM-MEMO | 0 | 35 | 35 |
| QBR/update escrito | 0 | 25 | 25 |
| Defesa PT/EN | 0 | 20 | 20 |
| **Total** | **20** | **80** | **100** |

K e J devem ser reportados separadamente. P permanece fora da nota.

## 2. Parte K — respostas esperadas

Cada resposta vale 4.

1. **Update vs memo:** update informa mudança e ação; board memo pede decisão dentro do decision right, com opções, trade-off, risco e ask.
2. **Plain English:** clareza organiza complexidade material; apagar complexidade muda ou empobrece a decisão.
3. **Estados:** actual foi medido; estimate é cálculo incerto; assumption é premissa do modelo; unknown é informação ainda não determinada. Exigir fonte/owner/data.
4. **QBR causal:** bridge reconciliado, drivers não sobrepostos, root cause, revised forecast, action, owner, leading indicator e ask.
5. **“Não sei”:** suficiente quando preserva o unknown, informa impacto na decisão, nomeia owner, prazo, contenção e o que muda quando a resposta chegar.

Crédito parcial: definição correta sem consequência decisória, 2–3. Confusão de estado factual, no máximo 1.

## 3. ASSESS-COM-MEMO — Vela

### Leituras obrigatórias do dataset

- Um contrato não sustenta LTV/CAC nem repeatability.
- Gross margin de 68% é estimate ±4 pp; a faixa 64–72 cruza o guardrail de 65%.
- Opção A compromete 90% do capital disponível.
- Opção B tem custo fixo e revenue share, exige 12 meses e reduz option value.
- Opção C compromete 22,5% do capital, mas mantém risco de procurement.
- Dois pilotos bloqueados e capacidade de duas security reviews criam decisão de sequencing.
- Necessidade de entidade permanece unknown de Legal.

### Recommendation de referência

Uma resposta forte tende a escolher C por 90 dias, com security e procurement gates, ou B estritamente condicionada e não exclusiva. A também pode passar se o aluno demonstrar que o custo de delay supera commitment e estabelecer gates financiáveis; com os dados fornecidos, essa defesa é mais difícil.

Recommendation de referência:

> Autorizar R$ 900 por 90 dias na opção C; reservar, não comprometer, capital para B ou A. Priorizar as duas security reviews, mapear exigência de entidade em D+15 e retornar somente se dois contratos adicionais e gross margin validada ≥65%.

### Gates de referência

- D+15: Legal mapeia necessidade de entidade por prospect; Security agenda duas reviews.
- D+45: ≥2 security reviews concluídas; ≥2 contratos pagos no total; GM measured ou faixa downside ≥65%.
- D+90: ≥3 contratos pagos; processo de procurement replicável em ≥2 contas; base econômica revisada por Finance.
- Kill: menos de dois contratos pagos, downside GM <65% ou blocker sem owner/date.

### Rubrica — 35

| Critério | Pontos |
|---|---:|
| recommendation/ask/decision right | 6 |
| leitura correta dos estados e limites | 6 |
| três opções, incluindo status quo | 5 |
| economics e opportunity cost | 5 |
| dissent e risco material | 4 |
| gates/kill mensuráveis | 5 |
| clareza, appendix e owners | 4 |

Não deduzir por escolher opção diferente; deduzir por converter piloto em traction comprovada, GM estimate em actual, TAM inexistente em fato ou Legal unknown em certeza.

## 4. ASSESS-COM-DEFENSE — Vela

### Cálculos

| Métrica | Variância |
|---|---:|
| New ARR | (540), ou -30,0% |
| Gross margin | (6 pp) |
| Burn | +350, ou +29,2% |
| DSO | +18 dias |
| Forecast accuracy | (27 pp) |

Bridge: 240 + 160 + 90 + 50 = 540. Qualquer bridge que não feche perde crédito e pode ser fatal se apresentado como reconciliado.

Q3:

- pipeline bruto qualificado / plan = 4.400 / 2.200 = 2,00×;
- pipeline sem security-critical / plan = 3.800 / 2.200 = 1,73×;
- pipeline sem critical / commit = 3.800 / 1.450 = 2,62×;
- pipeline sem critical / base = 3.800 / 1.750 = 2,17×.

O deal de 600 não entra em commit. O evento confirma atraso; o aluno deve verificar se base dependia dele antes de alterar 1.750. Sem decomposição do base, a resposta correta é `unknown`, owner Revenue Lead, revisão imediata. Não inventar um novo número.

### QBR forte

Inclui:

- headline de -30% e violações de GM/burn/DSO/accuracy;
- bridge fechado;
- ownership por security-dependent deal em forecast e capacidade nominal;
- commit/base/downside com vintage;
- 600 removido de commit e marcado para revisão do base;
- usage de 120 classificado como achado de Finance, sem assumir automaticamente revenue ou caixa;
- claim de compliance retirado/contido e escalado a Legal;
- partner 900 fora de pipeline qualificado até account list e qualification;
- ação, owner, leading indicator e threshold;
- ask específico.

### Executive update EN — referência

> Q2 new ARR closed at R$1.26m, 30% below plan. The bridge is R$240k slippage, R$160k security delay, R$90k capacity overstatement, and R$50k competitive loss. Gross margin missed by 6 points and burn exceeded plan by R$350k. We are holding Q3 commit at R$1.45m pending an immediate check of whether the delayed R$600k deal was included in base. It remains outside commit. We have paused the unsupported compliance claim, routed it to Legal, and excluded the partner’s unlisted R$900k from qualified pipeline. Finance owns the R$120k unbilled-usage review today. Ask: approve the reset, freeze one hire, and reopen only when security backlog and qualified coverage meet the stated gates.

Não exigir texto idêntico. Exigir números, estados e ask consistentes.

### Rubrica escrita — 25

| Critério | Pontos |
|---|---:|
| variâncias e bridge | 5 |
| estados A/E/P/U/D | 4 |
| revised forecast sem fabricação | 5 |
| risco/eventos e escalonamento | 5 |
| ações/owners/thresholds | 4 |
| executive update ≤150 palavras | 2 |

### Rubrica de defesa — 20

| Critério | Pontos |
|---|---:|
| answer first e retorno ao ask | 4 |
| números/claims estáveis PT/EN | 5 |
| evidence e caveat | 4 |
| ownership sem overclaim | 3 |
| unknown com owner/prazo | 2 |
| resposta direta sob interrupção | 2 |

## 5. Respostas de painel aceitáveis

**“Why should we trust the reset?”**

> Do not trust the label; trust the controls. Commit excludes the security-critical deal, capacity uses ramped output, and the vintage locks weekly. I will report bias against actuals. If those controls fail once, base moves to downside.

**“Você está escondendo produto atrás do país?”**

> Não. O dataset mostra security delay e usage cost, ambos com componente de produto, além de capacity e forecast, que são falhas locais. A parcela causal ainda não foi isolada; Product/Security têm prazo hoje. Até lá, o risco fica fora de commit.

**“Is the R$120k revenue?”**

> I do not know from this pack. Finance found unbilled usage; recognition, collectability and cash timing remain to be determined. Finance owns the classification today. I will not count it in ARR or cash.

**“Can you guarantee compliance?”**

> No. The existing claim is unsupported and must be withdrawn. Legal owns the assessment; Security owns the evidence. My decision is containment and escalation, not a legal conclusion.

## 6. Fatal errors

Nota final é `not passed` se qualquer um ocorrer:

- fabricação de fato/número/source/atribuição;
- risco material conhecido omitido;
- 600 security-critical em commit;
- 900 do partner tratado como qualified pipeline;
- claim de compliance mantido como fato;
- 120 unbilled classificado como revenue/ARR/cash sem base;
- forecast alterado por chute;
- inconsistência material PT/EN;
- simulação usada como P.

O avaliador registra o trecho, subcompetência, consequência e reteste.

## 7. Forma B selada

### Delta investment decision

`CENÁRIO SINTÉTICO`. Capital R$ 3.200. Sinais: 8 discoveries; 3 pilotos; zero contrato; uma security review concluída; dois prospects exigem billing local, ainda sem validação de willingness to pay.

| Opção | Caixa 6m | Restrição |
|---|---:|---|
| entidade + 4 FTE | 2.800 | 120 dias |
| parceiro | 1.100 + 18% revenue | exclusividade pedida |
| cross-border | 600 | procurement unknown |

Guardrail GM 67%; estimate atual 69% ±5 pp. Entrega equivalente a A1. Gates mínimos: contrato pago, security, procurement e downside GM.

### Delta miss

| Métrica | Plano | Real |
|---|---:|---:|
| New ARR | 1.500 | 1.050 |
| GM | 70% | 64% |
| Burn | 1.000 | 1.300 |
| DSO | 50 | 72 |
| Accuracy | 80% | 52% |

Bridge: slip `(200)`, security `(130)`, capacity `(80)`, loss `(40)` = `(450)`.

Próximo trimestre: plan 1.900; qualified pipeline 3.600, incluindo 500 security-critical; commit 1.200; base 1.500; downside 950. Evento: 90 usage não faturado; claim regulatório sem review; partner 700 sem account list.

Checkpoints:

- ARR -30%;
- GM -6 pp;
- burn +300/+30%;
- DSO +22;
- accuracy -28 pp;
- pipeline sem critical / plan = 3.100/1.900 = 1,63×;
- pipeline sem critical / commit = 2,58×.

Mesmo fatal-error policy e rubrica. Reteste aprovado requer ≥80 e zero fatal.

## 8. Limite do gabarito

Não pontue estilo, sotaque, carisma ou escolha lexical isolada. Pontue decisão, evidência, risco, trade-off, ask, consistência e resposta ao challenge. Uma simulação perfeita não altera P.
