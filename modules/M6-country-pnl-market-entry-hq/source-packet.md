# M6 — Referências de apoio herdadas

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

**Data de corte:** 2026-07-23.\
**Regra:** todo fato externo tem `source_id` e locator em `sources.md`. Fórmulas e frameworks marcados “definição do curso” são convenções operacionais, não fatos de mercado.

## 1. Claims aceitas

| claim_id | classe | claim | fonte/locator | consequência |
|---|---|---|---|---|
| M6-C01 | external_fact | Em 2025-11-04, OpenAI declarou Brasil top 3 em uso semanal do ChatGPT, cerca de 140 milhões de mensagens/dia e top 2 em developers ativos na API. | `SRC-M6-OAI-BRAZIL`, linhas 39–43 | Adoção é sinal de prioridade, não revenue access. |
| M6-C02 | external_fact | A JD Head GTM Partnerships LATAM fica em São Paulo e cobre estratégia/execução de ecossistema em Central e América do Sul. | `SRC-M6-OAI-GTM-JD`, linhas 23–39 | Unidade do cargo é região e função; não Full-P&L Brasil. |
| M6-C03 | external_fact | A JD possui resultados partner-sourced/influenced/delivered, alocação de recursos, governança e liderança de Partner Directors. | `SRC-M6-OAI-GTM-JD`, linhas 41–99 | Revenue model precisa attribution rules, capacity e decision rights. |
| M6-C04 | external_fact | A JD Regional Client Partner é baseada no escritório de São Paulo e inclui target, full cycle, account plans e previsão. | `SRC-M6-OAI-ADS-JD`, linhas 32–53 | Há operação funcional local observável; ainda não prova Country GM. |
| M6-C05 | external_fact | Claude foi disponibilizado a consumidores e empresas no Brasil em 2024-08-01 via web, apps e API. | `SRC-M6-ANT-BRAZIL`, linhas 11–22 | Product availability precede ou independe de local entity/team. |
| M6-C06 | external_fact | Anthropic colocou Índia em segundo em share de uso, seguida por Brasil, Japão e Coreia do Sul com shares semelhantes. | `SRC-M6-ANT-GEO`, linhas 27–38 | Usage share não autoriza ranking isolado nem revenue inference. |
| M6-C07 | external_fact | O guia ITA 2025 cita agentes, distribuidores e representantes e recomenda escolher cidades/regiões ao construir canais/base. | `SRC-M6-TRADE-ENTRY`, linhas 230–237 | Brasil não deve ser modelado como cobertura homogênea nacional. |
| M6-C08 | external_fact | Invest & Export Brasil reúne informação oficial para agentes estrangeiros que pretendem investir no país. | `SRC-M6-GOV-INVEST`, abertura; atualizado 2026-02-13 | Entry mode começa por source map oficial e specialist review. |
| M6-C09 | external_fact | A meta Selic vigente desde 2026-06-18 era 14,25% a.a. | `SRC-M6-BCB-SELIC`, tabela reunião 279 | Snapshot datado para cenário; nunca premise sem recheck. |
| M6-C10 | external_fact | A PTAX venda de 2026-07-22 às 13:03:20 era R$5,0638/US$. | `SRC-M6-BCB-PTAX`, JSON `cotacaoVenda` | Distinguir data, lado e fonte de FX. |
| M6-C11 | external_fact | Focus resume expectativas de mercado; projeções não são do BCB. | `SRC-M6-BCB-FOCUS`, introdução | Não chamar consenso de “previsão do Banco Central”. |
| M6-C12 | external_fact | IPCA de junho de 2026 foi 0,16%, divulgado em 2026-07-10. | `SRC-M6-IBGE-IPCA`, linhas 551–557 | Snapshot realizado; não annualizar um mês mecanicamente. |

## 2. Definições operacionais do curso

### Access funnel

```text
TAM teórico
× fit de use case
× product/localization readiness
× contracting/compliance readiness
× reachable coverage
× qualified conversion
× win rate
= logos acessíveis
```

`Accessible revenue = logos acessíveis × ACV/usage × ramp × retention`. Cada multiplicador tem fonte, responsável, data e faixa; se faltar, é hipótese.

### Country P&L em duas vistas

1. **Controllability view:** revenue; direct cost; gross profit; local controllable OPEX; local contribution.
2. **Fully allocated view:** local contribution menos HQ allocations e shared costs.

As duas reconciliam ao ledger corporativo. Não maquiar o país excluindo custo de servir nem responsabilizar o líder por alocação sem direito de decisão.

### FX

Separar:

- transaction exposure: contrato, cobrança e pagamento;
- translation exposure: conversão para reporting;
- economic exposure: preço/demanda/custo mudam com FX.

O módulo calcula sensitivities; hedge, tax e treasury policy exigem CFO/controller.

### Decision-right contract

Para cada decisão: `D` decide; `R` recomenda; `C` consulta; `V` veto especializado; `I` informado. Defina limite, SLA, expiry e escalation. “Alinhamento” sem decisão, responsável e prazo não é governance.

### 90/180/365 gates

- **90:** falsificar tese e provar acesso.
- **180:** provar motion repetível e delivery.
- **365:** provar economics, previsão e estrutura escalável.

São gates cumulativos, não calendário de atividade. Critérios de encerramento estratégicos pertencem ao M3; M6 registra evidence gates de entrada/escala.

## 3. Fatal-error guardrails

Bloqueia release: unsupported market claim; adoção tratada como revenue; P&L que não reconcilia; revenue sem cost-to-serve; FX sem data/moeda/lado; previsão sem categoria e next step; double count de partner-influenced revenue; entity/tributo/dados tratados como resolvidos sem M7; overreach de decision rights; cenário sintético atribuído a empresa real.

## 4. Escalation map

- CFO/controller: allocations, FX policy, pricing currency, cash, tax, hurdle, headcount release.
- Legal/tax/privacy/security via M7: entity, EOR, contracts, data, sector rules.
- Product/engineering: localization, roadmap exception, capacity and SLA.
- HQ GTM: territory, partner attribution, account ownership, conflict and previsão.
- Executive sponsor: escolha e renúncia regional, resource reallocation, exception above limite.
