# Currículo e dependências

Este é o currículo **disponível na primeira edição, aplicado a tecnologia e IA**. O OpenMBA tem como direção uma base geral de gestão, seguida de diagnóstico e percursos individuais. Consulte o [desenho curricular](docs/CURRICULUM-DESIGN.md) para distinguir cobertura existente, parcial e a desenvolver.

As horas abaixo são estimativas iniciais de estudo e prática por módulo completo. Não são tempos medidos em uma turma. Provas, retestes, leituras adicionais e prática real variam e ficam fora da estimativa.

| ID | Tema | Entrega | Pré-requisitos | Horas indicativas |
|---|---|---|---|---:|
| F1 | [Negócio e matemática](foundations/F1-business.md) | Modelo econômico de uma página | — | 6 |
| F2 | [Cliente e validação](foundations/F2-customer.md) | Hipótese e plano de entrevistas | F1 | 6 |
| F3 | [Distribuição e growth](foundations/F3-growth.md) | Funil e experimento de canal | F1, F2 | 6 |
| F4 | [Produto, dados e experimentação](foundations/F4-product.md) | Métrica, evento e teste | F1, F2 | 6 |
| M1 | [Finanças e P&L](modules/M1-financial-fluency-pnl/module.md) | Demonstrações e forecast | F1 | 30 |
| M2 | [Unit economics, pricing e capital](modules/M2-unit-economics-pricing-capital/module.md) | Coortes, custo e investimento | M1 | 22 |
| M3 | [Estratégia e incerteza](modules/M3-strategy-decision/module.md) | Memo de escolhas | F2, M2 | 16 |
| M4 | [Modelo operacional](modules/M4-operating-model/module.md) | Processo, direitos e cadência | M1 | 20 |
| M5 | [Organização e pessoas](modules/M5-org-managers/module.md) | Plano de organização | M4 | 22 |
| M6 | [Expansão e P&L de país](modules/M6-country-pnl-market-entry-hq/module.md) | Tese de entrada e contrato HQ/local | M2, M3, M4, M5 | 22 |
| M7 | [Governança e risco no Brasil](modules/M7-governance-risk-brazil-legal/module.md) | Registro de riscos e escalonamento | M1, M4 | 22 |
| M8 | [Comunicação executiva](modules/M8-executive-communication/module.md) | Memo e defesa | F1 | 14 |

M8 pode começar cedo para treinar síntese. Exercícios que exigem finanças, pessoas, país ou risco só devem ser feitos depois desses conteúdos; um memo curto inicial não dispensa a avaliação integrada.

Em cada pasta avançada:

- `module.md`: aulas e exemplos.
- `cases.md`: casos a analisar.
- `workbook.md`: exercícios a entregar.
- `answer-key.md`: resposta de referência, após a tentativa.
- `sources.md` e `source-packet.md`: referências herdadas e seus limites.

Os fundamentos são quatro oficinas introdutórias, não cursos extensos nas respectivas áreas. As competências estão em [curriculum/competencies.json](curriculum/competencies.json). O roteador inclui pré-requisitos mesmo que não apareçam na seleção principal da trilha.

## Depois da trilha

O [capstone](capstone/brief.md) usa os módulos selecionados. Quem quiser cobrir todos os módulos escolhe `explorer`. Isso ainda não cobre operações industriais, supply chain, contabilidade avançada, macroeconomia ou todos os setores; veja [ROADMAP.md](ROADMAP.md).
