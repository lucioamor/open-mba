# M7 — Answer key do avaliador

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

Não entregar junto com o enunciado. As respostas são modelos de qualidade, não parecer jurídico.

## 1. Práticas guiadas

### GP-M7-BOARD-MAP

Resposta esperada:

| Decisão | Recommend | Challenge | Approve | Execute | Assure |
|---|---|---|---|---|---|
| Miss de forecast / reforecast | Country lead + Finance | CFO + board/committee | Autoridade definida no budget policy | Country team | Finance/internal audit conforme desenho |
| Feature de IA | Product owner | AI risk + security + privacy | Product/risk authority conforme impacto | Product/Engineering | Test owner independente da entrega |
| Incidente | Incident commander | DPO + counsel + forensics | Comunicação por autoridade competente | Security/Privacy/Comms | After-action review e control testing |
| Entidade Brasil | Country lead + Finance | Corporate/tax/labor/privacy advisors | Board/shareholder conforme reserved matters | Legal/Finance/Ops | Corporate records + audit/control owner |

Aceitar variações se decision rights, conflito, evidência e escalation estiverem explícitos.

### GP-M7-RISK-CONTROL

Converter labels:

- “LGPD” → fluxo sem mecanismo/role mapping pode gerar tratamento incompatível, afetando titular, operação e resposta.
- “AI” → avaliação insuficiente pode permitir erro material não detectado, afetando cliente e continuidade.
- “tax” → contrato/invoice podem divergir da operação e da transição, gerando retrabalho, exposição e margem incorreta.
- “people” → fatos de direção e integração podem divergir do rótulo contratual, exigindo reclassificação e remediação.

Cada risco precisa de owner, controle e evidência. “Política”, “treinamento” ou “contrato” sem teste não bastam.

### GP-M7-INCIDENT-TRIAGE

Resposta esperada:

1. abrir incident ID e nomear commander;
2. preservar logs e conter credenciais;
3. separar ocorrência confirmada de hipótese de exfiltração;
4. mapear dado, titular, sistema, vendor, país e alcance;
5. acionar DPO, counsel, forensics, communications e negócio;
6. registrar o clock e checar regra setorial;
7. documentar decisão de comunicação e próximos checkpoints;
8. manter customer message factual, aprovado e versionado.

Fatal: “esperar certeza total”, “não notificar para proteger renewal” ou conclusão categórica sem análise.

### GP-M7-STRUCTURE

Resposta forte recomenda diligence, não entidade pronta. Ela:

- descreve atividade e customer promise;
- compara cross-border, partner/EOR e subsidiária;
- explicita contrato, invoice, pessoas, dado, IP, tax/FX e licenças;
- define bridge provisório reversível;
- bloqueia compromisso que dependa de opinião ausente;
- formula perguntas para corporate, tax, labor e privacy counsel.

### GP-M7-INTERCOMPANY

Para cada fluxo:

- **management service:** funções, pessoas, benefício, allocation key, contrato, invoice, evidência;
- **software/IP:** owner do IP, direito concedido, usuários, território, conduta real, charge;
- **funding:** entidade, instrumento, moeda, uso, approval, registro/reporting, repayment e accounting.

O aluno não escolhe método de transfer pricing.

### GP-M7-ADVISOR-BRIEF

“Legal aprova a feature?” deve virar:

> Decisão: autorizar piloto interno de versão X em data Y. Fatos: propósito, usuários, dados, vendor, região, avaliação, oversight, fallback e contrato. Issues: papel LGPD, transferência, comunicação, setor, trabalho e IP. Perguntas numeradas. Ação provisória: sandbox sem dado real. Stop trigger: falha de isolamento ou ausência de log.

## 2. CASE-M7-SES-SC

### Timeline permitida

Usar somente a sequência publicada: incidente → resposta/comunicação considerada inadequada ou intempestiva → requisições da ANPD → achados → advertências e medidas corretivas. Não inventar datas intermediárias ou causa.

### Failure modes

1. owner de incidente e comunicação não efetivo;
2. processo de avaliação/registro insuficiente;
3. evidência de segurança e accountability incompleta;
4. RIPD não disponível quando requisitado;
5. regulatory response sem owner e evidence pack.

### Control map modelo

| Objetivo | Preventivo | Detectivo | Corretivo | Evidência |
|---|---|---|---|---|
| Resposta tempestiva | Playbook, papéis, contatos | Exercise e clock audit | Incident command | Logs, decision log |
| Comunicação adequada | Template e approval path | Counsel/DPO review | Comunicação complementar | Versões e approvals |
| Segurança | Baseline e vendor controls | Monitoring/test | Contenção/remediação | Test log e tickets |
| RIPD/evidência | Trigger e repository | Quarterly completeness review | Remediation owner | RIPD versionado |
| Resposta à autoridade | Regulatory intake owner | Due-date tracker | Escalation ao executive | Protocolos e submissions |

### Limite obrigatório

Não extrapolar sanção, quantia, culpabilidade ou resultado privado.

## 3. CASE-M7-ORBE-INCIDENT

### Recomendação executiva

**External launch: condicionado e temporariamente bloqueado.**

Razões:

- teste identificou referências a conta errada;
- não existe kill switch por tenant;
- vendor/region/subprocessor e DPA estão incompletos;
- incidente confirmado está ativo;
- duas renovações criam pressão, não evidência de controle.

Bridge permitida: sandbox interno sem dado real, com tenant isolation, permission test, logging, kill switch, evaluation e approval.

### Próximas 24 horas

1. incident commander e war room;
2. preservar logs antes da retenção de sete dias;
3. revogar/rotacionar acessos e conter;
4. DPO, privacy counsel, forensics e communications;
5. mapear dado, titulares, geografia, vendor e subprocessors;
6. abrir communication decision log;
7. checar prazo setorial;
8. preparar factual holding statement;
9. checkpoint executivo com known/unknown;
10. registrar stop/continue decisions.

### Decisões de estrutura

- iniciar facts pack para cross-border, partner/EOR e subsidiária;
- não assumir que Ltda é resposta;
- documentar autoridade do country lead;
- bloquear exclusividade do parceiro até channel, competition, data, brand e termination review;
- criar reserved-matters e delegation matrix.

### Pessoas

- bloquear cinco novas contratações no desenho existente;
- preparar people-facts sheet dos oito contractors;
- acionar labor counsel;
- preservar continuidade sem orientar mudança artificial de fatos;
- revisar EOR, IP, confidentiality e performance process.

### Funding

- bloquear envio sem entidade, instrumento, purpose, tax/FX/accounting review;
- rejeitar fragmentação para “simplificar”;
- preparar flow-of-funds e advisor brief;
- envolver instituição autorizada quando o fluxo estiver definido.

### Board versus management

**Board/committee:** risk outside appetite, external launch, entidade/funding material, incidente material, conflito, public communication e exceção de produto.

**Management:** contenção, coleta de fatos, advisor engagement, internal sandbox dentro de limite e remediação operacional.

### Risk register modelo

**CENÁRIO SINTÉTICO.**

| ID | Risco | P | I | EI | Decisão |
|---|---|---:|---:|---:|---|
| R1 | Cross-tenant exposure | 4 | 5 | 20 | Bloquear external launch |
| R2 | Perda de logs antes da apuração | 4 | 5 | 20 | Preservar imediatamente |
| R3 | Comunicação inadequada | 3 | 5 | 15 | Clock + DPO/counsel |
| R4 | Transferência/vendor não mapeados | 4 | 4 | 16 | Data/vendor map + DPA |
| R5 | Contractor facts não revisados | 4 | 4 | 16 | Freeze + labor review |
| R6 | Funding sem estrutura | 3 | 5 | 15 | Freeze + flow-of-funds |
| R7 | Autoridade de assinatura ambígua | 3 | 4 | 12 | Delegation matrix |
| R8 | Miss gera override de controle | 4 | 4 | 16 | Board condition + dissent log |

Scores são priorização interna do cenário, não benchmark.

### Advisor questions mínimas

**Privacy**

1. Quais papéis LGPD resultam do fluxo real?
2. Que mecanismo de transferência se aplica?
3. O incidente atende aos critérios de comunicação?
4. Que informação pode ser comunicada em etapas?
5. Que prazo setorial precisa ser considerado?

**Corporate/contracts**

1. Qual bridge é executável antes da entidade?
2. Que poderes pode receber o country lead?
3. Que reserved matters sobem?
4. Como tratar exclusividade, reseller, IP, liability e termination?

**Labor**

1. Que fatos são materialmente relevantes nos oito contratos?
2. Que remediação evita agravar risco sem simular independência?
3. Que desenho EOR/local é apropriado?

**Tax/FX**

1. Qual entidade e instrumento suportam funding?
2. Que fatos definem serviço, IP, funding e charge?
3. Que documentação, registro e finalidade são exigidos?
4. Como a transição 2026 afeta produto, contrato e invoice?

**AI/product**

1. Que test suite prova tenant isolation?
2. Qual erro é bloqueante?
3. Quem revisa/override?
4. Qual fallback e kill switch?
5. Quando revalidar após mudança de modelo/vendor?

### Roadmap modelo

| Horizon | Entrega | Exit criterion |
|---|---|---|
| 30 | Incidente fechado/monitorado; logs preservados; data/vendor map; hiring/funding gates | Owners e evidência completos |
| 60 | Structure decision; delegation; DPA/transfer; contractor remediation; tax/FX design | Advisor memos e decisões registradas |
| 90 | Control testing; entity/bridge implementation; AI re-evaluation; board review | Residual accepted by authority |

## 4. Avaliação ASSESS-M7-BOARD-INCIDENT

### Distribuição K/J

| Dimensão | Evidência | Pontos |
|---|---|---:|
| K | Fonte, status normativo, LGPD/RCIS, transferência, tax/FX, AI regulation | 45 |
| J | Decisão, trade-offs, board, risk/control, action, advisor brief, challenge | 55 |
| **Total** | | **100** |

### Rubrica

| Critério | Dimensão | Pontos |
|---|---|---:|
| Distingue lei, regulation, projeto e framework | K | 10 |
| LGPD, fluxo, transferência e incident criteria/clock | K | 15 |
| Estrutura/trabalho/tax/FX/intercompany issues | K | 15 |
| Fontes, locators, as-of e limitações | K | 5 |
| Recomendação, opções, trade-offs e condições | J | 15 |
| Board/accountability, conflito e decision rights | J | 10 |
| Risk register, controles, evidence e triggers | J | 15 |
| Advisor brief, owners e roadmap | J | 10 |
| Defesa sob challenge | J | 5 |
| **Total** | | **100** |

### Mastery

- aprovação: **80/100**;
- mínimo K: **36/45**;
- mínimo J: **44/55**;
- zero fatal error;
- resultado certifica K/J; P permanece pendente.

### Fatal errors

1. projeto legislativo apresentado como lei;
2. conclusão jurídica/tributária categórica sem advisor;
3. incidente sem clock, owner ou preservação;
4. fato, número, sanção, fonte ou case inventado;
5. cenário sintético sem rótulo;
6. vendor/transferência sem fluxo e papéis;
7. conflito ocultado;
8. risco material sem controle/evidência/escalation;
9. framework tratado como safe harbor;
10. regra legal/regulatória sem T0, locator e as-of.

## 5. Feedback

Feedback deve apontar:

- claim ou decisão específica;
- evidência ausente;
- consequência executiva;
- correção;
- retest necessário.

Não aceitar prosa geral como remediação. Retest exige versão nova do artefato e defesa das mudanças.

### Retest Form B

Usar exclusivamente `ASSESS-M7-FORM-B — Vela Grid` em `cases.md`. O aluno cria artefato novo; não corrige a Form A.

O avaliador entrega o pacote T0 fechado e datado de 2026-07-23, após recheck de fontes `legal_current` e do status volátil do PL. Não entrega este answer key nem qualquer resposta da Form A.

Gates específicos do avaliador:

- conflito do diretor é divulgado e tratado com recusal/authority apropriada;
- acesso público confirmado inicia incident command mesmo com download incerto;
- perda parcial de log é registrada como deficiency, não ocultada;
- feature de recomendação recebe evaluation, human oversight, appeal/fallback e stop trigger;
- aquisição/JV, exclusividade e transferência de pessoas entram em diligence;
- royalty, management fee e funding recebem functional facts, tax/FX/accounting review;
- PL de IA permanece projeto, não fundamento jurídico vigente;
- mastery continua 80, K mínimo 36/45, J mínimo 44/55 e zero fatal error.

Qualquer fatal error novo na Form B reprova a tentativa. Pontos ou trechos corretos da Form A não compensam e não são transportados.
