# M1 — Fluência financeira e P&L de país

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## 1. Decisão executiva central

O plano mostra crescimento. O caixa cai. O previsão piora. HQ pergunta se deve liberar oito contratações ou congelar o Brasil.

Sua decisão não é “cortar custo” nem “defender o mercado”. É identificar:

1. o que mudou economicamente;
2. onde a mudança aparece em lucro, caixa e capital;
3. o que é timing, o que é deterioração estrutural e o que é erro de modelo;
4. qual ação preserva a opção de crescimento;
5. qual limite exige escalonamento.

Um country executive não precisa fechar a contabilidade estatutária. Precisa ler o sistema financeiro sem se esconder atrás do controller.

## 2. Como escolher a profundidade

Este módulo não presume experiência, senioridade ou lacunas do aluno. Use o diagnóstico por competência e o objetivo escolhido para decidir o que estudar. Sem avaliação, a recomendação é provisória: estudar ou fazer a prova de entrada. Cargo, tempo de carreira e autoavaliação não dispensam conteúdo. As regras da edição pública em `diagnostic/README.md` prevalecem sobre referências legadas a placement, avaliação para dispensa ou M0.

## 3. Conhecimentos prévios e avaliação para dispensa

M1 só admite avaliação para dispensa por subcompetência depois de M0:

- `FIN-01`: accrual/cash e reconhecimento;
- `FIN-02`: três demonstrações;
- `FIN-03`: P&L de país;
- `FIN-04`: previsão e bridge;
- `FIN-05`: cash, working capital e FX.

Cada subcompetência exige `K ≥ 85`, `J ≥ 80`, dois casos e zero erro crítico. Uma média alta não libera uma subcompetência com erro local. Enquanto M0 está pendente, faça tudo.

## 4. Objetivos de aprendizagem

Ao final, sem IA, você consegue:

1. registrar dez eventos simples em regime de competência e caixa;
2. conectar lucro líquido ao cash flow e ao balanço;
3. construir um P&L gerencial de 24 meses por receita, COGS, opex e responsabilidade;
4. fechar um rolling previsão com base/upside/downside;
5. produzir bridge de volume, preço, mix, churn, FX, timing e custo;
6. diagnosticar AR, deferred revenue, working capital e runway;
7. conduzir QBR com recommendation, ask, responsável e gatilho.

## 5. Mapa de conceitos em uma página

```text
Contrato
  ├─ billing ──> accounts receivable ──> collection ──> cash
  └─ prestação ──> revenue ──> gross profit ──> operating income
                         │
                         └─ retained earnings/equity

Income statement ── net income ──┐
                                 ├─ Cash flow reconciliation ── ending cash
Balance sheet changes ───────────┘                │
                                                 └─ Balance sheet cash

Plano anual ── rolling forecast ── actual ── variance bridge ── decisão
     │                  │                              │
 headcount          cenários                    owner + trigger
```

## 6. Lições

### L1 — Receita não é billing; billing não é caixa

Regime de competência registra a atividade econômica quando a obrigação é satisfeita, não quando o dinheiro entra ou sai. Em assinatura paga antecipadamente:

- invoice cria receivable e contract liability/unearned revenue;
- collection reduz receivable e aumenta cash;
- prestação reduz contract liability e reconhece revenue.

No 10-K FY2026, a Salesforce explica que normalmente fatura assinaturas antecipadamente e reconhece unearned revenue quando o serviço é prestado. O filing mostra o saldo de unearned revenue passando de US$20,743 bilhões para US$24,317 bilhões; isso não significa “receita escondida”, nem caixa disponível sem obrigação. `[SRC-FIN-SALESFORCE-10K-2026]`

**Perguntas de decisão**

- O cliente foi faturado? pagou? recebeu o serviço?
- Existe obrigação futura associada ao caixa recebido?
- A receita é ratable, point-in-time ou baseada em uso?
- Há risco de refund, credit, service-level penalty ou collectability?

**Erro fatal:** lançar contrato assinado como receita e caixa no mesmo instante sem examinar prestação, billing e collection.

#### Exemplo resolvido 1 — assinatura anual

`CENÁRIO SINTÉTICO`. Em 1º de janeiro, cliente assina 12 meses por R$120 mil, faturados e pagos no início.

No dia do pagamento:

- Cash `+120`;
- Contract liability `+120`;
- Revenue `0`;
- Profit `0`.

Após janeiro:

- Revenue `+10`;
- Contract liability `-10`;
- se COGS de janeiro foi `3`, gross profit `7`;
- cash não muda pelo reconhecimento.

Após seis meses, antes de novos eventos:

- receita acumulada `60`;
- liability remanescente `60`;
- cash ainda contém o recebido, menos pagamentos efetuados;
- lucro acumulado depende dos custos, não do saldo bancário.

**Decisão:** não financiar headcount permanente usando toda entrada anual como se fosse margem já ganha. Modele a obrigação e o burn.

### L2 — As três demonstrações formam um sistema

O 10-K contém income statement, balance sheet, cash flow e notas; o Investor.gov orienta usar também Business, Risk Factors e MD&A para interpretar o conjunto. `[SRC-FIN-INVESTOR-10K]`

**Income statement**

Mostra performance durante um período:

`Revenue – COGS = Gross profit`\
`Gross profit – operating expenses = Operating income`\
`Operating income ± non-operating items – tax = Net income`

**Balance sheet**

Mostra posição numa data:

`Assets = Liabilities + Equity`

**Cash flow**

Explica a mudança de caixa por operação, investimento e financiamento:

`Beginning cash + CFO + CFI + CFF + FX = Ending cash`

No método indireto:

`Net income + noncash items – increases in operating assets + increases in operating liabilities = CFO`

Na Salesforce FY2026, net income foi US$7,457 bilhões e CFO foi US$14,996 bilhões. A diferença inclui D&A, stock-based compensation e working-capital movements. O aumento de AR consumiu caixa; o aumento de unearned revenue favoreceu caixa. `[SRC-FIN-SALESFORCE-10K-2026]`

#### Exemplo resolvido 2 — fechar o loop

`CENÁRIO SINTÉTICO`, valores em R$ mil. Abertura: cash 100, AR 0, equipment 0, liabilities 0, equity 100.

Eventos:

1. vende serviço por 60 a prazo; custo reconhecido 20, ainda não pago;
2. compra equipamento à vista por 30;
3. recebe 40 do cliente;
4. paga 15 ao fornecedor.

Income statement:

- revenue 60;
- COGS 20;
- net income antes de impostos 40.

Cash flow:

- CFO: `net income 40 – increase AR 20 + increase AP 5 = 25`;
- CFI: `-30`;
- net cash change `-5`;
- ending cash `95`.

Balance sheet:

- cash 95;
- AR 20;
- equipment 30;
- assets 145;
- AP 5;
- equity 140 (`100 + 40`);
- liabilities + equity 145.

O lucro de 40 coexistiu com queda de caixa de 5. O modelo fecha.

**Erro fatal:** inserir “cash plug” para fazer o balanço bater sem explicar o evento faltante.

### L3 — P&L de país é contrato de responsabilidade

Um P&L gerencial precisa declarar:

- moeda funcional e moeda de reporte;
- períodos e vintage do previsão;
- revenue attribution: contracting entity, customer location ou seller credit;
- custos controláveis, alocados e não controláveis;
- política de transfer pricing e shared services, se aplicável;
- regra para COGS de cloud/inference/support;
- responsável de cada linha;
- tratamento de headcount aprovado, aberto e iniciado.

Sem essas definições, “Brasil bateu o plano” pode ser uma disputa de alocação, não um resultado.

**Estrutura mínima**

1. revenue: new, expansion, contraction, churn, usage;
2. COGS: inference/cloud, support, payment fees, service delivery;
3. gross profit e gross margin;
4. sales, marketing, success, product/localization, G&A;
5. margem de contribuição;
6. allocations claramente separadas;
7. operating income gerencial;
8. cash items: collections, capex, taxes, intercompany financiamento.

#### Exemplo resolvido 3 — contratação que “melhora” o P&L tarde demais

`CENÁRIO SINTÉTICO`. Um AE custa R$45 mil/mês com todos os custos incluídos, começa em abril, leva três meses para ramp e fecha receita reconhecida de R$80 mil/mês a partir de julho, com 25% de COGS.

Incremento anual:

- opex: `9 × 45 = 405`;
- revenue: `6 × 80 = 480`;
- gross profit: `480 × 75% = 360`;
- contribuição no ano: `360 – 405 = -45`.

No run-rate pós-ramp:

- monthly gross profit `60`;
- monthly contribution `15`;
- payback sobre o investimento de ramp deve considerar o caixa desembolsado, timing de billing e risco de churn.

**Decisão:** a contratação pode destruir resultado no ano e ainda ser correta se o hurdle, financiamento e leading indicators estiverem explícitos. Não chame run-rate futuro de lucro realizado.

### L4 — Budget é compromisso; previsão é melhor estimativa

Budget não deve ser “corrigido” para esconder miss. Previsão não deve ser mantido artificialmente para proteger o budget.

- **Budget/AOP:** alocação e compromisso aprovado.
- **Actual:** evento registrado com cut-off.
- **Previsão:** melhor estimativa atual, datada.
- **Outlook:** faixa executiva com incerteza.
- **Scenario:** mundo coerente condicionado a premissas.

Um rolling previsão responde:

1. qual resultado agora é mais provável;
2. o que mudou desde o último vintage;
3. qual driver explica a mudança;
4. o que a equipe controla;
5. qual decisão melhora o resultado;
6. quanto erro histórico existe no processo.

**Bridge aditivo**

`Previous forecast + volume + price + mix + expansion – contraction – churn + FX + timing + cost = New forecast`

Cada componente tem sinal, unidade, responsável e evidência. Não use “execution” como balde residual.

**Previsão accuracy**

Para uma métrica de receita:

- erro: `Actual – Forecast`;
- absolute percentage error: `|Actual – Forecast| / |Actual|`, quando actual não é zero;
- bias: média de `Forecast – Actual`; positivo recorrente indica overforecast.

Não agregue percentuais de unidades diferentes. Use valor absoluto ou erro ponderado.

### L5 — Caixa, working capital e FX

Working capital é timing operacional:

- AR cresce quando revenue/billing antecede collection;
- AP cresce quando o pagamento fica para depois;
- deferred/unearned revenue cresce quando billing precede prestação;
- prepaid expense consome caixa antes da despesa.

**Runway**

`Runway = available liquidity / normalized net cash burn`

Use burn normalizado, não um mês favorecido por recebimento anual. Se o burn muda com cenário, mostre a curva mensal.

**FX**

Separe:

1. transaction exposure: contrato/recebimento em moeda distinta do custo;
2. translation exposure: converter demonstração local para HQ;
3. economic exposure: pricing e demanda mudam com câmbio.

No exercício, a taxa oficial do BCB é referência auditável; não é a taxa econômica contratada. `[SRC-FX-BCB]`

**Escalar**

- controller: cut-off, reconhecimento, alocação e reconciliação;
- CFO/treasury: financiamento, liquidity, hedge, covenant e material FX exposure;
- tax counsel: incidência e estrutura;
- bank/FX provider: execução de câmbio;
- legal: obrigação contratual e collectability.

O executivo identifica o issue, quantifica materialidade e chama o especialista; não emite parecer improvisado.

### L6 — Fechamento, QBR e accountability

Um ciclo útil:

1. freeze de actual e reconciliações;
2. update de drivers por responsáveis;
3. finance challenge independente;
4. previsão lock com vintage;
5. bridge para o último previsão e budget;
6. pre-read 24–48h antes;
7. QBR focado em exceções e decisões;
8. decision log com responsáveis e limites;
9. revisão de previsão accuracy.

QBR ruim descreve vinte métricas. QBR bom declara:

- `miss/beat`;
- três drivers suficientes para reconciliar;
- o que mudou na visão;
- ação já tomada;
- ask a HQ;
- risco que exige escalonamento;
- gatilho de nova revisão.

## 7. Práticas guiadas

### GP1 — Teardown real da Salesforce

Use o filing FY2026 e preencha:

1. revenue, cost of revenue, operating expenses, operating income, net income;
2. cash, AR, unearned revenue e current liabilities;
3. CFO, CFI e CFF;
4. cinco reconciling items entre net income e CFO;
5. cinco movimentos que podem melhorar EBITDA e piorar caixa.

Não conclua “melhor/pior” sem definir horizonte e causa.

### GP2 — P&L Brasil de 24 meses

Use `templates/pnl-forecast.xlsx`. Preencha base/upside/downside; mantenha premissas em células próprias; execute os choques do caso.

### GP3 — Previsão bridge e QBR

Feche três ciclos. Em cada ciclo:

- trave o vintage anterior;
- registre actual;
- explique 100% da variação material;
- atualize o cenário;
- escreva recommendation e ask em uma página.

## 8. Caso real documentado e cenário sintético

O caso real é o filing Salesforce FY2026; a tarefa está em `cases.md`. O cenário Brasil é integralmente sintético e não representa economics das empresas-alvo.

## 9. Erros executivos frequentes e sinais de alerta

- receita tratada como caixa;
- bookings/ARR misturados com GAAP revenue;
- gross margin calculada sem carga de trabalho/inference/support;
- headcount “aprovado” contado como gasto sem start date;
- previsão igual ao budget apesar de novos dados;
- FX usado como explicação residual;
- AR vencido sem aging/responsável;
- cenário downside sem contingência;
- cash plug ou “other” que fecha o modelo;
- QBR que pede confiança em vez de decisão.

## 10. Checklist de decisão

- [ ] Período, moeda, unidade e as-of date declarados.
- [ ] Revenue attribution e recognition definidos.
- [ ] Três demonstrações fecham.
- [ ] Ending cash do cash flow = cash do balance sheet.
- [ ] Nenhum plug oculto.
- [ ] Premissas separadas de fórmulas.
- [ ] Base/upside/downside internamente coerentes.
- [ ] Bridge reconcilia integralmente.
- [ ] Cada variação material tem responsável.
- [ ] Decision, ask, gatilho e alternativa rejeitada explícitos.
- [ ] Questões contábeis/tributárias/jurídicas escaladas.

## 11. Exercício aplicado à operação Brasil

Execute os ciclos Q1–Q3 do cenário em `cases.md`. Entregue:

- modelo de três demonstrações;
- P&L de 24 meses;
- cash runway;
- previsão vintage por ciclo;
- BvA/reforecast bridge;
- QBR de duas páginas.

## 12. Avaliação e rubrica

Avaliações estão em `workbook.md`; soluções em `answer-key.md`. Pesos:

- K: 50;
- J: 50;
- mínimo: 80;
- zero erros críticos.

Erros críticos: P&L que não reconcilia; lucro tratado como caixa; erro material de previsão; plug oculto; cifra real sem fonte.

## 13. Artefato para o capstone

O capstone recebe:

1. três demonstrações do caso;
2. P&L de país de 24 meses;
3. base/upside/downside;
4. previsão pack;
5. bridge;
6. QBR e investment ask.

## 14. Leituras

### Essenciais — 90 min

- Investor.gov, *How to Read a 10-K* — 20 min; mapa do filing.
- Salesforce FY2026 10-K, Items 7–8 e notas de revenue — 70 min; caso real.

### Opcionais — 45 min

- Snowflake FY2026 10-K, business model e key metrics — comparar consumption revenue com assinatura ratable.
- Banco Central, página de câmbio — fonte e linguagem oficial.

## 15. Fontes e limitações

Veja `sources.md`. Este módulo ensina decisão gerencial, não contabilidade normativa, tax compliance ou hedge execution. O modelo é auditável, mas qualquer uso real requer revisão de controller/CFO e especialistas locais.
