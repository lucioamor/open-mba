# M2 — Casos

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## CASE-M2-REAL-CONSUMPTION — Dois NRRs com o mesmo nome

**Tipo:** caso real documentado; análise de disclosures públicos.\
**Regra:** não inferir CAC, margem por cliente, custo interno ou qualidade relativa das empresas.

### Evidência Snowflake

Snowflake descreve um modelo consumption-based; product revenue acompanha consumo e pode exceder capacidade contratada ou estender-se além do termo [SRC-M2-SNOW-10K, “Product Revenue”, linhas 1765–1767]. Para NRR, define uma janela de dois anos, seleciona clientes sob capacity contracts que usaram a plataforma no primeiro mês, divide product revenue do segundo ano pelo primeiro e mantém churned com zero [SRC-M2-SNOW-10K, “Net Revenue Retention Rate”, linhas 1774–1780].

### Evidência Confluent

Confluent Cloud admite pay-as-you-go ou usage-based commitment; revenue é reconhecida conforme uso [SRC-M2-CONFLUENT-10K, linhas 2115–2117]. Seu dollar-based NRR começa pelo ARR da coorte 12 meses antes, compara o ARR dos mesmos clientes no fim e, para Cloud/WarpStream, anualiza consumo dos últimos três meses [SRC-M2-CONFLUENT-10K, “Dollar-Based NRR”, linhas 2192–2197].

### Trabalho

Preencha para cada empresa:

1. unidade;
2. população;
3. receita/medida;
4. janela;
5. tratamento de churn;
6. tratamento de consumo;
7. exclusões/ajustes.

Responda:

- O que pode ser comparado diretamente?
- O que exige normalização?
- Quais cinco dados adicionais um operador pediria antes de usar NRR para capital allocation?
- Por que “NRR maior” não prova, isoladamente, melhor unit economics?

### Saída

Uma página com tabela de definição, três riscos de interpretação e uma recommendation: comparar, normalizar ou recusar a comparação.

## CASE-M2-SYNTHETIC-VETOR — Vetor AI Brasil

**Tipo:** cenário 100% sintético. “Vetor AI Brasil” não representa empresa real.\
**Moedas:** R$ mil quando indicado; supplier pricing em US$; FX didático explícito.\
**Data didática:** 2026-07-23.

### Bloco A — Opening cohort

MRR em R$ mil:

| cliente | opening | ending | nota |
|---|---:|---:|---|
| Alpha | 90 | 120 | expansão |
| Beta | 70 | 56 | contração |
| Gamma | 40 | 0 | churn |
| Delta | 50 | 50 | estável |

Dois logos novos iniciaram durante a janela; eles ficam fora da opening cohort.

### Bloco B — Aquisição

Pool trimestral, em R$ mil:

| item | valor |
|---|---:|
| salários de aquisição | 300 |
| mídia e eventos | 180 |
| comissão de new business | 60 |
| tooling | 30 |
| overhead alocado | 30 |

Foram adquiridos 15 logos pagos. MRR inicial médio = R$8 mil/logo; margem de contribuição esperada = 62,5%; churn mensal usado no cenário simples = 2,5%. Não há lag adicional no exercício; em uso real ele deve ser testado.

### Bloco C — Carga de trabalho enterprise

Fornecedor fictício do exercício: Modelo A, a US$2,50/MTok input e US$15/MTok output. Esses valores são premissas sintéticas e não descrevem um produto comercial.

| input | valor |
|---|---:|
| input tokens/mês | 400 MTok |
| output tokens/mês | 80 MTok |
| cloud + observability + support padrão | US$800/mês |
| FX didático | R$5,00/US$ |
| preço list direto | R$30 mil/mês |
| desconto pedido | 20% |
| support custom adicional pedido | R$3 mil/mês |
| margem-alvo mínima | 45% |

Opção de parceiro: share de 15% da receita líquida; sem custo adicional de support custom; margem-alvo mínima = 40%.

### Bloco D — Capital allocation

Cash flows incrementais after-tax em R$ mil; `CF0` ocorre hoje. Hurdle didático = 16% nominal em BRL.

| alternativa | CF0 | ano 1 | ano 2 | ano 3 | ano 4 |
|---|---:|---:|---:|---:|---:|
| Build direto | -750 | 100 | 300 | 500 | 550 |
| Partner-led | -400 | 160 | 220 | 260 | 260 |

Downside comum: todos os inflows ficam 20% menores; `CF0` não muda. Sunk cost anterior de R$120 mil existe, mas já foi pago e não entra na decisão futura. Não há valor terminal, dívida, capital de giro adicional ou inflação além do que já está nos cash flows. Para decisão real, esses itens exigiriam validação.

### Bloco E — Restrições de governança

- Orçamento pode financiar apenas uma alternativa.
- Qualquer preço abaixo do floor ou NPV negativo exige CFO review.
- Qualquer supplier price com mais de 30 dias exige recheck.
- Não use Rule of 40 como gate do projeto.
- Critérios de encerramento estratégicos serão definidos no M3; aqui, proponha somente gates financeiros de liberação.

### Deliverable do case

Um memo de até 600 palavras com:

1. economics reconstruídos;
2. preço/reformulação recomendada;
3. alternativa de capital recomendada e rejeitada;
4. downside;
5. dois gates de liberação;
6. CFO/controller questions.
