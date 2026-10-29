# M6 — Gabarito e rubrica

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

**Somente para o avaliador.** Arredondamento aceito: ±0,02 p.p. ou ±R$0,01 milhão.

## Chave dos exemplos resolvidos

### Exemplo 1 — access

```text
1.200 × 40% = 480 fit
480 × 65% = 312 ready
312 × 50% = 156 reachable
156 × 25% = 39 wins
bookings = 39 × R$120 mil = R$4,68 milhões
first-year revenue = 4,68 × 70% = R$3,276 milhões
```

### Exemplo 2 — country P&L

Base:

- COGS = `1,50 + 0,30 + 0,60 = 2,40`.
- GP = `6,00 − 2,40 = 3,60`; GM = `60,00%`.
- Despesas operacionais locais = `1,80 + 0,50 + 0,20 = 2,50`.
- Contribuição local = `1,10`; margin = `18,33%`.
- Resultado com todas as alocações = `1,10 − 0,50 = 0,60`; margin = `10,00%`.

Downside combinado:

- Revenue = `6,00 × 75% = 4,50`.
- Compute = `1,50 × 75% × 120% = 1,35`.
- Partner = `4,50 × 10% = 0,45`.
- COGS = `1,35 + 0,30 + 0,45 = 2,10`.
- GP = `2,40`; GM = `53,33%`.
- Despesas operacionais locais = `2,50 − 0,20 = 2,30`.
- Contribuição local = `0,10`; margin = `2,22%`.
- Resultado com todas as alocações = `−0,40`; margin = `−8,89%`.

### Exemplo 3 — exception

- Incremental probability = `55% − 10% = 45%`.
- Incremental expected ARR = `2,40 × 45% = 1,08`.
- Contribuição esperada = `1,08 × 45% = 0,486`.
- First-year net = `0,486 − 0,500 − 0,100 = −0,114`, ou **−R$114 mil**.

### Exemplo 4 — miss bridge

- Plan `3,0`; current `2,1`; gap `0,9`.
- `0,4 slip + 0,3 win-rate + 0,2 capacity = 0,9`.
- Qualquer revised commit precisa de deal-level evidence; “timing” não pode absorver win-rate/capacity.

## ASSESS-M6-A — Mechanics (40 K)

### 1. Access funnel (12)

```text
fit = 1.000 × 60% = 600
product ready = 600 × 70% = 420
contract ready = 420 × 80% = 336
reachable = 336 × 50% = 168
qualified = 168 × 40% = 67,20
expected wins = 67,20 × 25% = 16,80
bookings = 16,80 × R$240 mil = R$4,032 milhões
first-year revenue = 4,032 × 65% = R$2,6208 milhões
```

Pontuação: sequência e unidades 6; expected logos 2; bookings 2; revenue 2.

### 2. Base P&L (12)

```text
COGS = 2,00 + 0,80 + 0,80 = 3,60
gross profit = 8,00 − 3,60 = 4,40
gross margin = 4,40/8,00 = 55,00%

local OPEX = 2,40 + 0,60 + 0,20 = 3,20
local contribution = 4,40 − 3,20 = 1,20
local contribution margin = 15,00%

fully allocated result = 1,20 − 0,70 = 0,50
fully allocated margin = 6,25%
```

Pontuação: COGS/GP/GM 5; local 4; allocated 3.

### 3. Stress P&L (10)

```text
revenue = 8,00 × 85% = 6,80
compute = 2,00 × 85% × 125% = 2,125
implementation = 0,80
partner = 6,80 × 10% = 0,68
COGS = 3,605
gross profit = 6,80 − 3,605 = 3,195
gross margin = 46,99%

local OPEX = (2,40−0,20) + (0,60−0,10) + 0,20 = 2,90
local contribution = 3,195 − 2,90 = 0,295
local contribution margin = 4,34%

fully allocated result = 0,295 − 0,70 = −0,405
fully allocated margin = −5,96%
```

Pontuação: revenue/compute 3; GP/GM 3; local 2; allocated 2.

### 4. Macro/FX classification (6)

Resposta completa:

- PTAX = taxa oficial observada com data/hora e lado; não é preço contratual nem previsão.
- Focus = distribuição/mediana de expectativas de mercado; não é projeção do BCB.
- FX scenario = premissa interna para sensitivity/previsão, com responsável e versão.
- CFO/treasury valida hedge; controller/tax valida accounting/tax effects.

Pontuação: distinções 4; responsáveis 2.

### Fatals A

- TAM/uso lançado diretamente como revenue;
- COGS, local OPEX ou HQ allocation omitidos;
- P&L não reconcilia;
- FX sem moeda/data/tipo;
- número de Arco atribuído a empresa real.

## ASSESS-M6-B — Julgamento executivo (60 J)

### 1. Entry-mode score (12)

Pesos: 20/20/30/20/10%.

```text
cross-border =
5×20% + 2×20% + 2×30% + 5×20% + 5×10% = 3,50

partner-led =
4×20% + 3×20% + 4×30% + 4×20% + 4×10% = 3,80

subsidiary =
1×20% + 5×20% + 5×30% + 1×20% + 1×10% = 3,00
```

Resposta-modelo: experimentar **partner-led**, com SLA/attribution/economics e gate; manter cross-border como fallback; não liberar subsidiary antes de repeatability/economics. M7 valida entity, tax, employment, contracts, data e sector rules.

Pontuação: três scores 6; recommendation/escolha e renúncia 4; M7 scope 2.

### 2. Previsão call (12)

```text
commit = Luma 0,60 + Terra 0,30 = 0,90
best-case incremental = Nexo 0,50 + Sol 0,20 = 0,70
best-case total = 0,90 + 0,70 = 1,60
pipeline incremental = Prisma 0,40
pipeline total = 2,00
commit gap vs plan = 1,50 − 0,90 = 0,60
```

Partner influence não adiciona R$0,50; Nexo já está no revenue previsão. Previsão call recomendada: commit R$0,90; best-case R$1,60, com Nexo/Sol abaixo de evidence limite; plano não é commit.

Pontuação: categorias 6; plan gap 2; call 2; zero double count 2.

### 3. Gate 180 (12)

Resultado:

- deployments `4/4`: passa;
- resultados `3/3`: passa;
- partner pipeline `25% vs 30%`: falha 5 p.p.;
- previsão error `18% vs ≤15%`: falha 3 p.p.;
- GM `48% vs ≥50%`: falha 2 p.p.

Decisão-modelo: **hold/remediate**, não scale integral e não stop. Há proof de paid deployment/outcome, mas economics e predictability não atingem gate. Responsáveis: Partnerships para pipeline; Revenue Ops/country lead para previsão; Finance/Product/Delivery para GM. Novo gate em 60–90 dias com os mesmos limites e action plan.

Pontuação: avaliação 5; decisão 3; responsáveis 2; próximo gate 2.

### 4. HQ exception (12)

```text
incremental probability = 50% − 20% = 30%
incremental expected ARR = 3,00 × 30% = 0,90
expected contribution = 0,90 × 50% = 0,45
first-year net = 0,45 − 0,40 − 0,08 = −0,03
```

Resposta-modelo: **reformular**. O caso de primeiro ano é −R$30 mil. Propor discovery/stage 1, design-partner commitment, scope reutilizável, stage 2 após proof; Product decide em 15 dias; Finance/Legal/Security mantêm veto; expiry 12 meses e reapproval gatilho.

Pontuação: math 6; recommendation 2; staged ask 2; rights/expiry 2.

### 5. Resource ask (12)

Resposta-modelo:

> O commit atual é R$0,90m contra plano R$1,50m; no dia 180, previsão error é 18% e GM 48%, ambos abaixo do gate. O gap inclui capacity, mas a vaga de R$300k/ano não deve ser liberada apenas por narrativa local. Opções: manter freeze; cobertura temporária via parceiro; liberar contratação condicional. Recomendo 90 dias de partner coverage e job design agora, com liberação automática se pipeline qualificado por responsável exceder 3× quota, previsão error cair a ≤15%, GM atingir ≥50% e delivery capacity permanecer verde. Local recomenda e reconfigura coverage; HQ/Finance decide headcount. Decision-by em 10 dias para não perder o próximo hiring window.

Variações são válidas se contêm fato, economia, opções, recommendation, rights, milestone e data.

Pontuação: fato/economia 3; opções 2; recommendation 2; rights 2; milestone 2; date 1.

### Fatals B

- unsupported claim;
- partner-influenced somado como revenue;
- subsidiary/EOR/reseller tratado como legalmente resolvido;
- exception sem economics, approver ou expiry;
- promessa fora do direito local;
- estereótipo como evidência;
- scale apesar de gate falho sem condition/remediation.

## Decisão de mastery

- `80–100` e zero fatal: mastery local.
- `70–79` e zero fatal: remediation e forma nova de reteste.
- `<70` ou fatal: rota DEEP permanece.
- Nenhuma nota altera `P` ou readiness C-level sem evidência operacional revisada.

## Verificação determinística

Recalculado em 2026-07-23:

```text
accessible_expected_logos = 16.8
accessible_bookings_m = 4.032
accessible_first_year_revenue_m = 2.6208
base_gp_m = 4.4
base_local_contribution_m = 1.2
base_fully_allocated_m = 0.5
stress_compute_m = 2.125
stress_gp_m = 3.195
stress_local_contribution_m = 0.295
stress_fully_allocated_m = -0.405
entry_scores = [3.5, 3.8, 3.0]
exception_first_year_net_m = -0.03
```

## Form B — reteste executável

**Cenário sintético.** Reach cai de 35% para 25%; qualification permanece 40%, win rate 20%, 600 contas, ACV R$240 mil e first-year recognition 65%. Calcule logos, bookings e receita do primeiro ano; depois revise entry mode, resource ask e gates 90/180/365. Respostas: 12 logos; R$2,88 mi bookings; R$1,872 mi receita do primeiro ano. Nenhum dado é atribuído a empresa real. Fatal original é reavaliado isoladamente e P continua pendente.
