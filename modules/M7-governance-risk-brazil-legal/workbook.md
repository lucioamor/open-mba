# WB-M7-GOV-RISK — Caderno de exercícios auditável

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

**Data de referência:** 2026-07-23\
**Formato:** Markdown tabular canônico. Não há `.xlsx`; as fórmulas abaixo devem ser preservadas se o caderno de exercícios for convertido.

## Instruções

1. Não preencha conclusão jurídica. Registre `issue`, fatos, hipótese, pergunta e advisor.
2. Use `source_id`, locator e data para toda regra externa.
3. Marque dados do caso fictício como `CENÁRIO SINTÉTICO`.
4. Um controle só existe se tiver responsável, frequência, evidência e teste.
5. Não apague linhas fechadas; mude o status e registre a data.

## Pacote para o conselho

| Campo | Conteúdo |
|---|---|
| Decision ID | |
| Meeting / date | |
| Decision requested | |
| Executive responsável | |
| Por que agora | |
| Facts verified | |
| Hypotheses | |
| Unknowns | |
| Opções | |
| Recomendação | |
| Trade-offs | |
| Risk outside appetite | |
| Conflicts / recusal | |
| Conditions precedent | |
| Stop gatilho | |
| Advisor opinions required | |
| Dissent | |
| Decision / responsável / due | |
| Next review | |

## Registro de riscos

### Escala interna

Esta é uma escala pedagógica interna, não benchmark externo.

- Probabilidade `P`: 1 rara; 2 improvável; 3 possível; 4 provável; 5 recorrente.
- Impacto `I`: 1 limitado; 2 baixo; 3 relevante; 4 severo; 5 crítico.
- Exposição inerente `EI = P × I`.
- Efetividade do conjunto de controles `EC`: 0 a 1, baseada em teste.
- Exposição residual `ER = EI × (1 − EC)`.

O score prioriza discussão; não substitui análise qualitativa, apetite ou advisor.

| Risk ID | Objetivo | Causa → evento → impacto | Responsável | P | I | EI | Tratamento | Controles | EC | ER | Indicador | Trigger | Status |
|---|---|---|---|---:|---:|---:|---|---|---:|---:|---|---|---|
| | | | | | | `P*I` | | | | `EI*(1-EC)` | | | |

### Exemplo preenchido

**CENÁRIO SINTÉTICO.**

| Risk ID | Objetivo | Causa → evento → impacto | Responsável | P | I | EI | Tratamento | Controles | EC | ER | Indicador | Trigger | Status |
|---|---|---|---|---:|---:|---:|---|---|---:|---:|---|---|---|
| R-AI-01 | Lançar assistente sem exposição cross-tenant | Permissão herdada → resposta exibe dado de outro cliente → confiança e continuidade afetadas | Product VP | 4 | 5 | 20 | Reduzir | Tenant isolation; permission test; logging; kill switch | 0,60 | 8 | Falhas no test suite | Qualquer leak cross-tenant | Condicionado |

**Cálculo:** `EI = 4 × 5 = 20`; `ER = 20 × (1 − 0,60) = 8`.

**Decisão:** piloto interno somente após evidência dos quatro controles. External launch bloqueado até nova aprovação.

## Mapa de controles

| Control ID | Risco | Objetivo do controle | Tipo | Atividade | Responsável | Frequência | Evidência | Tester | Resultado | Deficiência / ação |
|---|---|---|---|---|---|---|---|---|---|---|
| | | | Preventivo / detectivo / corretivo | | | | | | | |

### Teste de desenho

- O controle atua antes, durante ou depois do evento?
- O responsável tem autoridade e acesso?
- A evidência prova execução, não apenas intenção?
- O controle cobre população e frequência?
- Existe segregação adequada?
- A exceção é detectada e escalada?
- Há fallback se o controle falhar?

## Matriz de escalonamento

| Issue | Severidade | Responsável operacional | Advisor | Comitê/board | Clock | Ação provisória | Stop gatilho | Evidência |
|---|---|---|---|---|---|---|---|---|
| Incidente com dado pessoal | | Incident commander | DPO + privacy counsel + forensics | | Desde confirmação | Conter e preservar | | Incident log |
| Estrutura/entidade | | Country lead | Corporate + tax counsel | | Antes do compromisso | Condicionar | Assinatura/contratação sem estrutura | Opções memo |
| Trabalho/contractor | | People lead | Labor counsel | | Antes da contratação/mudança | Congelar desenho | Fatos incompatíveis | People-facts sheet |
| FX/intercompany | | Finance lead | Tax/FX counsel + instituição autorizada | | Antes do fluxo | Não executar | Divergência contrato/invoice/finalidade | Fluxo de recursos |
| IA de alto impacto interno | | Product responsável | AI risk + privacy + sector counsel | | Antes do rollout | Sandbox | Falha em avaliação/oversight | Model card/test log |

## Mapa de questões

| Issue ID | Domínio | Fatos confirmados | Hipótese | Regra/fonte | Implicação | Pergunta decidível | Advisor | Decisão requerida | Due | Status |
|---|---|---|---|---|---|---|---|---|---|---|
| | Corporate / contract / labor / tax / FX / LGPD / AI / sector | | | SRC-... + locator | | | | | | |

### Linguagem permitida

- “Precisamos confirmar se…”
- “Os fatos indicam exposição em…”
- “Até parecer do advisor, a ação provisória é…”
- “A decisão requerida é…”

### Linguagem proibida

- “É legal.”
- “Não há vínculo.”
- “A alíquota é definitivamente…”
- “O PL já exige…”
- “NIST compliance elimina responsabilidade.”

## Opções de estrutura

| Critério | Cross-border | Partner/reseller | EOR | Subsidiária/Ltda | Aquisição/JV |
|---|---|---|---|---|---|
| Customer contract | | | | | |
| Invoice / collection | | | | | |
| People | | | | | |
| Data / transfer | | | | | |
| IP / product control | | | | | |
| Tax / FX | | | | | |
| Licenses / sector | | | | | |
| Decision rights | | | | | |
| Intercompany | | | | | |
| Reversibility | | | | | |
| Perguntas ao especialista | | | | | |

## Mapa de dados e fornecedores

| Flow ID | Titular | Dado | Finalidade | Controlador | Operador | Sistema/vendor | País | Transferência posterior | Retenção | Direito/canal | Fonte/contrato | Gap |
|---|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | | |

## Registro de decisões sobre incidente

| Timestamp | Fato conhecido | Hipótese/lacuna | Ação | Responsável | Evidência preservada | Advisor question | Comunicação / decisão |
|---|---|---|---|---|---|---|---|
| | | | | | | | |

### Gates

- ocorrência confirmada?
- envolve dado pessoal sujeito à LGPD?
- pode acarretar risco ou dano relevante?
- existe prazo setorial?
- quais titulares/dados/países/vendors?
- comunicação em etapa é necessária?
- segredo comercial foi identificado sem ocultar fato material?
- próxima atualização tem responsável e hora?

## Ficha de portfólio de IA

| Campo | Resposta |
|---|---|
| Use-case ID / version | |
| Purpose / decision influenced | |
| Business responsável | |
| People affected | |
| Inputs / outputs | |
| Personal or sensitive data | |
| Model / vendor / region | |
| Evaluation set and limits | |
| Error and subgroup checks | |
| Human oversight / override | |
| Monitoring / drift | |
| Fallback | |
| Stop gatilho | |
| Legal/regulatory issues | |
| Approval / expiry | |

## Fluxo de recursos e intercompany

| Flow ID | From | To | Currency | Economic purpose | Contract | Invoice | Service/IP/financiamento facts | FX path | Tax question | Accounting evidence | Responsável |
|---|---|---|---|---|---|---|---|---|---|---|---|
| | | | | | | | | | | | |

## Briefing para especialista

### 1. Decisão requerida

### 2. Deadline e razão

### 3. Fatos confirmados

### 4. Hipóteses e lacunas

### 5. Estrutura e fluxos

### 6. Pessoas, dados, IA e vendors

### 7. Exposição e ação provisória

### 8. Perguntas numeradas

Cada pergunta deve poder receber: `sim`, `não`, `depende de X`, ou `faltam Y documentos`.

### 9. Documentos anexos

### 10. Decisão depois do advice

## Plano de conformidade 30/60/90

| Horizon | Deliverable | Responsável | Dependency | Evidence | Exit criterion | Risk if late |
|---|---|---|---|---|---|---|
| 30 | | | | | | |
| 60 | | | | | | |
| 90 | | | | | | |

## Verificação antes de entregar

- [ ] Fórmulas recalculadas.
- [ ] Todos os scores têm escala e responsável.
- [ ] Toda regra externa tem fonte e as-of date.
- [ ] Todo cenário fictício está rotulado.
- [ ] Não há conclusão jurídica.
- [ ] Advisors e stop gatilhos estão explícitos.
- [ ] Board ask cabe em uma frase.
- [ ] Dissent, conflito e condição estão registrados.
