# Casos — M1

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## Caso real — Salesforce FY2026: lucro, caixa e obrigações contratuais

**Fonte:** `SRC-FIN-SALESFORCE-10K-2026`\
**As of:** fiscal year ended 2026-01-31\
**Unidade:** US$ milhões

Dados extraídos do filing:

| Linha | FY2026 | FY2025 |
|---|---:|---:|
| Revenue | 41.525 | 37.895 |
| Cost of revenue | 9.270 | 8.643 |
| Operating expenses | 23.924 | 22.047 |
| Operating income | 8.331 | 7.205 |
| Net income | 7.457 | 6.197 |
| CFO | 14.996 | 13.092 |
| Cash | 7.327 | 8.848 |
| Accounts receivable | 14.339 | 11.945 |
| Unearned revenue | 24.317 | 20.743 |

### Tarefa

1. Recalcule gross profit e margens.
2. Explique por que CFO excede net income sem chamar a diferença de “qualidade” automaticamente.
3. Identifique os drivers de working capital citados no filing.
4. Explique por que cash caiu apesar de CFO positivo.
5. Escreva cinco perguntas ao CFO antes de concluir sobre sustentabilidade.
6. Liste cinco ações que podem aumentar operating income e piorar caixa no mesmo período.

## CENÁRIO SINTÉTICO — Atlas AI Brasil

Os dados abaixo são didáticos. Atlas AI não é empresa real.

### Premissas iniciais

- Moeda de reporte: R$ mil.
- Horizonte: 24 meses, mensal.
- Caixa inicial: 6.000.
- Funding HQ já aprovado: 4.000 no M7.
- Contratos enterprise: billing anual antecipado; revenue ratable.
- Self-serve: billing e revenue no mês.
- COGS: 28% de revenue no base case.
- Headcount inicial: Country Lead, AE, Solutions, CS, Ops.
- Opex fixo inicial: 650/mês; 60% headcount.
- AR: enterprise recebe em média 45 dias depois da invoice.
- Tax line: premissa gerencial de 8% sobre revenue, explicitamente não validada para uso real.

### Base case inicial

| Quarter | Revenue | New ARR exit | Gross margin | Opex | Ending cash |
|---|---:|---:|---:|---:|---:|
| Q1 | 900 | 2.400 | 72% | 1.950 | 5.120 |
| Q2 | 1.800 | 4.800 | 72% | 2.250 | 4.210 |
| Q3 | 3.000 | 7.200 | 72% | 2.700 | 6.030 |
| Q4 | 4.200 | 9.600 | 72% | 3.150 | 6.420 |

Esses totais não são um modelo completo; o aluno deve reconstruir drivers mensais e fazer as demonstrações fecharem.

### Ciclo Q1 — FX e collections

- BRL deprecia 15% contra a moeda de custo de inference.
- COGS de workloads denominados em moeda estrangeira aumenta.
- Dois clientes enterprise atrasam collection em 30 dias.
- Revenue recognition não muda automaticamente.

**Decisão:** contratar o segundo AE ou preservar caixa? Entregue bridge, runway e trigger.

### Ciclo Q2 — churn e desconto

- Um cohort self-serve apresenta revenue churn mensal de 4,0%, contra 2,0% no plano.
- Cliente grande oferece contrato de dois anos com 25% de desconto e pagamento anual.
- A customização pedida adiciona R$180 mil de custo inicial e R$20 mil/mês de COGS.

**Decisão:** aceitar, renegociar ou recusar? Mostre economics, caixa, capacidade e alternativa rejeitada.

### Ciclo Q3 — hiring delay e pressão de HQ

- Hiring do CS Lead atrasa três meses.
- Expansion revenue cai 20% versus forecast.
- HQ congela novas vagas e exige redução de 12% no cash burn dos próximos seis meses.

**Decisão:** reforecast, reallocate e preparar QBR. Não use corte linear sem examinar capacity e retention.
