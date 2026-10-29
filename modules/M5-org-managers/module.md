# M5 — Organização e gestores: escala sem heroísmo

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## 1. Decisão executiva central

> **Que estrutura, gestores, incentivos e sucessores permitem crescer de 5 para 20 e 50 pessoas sem concentrar decisões, premiar comportamento destrutivo ou criar camadas sem trabalho gerencial real?**

Organograma é output. O input é trabalho: resultados, decisões, interfaces, carga, risco e horizonte. M5 não otimiza caixas; cria um sistema em que alguém sabe o que entregar, gestores aumentam a capacidade de outros e a empresa continua funcionando quando uma pessoa sai.

## 2. Como escolher a profundidade

Este módulo não presume experiência, senioridade ou lacunas do aluno. Use o diagnóstico por competência e o objetivo escolhido para decidir o que estudar. Sem avaliação, a recomendação é provisória: estudar ou fazer a prova de entrada. Cargo, tempo de carreira e autoavaliação não dispensam conteúdo. As regras da edição pública em `diagnostic/README.md` prevalecem sobre referências legadas a placement, avaliação para dispensa ou M0.

## 3. Pré-requisitos e avaliação para dispensa

M5 consome:

- diagnóstico de M0;
- decision rights e cadence de M4;
- economics de headcount de M1/M2;
- registro de riscos de M7.

M5 não reensina RACI/DACI nem P&L. Ele aloca direitos já definidos a papéis e verifica se a estrutura consegue exercê-los.

Avaliação para dispensa por subcompetência exige `K ≥ 85`, `J ≥ 80`, zero erros críticos e dois casos independentes. ORG-02 e ORG-04 exigem ainda evidência futura em campo para P; simulação não basta.

## 4. Objetivos de aprendizagem mensuráveis

Ao final, você consegue:

1. diagnosticar overload e interfaces antes de desenhar caixas;
2. justificar cada role, span e layer por trabalho observável;
3. sequenciar estrutura para 0–5, 5–20 e 20–50;
4. construir quadro de indicadores de gestor a partir de job analysis;
5. conduzir entrevista e work sample estruturados;
6. operar plan–monitor–develop–rate–reward;
7. desenhar incentivo com quality/risk gates e override governado;
8. liderar gestores por sistema, não por bypass;
9. produzir sucessão com contingência, readiness e experiências;
10. separar K/J demonstrado de P ainda não observado.

## 5. Mapa de conceitos

```text
strategy + work + risk
        │
        ├── decisions/interfaces/load ──> roles ──> spans/layers
        │                                      │
        │                                      └── managers
        │                                            │
        ├── job analysis ──> scorecard ──> selection ┤
        │                                            │
        ├── expectations ──> evidence ──> consequence
        │                         │             │
        │                         └── incentive + anti-gaming
        │
        └── critical roles ──> successors ──> experiences ──> transition test
```

Regra: uma caixa sem outcome, decision right, interfaces e carga é decoração.

## 6. Lições

### L1 — Estrutura segue trabalho, não ego

GitLab explicita que sua guidance de span é orientação, não requisito, porque partes diferentes da organização pedem estruturas e reporting lines diferentes. `[SRC-ORG-GITLAB-SPAN]`

#### Quatro unidades distintas

| Unidade | Pergunta |
|---|---|
| Role | que resultados e decisões pertencem a este papel? |
| Span | quantos reports este gestor consegue apoiar com a intensidade requerida? |
| Layer | que trabalho gerencial adicional existe entre executor e decisor? |
| Interface | onde trabalho, informação ou decisão atravessa papéis? |

Não escolha span por moda. Calcule demanda gerencial semanal:

`carga = 1:1 + coaching/review + decisões/escalations + hiring + planejamento + coordenação + reserva`

Compare com horas realmente disponíveis após o gestor cumprir suas próprias obrigações. Complexidade, senioridade dos reports, volatilidade e dependências mudam a carga.

#### Sequência 0–5 / 5–20 / 20–50

| Faixa | Problema dominante | Estrutura mínima | Trigger de mudança |
|---|---|---|---|
| 0–5 | descoberta e sobrevivência | founder + responsáveis de resultados; poucos títulos | decisões recorrentes bloqueadas no founder ou função crítica sem responsável |
| 5–20 | especialização e handoffs | leads/gestores apenas onde há coaching, planning e coordenação persistentes | carga gerencial excede capacidade por 4 semanas ou qualidade/velocidade cai por interface |
| 20–50 | portfólio e gestão por gestores | funções claras, gestores de primeira linha e, só onde há sistema multi-time, líder de gestores | 2+ gestores requerem priorização comum, talent calibration e recursos compartilhados |

Essas faixas organizam o caso; não são lei natural. O gatilho é evidência, não headcount isolado.

#### Exemplo resolvido 1 — a camada que não deve existir

`CENÁRIO SINTÉTICO — Atlas AI Brasil, 18 pessoas.`

Revenue tem 6 AEs seniores, 1 RevOps, 1 Sales Manager. A proposta é criar Director of Sales entre o Country Lead e o Sales Manager.

Carga semanal do Sales Manager:

| trabalho | horas |
|---|---:|
| seis 1:1s | 3 |
| deal reviews | 4 |
| coaching/call review | 4 |
| previsão e planning | 4 |
| hiring | 2 |
| interfaces com Product/Finance | 3 |
| reserva/escalonamentos | 3 |
| total | 23 |

Há 32 horas gerenciais disponíveis. Nenhum segundo time ou gestor existe. O Country Lead gasta 2 horas/semana com Revenue.

**Decisão:** não criar Director. O problema é previsão quality, não span. Redesenhar commit criteria e preservar 9 horas de capacidade no Sales Manager. Trigger para reabrir: segundo gestor com time distinto + conflito persistente de prioridade/recursos + ≥8 horas/semana de trabalho legítimo de líder de gestores.

Uma layer sem trabalho desloca decisão, adiciona handoff e cria status; não adiciona capacidade.

### L2 — Quadro de indicadores antes de candidato

OPM orienta começar por job analysis atual: tarefas, responsabilidades, competências, recursos e contexto devem se ligar à seleção. Entrevista estruturada mede competências job-related com mesmas perguntas, ordem, escala e padrão. `[SRC-ORG-OPM-ASSESS] [SRC-ORG-OPM-INTERVIEW]`

#### Quadro de indicadores de gestor

1. **Mission:** por que o papel existe em 12 meses.
2. **Outcomes:** 4–6 resultados, métrica, baseline, target e prazo.
3. **Competencies:** comportamentos necessários para produzir resultados.
4. **Constraints:** budget, authority, compliance e interfaces.
5. **Evidence method:** pergunta, work sample, reference ou histórico.
6. **Anchors:** o que 1, 3 e 5 significam antes de ver pessoas.

Não use “culture fit” ou “executive presence” sem comportamento observável. Um critério elástico permite justificar o favorito depois.

#### Exemplo resolvido 2 — quadro de indicadores de Sales Manager

`CENÁRIO SINTÉTICO — Atlas AI Brasil, próxima fase 20–50.`

**Mission:** até D+180, transformar sete AEs em um sistema de receita previsível e compatível com guardrails.

| outcome | baseline | target | prazo |
|---|---:|---:|---|
| previsão accuracy | 58% | ≥80% | D+120 |
| ramp até produtividade | 150 dias | ≤110 dias | D+180 |
| deals sem security sign-off em commit | 3/trimestre | 0 | imediato |
| coaching baseado em call review | 20% dos AEs/mês | 100%/mês | D+60 |
| regrettable attrition | não medido | medir + plano | D+45 |

Competências: coaching com evidência, previsão judgment, performance conversations, cross-functional escalation e ética de revenue.

Work sample: com oito deals, capacidade e flags de security, produzir commit/base/downside e plano de coaching em 45 minutos.

Âncora para previsão judgment:

- `1`: inclui deal bloqueado em commit e não explicita premissas;
- `3`: classifica corretamente, mas não quantifica risco/capacidade;
- `5`: classifica, mostra vintage, downside, capacidade e escalonamentos sem ocultar risco.

Pergunta estruturada:

> Conte o caso mais recente em que você retirou um deal relevante do commit contra pressão comercial. Qual era a evidência, o que você decidiu e qual foi o resultado?

Todos recebem a mesma pergunta e probes. O painel pontua em silêncio antes de calibrar.

### L3 — Desempenho e incentivos são um sistema

OPM descreve ciclo contínuo de planning, monitoring, developing, rating e rewarding. Expectativas e medidas vêm antes do julgamento; feedback permite corrigir cedo. `[SRC-ORG-OPM-PERFORMANCE]`

#### Desempenho contract

Para cada papel:

- resultados e guardrails;
- evidência e fonte;
- cadence de check-in;
- support/development;
- limites e janela;
- consequência possível;
- dissent e change log.

Rating sem contrato anterior vira memória seletiva. Feedback sem decisão vira ritual.

#### Incentivo: fórmula + gates + julgamento governado

A FRC recomenda considerar medidas financeiras, não financeiras e estratégicas, testar comportamento negativo e permitir override de resultado formulaico. M5 adapta o mecanismo; não exporta as obrigações do Code. `[SRC-ORG-FRC-GOVERNANCE]`

Exemplo de bônus de Sales Manager:

`score = 40% ARR + 20% gross margin + 15% retention/collection + 15% forecast quality + 10% people system`

Gates:

- zero payout variável em receita associada a fraude ou venda proibida;
- cap de 50% se security/discount controls forem violados materialmente;
- clawback/ajuste somente se política e contrato locais válidos o permitirem;
- override exige responsável, evidência, conflito declarado e decisão registrada.

**Caso de manipulação de métricas:** AE entrega 140% da quota, mas concede descontos não autorizados e promete integração inexistente. Resultado financeiro não apaga o fatal behavior. Separar investigação/fatos, excluir receita inválida do cálculo, conter cliente, revisar controles e decidir consequência com RH/Jurídico competente. Não improvisar sanção.

### L4 — Manager-of-managers e sucessão

GitLab trata management como trabalho distinto do papel de IC e organiza atenção entre indivíduos, organização e work, no curto, médio e longo prazo. É framework primário da empresa, não prescrição universal. `[SRC-ORG-GITLAB-MANAGER]`

#### Manager vs líder de gestores

| Manager | Manager-of-managers |
|---|---|
| desenvolve ICs | desenvolve gestores |
| opera um sistema de equipe | calibra sistemas entre equipes |
| resolve escalonamentos do time | melhora limites e interfaces que geram escalonamentos |
| planeja capacidade local | aloca recursos entre portfólios |
| avalia desempenho individual | calibra qualidade do julgamento dos gestores |

Bypass constante destrói o papel intermediário. O líder pode inspecionar; não deve reassumir silenciosamente todas as decisões.

#### Succession system

A FRC separa contingência, médio prazo e skills futuros; também recomenda explicitar gaps, critérios e plano escrito. `[SRC-ORG-FRC-GOVERNANCE]`

Para cada papel crítico:

| campo | definição |
|---|---|
| criticality | impacto de vacância por 30/90 dias |
| interim | quem assume amanhã e quais limites |
| candidates | pessoas consideradas por critérios transparentes |
| readiness | now, <6m, 6–12m, >12m |
| gaps | evidência que falta |
| experiences | assignment que testa o gap |
| fallback | external search ou redistribuição |
| review | responsável, data e mudança desde a última rodada |

Readiness não é promessa. Candidate não é successor até existir evidência e decisão.

## 7. Práticas guiadas

### GP1 — workload-to-org

Receba backlog de decisões, interfaces e carga. Produza três estruturas possíveis, incluindo status quo. Para cada layer, declare:

- trabalho absorvido;
- custo e latency adicionados;
- alternativa sem headcount;
- gatilho de entrada e remoção.

### GP2 — structured gestor selection

Em trio:

1. faça job analysis;
2. escreva quadro de indicadores e âncoras;
3. conduza work sample idêntico com dois perfis;
4. pontue individualmente;
5. calibre divergência contra evidência, sem mudar critério.

### GP3 — performance, incentive e succession red team

Um grupo desenha o sistema; outro tenta:

- maximizar payout destruindo qualidade;
- esconder underperformance;
- escolher sucessor por afinidade;
- criar layer por título.

O grupo autor revisa gates, evidência e governance log.

## 8. Casos

`cases.md` contém:

- caso real documentado GitLab: management como trabalho próprio e span guidance contextual;
- caso sintético Atlas AI Brasil, com dados suficientes para 5→20→50, seleção, performance, incentivos e sucessão.

Empresas reais não recebem números inventados. Todo número operacional é sintético e rotulado.

## 9. Erros executivos e erros críticos

Erros comuns:

- organograma antes de workflow;
- benchmark de span usado como lei;
- layer para reter ou premiar alguém;
- founder continua como approval de tudo;
- melhor IC promovido sem quadro de indicadores de gestor;
- pergunta diferente para candidato favorito;
- rating anual sem evidência;
- incentivo de uma métrica;
- top performer acima de controles;
- líder de gestores que bypassa gestores;
- “sucessor” sem readiness ou experiência.

Erros críticos:

- ação de pessoas ilegal, discriminatória, retaliatória ou recomendada sem encaminhamento competente;
- usar atributo protegido, afinidade ou critério inventado depois como seleção/performance/sucessão;
- fabricar evidência sobre candidato ou colaborador;
- recompensar conscientemente fraude, assédio, discriminação ou violação material de controle;
- executar sanção/terminação sem fatos, processo e revisão local competente;
- ocultar conflito de interesse em seleção, rating, payout ou sucessão;
- afirmar P com base apenas em caso ou simulação.

## 10. Checklist de decisão

- [ ] Outcomes e decisões antecedem caixas.
- [ ] Cada role tem mission, interfaces e constraints.
- [ ] Cada layer absorve trabalho real.
- [ ] Span deriva de carga, senioridade e complexidade.
- [ ] Existe alternativa sem headcount.
- [ ] Trigger de entrada/remoção é mensurável.
- [ ] M4 decision rights estão alocados, não duplicados.
- [ ] Quadro de indicadores deriva de job analysis.
- [ ] Perguntas, ordem, escala e anchors foram congelados antes.
- [ ] Evidência foi pontuada antes de consenso.
- [ ] Desempenho cobre plan–monitor–develop–rate–reward.
- [ ] Incentivo equilibra resultado, qualidade, risco e people system.
- [ ] Gates tratam conduta/controle.
- [ ] Override tem responsável, evidência e log.
- [ ] Papel crítico tem interim e limites.
- [ ] Readiness tem gap e experiência.
- [ ] Conflitos e incertezas estão registrados.

## 11. Exercício aplicado à operação Brasil

Use o operating model de M4 e economics de M1/M2. Produza:

1. org plan para 5, 20 e 50 pessoas;
2. role charters e carga de trabalho model;
3. hiring quadro de indicadores de gestor;
4. interview/work-sample pack;
5. performance contract;
6. incentive plan com manipulação de métricas tests;
7. succession slate de quatro papéis críticos;
8. 90-day implementation plan com reversibility.

Dependências trabalhistas, remuneração, privacidade e sanções devem ser encaminhadas a RH/Jurídico local competente.

## 12. Avaliação e rubrica

Veja `workbook.md` e `answer-key.md`.

- `K`: 35%.
- `J`: 65%.
- aprovação: ≥80/100;
- zero erros críticos;
- entrega e defesa individuais;
- primeira tentativa sem IA;
- IA pode criticar depois da entrega com disclosure, sem alterar a nota original.

A1 mede org plan. A2 mede quadro de indicadores, performance, incentive e succession system. Nenhuma avaliação depende de ter feito GP1–GP3.

## 13. Artefatos para o capstone

- org plan 0–5/5–20/20–50;
- role/carga de trabalho map;
- gestor quadro de indicadores e evidence log;
- performance contract;
- incentive plan e manipulação de métricas tests;
- succession slate e transition drill;
- implementation/decision log.

## 14. Leituras

Essenciais — 240 min:

- GitLab, `Span of Control Guidance` — 25 min;
- GitLab, `Work Of A Manager` — 45 min;
- OPM, `Assessment and Selection` — 35 min;
- OPM, `Structured Interviews` — 35 min;
- OPM, `Performance Management Cycle` — 45 min;
- FRC, §3 paras 159–166 e §5 paras 319–329 — 55 min.

Leitura não substitui exercício. Cada claim usado deve apontar ao locator em `sources.md`.

## 15. Fontes, limites e transferência

Veja `sources.md` e `source-packet.md`.

M5 não é aconselhamento trabalhista, de remuneração ou discriminação. Instrumentos reais exigem revisão conforme jurisdição, contrato e política aplicável. Guidance pública é usada por mecanismo e com limites explícitos.

O módulo pode demonstrar K/J. P só sobe quando houver observação futura de pelo menos um ciclo real: seleção, performance, gestão de gestores ou sucessão, com artefato, resultado e reviewer independente.
