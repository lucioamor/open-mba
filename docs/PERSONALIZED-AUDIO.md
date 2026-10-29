# Seu currículo, seu contexto, suas aulas em áudio

A personalização do OpenMBA inclui as situações em que você aprende a aplicar o conteúdo. Além de escolher o percurso, você pode estudar finanças usando uma indústria que conhece, estratégia numa empresa que quer entender ou operações num projeto próprio. Os objetivos de aprendizagem continuam sendo os da lição; dados, exemplos e decisões mudam conforme o contexto.

Este guia reproduz um método usado no programa pessoal que deu origem ao OpenMBA: combinar documentos centrais de contexto com a lição de cada um dos oito módulos e instruções para uma aula em áudio. A experiência do autor motivou o guia; não constitui validação de eficácia para outros alunos.

## O que você vai montar

Um notebook seu por módulo, com três camadas: **lição + contexto de aprendizagem + fontes de aplicação**. O mesmo contexto central pode acompanhar M1–M8, com um foco diferente em cada sessão. Não é necessário escrever oito biografias nem criar oito comandos do zero.

Um notebook público pronto pode demonstrar o método com um caso sintético. Como leitor, você recebe as fontes escolhidas pelo autor; isso não cria um espaço individual para incluir suas próprias fontes. Para seguir este guia, crie seus próprios notebooks. O OpenMBA distribui os materiais e as instruções; este guia não provisiona notebooks nem inclui áudios gerados.

## 1. Prepare seu contexto uma vez

Baixe o repositório pelo menu **Code → Download ZIP** do GitHub ou clone-o. Copie o [modelo de contexto](../templates/learning-context.md), preencha e guarde a sua versão em `learner/contexto.md` ou fora do repositório. `learner/` é ignorado pelo Git; isso não controla o compartilhamento em serviços externos.

Escolha uma decisão de aprendizagem, um setor e uma organização real ou fictícia. Use apenas o contexto necessário. Você não precisa conhecer dados internos: demonstrações públicas, relatórios setoriais ou hipóteses explícitas podem bastar. Registre origem, período e limites dos dados. Não envie informações confidenciais ou de terceiros sem autorização.

## 2. Crie um notebook para o módulo

No NotebookLM, apresentado na documentação atual do Google como Gemini Notebook, crie um notebook e adicione:

1. O `module.md` do módulo escolhido na tabela abaixo.
2. Seu contexto preenchido.
3. Opcionalmente, `cases.md` e `source-packet.md` da mesma pasta, além de uma ou duas fontes públicas relevantes ao seu setor ou empresa.

Markdown (`.md`) é um formato aceito na versão para computador. Você também pode colar o texto como fonte. Confira se o conteúdo importado está completo. Um arquivo `sources.md` contém referências, não necessariamente o conteúdo integral dessas referências; importe os documentos necessários separadamente. O pacote de fontes do currículo também não equivale ao texto integral de todas as obras citadas.

| Módulo | Lição para enviar | Exemplo de decisão de aplicação |
|---|---|---|
| M1 — Finanças | [Lição M1](../modules/M1-financial-fluency-pnl/module.md) | Como receita, margem e caixa se relacionam neste negócio? |
| M2 — Economia unitária e capital | [Lição M2](../modules/M2-unit-economics-pricing-capital/module.md) | Que preço ou investimento faz sentido sob estas hipóteses? |
| M3 — Estratégia | [Lição M3](../modules/M3-strategy-decision/module.md) | Em que segmento competir e o que deixar de fazer? |
| M4 — Operações | [Lição M4](../modules/M4-operating-model/module.md) | Que processo limita a entrega e como redesenhá-lo? |
| M5 — Pessoas e organização | [Lição M5](../modules/M5-org-managers/module.md) | Como distribuir responsabilidades e desenvolver gestores? |
| M6 — Expansão e resultado local | [Lição M6](../modules/M6-country-pnl-market-entry-hq/module.md) | Como testar a entrada num mercado e negociar autonomia? |
| M7 — Governança e risco | [Lição M7](../modules/M7-governance-risk-brazil-legal/module.md) | Que risco exige controle ou validação especializada no Brasil? |
| M8 — Comunicação executiva | [Lição M8](../modules/M8-executive-communication/module.md) | Como defender uma recomendação e seus limites? |

Mantenha `answer-key.md`, rubricas e respostas de avaliações fora do notebook de aula. Use o `workbook.md` para a tentativa independente, em separado. Nos fundamentos F1–F4, lição e resposta estão no mesmo arquivo: copie apenas a parte anterior a **Resposta e rubrica** para o notebook.

## 3. Gere a aula

Selecione apenas as fontes desta sessão. Em **Estúdio → Resumo em Áudio**, escolha português brasileiro e use o [comando de aula contextualizada](../prompts/audio-lesson.md) no campo de personalização. Preencha módulo, nome do contexto e decisão. Use Deep Dive para compreensão ou Debate para comparar alternativas plausíveis.

Confirme que o áudio explica os conceitos e aplica seu contexto. Se ele apenas resumir documentos ou repetir seu nome, refine a decisão e os dados de aplicação e gere outra versão. O comando não garante que todas as instruções serão seguidas. Não há duração garantida; a documentação consultada limita o ajuste de duração ao inglês.

## 4. Transforme o áudio em prática

Depois de ouvir, escreva uma decisão em cinco linhas: escolha, mecanismo, alternativa rejeitada, risco e evidência que mudaria sua opinião. Confira nas fontes duas afirmações relevantes e qualquer conta que sustente a decisão. Resolva o exercício sem IA e faça uma defesa oral. Registre dúvidas e revise o contexto para a sessão seguinte.

Ouvir é uma forma de estudar. A demonstração de aprendizagem vem de explicar, calcular, decidir e revisar; o áudio não gera nota, dispensa nem evidência de experiência profissional. Ao alterar fontes ou contexto, gere um novo áudio: saídas anteriores não são atualizadas automaticamente.

## Automação e limites atuais

Este fluxo é manual e não exige integração de software. A documentação oficial consultada em **29 de outubro de 2026** descreve APIs para gerenciar notebooks, fontes e áudio na edição **Enterprise**, com configuração e licenças próprias; o gerenciamento de notebooks está em prévia. Essa API não deve ser confundida com uma integração disponível para qualquer conta pessoal. O OpenMBA não depende dela e não inclui integração Enterprise ou automação do navegador.

## Documentação da ferramenta

As telas e condições do serviço podem mudar. Fontes oficiais consultadas em 29 de outubro de 2026:

- [Criar um notebook e compartilhar acesso](https://support.google.com/gemininotebook/answer/16206563?hl=pt-BR).
- [Importar fontes e formatos aceitos](https://support.google.com/gemininotebook/answer/16215270?co=GENIE.Platform%3DDesktop&hl=en).
- [Criar e personalizar um Resumo em Áudio](https://support.google.com/gemininotebook/answer/16212820?hl=pt-BR).
- [APIs do Gemini Notebook Enterprise](https://docs.cloud.google.com/gemini/enterprise/notebooklm-enterprise/docs/api-notebooks).

Os materiais do OpenMBA podem ser usados com outras ferramentas que aceitem documentos e instruções. Recursos, limites e condições de cada serviço devem ser conferidos na ferramenta escolhida.
