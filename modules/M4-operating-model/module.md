# M4 — Modelo operacional: resultado sem depender de uma pessoa

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## 1. Decisão executiva central

A operação cresce, mas toda exceção chega ao Country Lead. Ele aprova descontos, traduz HQ, revisa eventos, destrava procurement, corrige mensagem e fecha handoffs. O output parece alto; o sistema é frágil.

A decisão é: **que mecanismo remove o líder do caminho crítico sem dispersar controle?**

Operating model é a ligação entre estratégia e trabalho recorrente:

- decisões e autoridade;
- fluxo de valor;
- interfaces HQ↔local;
- informação e cadência;
- controles e escalation;
- capacidade e tecnologia;
- aprendizagem e mudança.

Organograma mostra reporting. Operating model mostra como uma decisão atravessa o sistema.

## 2. Como escolher a profundidade

Este módulo não presume experiência, senioridade ou lacunas do aluno. Use o diagnóstico por competência e o objetivo escolhido para decidir o que estudar. Sem avaliação, a recomendação é provisória: estudar ou fazer a prova de entrada. Cargo, tempo de carreira e autoavaliação não dispensam conteúdo. As regras da edição pública em `diagnostic/README.md` prevalecem sobre referências legadas a placement, avaliação para dispensa ou M0.

## 3. Conhecimentos prévios e avaliação para dispensa

Avaliação para dispensa exige:

- desenhar decision rights de um caso real;
- provar dois mecanismos que funcionaram por ciclos sem intervenção pessoal;
- `K ≥ 85`, `J ≥ 80`;
- zero decisão crítica sem responsável, boundary ou escalation.

Sem resultado M0, faça o módulo completo.

## 4. Objetivos de aprendizagem

Ao final, você consegue:

1. distinguir estrutura, processo, mecanismo e controle;
2. mapear value stream e interfaces críticas;
3. atribuir responsável, authority, input, output e escalation a decisões;
4. calibrar velocidade por reversibilidade;
5. desenhar cadence que fecha o loop entre sinal, decisão, ação e revisão;
6. provar que um mecanismo funciona sem o designer.

## 5. Mapa de conceitos

```text
Strategy
   │
   ├─ choices ──> objectives ──> metrics
   │                               │
   └─ constraints                  ▼
                         Operating cadence
Value stream ── handoffs ── decisions ── actions ── review
                    │            │             │
                 controls     authority     learning
                    │            │             │
                    └──── escalation ──────────┘
```

## 6. Lições

### L1 — Resultado antes de atividade

Comece pelo resultado que o sistema precisa produzir e pela restrição:

- “reduzir time-to-value enterprise sem bypass de security”;
- “produzir previsão confiável até D-5”;
- “converter comunidade em oportunidades qualificadas sem capturar autoridade de Sales”.

Depois mapeie:

1. gatilho;
2. inputs;
3. decisão;
4. execução;
5. output;
6. customer interno/externo;
7. evidence;
8. failure mode.

Processo descreve passos. Mecanismo inclui responsável, cadence, input, output, limite e feedback. Controle reduz risco dentro do mecanismo.

**Teste do mecanismo**

Se remover o nome de o participante, outra pessoa sabe:

- quando começar;
- o que decidir;
- com que dados;
- dentro de qual boundary;
- quando escalar;
- como provar que terminou?

Se não, há um playbook dependente de autor, não uma capacidade organizacional.

### L2 — Decision rights e interfaces

Para cada decisão recorrente, registre:

| Campo | Pergunta |
|---|---|
| Decision | qual escolha muda recurso, risco ou compromisso? |
| DRI/Responsável | quem integra inputs e responde pelo resultado? |
| Decider | quem tem autoridade final? |
| Contributors | quem fornece expertise? |
| Informed | quem precisa agir depois? |
| Boundary | até onde a decisão é local? |
| SLA | quando precisa estar decidida? |
| Evidence | o que sustenta e registra? |
| Escalation | qual limite muda o nível? |

GitLab documenta DRI como poder decisório final dentro do escopo, com dever de consultar e responsabilidade pela execução. Seu operating rhythm de Enterprise AI divide priorização, construção técnica, plataforma, governance review e métricas entre responsáveis explícitos. Isso é evidência de uma escolha organizacional real, não prescrição universal. `[SRC-OPS-GITLAB-DRI]` `[SRC-OPS-GITLAB-RHYTHM]`

#### Exemplo resolvido 1 — desconto enterprise

`CENÁRIO SINTÉTICO`.

Decisão: aprovar desconto.

- AE: propõe economics e alternativa.
- Brazil Sales Lead: DRI até 10% dentro de guardrails.
- Finance: consulta margem, term e collectability.
- Product/Security: consulta somente se houver compromisso não padrão.
- Regional VP: decide 10–20% ou concessão estratégica.
- CFO/Deal Desk: decide acima de 20%, liability material ou precedent global.
- Legal: decide linguagem contratual dentro de sua autoridade; não “aprova economics”.

Boundary não é só percentual. Inclui:

- minimum gross margin;
- term/payment;
- custom work;
- data/security liability;
- most-favored terms;
- precedent.

O objetivo não é acelerar todo deal. É acelerar o deal padrão e tornar exceção visível.

### L3 — Reversibilidade calibra o processo

A carta da Amazon de 2015 distingue decisões quase irreversíveis, tratadas com deliberação, de decisões reversíveis, que podem ser tomadas rapidamente por indivíduos ou grupos pequenos de alto julgamento. `[SRC-OPS-AMAZON-2015]`

Use como pergunta, não dogma:

- custo financeiro de reversão;
- exposição legal/reputacional;
- customer harm;
- lock-in técnico/contratual;
- prazo para detectar erro;
- blast radius;
- option value preservado.

**Regra prática**

- two-way door: responsável local, timebox, guardrail, observability e rollback;
- one-way door: broader input, premortem, independent challenge, authority maior e contingency.

Erro comum: chamar qualquer decisão desejada de “reversível” ignorando reputação, dados ou precedente.

### L4 — Cadence fecha loops

Cadência não é calendário de reuniões. É frequência coerente com a meia-vida do sinal.

| Loop | Frequência | Input | Decisão | Output |
|---|---|---|---|---|
| pipeline/previsão | semanal | stages, capacity, risk | commit/upside e ação | previsão vintage |
| customer health | quinzenal | usage, support, sponsor | save/expand/escalate | account plan |
| operating review | mensal | P&L, people, risk | reallocate/correct | actions e responsáveis |
| QBR | trimestral | trend, strategy, capital | continue/change/kill | board/HQ ask |

O GOV.UK Service Manual recomenda autoridade no nível do serviço, boundaries claros e escalation somente quando a decisão sai desses limites. `[SRC-OPS-GOVUK-GOVERNANCE]`

Cada loop tem:

1. cut-off;
2. pre-read;
3. responsável de dados;
4. decision list;
5. timebox;
6. log;
7. follow-through;
8. accuracy/quality review.

Reunião sem decisão, responsável ou evidência é consumo de coordenação.

#### Exemplo resolvido 2 — previsão que dependia do líder

`CENÁRIO SINTÉTICO`.

Antes:

- AEs mandam opiniões por chat;
- Country Lead edita planilha domingo;
- HQ recebe commit sem definições;
- miss vira surpresa.

Mecanismo:

- segunda D-2: CRM cut-off automático;
- terça D-1: cada gestor certifica stage, amount, close date, next step e risk;
- quarta: Finance valida changes e exceptions;
- quinta: Previsão Council decide commit/upside/downside;
- sexta: vintage bloqueado e enviado;
- mês seguinte: score por erro e bias, não por otimismo.

Escalation:

- deal >15% do quarter commit;
- close date movido duas vezes;
- non-standard liability;
- coverage abaixo do limite definido;
- bias do gestor acima do limite por três vintages.

O líder não recompila dados. Ele desafia premissas e decide intervenção.

### L5 — Controles e melhoria

O Green Book 2025 organiza internal control em control environment, risk assessment, control activities, information and communication e monitoring; seu escopo é federal, mas a lente é útil para testar se um mecanismo produz operações, reporting e compliance confiáveis. `[SRC-CONTROL-GAO-2025]`

Para cada risco material:

- objetivo;
- risco;
- preventive control;
- detective control;
- responsável;
- frequency;
- evidence;
- exception path;
- monitoring.

**Controle sem evidência não é controle.** “Finance revisa” é vago. “Controller aprova o checklist fechado, com timestamp e exceptions, antes do previsão lock” é testável.

Evite process debt:

- não crie policy para erro isolado de baixo impacto;
- retire controles que não detectam nada útil;
- automatize captura, não judgment crítico;
- examine manipulação de métricas;
- revise o mecanismo após incidentes e mudanças de estágio.

## 7. Práticas guiadas

### GP1 — Value stream e decision inventory

Escolha “community lead → enterprise opportunity → AE handoff”. Mapeie:

- gatilho e qualification;
- responsáveis;
- dados mínimos;
- autoridade;
- SLA;
- feedback ao originador;
- attribution;
- confidentiality;
- exceptions.

Redesenhe para funcionar por quatro semanas sem o originador.

### GP2 — Mechanism review

Escolha um mecanismo real. Rode:

1. walk-through com novo operador;
2. exception injection;
3. missing-data test;
4. responsável absence;
5. authority conflict;
6. postmortem.

Registre falhas e ajuste uma vez. Simulação aumenta K/J, não P.

## 8. Caso real e cenário sintético

O caso real usa o operating rhythm público da GitLab. O cenário “Orbe Brasil” em `cases.md` é sintético.

## 9. Erros e sinais de alerta

- RACI com múltiplos `A`;
- DRI sem authority ou budget;
- “cross-functional” como ausência de responsável;
- cadence baseada em calendário, não em decisão;
- HQ consultada em tudo;
- local otimiza velocidade quebrando security/finance;
- playbook sem exception path;
- controle manual sem evidência;
- automação de dado ruim;
- founder continua sendo fallback universal.

## 10. Checklist de decisão

- [ ] Resultado e customer definidos.
- [ ] Decision inventory completo.
- [ ] Um responsável integrador por decisão.
- [ ] Authority e boundary reais.
- [ ] Contributors não viraram veto invisível.
- [ ] SLA e evidence definidos.
- [ ] Escalation por limite.
- [ ] Cadence compatível com o sinal.
- [ ] Control responsável diferente quando independência é necessária.
- [ ] Mecanismo testado sem o designer.
- [ ] Review/retirement date definida.

## 11. Exercício Brasil

Desenhe o operating model do primeiro ano:

- product/pricing localization;
- enterprise qualification e deal desk;
- partner onboarding;
- customer incident;
- previsão;
- hiring;
- regulatory issue;
- HQ resource ask.

Entregue decision rights, interface contracts, cadence e mechanism register.

## 12. Avaliação e rubrica

Veja `workbook.md`. Pesos: K 35, J 65. Mínimo 80, sem:

- decisão crítica órfã;
- control sem evidence;
- conflito de autoridade não resolvido;
- bypass de global security/legal/finance.

## 13. Artefato para o capstone

- one-page operating model;
- decision rights matrix;
- interface contracts;
- cadence;
- mechanism register;
- escalation limites.

## 14. Leituras

Essenciais, 75 min:

- GitLab DRI — 20 min.
- GitLab Operating Rhythm — 20 min.
- GOV.UK governance principles — 15 min.
- GAO Green Book overview — 20 min.

Opcional, 15 min:

- Amazon 2015 Shareholder Letter, trecho Tipo 1/Tipo 2.

## 15. Fontes e limitações

Veja `sources.md`. Práticas públicas de GitLab e Amazon são casos, não benchmarks universais. O desenho deve respeitar estágio, regulação, cultura, capacidade e delegação real.
