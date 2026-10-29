# M2 — Registro de fontes

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

Verificação: **2026-07-23**. T0 = filing/registro oficial; T1 = documentação ou preço oficial; T2 = material operacional, acadêmico ou de especialista institucional. Uso: resumo curto para estudo; referências externas conservam seus próprios direitos; nenhuma reprodução extensa. Preços são voláteis e devem ser reverificados antes de uma decisão real.

| source_id | tier | fonte e URL | locator usado | uso e limite |
|---|---:|---|---|---|
| `SRC-M2-SNOW-10K` | T0 | Snowflake, FY2026 Form 10-K, [SEC filing](https://www.sec.gov/Archives/edgar/data/1640147/000164014726000008/snow-20260131.htm) | “Key Business Metrics”, “Product Revenue”, “Net Revenue Retention Rate”, linhas SEC 1765–1781 | Definição oficial de consumo e NRR; métrica específica da companhia, não benchmark universal. |
| `SRC-M2-CONFLUENT-10K` | T0 | Confluent, FY2025 Form 10-K, [SEC filing](https://www.sec.gov/Archives/edgar/data/1699838/000169983826000006/cflt-20251231.htm) | “Dollar-Based Net Retention Rate”, linhas SEC 2192–2197; “Subscription”, 2115–2117 | Definição oficial de NRR/ARR e volatilidade do consumo; não comparar sem normalização. |
| `SRC-M2-SNOW-PRICING` | T1 | Snowflake, [Pricing Calculator FAQ](https://www.snowflake.com/en/pricing-options/calculator/feedback-faqs/) | “Basic pricing model”; “Compute costs and credits” | Metros de storage, compute e transfer; total = créditos × preço contratual. Sem fixar preço universal. |
| `SRC-M2-CONFLUENT-BILLING` | T1 | Confluent Docs, [Manage Billing in Confluent Cloud](https://docs.confluent.io/cloud/current/billing/overview.html) | “Manage Billing”, linhas 1083–1116; “Pay-as-you-go”, 1150–1159 | Dimensões de consumo, cobrança horária e compromissos; preços atuais ficam no pricing oficial. |
| `SRC-M2-LOVABLE-PRICING` | T1 | Lovable, [Pricing](https://lovable.dev/pricing) | FAQ “What is a credit?”, linhas 22–35; teams/seats, 62–70 | Crédito compartilhado, consumo variável por feature/plano e ausência de seat pricing. |
| `SRC-M2-LOVABLE-BILLING` | T1 | Lovable, [Simplifying billing](https://lovable.dev/blog/simplifying-billing) | publicado em 2026-06-13; linhas 20–49 | Migração para saldo único e telemetria por membro/projeto/categoria. |
| `SRC-M2-OPENAI-PRICING` | T1 | OpenAI, [API model catalog](https://developers.openai.com/api/docs/models) | Locator herdado, pendente de revisão | Ponto de partida para consulta; nenhum preço específico é confirmado por esta edição. |
| `SRC-M2-ANTHROPIC-PRICING` | T1 | Anthropic, [Claude pricing](https://claude.com/pricing) | Locator herdado, pendente de revisão | Ponto de partida para consulta; nenhum modelo ou preço específico é confirmado por esta edição. |
| `SRC-M2-STRIPE-CAC` | T2 | Stripe, [CAC in SaaS](https://stripe.com/resources/more/cac-in-saas) | atualizado em 2025-07-30; “How to calculate CAC”, linhas 337–348 | Definição e disciplina de período/alocação; não adotar benchmark como regra. |
| `SRC-M2-BVP-CLOUD-METRICS` | T2 | Bessemer Venture Partners, [The five accounting metrics for cloud companies](https://www.bvp.com/atlas/cloud-computing-metrics) | “CAC payback” e exemplo CLTV, linhas 183–194 | Payback ajustado por custo de servir e limites do CLTV; material de investidor, não norma contábil. |
| `SRC-M2-BVP-RULE-X` | T2 | Bessemer Venture Partners, [The Rule of X](https://www.bvp.com/atlas/the-rule-of-x) | linhas 88 e 179–200 | Mostra Rule of 40 como heurística e critica ponderação 1:1; não usar como aprovação automática. |
| `SRC-M2-MIT-NPV` | T2 | MIT OpenCourseWare, [Normative Frameworks for Business Decisions](https://ocw.mit.edu/courses/15-031j-energy-decisions-markets-and-policies-spring-2012/ba02e762046b99e81578e7d19980bb22_MIT15_031JS12_lec10.pdf) | PDF pp. 5–8 | NPV, cash flow versus lucro, consistência real/nominal e opportunity cost of capital; apenas resumo curto e fórmula, sem reprodução de slides. |
| `SRC-M2-GITLAB-DEAL` | T2 | GitLab Handbook, [Sales Order Processing](https://handbook.gitlab.com/handbook/sales/field-operations/order-processing/) | “How to Submit a Quote for Discount and Payment Term Approval”, linhas 4082–4103 | Exemplo público de workflow de exceção, give-get e reaprovação; matriz interna não foi acessada nem reproduzida. |

## Fontes rejeitadas ou não usadas

- Fragmentos `mba-*.md`, blogs T4 e agregadores: apenas leads, nunca autoridade.
- Benchmarks universais de “CAC payback ideal”, “LTV/CAC ideal” ou “gross margin ideal”: excluídos. Variam por estágio, motion, segmento e definição.
- Preço contratual de Snowflake/Confluent: excluído porque depende de região, edição, compromisso e contrato.
- Qualquer unit economics interno de Lovable, Anthropic ou OpenAI: não é público nas fontes aceitas; nenhum foi inferido.
- Deal Approval Matrix do GitLab: link não público/terceiro ao handbook; o módulo usa somente o workflow público visível.

## Limites de uso

Este módulo ensina decisão e escalada. Não substitui política contábil, orçamento, treasury, tax, valuation ou parecer financeiro. Antes de uso real, o CFO/controller deve validar pool de CAC, COGS, hurdle, WACC, FX, tributos, capitalização, covenants e materialidade.
