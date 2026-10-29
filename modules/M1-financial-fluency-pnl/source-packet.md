# Referências de apoio — M1

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

**Status:** aceito para autoria do piloto\
**Data de referência:** 2026-07-23

## Decisões suportadas

- distinguir receita, billing, recebimento e caixa;
- reconciliar income statement, balance sheet e cash flow;
- construir P&L gerencial de país sem tratá-lo como demonstração estatutária;
- fechar rolling previsão, bridge e resposta ao desvio;
- identificar quando escalar para controller, CFO, banco ou especialista tributário.

## Fontes aceitas

| source_id | Tier | Uso | Locator |
|---|---|---|---|
| SRC-FIN-INVESTOR-10K | T0 | estrutura e leitura de 10-K | “Financial Statements and Supplementary Data” |
| SRC-FIN-SALESFORCE-10K-2026 | T0 | caso real de demonstrações, deferred revenue, AR e cash flow | Items 7–8; pp. 42–89; linhas SEC indicadas em `sources.md` |
| SRC-FX-BCB | T0 | fonte oficial para PTAX e dados cambiais no exercício | página de câmbio e capitais internacionais |
| SRC-PED-CMU-ALIGN | T1 | alinhamento outcome–prática–avaliação | “Align Assessments, Objectives, Instructional Strategies” |

## Claims admitidas

1. Um 10-K inclui demonstrações auditadas e notas; a leitura econômica exige Business, Risk Factors, MD&A e Item 8, não apenas a DRE. `[SRC-FIN-INVESTOR-10K]`
2. A Salesforce FY2026 reportou receita de US$41,525 bilhões, net income de US$7,457 bilhões e cash flow operacional de US$14,996 bilhões; as grandezas não são intercambiáveis. `[SRC-FIN-SALESFORCE-10K-2026]`
3. A Salesforce normalmente fatura assinaturas antecipadamente; valores faturados antes da prestação aparecem como unearned revenue e passam a receita conforme controle/serviço é transferido. `[SRC-FIN-SALESFORCE-10K-2026]`
4. O mesmo filing mostra que aumento de AR consumiu caixa operacional enquanto aumento de unearned revenue o favoreceu; lucro e caixa divergem por timing e itens não caixa. `[SRC-FIN-SALESFORCE-10K-2026]`

## Limitações

- O caso usa US GAAP e uma companhia consolidada dos EUA; não ensina BR GAAP/IFRS normativo nem fechamento estatutário brasileiro.
- O P&L de país do cenário é gerencial e sintético; não é demonstração oficial de Lovable, Anthropic ou OpenAI.
- Regras tributárias não são modeladas em M1. M7 define issue-spotting e escalation; o modelo usa uma linha de impostos como premissa editável, não parecer.
- PTAX é fonte de referência do exercício; a taxa contratada real inclui spread, timing e instituição.
