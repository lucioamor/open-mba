# M6 — Casos

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## CASE-M6-REAL-ROLE-SIGNAL — Adoção, presença e autoridade

**Tipo:** caso real documentado.\
**Regra:** nenhuma receita, margem, headcount ou authority é inferida.

### Evidência A — OpenAI

Em 2025-11-04, a OpenAI declarou Brasil top 3 em uso semanal do ChatGPT, cerca de 140 milhões de mensagens/dia e top 2 em developers ativos na API [SRC-M6-OAI-BRAZIL, linhas 39–43].

A JD `Head of GTM Partnerships, LATAM`, em São Paulo, cobre Central e América do Sul; possui estratégia regional, resultados partner-sourced/influenced/delivered, alocação de recursos, governance, escalation e liderança de Partner Directors [SRC-M6-OAI-GTM-JD, linhas 33–99]. A JD não declara P&L Brasil.

A JD `Regional Client Partner, Ads Solutions` é baseada no escritório de São Paulo e inclui target, full sales cycle, account plans e previsão [SRC-M6-OAI-ADS-JD, linhas 32–53]. É responsabilidade funcional de revenue, não Country GM.

### Evidência B — Anthropic

Claude ficou disponível no Brasil em 2024-08-01 via web, apps e API [SRC-M6-ANT-BRAZIL, linhas 11–22]. O Economic Index de 2025 colocou Índia em segundo por share de uso, seguida por Brasil, Japão e Coreia do Sul com shares semelhantes [SRC-M6-ANT-GEO, linhas 27–38].

Disponibilidade e share de uso não revelam enterprise revenue, local team, contracting model ou P&L.

### Trabalho

1. Classifique cada evidência como `adoption`, `product access`, `commercial presence`, `functional accountability` ou `Full-P&L`.
2. Liste o que a evidência permite afirmar e o que permanece hipótese.
3. Produza um role charter para a JD OpenAI, com cinco direitos observáveis e cinco direitos não presumidos.
4. Proponha um evidence request para transformar uso em revenue-access model.
5. Responda: “por que Brasil antes de outro mercado regional?” sem inventar market size.

### Saída

Uma página com claim ledger, authority boundary, access funnel e recommendation `enter / experiment / wait`.

## CASE-M6-SYNTHETIC-ARCO — Arco AI entra no Brasil

**Tipo:** cenário 100% sintético. Arco AI não representa empresa real.\
**Unidade:** R$ milhões, salvo indicação.

### Bloco A — Access funnel

| input | valor |
|---|---:|
| contas TAM teóricas | 1.000 |
| use-case fit | 60% |
| product readiness | 70% |
| contracting readiness | 80% |
| reachable coverage | 50% |
| qualified conversion | 40% |
| win rate | 25% |
| ACV médio | R$240 mil |
| receita do primeiro ano ramp | 65% |

Calcule em valor esperado; não arredonde logos antes de bookings.

### Bloco B — Country P&L

Base 365 dias:

| linha | base |
|---|---:|
| revenue | 8,00 |
| compute/inference | 2,00 |
| implementation/delivery | 0,80 |
| partner fees | 0,80 |
| local payroll | 2,40 |
| marketing/programs | 0,60 |
| office/travel | 0,20 |
| HQ allocation | 0,70 |

Stress:

- revenue −15%;
- compute volume acompanha revenue, depois BRL unit cost sobe 25% por FX;
- implementation fica R$0,80;
- partner fee = 10% do revenue;
- hiring freeze reduz payroll em R$0,20;
- programs reduzem R$0,10;
- office/travel e HQ allocation não mudam.

### Bloco C — Previsão trimestral

Plano = R$1,50 milhão.

| deal | amount | category | evidence | partner attribution |
|---|---:|---|---|---|
| Luma | 0,60 | commit | procurement concluído; PO draft | direct |
| Nexo | 0,50 | best case | security review sem decision date | partner-sourced |
| Prisma | 0,40 | pipeline | discovery; buyer não confirmado | direct |
| Terra | 0,30 | commit | redlines finais; assinatura em 10 dias | partner-influenced |
| Sol | 0,20 | best case | partner intro; sem buyer meeting | partner-influenced |

Partner-influenced é atributo, não receita adicional.

### Bloco D — Entry modes

Scores sintéticos de 1 (pior) a 5 (melhor):

| mode | speed | control | delivery | reversibility | fixed-cost efficiency |
|---|---:|---:|---:|---:|---:|
| cross-border | 5 | 2 | 2 | 5 | 5 |
| partner-led | 4 | 3 | 4 | 4 | 4 |
| subsidiary | 1 | 5 | 5 | 1 | 1 |

Pesos: speed 20%; control 20%; delivery 30%; reversibility 20%; fixed-cost efficiency 10%.

Nenhum score resolve legal/tax/entity. M7 deve validar o veículo.

### Bloco E — Gates observados

**Dia 90:** 32 buyer interviews; 12 qualified accounts; 3 design partners assinados; 1 paid deployment; 1 partner-sourced opportunity; product/contract blockers documentados.

**Dia 180:** 4 paid deployments; 3 atingiram o outcome acordado; partner-sourced pipeline = 25%; previsão error = 18%; gross margin = 48%.

Targets de promoção no dia 180:

- ≥4 paid deployments;
- ≥3 com outcome;
- partner-sourced pipeline ≥30%;
- previsão error ≤15%;
- gross margin ≥50%.

### Bloco F — HQ exception

Três deals têm ARR total de R$3,00 milhões. Win probability sem feature = 20%; com feature = 50%; margem de contribuição = 50%. Build one-off = R$400 mil; support incremental = R$80 mil no primeiro ano.

Rights vigentes:

- local `R` recomenda roadmap exception;
- HQ Product `D` decide;
- Finance `V` veta preço/motion abaixo da margem-floor;
- Security/Legal `V` em risco especializado;
- decision SLA = 15 dias; exception expiry = 12 meses.

### Bloco G — Miss e resource constraint

HQ congela uma contratação de R$300 mil/ano. O previsão commit está abaixo do plano. O country lead pede a vaga dizendo “Brasil é diferente e relacionamento leva tempo”.

### Deliverable

Memo de até 700 palavras:

1. access/revenue;
2. P&L base/stress;
3. entry mode;
4. previsão call;
5. gate 180;
6. exception recommendation;
7. rights/resource ask em linguagem econômica.
