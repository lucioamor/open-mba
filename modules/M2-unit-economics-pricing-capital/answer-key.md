# M2 — Answer key e rubrica

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

**Evaluator only.** Não entregar junto ao exercício. Arredondamento aceito: ±0,02 p.p. ou ±R$0,02 mil, salvo indicação.

## Chave dos exemplos resolvidos

### Exemplo 1

- Opening = `120 + 80 + 60 = R$260k`.
- Ending opening cohort = `150 + 0 + 45 = R$195k`.
- Expansão = R$30k; contração = R$15k; churn = R$80k.
- NRR = `195/260 = 75,00%`.
- GRR = `(120 + 0 + 45)/260 = 63,46%`.

### Exemplo 2

- CAC/logo = `540.000/12 = R$45.000`.
- Gross profit mensal = `10.000 × 70% = R$7.000`.
- Payback = `45.000/7.000 = 6,43 meses`.
- LTV simples = `10.000 × 70%/2% = R$350.000`.
- LTV/CAC = `350.000/45.000 = 7,78x`.

### Exemplo 3

- Model cost = `300 × 2,50 + 60 × 15 = US$1.650`.
- Total cost = `1.650 + 850 = US$2.500 = R$13.000`.
- List contribution/margin = `26.000 − 13.000 = R$13.000`; `50,00%`.
- Com 20% desconto: preço R$20.800; contribuição R$7.800; margem `37,50%`.
- Com support adicional de R$2.080: custo R$15.080; contribuição R$5.720; margem `27,50%`.
- Floor a 50% = `15.080/(1−0,50) = R$30.160`.

### Exemplo 4

- NPV Partner-led = `−600 + 200/1,14 + 300/1,14² + 350/1,14³ = R$42,52 mil`.
- IRR Partner-led = `17,81%`; payback simples = `2 + 100/350 = 2,29 anos`.
- NPV Direct team = `−900 + 150/1,14 + 400/1,14² + 550/1,14³ = −R$89,40 mil`.
- IRR Direct team = `8,95%`; payback simples = `2 + 350/550 = 2,64 anos`.
- Partner downside −20% = `−600 + 160/1,14 + 240/1,14² + 280/1,14³ = −R$85,98 mil`.

## ASSESS-M2-A — Mechanics (45 K)

### 1. Coorte (8)

```text
opening = 90 + 70 + 40 + 50 = R$250 mil
ending = 120 + 56 + 0 + 50 = R$226 mil
expansão Alpha = 120 - 90 = R$30 mil
contração Beta = 70 - 56 = R$14 mil
churn Gamma = R$40 mil
```

Pontuação: opening/ending 2; expansão 2; contração 2; churn 2.

### 2. NRR e GRR (10)

```text
NRR = 226/250 = 90,40%
GRR = (90 + 56 + 0 + 50)/250 = 196/250 = 78,40%
```

Novos logos são excluídos porque não pertenciam à população no início; incluí-los mistura retenção e aquisição.

Pontuação: NRR 4; GRR 4; explicação 2.

### 3. CAC e payback (10)

```text
pool = 300 + 180 + 60 + 30 + 30 = R$600 mil
CAC/logo = 600/15 = R$40 mil
gross profit mensal/logo = 8 × 62,5% = R$5 mil
payback = 40/5 = 8,00 meses
```

Pontuação: pool 2; CAC 3; gross profit 2; payback 3.

### 4. LTV (9)

```text
LTV simples = 8 × 62,5% / 2,5% = R$200 mil
LTV/CAC = 200/40 = 5,00x
```

Duas limitações válidas, 2 pontos cada: churn estacionário; coorte pequena/imatura; expansão ausente; margem constante; heterogeneidade; sem desconto de fluxo; lag ignorado; LTV é projeção, não caixa.

Pontuação: LTV 3; razão 2; limites 4.

### 5. Contrato de definição (8)

Resposta completa nomeia: unidade/denominador; população/inclusões; período e lag; moeda/FX; receita/custo usado; owner/versão. Um exemplo coerente vale nota integral; não há texto único.

### Fatals A

Qualquer um zera o item e bloqueia mastery:

- expansão em GRR;
- novos logos na coorte inicial;
- payback `CAC/MRR` sem margem;
- omitir pool ou denominador;
- trocar R$ mil por R$ sem sinalizar.

## ASSESS-M2-B — Executive judgment (55 J)

### Parte 1 — Workload e desconto (30)

#### 1. Base (8)

O supplier price foi dado no case; o aluno não precisa pesquisar.

```text
input = 400 × US$2,50 = US$1.000
output = 80 × US$15 = US$1.200
model cost = US$2.200
total direct cost = 2.200 + 800 = US$3.000
total direct cost BRL = 3.000 × 5,00 = R$15 mil
contribuição no list = 30 - 15 = R$15 mil
margem no list = 15/30 = 50,00%
```

Pontuação: input/output 2; total USD 2; BRL 1; contribuição/margem 3.

#### 2. Discount + custom support (6)

```text
net price = 30 × (1−20%) = R$24 mil
cost = 15 + 3 = R$18 mil
contribuição = 24 - 18 = R$6 mil
margem = 6/24 = 25,00%
```

#### 3. Direct floor (4)

```text
floor = 18/(1−45%) = 18/0,55 = R$32,73 mil/mês
```

O floor é superior ao list; o pacote solicitado não pode preservar a margem-alvo sem reformulação.

#### 4. Partner option (5)

No list:

```text
partner share = 30 × 15% = R$4,50 mil
total cost = 15 + 4,50 = R$19,50 mil
contribuição = 30 - 19,50 = R$10,50 mil
margem = 10,50/30 = 35,00%
```

Floor com share proporcional:

```text
(P − 0,15P − 15)/P = 40%
0,45P = 15
P = R$33,33 mil/mês
```

Pontuação: list 2; equação 2; floor 1.

#### 5. Recomendação (7)

Resposta-modelo: **reformular**, não aprovar o pedido. Opções: preço ≥ R$32,73 mil direto; remover support custom; reduzir workload/SLA; commit/prepay; overage; rate limit. Partner exige ≥R$33,33 mil ou share/COGS menor. Exigir give-get, CFO/Deal Desk approval, validade curta, reaprovação após mudança, supplier-price recheck imediato se >30 dias e triggers de p95/margem.

Rubrica: decisão 1; rationale econômico 2; give-get 1; owner/expiry 1; recheck 1; dois triggers 1.

### Parte 2 — Capital allocation (25)

#### 1. NPV base (8)

```text
NPV build =
-750 + 100/1,16 + 300/1,16² + 500/1,16³ + 550/1,16⁴
= R$183,24 mil

NPV partner =
-400 + 160/1,16 + 220/1,16² + 260/1,16³ + 260/1,16⁴
= R$211,59 mil
```

Pontuação: fórmula/período 2; build 3; partner 3.

#### 2. Downside (6)

```text
NPV build downside = −R$3,40 mil
NPV partner downside = R$89,27 mil
```

Somente inflows são multiplicados por 80%; `CF0` permanece.

#### 3. Payback e limites (4)

```text
build = 2 + (750−100−300)/500 = 2,70 anos
partner = 2 + (400−160−220)/260 = 2,08 anos
```

Dois limites, um ponto cada: payback simples ignora time value e fluxos posteriores; IRR pode conflitar com NPV por escala/timing e pode ter múltiplas raízes em fluxos não convencionais.

#### 4. Recommendation (7)

Resposta-modelo: escolher **partner-led**. Tem NPV base maior, menor upfront, payback menor e permanece positivo no downside. Rejeitar build neste gate: NPV base positivo, porém menor e levemente negativo no downside. O sunk cost de R$120 mil não entra.

Gates financeiros aceitáveis:

1. liberar tranche 2 somente se gross contribution/workload e consumo observado preservarem floor;
2. liberar expansão somente se forecast de cash flow mantiver NPV positivo no downside atualizado.

Trigger: supplier cost/FX/volume/margem cruza threshold aprovado. CFO/controller questions: hurdle/WACC; tributos/FX/working capital; classificação de COGS/capex; compromisso/covenant; materialidade.

Pontuação: recommendation 2; alternativa rejeitada 1; downside 1; dois gates 1; trigger 1; três perguntas 1.

### Fatals B

Qualquer um bloqueia mastery:

- omitir output, support custom, FX ou partner share;
- margem calculada sobre custo, não receita;
- supplier price tratado como permanente;
- incluir sunk cost de R$120 mil;
- hurdle de 14% em vez de 16%;
- reduzir `CF0` no downside;
- aprovar NPV negativo sem condição/escalation;
- atribuir qualquer número sintético a empresa real.

## Decisão de mastery

- `80–100` e zero fatal: mastery local.
- `70–79` e zero fatal: forma nova de reteste após remediation dirigida.
- `<70` ou qualquer fatal: DEEP permanece; reteste independente obrigatório.

## Form B — reteste executável

**Cenário sintético.** Cohort abre com 20 clientes e MRR de R$50 mil. Em 12 meses perde 15% do opening MRR por logo churn, 10% por contraction e ganha 25% por expansion. Gross margin 65%. Custo de aquisição fully-loaded: R$300 mil. Calcule GRR, NRR, CAC por logo e payback simples sobre new MRR. Respostas: GRR 75%; NRR 100%; CAC R$15 mil; payback `300/(50×65%) = 9,23 meses`.

Capital Form B, R$ mil: `CF0=-1.000`, `CF1=400`, `CF2=450`, `CF3=500`, hurdle 12%. Respostas: NPV R$71,77 mil; IRR 15,98%; decisão condicionalmente positiva antes de risco/capacidade. Reteste usa nova recomendação e novo discount guardrail; fatal error original é pontuado isoladamente.
- Não elevar `P` ou prontidão C-level com base nesta nota.

## Verificação determinística

Equações recalculadas em 2026-07-23 com Python/IEEE double. Valores não arredondados usados antes da apresentação:

```text
example_partner_npv = 42.5188857030
example_partner_downside_npv = -85.9848914376
example_direct_npv = -89.3997073324
assessment_build_npv = 183.2447075491
assessment_build_downside_npv = -3.4042339608
assessment_partner_npv = 211.5935533402
assessment_partner_downside_npv = 89.2748426721
```
