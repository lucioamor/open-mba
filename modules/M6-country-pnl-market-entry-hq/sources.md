# M6 — Registro de fontes

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

**Verificação:** 2026-07-23. T0 = dado/portal de governo; T1 = página oficial de empresa, carreira ou governo. Referência educacional resumida; sem reprodução extensa. JDs, macro e FX são voláteis.

| source_id | tier | fonte e URL | locator usado | uso e limite |
|---|---:|---|---|---|
| `SRC-M6-OAI-BRAZIL` | T1 | OpenAI, [Brazil’s AI moment is here](https://openai.com/global-affairs/brazil-ai-moment-is-here/) | publicado 2025-11-04; linhas 39–43 | Sinal oficial de adoção; não prova receita, share ou P&L. |
| `SRC-M6-OAI-GTM-JD` | T1 | OpenAI, [Head of GTM Partnerships, LATAM](https://openai.com/careers/head-of-gtm-partnerships-latam-sao-paulo/) | “About the Role”; “Revenue & Go-to-Market Leadership”; “Operational Excellence”; “Team Leadership”, linhas 33–99 | Role charter funcional-regional e decision rights observáveis; JD viva, sem data de publicação, verificada em 2026-07-23. |
| `SRC-M6-OAI-ADS-JD` | T1 | OpenAI, [Regional Client Partner, Ads Solutions](https://openai.com/careers/regional-client-partner-ads-solutions-sao-paulo/) | “About the Role” e “In this role”, linhas 32–53 | Evidência de cargo baseado no escritório de São Paulo, target e forecast; não é P&L de país. |
| `SRC-M6-ANT-BRAZIL` | T1 | Anthropic, [Claude is now available in Brazil](https://www.anthropic.com/news/claude-brazil) | publicado 2024-08-01; linhas 11–22 | Disponibilidade de produto/canais; preços antigos da página não são usados. |
| `SRC-M6-ANT-GEO` | T1 | Anthropic, [Economic Index — Geography](https://www.anthropic.com/research/economic-index-geography) | publicado 2025-09-15; “Across countries”, linhas 27–38 | Participação de uso; não equivale a enterprise revenue nem market access. |
| `SRC-M6-TRADE-ENTRY` | T1 | U.S. International Trade Administration, [Brazil — Market Entry Strategy](https://www.trade.gov/country-commercial-guides/brazil-market-entry-strategy) | publicado 2025-08-21; “Overview”, linhas 230–237 | Alternativas de agentes/distribuidores/representantes e necessidade de foco regional; guia para exportadores, não parecer jurídico. |
| `SRC-M6-GOV-INVEST` | T0 | Governo Federal, [Invest & Export Brasil](https://www.gov.br/empresas-e-negocios/pt-br/invest-export-brasil) | atualizado 2026-02-13; abertura | Portal oficial de informações para investir/operar; serve como ponto de verificação, não como autorização automática. |
| `SRC-M6-BCB-SELIC` | T0 | Banco Central do Brasil, [Interest rate policy decisions](https://www.bcb.gov.br/en/monetarypolicy/interestrates) | reunião 279, 2026-06-17; vigência desde 2026-06-18 | Snapshot da meta Selic; reverificar na data da decisão. |
| `SRC-M6-BCB-PTAX` | T0 | Banco Central do Brasil, [PTAX OData — 2026-07-22](https://olinda.bcb.gov.br/olinda/servico/PTAX/versao/v1/odata/CotacaoDolarDia%28dataCotacao%3D%40dataCotacao%29?%40dataCotacao=%2707-22-2026%27&%24format=json) | `cotacaoVenda`; `dataHoraCotacao=2026-07-22 13:03:20.263945` | Snapshot de FX para ensinar data/side; não usar como forecast nem preço contratado. |
| `SRC-M6-BCB-FOCUS` | T0 | Banco Central do Brasil, [Focus — Relatório de Mercado](https://www.bcb.gov.br/publicacoes/focus) | relatório 2026-07-10, publicado 2026-07-13; introdução | Explica que projeções são expectativas de mercado, não projeções do BCB. |
| `SRC-M6-IBGE-IPCA` | T0 | IBGE, [National Consumer Price Index](https://www.ibge.gov.br/en/statistics/economic/prices-and-costs/17136-national-consumer-pricce-index.html) | “News and Releases”, linhas 551–557; calendário 629–653 | Snapshot mensal do IPCA e calendário; não extrapolar sem cenário. |

## Fontes rejeitadas e claims proibidos

- `mba-*.md` e o `target-intel-pack.md`: usados somente para calibrar perguntas; nunca como autoridade externa.
- “Top usage” ou disponibilidade de produto = receita acessível: rejeitado.
- “OpenAI Country GM Brasil” ou Full-P&L na JD observada: rejeitado; a vaga pública é Head funcional de partnerships LATAM.
- “Anthropic é isoladamente o terceiro maior mercado”: rejeitado; a fonte agrupa Brasil, Japão e Coreia do Sul com participações semelhantes.
- “Lovable tem Country Lead Brasil”: não demonstrado por fonte oficial; só pode aparecer como hipótese.
- Entidade, EOR, reseller, subsidiária, tributário, trabalhista, LGPD ou contratação: nenhuma conclusão jurídica é emitida; encaminhar ao M7 e especialistas.
- Números reais de receita Brasil, margem, headcount, pipeline, conversão ou CAC das empresas-alvo: não públicos nas fontes aceitas; não inferir.

## Limites de atualização

Antes de um memo real: reverificar JDs e target signals; capturar PTAX, Selic, IPCA e Focus com data/hora; obter forecast interno; validar tax/entity/contracting no M7; separar dado realizado de expectativa e cenário.
