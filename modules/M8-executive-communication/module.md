# M8 — Comunicação executiva: decisão legível sob challenge

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## 1. Decisão executiva central

Um board, CFO ou HQ não precisa de mais narrativa. Precisa responder:

> **Qual decisão deve ser tomada agora, com qual evidência, contra quais alternativas, aceitando qual risco e com que trigger de revisão?**

Comunicação executiva é parte do mecanismo de decisão. O memo prepara o debate; o QBR corrige a visão do negócio; a defesa testa autoria e julgamento; o registro preserva por que a decisão foi tomada. O output não é “parecer executivo”. É reduzir ambiguidade sem apagar incerteza.

## 2. Como escolher a profundidade

Este módulo não presume experiência, senioridade ou lacunas do aluno. Use o diagnóstico por competência e o objetivo escolhido para decidir o que estudar. Sem avaliação, a recomendação é provisória: estudar ou fazer a prova de entrada. Cargo, tempo de carreira e autoavaliação não dispensam conteúdo. As regras da edição pública em `diagnostic/README.md` prevalecem sobre referências legadas a placement, test-out ou M0.

## 3. Conhecimentos prévios e test-out

M8 consome, sem reensinar:

- P&L, forecast e bridge de M1;
- unit economics e investment logic de M2;
- choices e kill criteria de M3;
- cadence/decision rights de M4;
- country economics e HQ contract de M6;
- risk register e escalonamento de M7.

Test-out por subcompetência exige:

- `K ≥ 85`, `J ≥ 80`;
- dois casos independentes do mesmo domínio;
- zero fabricação factual;
- zero omissão de risco material;
- um memo e uma defesa oral individual em forma nova.

Sem resultado M0, faça o módulo completo. Simulação melhora K/J; P permanece pendente.

## 4. Learning outcomes mensuráveis

Ao final, você consegue:

1. distinguir board memo, investment memo, executive update e QBR pelo decision right;
2. escrever recommendation, options, economics, risk, dissent, trigger e ask em duas páginas;
3. explicar miss por bridge causal, revisar forecast e propor ação;
4. marcar `actual`, `estimate`, `assumption`, `unknown` e `decision`;
5. defender a mesma decisão em PT e EN sem trocar números ou limites;
6. mudar altitude entre headline, mecanismo e evidência;
7. responder “não sei” com contenção, owner, prazo e impacto;
8. converter challenge em decisão ou próximo passo registrado.

## 5. Mapa de conceitos

```text
Decision right
     │
     ├── information need ──> memo / update / QBR
     │                           │
     │                           ├── facts + status
     │                           ├── options + economics
     │                           ├── risk + dissent
     │                           └── recommendation + ask
     │
     └── challenge room ──> answer ─> evidence ─> caveat ─> decision
                                      │
                                      └── action / owner / date / log
```

**Regra:** formato segue decisão. Slide, memo ou fala são recipientes. Nenhum formato salva raciocínio sem recommendation, consequência e ask.

## 6. Lições

### L1 — O memo começa pelo decision right

A FRC orienta que papers de board sejam precisos, claros, completos e atuais, tragam resumo, indiquem o que se espera do diretor e cheguem com antecedência suficiente; também recomenda explicitar success criteria e permitir constructive challenge. `[SRC-COM-FRC-2024]`

A SEC separa clareza de simplificação indevida: plain English organiza informação complexa para entendimento, não remove complexidade necessária. `[SRC-COM-SEC-PLAIN]`

#### Quatro outputs diferentes

| Output | Pergunta | Ask | Erro típico |
|---|---|---|---|
| Board memo | que decisão reservada ao board é requerida? | approve / reject / defer / condition | contexto longo antes da recomendação |
| Investment memo | este capital merece ser comprometido ou continuado? | fund / stage / stop / reallocate | upside sem downside ou kill trigger |
| Executive update | o que mudou e quem precisa agir/saber? | acknowledge / unblock / escalate | update que esconde uma decisão |
| QBR de miss | por que o plano falhou e qual forecast substitui o anterior? | accept reset / resource / corrective action | desculpa, atividade ou cherry-picking |

O practitioner insight publicado pelo HKS Policy Memos Resource recomenda memo curto centrado na decisão, razão de urgência, próximos passos e perguntas prováveis. É uma preferência identificada em contexto de policy, útil como lente, não uma regra corporativa. `[SRC-COM-HKS-MEMO]`

#### Arquitetura de duas páginas

1. `Decision required` — verbo, owner e deadline.
2. `Recommendation` — uma frase testável.
3. `Why now` — custo de esperar ou janela que fecha.
4. `Evidence` — três a cinco fatos, cada um com status.
5. `Options` — incluindo status quo.
6. `Economics` — capital, downside, reversibilidade e opportunity cost.
7. `Risk and dissent` — o melhor argumento contrário.
8. `Conditions` — gate, trigger, kill criterion.
9. `Next 30/60/90` — owner e data.

O memo da Amazon é um caso de processo: a carta de 2017 descreve narrativas de seis páginas, leitura silenciosa no início da reunião, reescrita e colaboração. Isso prova a prática declarada da empresa; não prova que seis páginas sejam ideais em outro contexto. `[SRC-COM-AMZN-2017]`

#### Exemplo resolvido 1 — investment ask em estágios

`CENÁRIO SINTÉTICO — Aurora AI Brasil`.

Dados disponíveis:

- 12 discovery calls concluídas;
- 6 problemas confirmados;
- 3 pilotos aceitos;
- zero contrato assinado;
- entidade local custaria R$ 4,8 milhões por 12 meses;
- fase de validação cross-border custaria R$ 1,2 milhão por 90 dias;
- board tem R$ 6 milhões disponíveis.

**Versão fraca**

> Brasil é estratégico e já temos forte tração. Recomendo abrir a entidade agora para capturar o mercado.

Falhas: “estratégico” sem critério; piloto vira tração; não há alternativa, downside, gate ou ask delimitado.

**Versão resolvida**

> **Decisão requerida até sexta:** autorizar R$ 1,2 milhão para uma fase cross-border de 90 dias; não autorizar entidade local agora.
>
> **Recommendation:** comprar informação antes de comprar estrutura. Os 12 discoveries e 3 pilotos demonstram problema e willingness to test, não repeatable revenue. A fase preserva R$ 4,8 milhões de option value.
>
> **Alternativas:** (A) entidade agora — maior controle, mas compromete 80% do capital antes do primeiro contrato; (B) validação em estágio — menor velocidade aparente, preserva capital; (C) esperar — preserva caixa, mas perde os três pilotos.
>
> **Gates em D+90:** ≥2 contratos pagos; ≥1 processo enterprise de security concluído; pipeline qualificado ≥3× o target do próximo trimestre; unit economics dentro do guardrail aprovado por Finance.
>
> **Kill trigger:** menos de dois contratos ou blocker de security sem owner/roadmap. Nesse caso, não abrir entidade e realocar o saldo.
>
> **Risco contrário:** cross-border pode atrasar procurement. Mitigação: mapear blocker por piloto em D+15 e escalar ao board se dois dos três exigirem entidade.
>
> **Ask:** approve R$ 1,2 milhão, gates e authority para interromper sem nova rodada de defesa.

Por que funciona: não converte sinal em fato; explicita renúncia; liga capital a informação; pede uma decisão específica; permite ao board discordar.

### L2 — QBR de miss: verdade, bridge, forecast, ação

A guidance de MD&A da SEC pede foco em informação material, trends/uncertainties e análise das causas; também diz que uma visão balanceada inclui misses materiais, não só sucessos. M8 usa essa disciplina por analogia. Um QBR interno não é filing e pode ter outros deveres de confidencialidade e escalonamento. `[SRC-COM-SEC-MDA]`

#### Cinco estados de informação

| Código | Estado | Linguagem |
|---|---|---|
| A | actual medido | “fechamos em 1,62” |
| E | estimate | “estimamos 0,30–0,45 de impacto” |
| P | assumption/premissa | “assume contratação em M2” |
| U | unknown | “a causa ainda não foi isolada” |
| D | decision | “reduzimos o commit para 2,0” |

Nunca apresentar `E`, `P` ou `U` como `A`. Incerteza explícita é informação gerenciável; certeza fabricada é um risco adicional.

#### Estrutura do QBR de miss

1. `Headline`: actual vs plan e consequência.
2. `Bridge`: quantificação mutuamente exclusiva, sem dupla contagem.
3. `Root causes`: controlável, não controlável e causa ainda aberta.
4. `What we got wrong`: premissa/processo/controle.
5. `Revised forecast`: base, downside e data vintage.
6. `Corrective action`: owner, leading indicator, threshold.
7. `Risk`: o que pode piorar antes de melhorar.
8. `Ask`: decisão ou recurso.

#### Caso público — NIKE FY2025

No release FY2025, a NIKE reportou revenue anual de US$ 46,3 bilhões, 10% abaixo do ano anterior, e gross margin de 42,7%, queda de 190 basis points; no Q4, revenue caiu 12% e net income 86%. O release atribuiu pressão de margem a descontos, mix e inventory obsolescence, entre outros drivers. `[SRC-COM-NIKE-Q4FY25]`

O 10-K confirma revenue de US$ 46,309 bilhões e detalha a bridge de gross margin, incluindo efeito de average selling price/descontos e mix, outros custos, Converse, FX e custos de produto. `[SRC-COM-NIKE-10KFY25]`

O caso é útil porque:

- abre com números que enfraquecem a narrativa;
- separa reported e currency-neutral quando aplicável;
- expõe drivers;
- mostra action language.

Limite: earnings release é comunicação externa regulada; não revela o debate interno, o forecast vintage nem todas as alternativas. Não o trate como “QBR perfeito”.

#### Exemplo resolvido 2 — QBR de miss

`CENÁRIO SINTÉTICO — Aurora AI Brasil, Q3`.

| Métrica | Plano | Real | Variância |
|---|---:|---:|---:|
| New ARR | 2.400 | 1.620 | (780) |
| Gross margin | 70% | 63% | (7 pp) |
| Burn | 1.800 | 2.350 | +550 |
| Pipeline qualificado Q4 | 7.200 | 5.100 | (2.100) |
| Forecast accuracy | 85% | 58% | (27 pp) |

Bridge do new ARR: deal escorregado `(350)`; security atrasou dois deals `(220)`; capacidade superestimada `(140)`; perda competitiva `(70)`. Total `(780)`.

**QBR resolvido**

> **Headline:** Q3 fechou 32,5% abaixo do plano de new ARR; o problema é simultaneamente execução e qualidade do forecast. Gross margin e burn também violaram guardrails.
>
> **O que erramos:** incluímos um deal com security pendente em commit; modelamos capacidade pela quota nominal, não pela ramp; o approval de contratação ocorreu antes do gate de pipeline.
>
> **Forecast revisado:** Q4 commit 2.000, base 2.350, downside 1.650. Vintage bloqueado em 03/out; assumptions anexas.
>
> **Ações:** Revenue Lead remove deal sem security do commit imediatamente; Finance implementa forecast vintage semanal; Country Lead congela uma vaga até pipeline qualificado ≥3× commit por duas semanas.
>
> **Risco:** o freeze reduz cobertura no fim do trimestre. Trigger para reabrir: security backlog <10 dias e coverage ≥3×.
>
> **Ask ao HQ:** aceitar reset de Q4 para 2.350 base e manter budget apenas sob os dois triggers.

O memo assume responsabilidade sem fingir controle sobre tudo. A causa não controlável continua visível, mas não serve de desculpa.

### L3 — Defesa adversarial EN/PT

O challenge não é interrupção do memo; é parte do processo decisório. A FRC associa board effectiveness a debate, constructive challenge, success criteria e registro das razões da decisão. `[SRC-COM-FRC-2024]`

#### Protocolo A-B-C-D

1. `Answer`: responda a pergunta em uma frase.
2. `Basis`: dê o fato, cálculo ou mecanismo que sustenta.
3. `Caveat`: diga o limite, risco ou unknown material.
4. `Decision`: volte ao ask ou próximo passo.

**PT**

> Minha recomendação é manter a fase de validação e adiar a entidade. A base é zero contrato assinado e três pilotos ativos. O risco é procurement exigir presença local; saberemos em D+15. Peço autorização para R$ 1,2 milhão com kill gate em D+90.

**EN**

> My recommendation is to keep the validation phase and defer the entity. The evidence is zero signed contracts and three active pilots. The material risk is that procurement may require local presence; we will know by day 15. I am asking for R$1.2 million with a day-90 kill gate.

A língua muda; o claim não.

#### Três níveis de altitude

| Nível | Uso | Resposta |
|---|---|---|
| 1 — headline | decisão | “Adiar entidade; financiar validação.” |
| 2 — mechanism | lógica | “Stage capital against three gates.” |
| 3 — evidence | auditoria | números, fonte, fórmula, owner, data |

Comece no nível 1. Desça quando perguntado. Não despeje nível 3 para evitar responder.

#### Hostile challenge

**“Why did you miss this?”**

Resposta ruim: “The market changed.”

Resposta forte:

> We missed because I allowed a security-dependent deal into commit and used nominal capacity. The market did not create those control failures. I have removed that deal, reset capacity, and locked a weekly vintage. The remaining unknown is procurement timing on two accounts; it is in downside, not commit.

**“Você está escondendo um problema de produto atrás do Brasil?”**

> Não. Dois sinais são locais — procurement e cobrança — e um é global — o gap de security workflow. Ainda não sei a parcela causal de cada um. Em D+10, Product e Security fecham a análise. Até lá, retiro os dois deals do commit e preservo o risco no downside.

**“Give me one number.”**

> The decision number is R$1.2 million at risk for 90 days. The range that matters is two to three paid contracts; below two, we stop.

Precisão executiva não é falsa exatidão. É tornar a incerteza decisiva explícita.

## 7. Práticas guiadas

### GP1 — compressão sem perda

Receba um pack de seis páginas. Produza:

- uma headline de 25 palavras;
- um memo de duas páginas;
- appendix de evidência;
- um ask com verbo, owner e deadline.

Teste: um leitor independente identifica recommendation, downside e ask em 90 segundos.

### GP2 — QBR red team

Use o cenário Aurora:

1. reconcilie o bridge;
2. marque A/E/P/U/D;
3. escreva QBR de uma página;
4. entregue a um reviewer que procura risco omitido;
5. revise apenas onde nova informação muda decisão.

### GP3 — defesa em três altitudes

Defenda o mesmo memo:

- 90 segundos em PT;
- 90 segundos em EN;
- cinco minutos de Q&A em cada idioma.

O painel compara números, claims, unknowns e ask entre as duas versões.

## 8. Casos

`cases.md` contém:

- caso real documentado NIKE FY2025;
- caso primário de processo Amazon 2017;
- cenário sintético Aurora Brasil com investment memo, QBR e painel hostil.

Empresa real nunca recebe fato inventado. Pergunta sem dado vira unknown ou pedido de fonte.

## 9. Erros executivos e sinais de alerta

- contexto antes da recomendação;
- “FYI” que contém decisão escondida;
- opção preferida sem status quo;
- número sem definição, período ou unidade;
- forecast sem vintage;
- miss explicado por atividade;
- causa e ação sem owner;
- upside tratado como base;
- material risk enterrado em appendix;
- unknown convertido em certeza durante challenge;
- mudar número entre PT e EN;
- responder pergunta diferente;
- excesso de detalhe como evasão;
- confidence teatral;
- “legal approved” sem owner/locator.

Fatal errors:

- fabricar fato, número, quote, source ou atribuição;
- ocultar risco material conhecido;
- mudar o status de estimate/assumption/unknown para actual sem evidência;
- defender recomendação incompatível com o próprio modelo;
- omitir conflito de interesse ou dissent material;
- alegar P real com base na simulação.

## 10. Checklist de decisão

- [ ] O decision right e o leitor estão nomeados.
- [ ] A primeira frase contém recommendation.
- [ ] O ask tem verbo, owner e deadline.
- [ ] Fatos têm fonte/locator; cenários estão rotulados.
- [ ] Actual, estimate, assumption, unknown e decision estão separados.
- [ ] Status quo aparece como opção.
- [ ] Economics e opportunity cost estão visíveis.
- [ ] O melhor argumento contrário foi steelmanned.
- [ ] Risco material não está enterrado.
- [ ] Gate, trigger e kill criterion são mensuráveis.
- [ ] Owners e datas fecham o loop.
- [ ] PT e EN mantêm a mesma verdade.
- [ ] A defesa retorna ao ask.
- [ ] Decision log registra razão e dissent.

## 11. Exercício aplicado à operação Brasil

Consuma o Brazil investment case de M6 e os outputs de M1/M2/M7. Não recalcule conceitos proprietários de outros módulos.

Entregue:

1. board memo PT de duas páginas;
2. investment memo EN de duas páginas;
3. QBR de miss de uma página;
4. executive update de 150 palavras;
5. appendix de evidence/status;
6. defesa gravada PT/EN;
7. decision log pós-painel.

O memo deve declarar onde depende de CFO/controller, Legal, Security ou HQ.

## 12. Avaliação e rubrica

Veja `workbook.md` para o enunciado e `answer-key.md` para o avaliador.

- `K`: 20%.
- `J`: 80%.
- mínimo: 80/100.
- zero fatal errors.
- primeira tentativa e defesa: individual, sem IA.
- IA permitida apenas para crítica pós-entrega, com disclosure; não altera a nota da primeira tentativa.

Avaliações:

- A1 — board/investment memo;
- A2 — QBR de miss + painel adversarial PT/EN.

## 13. Artefatos para o capstone

- board memo com recommendation e ask;
- investment memo com options, economics e kill trigger;
- QBR de miss com bridge e revised forecast;
- executive update;
- evidence/status appendix;
- bilingual defense log;
- decision/dissent log.

## 14. Leituras

Essenciais — 120 min:

- FRC, §§27–32 e 73–78 — 30 min: decision process, papers e challenge.
- SEC MD&A, III.A–B — 30 min: materialidade, miss, tendências e análise.
- SEC Plain English, pp. 5 e 9–17 — 20 min: clareza sem apagar complexidade.
- Amazon 2017, “Six-Page Narratives” — 15 min: processo de memo.
- NIKE FY2025 release + 10-K Item 7 — 25 min: caso de miss e drivers.

Opcional — 15 min:

- HKS Policy Memos Resource, practitioner insight: recommendation, why now, next steps e perguntas.

## 15. Fontes e limitações

Veja `sources.md`. Filings, guidance de board e practitioner materials têm audiências e deveres diferentes. M8 extrai mecanismos delimitados, não os transforma em regra universal.

O módulo não é aconselhamento de securities disclosure, jurídico ou investor relations. Comunicação real de companhia pública exige revisão competente. Nenhuma claim pessoal foi promovida. `course mastery` e `field readiness` permanecem separados.
