# M2 — Caderno de exercícios

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

Use somente dados fornecidos. Exercícios `ASSESS` são individuais e sem AI. Mostre fórmula, unidade e arredondamento a duas casas.

## WB-M2-01 — Cohort model e acquisition economics

### Prática

Recalcule os exemplos 1 e 2 de `module.md` e altere apenas uma premissa por vez: expansão −50%, margem −10 p.p. e churn +1 p.p. Registre impacto e decisão.

### ASSESS-M2-A — Mechanics (45 pontos K)

Use `CASE-M2-SYNTHETIC-VETOR`, blocos A e B.

1. Calcule opening MRR, ending MRR da coorte, expansão, contração e churn em R$ mil. **(8)**
2. Calcule NRR e GRR. Explique por que novos logos não entram. **(10)**
3. Calcule pool fully-loaded, CAC/logo, gross profit mensal/logo e payback. **(10)**
4. Calcule LTV simples e LTV/CAC. Dê duas razões para não tratar o resultado como caixa observado. **(9)**
5. Escreva o contrato de definição mínimo para CAC e NRR: unidade, população, período, moeda, receita/custo e versão. **(8)**

**Erros críticos:** expansão em GRR; novos logos na opening cohort; payback usando revenue em vez de gross profit; pool/denominador oculto.

## WB-M2-02 — Pricing architecture e deal guardrails

### Prática

Monte uma tabela com três ofertas para startups, mid-market e enterprise: meter, commit, overage, cost tree, p50/p95, floor, rate limit, approver e recheck date.

### ASSESS-M2-B, parte 1 — Carga de trabalho e desconto (30 dos 55 pontos J)

Use `CASE-M2-SYNTHETIC-VETOR`, blocos C e E.

1. Calcule custo do modelo em US$, custo total em US$ e R$, contribuição e margem no list direto. **(8)**
2. Calcule contribuição e margem após 20% de desconto e support custom. **(6)**
3. Calcule price floor direto para margem-alvo de 45%. **(4)**
4. Na opção partner-led, calcule margem no list e preço mínimo para margem de 40%, considerando share de 15% da receita. **(5)**
5. Recomende `aprovar`, `reformular` ou `recusar`. Inclua give-get, approval responsável, expiry, supplier-price recheck e dois gatilhos. **(7)**

**Erros críticos:** omitir output tokens, support custom, FX ou partner share; calcular margem sobre custo; tratar preço público como permanente.

## WB-M2-03 — Capital allocation memo

### Prática guiada

Recalcule o exemplo 4 de `module.md`, inclusive downside. Explique por que sunk cost não entra e por que payback não substitui NPV.

### ASSESS-M2-B, parte 2 — Investment committee (25 dos 55 pontos J)

Use `CASE-M2-SYNTHETIC-VETOR`, blocos D e E.

1. Calcule NPV base das duas alternativas a 16%. **(8)**
2. Calcule NPV no downside de −20% nos inflows. **(6)**
3. Calcule payback simples e explique dois limites de IRR/payback. Não é necessário calcular IRR. **(4)**
4. Escreva recommendation de até 250 palavras com alternativa rejeitada, dois gates financeiros, gatilho de revisão e três questões para CFO/controller. **(7)**

**Erros críticos:** incluir sunk cost de R$120 mil; descontar com 14%; reduzir `CF0` no downside; usar lucro em lugar dos cash flows; aprovar alternativa de NPV negativo sem condição/escalation.

## Template — Decision ledger

```text
Decisão:
Unidade/população/período:
Economics base:
Economics downside:
Preço/floor:
Alternativa recomendada:
Alternativa rejeitada:
Trade-off:
Gate 1 / owner / data:
Gate 2 / owner / data:
Trigger de revisão:
CFO/controller escalation:
Source recheck date:
```

## Critério de conclusão

`ASSESS-M2-A + ASSESS-M2-B ≥ 80/100`, zero erro crítico. Artefato pode alimentar capstone, mas não altera prontidão sem revisão individual.
