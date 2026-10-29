# M6 — Workbook

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

Use somente os dados do case. Exercícios `ASSESS` são individuais e sem AI. Mostre fórmula, unidade e arredondamento a duas casas.

## WB-M6-01 — Market-access thesis

### Prática

Use `CASE-M6-REAL-ROLE-SIGNAL`. Construa claim ledger com colunas `claim, class, source_id, locator, allowed inference, prohibited inference, recheck date`.

Depois produza três modes para o Brasil: cross-border, partner-led e first local team. Cada um precisa de hipótese, custo, control, delivery, risk, gate e alternative rejected.

## WB-M6-02 — Country P&L e revenue operating model

### ASSESS-M6-A — Mechanics (40 pontos K)

Use `CASE-M6-SYNTHETIC-ARCO`, blocos A e B.

1. Calcule expected accessible logos, bookings e first-year revenue. **(12)**
2. Reconstrua gross profit/margin, local contribution/margin e fully allocated result/margin no base. **(12)**
3. Recalcule as mesmas linhas no stress. **(10)**
4. Explique a diferença entre PTAX spot, Focus expectation e um FX scenario interno; diga qual owner valida hedge. **(6)**

**Fatal errors:** TAM lançado como revenue; P&L não reconcilia; HQ allocation oculto; FX sem moeda/data/tipo; dado sintético atribuído a empresa real.

### Prática

Crie bridge de P&L `base → volume → FX → fixed cost → allocation`. Em seguida modele coverage: accounts por owner, partner lane, implementation capacity, stage criteria e forecast cadence.

## WB-M6-03 — Entry, HQ rights e diplomacy

### ASSESS-M6-B — Executive judgment (60 pontos J)

Use `CASE-M6-SYNTHETIC-ARCO`, blocos C–G.

1. Calcule o weighted score dos três entry modes; recomende um e declare o que M7 ainda precisa validar. **(12)**
2. Calcule commit, best-case total e pipeline total; faça a forecast call contra o plano sem double count de partner influence. **(12)**
3. Avalie o gate 180: `scale`, `hold/remediate` ou `stop`. Dê evidência, owner e próximo gate. **(12)**
4. Calcule incremental expected ARR, contribution e first-year net da exception. Recomende approve/reformulate/reject. **(12)**
5. Responda ao freeze com um resource ask de até 180 palavras: fato, economic implication, options, recommendation, rights, milestone e decision-by date. **(12)**

**Fatal errors:** claim sem fonte; partner influence somado como revenue; subsidiária tratada como automaticamente autorizada; exception aprovada sem economics/expiry; promessa fora de decision right; “Brasil é diferente” usado sem evidência.

## Templates

### Entry gate card

```text
Gate/date:
Hypothesis:
Evidence required:
Actual:
Economics:
Decision: scale / hold / reallocate
Owner:
Next review:
M3 kill-criteria interface:
```

### HQ exception ledger

```text
Exception ID:
Standard:
Requested delta:
Economic delta:
Risk/specialist veto:
Decision right:
Approver:
SLA:
Expiry:
Reapproval trigger:
Outcome:
```

### Corporate diplomacy note

```text
Fact + source/date:
Economic/operational implication:
Options:
Recommendation:
Ask:
Owner:
Decision-by:
```

## Conclusão

`ASSESS-M6-A + ASSESS-M6-B ≥ 80/100`, zero fatal. Artefatos alimentam capstone; não provam readiness sem revisão individual.
