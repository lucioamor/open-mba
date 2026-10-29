# M5 — Referências de apoio para ingestão controlada

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

Este arquivo prepara claims para a camada central. Não altera `sources/`.

## Escopo de ingestão

| source_id | tier | claim mínimo aceito | uso em M5 |
|---|---|---|---|
| SRC-ORG-GITLAB-SPAN | T1 | span guidance é contextual e não obrigatória | spans/layers por carga de trabalho |
| SRC-ORG-GITLAB-MANAGER | T1 | management é trabalho próprio e multidimensional | gestor e líder de gestores |
| SRC-ORG-OPM-ASSESS | T0 | job analysis liga trabalho, competências e seleção | quadro de indicadores |
| SRC-ORG-OPM-INTERVIEW | T0 | mesmas perguntas, ordem, escala e padrões | entrevista estruturada |
| SRC-ORG-OPM-PERFORMANCE | T0 | ciclo: plan, monitor, develop, rate, reward | performance system |
| SRC-ORG-FRC-GOVERNANCE | T0 | skill gaps, horizontes de sucessão e incentivos balanceados/override | sucessão e anti-gaming |

## Claims permitidos

1. Não existe no pacote fonte que sustente span universal; qualquer número em caso é dado sintético.
2. Uma camada só entra no desenho M5 quando absorve trabalho gerencial e interfaces que não cabem no nível existente.
3. Quadro de indicadores deve derivar de job analysis, resultados e competências job-related.
4. Candidatos recebem perguntas e critérios comparáveis definidos antes da avaliação.
5. Desempenho é um ciclo e não uma nota anual isolada.
6. Incentivo precisa combinar resultado e controles de qualidade/risco, com governança para override.
7. Sucessão inclui contingência, médio prazo e necessidade futura de skills; readiness exige gap e experiência, não preferência pessoal.

## Claims proibidos

- “o span ideal é X”;
- “estrutura plana é sempre melhor”;
- “entrevista estruturada elimina viés”;
- “este processo garante conformidade trabalhista no Brasil”;
- “alta performance financeira compensa violação ética ou de controle”;
- “simulação prova prontidão real para liderar gestores”.

## Volatilidade e rechecagem

- Rechecagem operacional: 30 dias antes de release.
- FRC: confirmar versão/updates log.
- OPM: confirmar avisos de revisão na página de assessment.
- GitLab: confirmar seção e `last modified`.
- Se locator desaparecer, congelar o claim até nova verificação T0/T1; não substituir automaticamente por snippet de busca.

## Alternativa aberta

Todos os instrumentos podem ser executados com Markdown, planilha e formulário local. Nenhum SaaS pago é requisito.
