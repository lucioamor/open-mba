# M2 — Source packet aceito

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

**Data de corte:** 2026-07-23.\
**Regra:** cada fato externo abaixo aponta para `source_id` e locator em `sources.md`. Fórmulas marcadas “definição operacional do curso” são convenções explícitas para os exercícios, não uma norma universal.

## 1. Claims aceitas

| claim_id | tipo | claim curto | fonte/locator | implicação didática |
|---|---|---|---|---|
| M2-C01 | external_fact | Snowflake reconhece product revenue conforme consumo; timing pode exceder capacidade contratada ou rolar além do termo. | `SRC-M2-SNOW-10K`, “Product Revenue”, linhas 1765–1767 | Booking, compromisso, RPO e receita não são intercambiáveis. |
| M2-C02 | external_fact | O NRR de Snowflake usa uma coorte de contratos de capacidade e compara product revenue em dois anos; churned fica com zero. | `SRC-M2-SNOW-10K`, “Net Revenue Retention Rate”, linhas 1774–1780 | Registrar população, receita, janela e tratamento de churn. |
| M2-C03 | external_fact | O NRR de Confluent usa ARR da mesma coorte em dois pontos e anualiza três meses de consumo Cloud/WarpStream. | `SRC-M2-CONFLUENT-10K`, “Dollar-Based NRR”, linhas 2192–2197 | Mesmo nome de métrica pode ter construção diferente. |
| M2-C04 | external_fact | Confluent Cloud inclui data transfer, storage, compute units e add-ons; billing acumula por hora. | `SRC-M2-CONFLUENT-BILLING`, linhas 1083–1107 | Cost-to-serve deve decompor cada meter e granularidade. |
| M2-C05 | external_fact | Snowflake cobra principalmente storage, compute e transfer; créditos consumidos são multiplicados pelo preço do acordo. | `SRC-M2-SNOW-PRICING`, “Basic pricing model” e “Compute costs and credits” | Não usar um único preço médio sem workload/contrato. |
| M2-C06 | external_fact | Lovable usa créditos compartilhados; consumo varia por ação/plano e o pricing não é por seat. | `SRC-M2-LOVABLE-PRICING`, linhas 22–35 e 62–70 | Metro comercial pode combinar uso, grants e governança de workspace. |
| M2-C07 | external_fact | Lovable passou a saldo único para build, Cloud e AI, com visibilidade por membro, projeto e categoria. | `SRC-M2-LOVABLE-BILLING`, linhas 27–49 | Pricing confiável exige ledger de consumo, não só tabela de planos. |
| M2-C08 | synthetic_assumption | O Modelo A fictício do exercício custa US$2,50/MTok input e US$15/MTok output. | Premissa autoral do exercício, sem atribuição a fornecedor real | Separar input/output no custo por workload. |
| M2-C09 | teaching_convention | A decisão real deve conferir data, tier, cache e modalidade do preço contratado. | Protocolo de decisão do curso | As antigas afirmações sobre modelos e preços foram retiradas por falta de revalidação. |
| M2-C10 | external_fact | Stripe define CAC como sales and marketing costs divididos por novos clientes e alerta para timing/alocação. | `SRC-M2-STRIPE-CAC`, linhas 337–348 e seção seguinte | “Fully-loaded” exige pool e denominador documentados. |
| M2-C11 | external_fact | BVP define CAC payback considerando custo variável de servir e mostra CLTV sensível a alocação e desconto de fluxos. | `SRC-M2-BVP-CLOUD-METRICS`, linhas 183–194 | LTV simples é hipótese; cohort contribution é evidência melhor. |
| M2-C12 | external_fact | BVP descreve Rule of 40 como heurística e argumenta que ponderar crescimento e margem 1:1 pode ser inadequado. | `SRC-M2-BVP-RULE-X`, linhas 88 e 179–200 | Sempre nomear growth, margem, período e finalidade; nunca gate universal. |
| M2-C13 | external_fact | MIT define NPV como cash flows descontados, líquidos do upfront, usando opportunity cost of capital; não lucro contábil. | `SRC-M2-MIT-NPV`, PDF pp. 5–8 | Cash flow incremental, consistência nominal/real e risco vêm antes do NPV. |
| M2-C14 | external_fact | GitLab exige aprovação para elementos não padrão, racional de desconto, “what are we getting in return?” e reaprovação após alteração. | `SRC-M2-GITLAB-DEAL`, linhas 4082–4103 | Exception log, approver, give-get, validade e reaprovação são controles mínimos. |

## 2. Definições operacionais do curso

- **ARR contratual recorrente:** run-rate anual de componentes recorrentes ativos na data, excluindo serviços one-off e consumo não contratado. Em consumo, só usar um run-rate se a política disser janela, sazonalidade e tratamento de compromisso.
- **Opening cohort:** clientes ativos no início da janela; novos clientes ficam fora de GRR/NRR dessa coorte.
- **NRR:** `(receita final da coorte inicial, incluindo expansão) / receita inicial da coorte`.
- **GRR:** `(receita final da coorte inicial, limitada ao opening por cliente) / receita inicial da coorte`.
- **CAC fully-loaded:** `pool de aquisição definido / unidades adquiridas definidas`. Pool deve registrar pessoal, comissão, mídia, tooling, terceiros e overhead alocado; denominador pode ser logo ou gross new ARR, mas nunca ambos.
- **Payback:** `CAC / gross profit mensal incremental da coorte`. O cálculo usa margem do mesmo workload/coorte, não gross margin corporativa por conveniência.
- **LTV simples:** `ARPA mensal × margem de contribuição / churn mensal`. É uma hipótese estacionária; não usar quando churn é zero/negativo, instável, misto ou quando expansão/custo mudam materialmente.
- **Contribuição por workload:** `receita do workload – custo marginal atribuível`. Incluir modelo/inferência, cloud, storage, data transfer, support incremental, observability, fraude/abuso e taxas de canal quando materiais.
- **Preço-floor para margem-alvo `m`:** `custo atribuível / (1 − m)`.
- **Rule of 40 score:** `growth definido + margem definida`; escrever explicitamente os dois componentes e o período.
- **NPV:** `Σ CF_t/(1+r)^t`, incluindo `CF_0`. IRR é a taxa que zera NPV; não resolve escala, múltiplas raízes ou reinvestimento. Payback ignora fluxos após a recuperação e, se não descontado, time value.

## 3. Fatal-error guardrails

Bloqueia release local: unidade/população/período ocultos; expansão incluída em GRR; payback com receita em vez de gross profit; custo de workload incompleto; preço real desatualizado tratado como permanente; NPV com lucro contábil ou mix real/nominal; benchmark apresentado como regra; empresa real recebendo número sintético.

## 4. CFO/controller escalation

Escalar antes de decisão real quando houver: definição oficial de ARR/NRR; mudança de política de COGS; alocação de CAC material; custo compartilhado; hurdle/WACC; inflação/FX/tributo; capitalização; dívida/covenant; diluição/cap table; compromisso mínimo; preço abaixo do floor; exceção contratual; NPV material ou assimétrico.
