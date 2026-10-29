# M2 — Economia por unidade, preços e eficiência de capital em software e IA

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## 1. Decisão executiva central

**Quem servir, a que preço, com qual motion e estrutura de margem — e qual investimento financiar, condicionar ou recusar?**

Uma resposta executiva completa contém: unidade e coorte; economics observados; pricing meter; custo por carga de trabalho; cash flow incremental; alternativa rejeitada; risco; gate de liberação; gatilho de revisão; responsável e escalation.

O módulo termina quando o participante consegue defender a decisão sem esconder mix, média, timing, custo compartilhado ou uma premissa financeira atrás de um benchmark.

## 2. Como escolher a profundidade

Este módulo não presume experiência, senioridade ou lacunas do aluno. Use o diagnóstico por competência e o objetivo escolhido para decidir o que estudar. Sem avaliação, a recomendação é provisória: estudar ou fazer a prova de entrada. Cargo, tempo de carreira e autoavaliação não dispensam conteúdo. As regras da edição pública em `diagnostic/README.md` prevalecem sobre referências legadas a placement, avaliação para dispensa ou M0.

## 3. Conhecimentos prévios e avaliação para dispensa

Pré-requisitos:

1. Separar receita, gross profit, OPEX e caixa.
2. Calcular percentuais, média ponderada e valor presente.
3. Explicitar premissa, período, moeda e unidade.

Avaliação para dispensa por subcompetência: `K ≥ 85`, `J ≥ 80`, dois casos independentes e zero erro crítico local. Resultado 70–84 pode comprimir; erro em definição de unidade, gross margin, payback ou carga de trabalho cost mantém DEEP, mesmo com média agregada alta.

Antes de começar, responda sem consulta: “qual é o denominador de CAC?”, “por que NRR de duas empresas pode não ser comparável?” e “qual custo entra no floor de preço?”. Se qualquer resposta omitir população, período ou margem, execute o módulo integral.

## 4. Objetivos de aprendizagem

Ao concluir, o participante será capaz de:

- **M2-LO-01 / UE-01:** reconstruir ARR, GRR, NRR e coortes com unidade, população e período auditáveis.
- **M2-LO-02 / UE-02:** calcular CAC fully-loaded, payback e LTV e rejeitar premissas incompatíveis.
- **M2-LO-03 / UE-03:** desenhar preço e guardrails que preservem contribuição por carga de trabalho sob consumo e desconto.
- **M2-LO-04 / CAP-01:** recomendar, condicionar ou recusar capital usando NPV, sensibilidade, alternativa rejeitada e escalation.

## 5. Mapa de conceitos em uma página

```text
UNIDADE/COORTE
  ├─ receita: recorrente contratual | consumo | serviço
  ├─ retenção: GRR | NRR | logo | workload
  └─ aquisição: pool CAC / denominador / lag
          ↓
UNIT ECONOMICS
  ├─ gross profit incremental
  ├─ payback
  ├─ LTV como modelo, não observação
  └─ contribuição por workload
          ↓
PRICING E DEAL
  ├─ meter: seat | tier | uso | resultado | enterprise
  ├─ floor = custo / (1 - margem-alvo)
  ├─ desconto + give-get + aprovação
  └─ leakage: suporte, canal, FX, overage, abuso
          ↓
CAPITAL
  ├─ cash flow incremental / opportunity cost
  ├─ NPV / IRR / payback e limites
  ├─ sensibilidade / gate de liberação
  └─ CFO/controller escalation
```

Rule of 40 é uma lente lateral de crescimento + margem, não uma ponte que apaga os nós acima.

## 6. Lições

### Lição 1 — Unidade, receita recorrente e coorte

**Decisão:** qual unidade pode ser comparada sem misturar população, receita ou período?

#### 1.1 Contrato de definição

Antes do cálculo, escreva:

| campo | pergunta mínima |
|---|---|
| unidade | logo, contrato, workspace, seat, carga de trabalho ou R$ de ARR? |
| população | quem entra e quem fica fora? |
| evento | assinatura, ativação, primeira receita ou primeiro consumo? |
| janela | mês, trimestre, trailing 12 meses ou dois anos? |
| moeda | nominal, constante, BRL ou USD? |
| receita | contratual recorrente, revenue reconhecida ou consumo anualizado? |
| custo | COGS contábil, custo marginal ou contribuição? |
| versão | quem aprovou a definição e quando? |

Snowflake informa que product revenue acompanha consumo e que esse timing pode ultrapassar capacidade contratada ou o termo original; isso difere de software reconhecido ratably [SRC-M2-SNOW-10K, “Product Revenue”, linhas 1765–1767]. Confluent descreve pay-as-you-go e compromissos usage-based com revenue reconhecida por uso [SRC-M2-CONFLUENT-10K, linhas 2115–2117]. Portanto, booking, ACV, compromisso, ARR operacional e revenue não são sinônimos.

#### 1.2 ARR/MRR operacional

Definição do curso: ARR é o run-rate anual de componentes recorrentes ativos na data; exclui serviço one-off. Para consumo, qualquer annualização deve declarar janela, sazonalidade, compromisso e política de outlier. Nunca force “ARR” onde o melhor indicador é revenue de consumo por coorte e carga de trabalho.

**Fatal error:** somar serviços, implementação e uso não contratado ao ARR sem política explícita.

### Lição 2 — Retenção e cohort economics

**Decisão:** expansão compensa uma base que contrai, e em qual definição isso é verdade?

Definições do curso:

```text
NRR = ending revenue da opening cohort, com expansão / opening revenue
GRR = ending revenue da opening cohort, limitado ao opening por cliente / opening revenue
```

Novos clientes ficam fora. Cliente churned permanece no denominador e contribui zero. GRR nunca recebe expansão.

Snowflake calcula NRR com product revenue de uma coorte de clientes sob capacity contracts em uma janela de dois anos [SRC-M2-SNOW-10K, “Net Revenue Retention Rate”, linhas 1774–1780]. Confluent compara ARR da mesma coorte em dois pontos, mas anualiza os três meses finais de consumo Cloud/WarpStream [SRC-M2-CONFLUENT-10K, “Dollar-Based NRR”, linhas 2192–2197]. O rótulo é parecido; população, medida e janela não são.

#### Exemplo resolvido 1 — NRR e GRR

**Cenário sintético.** Opening cohort: A = R$120k MRR, B = R$80k, C = R$60k; total R$260k. No fim: A = R$150k, B = R$0, C = R$45k.

```text
expansão A = 150 - 120 = 30
churn B = 80
contração C = 60 - 45 = 15
NRR = (150 + 0 + 45) / 260 = 75,00%
GRR = (min(150,120) + 0 + 45) / 260 = 63,46%
```

Interpretação: a expansão de A melhora NRR em 11,54 p.p., mas não corrige o leakage de R$95k. “NRR 75%” sem GRR, concentração e drivers encobre o problema.

### Lição 3 — CAC fully-loaded, payback, LTV e eficiência

**Decisão:** qual motion recupera aquisição com caixa e margem aceitáveis?

Stripe apresenta a base `CAC = sales and marketing costs / novos clientes` e alerta para alinhamento de período e alocação [SRC-M2-STRIPE-CAC, linhas 337–348]. Aqui, “fully-loaded” significa publicar o pool:

```text
pessoal + comissão + mídia + eventos + tooling + terceiros
+ overhead de aquisição alocado
---------------------------------------------------------
logos adquiridos OU gross new ARR adquirido
```

Escolha um denominador. Para comparar motions enterprise e self-serve, produza pelo menos CAC/logo e CAC/gross new ARR; não misture os dois.

Payback do curso:

```text
payback em meses = CAC / gross profit mensal incremental da coorte
```

BVP descreve payback após custo variável de servir e mostra que CLTV muda com alocação e desconto de fluxos [SRC-M2-BVP-CLOUD-METRICS, linhas 183–194]. Receita mensal, isoladamente, subestima payback.

LTV simples:

```text
LTV = ARPA mensal × margem de contribuição / churn mensal
```

É modelo estacionário. Se churn for zero, negativo, instável ou misturar segmentos; se expansão e custo mudarem; ou se a coorte for pequena, use curvas de contribuição observada e cenários. LTV não é dinheiro já recebido.

#### Exemplo resolvido 2 — CAC, payback e LTV

**Cenário sintético.** Pool trimestral de aquisição = R$540k; 12 logos pagos; MRR inicial médio = R$10k; margem de contribuição = 70%; churn mensal assumido = 2%.

```text
CAC/logo = 540.000 / 12 = R$45.000
gross profit mensal/logo = 10.000 × 70% = R$7.000
payback = 45.000 / 7.000 = 6,43 meses
LTV simples = 10.000 × 70% / 2% = R$350.000
LTV/CAC = 350.000 / 45.000 = 7,78x
```

Decisão: payback é calculável; LTV/CAC é apenas uma hipótese até validar churn, margem, ramp e cohort mix. A aparente eficiência alta pode ser subinvestimento, coorte imatura ou custo omitido.

#### Rule of 40 e magic number

Definição do curso: `score = growth definido + margem definida`, sempre com período e reconciliação. BVP chama a Rule of 40 de heurística e contesta a equivalência 1:1 entre crescimento e margem [SRC-M2-BVP-RULE-X, linhas 88 e 179–200]. Não existe score universal sem escolher revenue/ARR growth e GAAP operating/EBITDA/FCF margin.

**Cenário sintético:** 32% revenue growth + (−18%) GAAP operating margin = 14. A mesma empresa teria 43 com 11% adjusted FCF margin. Os números não são versões intercambiáveis do mesmo fato.

Magic number pode ser uma razão de sales efficiency, mas sua fórmula varia. Neste curso, qualquer uso exige fórmula, lag, margem, organic/paid e reconciliação ao ledger; não há benchmark de aprovação automática.

### Lição 4 — Pricing por consumo e margem por carga de trabalho

**Decisão:** qual meter, preço e limite tornam o carga de trabalho observável?

Arquiteturas:

| arquitetura | serve quando | risco principal |
|---|---|---|
| seat | valor cresce com usuários identificáveis | shelfware e compartilhamento |
| tier | pacotes de valor e governança | cliff e feature leakage |
| usage | custo/valor correlaciona a uso medível | bill shock e volatilidade |
| outcome | resultado é atribuível e contratável | causalidade e disputa |
| enterprise | risco, SLA, volume e termos importam | desconto, suporte e customização |
| hybrid | base/commit + overage/usage | complexidade e breakage |

Snowflake publica meters de compute, storage e transfer; créditos consumidos multiplicam o preço do acordo [SRC-M2-SNOW-PRICING, “Basic pricing model”]. Confluent lista data transfer, storage, compute units e add-ons, com billing horário [SRC-M2-CONFLUENT-BILLING, linhas 1083–1107]. Lovable usa créditos compartilhados cujo consumo varia por ação/plano e não cobra por seat [SRC-M2-LOVABLE-PRICING, linhas 22–35 e 62–70]; em 2026 unificou saldo de build, Cloud e AI com visibilidade por membro/projeto/categoria [SRC-M2-LOVABLE-BILLING, linhas 27–49]. São padrões observáveis, não economics internos comparáveis.

#### Carga de trabalho cost tree

```text
tokens input + tokens output + cache
+ orchestration/tool calls/search
+ compute/storage/transfer
+ observability/security
+ support/SLA incremental
+ fraude, retry e abuso esperado
+ marketplace/canal/payment fees
= custo atribuível do workload
```

Calcule p50, p95 e stress. Defina unit cost, rate limit, alert, budget cap, overage, kill switch operacional e responsável. O kill criterion estratégico canônico pertence ao M3; aqui há apenas proteção financeira e de serviço.

Para os exercícios, adote um fornecedor fictício com input a US$2,50/MTok e output a US$15/MTok. São premissas didáticas, não preços públicos verificados. Para uma decisão real, registre provedor, modelo, moeda, tier, data e fonte do contrato ou catálogo consultado.

#### Exemplo resolvido 3 — margem por carga de trabalho e desconto

**Cenário sintético; preços do fornecedor são premissas fictícias.** Carga de trabalho mensal: 300 MTok input e 60 MTok output em Modelo A (sintético); demais custos diretos = US$850; FX didático = R$5,20/US$; preço ao cliente = R$26.000.

```text
modelo = 300 × 2,50 + 60 × 15 = US$1.650
custo total = 1.650 + 850 = US$2.500 = R$13.000
contribuição = 26.000 - 13.000 = R$13.000
margem = 13.000 / 26.000 = 50,00%
```

Com desconto de 20%, preço = R$20.800; margem cai para `(20.800 − 13.000)/20.800 = 37,50%`. Se o cliente também exigir R$2.080 de suporte incremental, margem cai para 27,50%. Para preservar 50%, o floor passa a `15.080/(1−0,50) = R$30.160`, acima do list. Decisão: rejeitar pacote, reduzir escopo/uso/SLA, trocar carga de trabalho ou obter contrapartida econômica; não aprovar só pelo ARR.

### Lição 5 — Discount governance e leakage

**Decisão:** qual concessão aprovar, qual contrapartida exigir e quando escalar?

O handbook público do GitLab exige aprovação para elementos não padrão, racional do desconto, resposta a “what are we getting in return?” e reaprovação após mudança [SRC-M2-GITLAB-DEAL, linhas 4082–4103]. O módulo transforma esse exemplo em um controle mínimo próprio:

1. list, net, TCV, term, payment e ramp;
2. custo por carga de trabalho p50/p95 e margem após canal/suporte;
3. desconto efetivo e price waterfall;
4. contrapartida: prepay, commit, volume, escopo, prazo, referência ou menor SLA;
5. approver por impacto, não por título comercial;
6. validade, exception ID e reaprovação após mudança;
7. floor e CFO gatilho.

Leakage inclui desconto informal, implantação grátis, suporte customizado, rate limit ausente, overage não cobrado, parceiro sem margin waterfall, FX sem clause, pagamento longo e renewal price lock. Cada item tem responsável e valor esperado.

**Escalar ao CFO/controller:** preço abaixo do floor, margem negativa em p95, compromisso mínimo, pagamento/FX material, revenue recognition incomum, canal com risco de principal-versus-agent, ou exceção que cria precedente.

### Lição 6 — Capital allocation e recusa de crescimento

**Decisão:** qual alternativa cria valor após risco, timing e opportunity cost?

MIT define NPV como cash flows descontados, líquidos do upfront, usando opportunity cost of capital; recomenda cash flow, não lucro contábil, e coerência real/nominal [SRC-M2-MIT-NPV, PDF pp. 5–8].

Workflow:

1. definir decisão, alternativas e restrição de capital;
2. projetar cash flow **incremental after-tax**, incluindo cannibalization e opportunity cost;
3. excluir sunk cost da decisão futura;
4. alinhar moeda, inflação, risco e hurdle;
5. calcular NPV; reportar IRR e payback apenas como lentes;
6. testar downside, atraso, volume, margem e FX;
7. liberar em tranches com evidence gates;
8. registrar alternativa rejeitada, risco e CFO escalation.

```text
NPV = Σ CF_t / (1+r)^t
IRR = r que zera o NPV
```

IRR pode falhar com fluxos não convencionais, escala ou múltiplas raízes. Payback ignora caixa posterior e, se simples, time value. Rule of 40 não substitui NPV de uma decisão incremental.

#### Exemplo resolvido 4 — duas expansões

**Cenário sintético, valores em R$ mil, hurdle didático de 14%.**

| alternativa | CF0 | ano 1 | ano 2 | ano 3 |
|---|---:|---:|---:|---:|
| Partner-led | -600 | 200 | 300 | 350 |
| Direct team | -900 | 150 | 400 | 550 |

```text
NPV partner = -600 + 200/1,14 + 300/1,14² + 350/1,14³
            = R$42,52 mil; IRR = 17,81%; payback simples = 2,29 anos

NPV direct  = -900 + 150/1,14 + 400/1,14² + 550/1,14³
            = -R$89,40 mil; IRR = 8,95%; payback simples = 2,64 anos
```

Recomendação preliminar: partner-led, condicionado a quality/economics gates. Com inflows 20% menores, seu NPV vira **−R$85,98 mil**; a decisão exige staged financiamento. Hurdle real, tributos, FX e risco de parceiro devem ser aprovados pelo CFO/controller.

**Capital structure literacy:** equity dilui, dívida cria obrigação/covenant e compromisso contratual cria downside mesmo sem dívida. O objetivo aqui é ler efeitos e escalar; valuation, cap-table modeling e M&A avançados ficam fora.

## 7. Práticas guiadas

### GP-M2-01 — Cohort teardown (90 min)

Use `CASE-M2-REAL-CONSUMPTION`. Em dupla com facilitador:

1. escreva as definições Snowflake e Confluent em sete campos;
2. marque diferenças que impedem comparação direta;
3. reconstrua o cenário A/B/C do exemplo 1;
4. produza uma nota de 150 palavras: “o que NRR não responde?”.

Gate: zero mistura de ARR/revenue e GRR sem expansão.

### GP-M2-02 — Pricing war room (150 min)

Use o carga de trabalho do exemplo 3. Recalcule p50, p95 (+40% output, +20% support) e três propostas: seat, commit+overage, enterprise floor. Simule pedido de 25% desconto e SLA customizado. Registre give-get, approver e expiry.

Gate: todos os custos atribuíveis e supplier price “as of” visíveis.

### GP-M2-03 — Investment committee (120 min)

Use `CASE-M2-SYNTHETIC-VETOR`. Calcule NPV base/downside, critique IRR/payback, proponha duas tranches e defina as perguntas que obrigam CFO/controller. O facilitador desafia volume, FX, tributo e sunk cost.

Gate: recomendação, alternativa rejeitada, sensibilidade e escalation.

## 8. Caso real documentado e cenário sintético

O caso real compara somente definições públicas de consumo e NRR de Snowflake e Confluent; não atribui economics internos. O cenário `Vetor AI Brasil` é totalmente sintético e contém os números usados nos exercícios. Ambos estão em `cases.md`.

Separação obrigatória:

- **real:** texto verificável com `[source_id, locator]`;
- **interpretação:** inferência explicitamente rotulada;
- **sintético:** nenhum número atribuído a empresa real.

## 9. Erros executivos frequentes e sinais de alerta

| erro | sinal | correção |
|---|---|---|
| unidade oculta | “CAC caiu” sem denominador | contrato de definição |
| média mascara mix | blended margin sem p95/segmento | cohort/carga de trabalho view |
| NRR comparado cru | empresas usam janelas diferentes | normalize ou não compare |
| GRR com expansão | GRR >100% | cap por cliente no opening |
| payback em revenue | divide CAC por MRR | usar gross profit |
| LTV ornamental | churn zero gera infinito | cohort curve + cenários |
| preço sem cost tree | markup só no modelo | incluir suporte/cloud/canal |
| desconto por ARR | TCV cresce, margem cai | waterfall + floor + give-get |
| Rule of 40 como lei | componente de margem não nomeado | fórmula/período/finalidade |
| NPV com lucro | depreciation/working capital ignorados | cash flow incremental |
| sunk-cost fallacy | “já gastamos demais para parar” | decidir apenas caixa futuro |
| escalation tardia | WACC/FX/tributo assumidos | CFO/controller antes do ask |

## 10. Checklist de decisão

- [ ] Unidade, população, período, moeda e versão definidos.
- [ ] ARR/revenue/booking/consumo separados.
- [ ] NRR e GRR reconciliados à opening cohort.
- [ ] CAC pool, denominador e lag publicados.
- [ ] Payback usa gross profit incremental.
- [ ] LTV inclui limites e cenário, não falsa precisão.
- [ ] Carga de trabalho p50/p95/stress com todos os meters.
- [ ] Supplier price tem data e recheck.
- [ ] Floor, discount waterfall, give-get, expiry e approver.
- [ ] Cash flows incrementais, after-tax e coerentes com hurdle.
- [ ] NPV e sensibilidade; IRR/payback com limites.
- [ ] Alternativa rejeitada e opportunity cost.
- [ ] Gate de liberação, responsável e gatilho de revisão.
- [ ] CFO/controller escalation explícita.

## 11. Exercício aplicado à operação Brasil

Uma empresa global de AI avalia entrada no Brasil com três segmentos: startups self-serve, mid-market via parceiros e enterprise direto. Construa:

1. unit-economics tree por segmento;
2. pricing meter e price floor por carga de trabalho;
3. cohort model com GRR/NRR;
4. discount approval card;
5. investment memo build-versus-partner.

Use BRL e USD em colunas separadas, FX como premissa, impostos como linha pendente de validação e nenhum dado “de mercado” sem fonte. Não invente preço, margem ou churn de empresa-alvo. O caderno de exercícios fornece dados sintéticos completos.

## 12. Avaliação e rubrica

Avaliação individual, sem AI:

- **ASSESS-M2-A — Mechanics (45 pontos K):** coorte, CAC, payback e LTV.
- **ASSESS-M2-B — Julgamento executivo (55 pontos J):** carga de trabalho pricing, desconto e capital allocation.

Domínio = 80/100 e zero erro crítico. K/J não são compensados quando há erro crítico local. `P` não é pontuado neste módulo; artefatos alimentam capstone, mas não provam field readiness.

Rubrica:

| dimensão | pontos | evidência |
|---|---:|---|
| definição/reconciliação | 15 | unidade, população, período e ledger |
| cálculos | 30 | GRR/NRR, CAC, payback, LTV, carga de trabalho, NPV |
| julgamento | 25 | decisão, escolha e renúncia e alternativa |
| risco/governança | 20 | p95, floor, gate, approver, escalation |
| comunicação | 10 | recomendação curta e auditável |

## 13. Artefato para o capstone

Entregáveis:

1. `ART-M2-UE-TREE`: cohort model e unit-economics tree.
2. `ART-M2-PRICING`: pricing architecture, carga de trabalho ledger, floor e approval matrix.
3. `ART-M2-ALLOC`: investment memo curto com NPV, sensibilidade, alternativa rejeitada, tranches e CFO ask.

O M3 é dono dos kill criteria estratégicos. M2 fornece evidence gates financeiros; não duplica o registro canônico. O M8 transforma a recomendação em board memo.

## 14. Leituras

Ordem mínima:

1. Snowflake e Confluent 10-K — somente seções indicadas em `sources.md`.
2. Pricing/billing oficial de Snowflake, Confluent e Lovable.
3. Catálogos OpenAI e Anthropic no dia da prática.
4. Stripe CAC e BVP cloud metrics, lidos criticamente.
5. BVP Rule of X para entender por que Rule of 40 é heurística.
6. MIT OCW pp. 5–8 para NPV e taxa de desconto.
7. GitLab Sales Order Processing para workflow público de exceção.

## 15. Fontes e limitações

Registro completo em `sources.md`; claims aceitas em `source-packet.md`; cálculo oficial em `answer-key.md`.

Limitações:

- preços mudam; recheck em até 30 dias e sempre antes de uso real;
- company-reported NRR/ARR são non-GAAP operational metrics com definições próprias;
- nenhum economics interno de Lovable, Anthropic, OpenAI, Snowflake ou Confluent foi inferido;
- benchmarks não são gates universais;
- hurdle, WACC, FX, tributos, revenue recognition, dívida, covenant e diluição reais exigem CFO/controller;
- o módulo forma decisão e escalation, não especialista em valuation ou M&A.
