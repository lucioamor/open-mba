# F4 — Produto, dados e experimentação

**Competência:** FND-04. **Pré-requisitos:** F1 e F2. **Entrega:** plano de decisão, instrumentação e teste. Oficina introdutória, cerca de 6 horas com prática.

## Decisão

O que construir ou mudar, e como saber se ajudou?

## Lição

Comece por problema, usuário e resultado esperado. Uma funcionalidade é uma intervenção proposta, não o resultado. Instrumentação registra eventos com unidade, momento, versão e propriedades mínimas. Defina o denominador e o que exclui duplicatas, equipe interna ou tráfego automatizado.

Antes de testar, escreva hipótese, intervenção, unidade de alocação, resultado principal, janela, guardrails e regra de decisão. Um antes/depois pode refletir sazonalidade, seleção ou outras mudanças. Randomização ajuda a comparar grupos, mas não corrige uma métrica mal medida nem dispensa incerteza.

Efeito absoluto e relativo são diferentes: passar de 20% para 24% representa 4 pontos percentuais e aumento relativo de 20%. Uma taxa melhor pode ter custo, erro ou efeito adverso maior. Não declare significância sem análise adequada ao desenho e aos dados.

## Exemplo resolvido — cenário sintético

Hipótese: um exemplo preenchido ajuda novas contas a completar a primeira tarefa. A métrica é a fração de contas elegíveis que conclui uma tarefa válida em 7 dias. Uma proteção é não aumentar erros ou solicitações de suporte. O evento registra conta, versão do fluxo e timestamp, sem incluir o conteúdo confidencial da tarefa.

## Faça antes de ler a resposta

Em um teste fictício randomizado por conta, A teve 200 conclusões entre 1.000 contas e B teve 240 entre 1.000. No mesmo período, A gerou 10 chamados e B 45. Não há informação sobre gravidade, custo de suporte ou análise de incerteza. Uma diretora pede liberar B para todos amanhã.

1. Calcule diferença absoluta e relativa de conclusão.
2. Calcule chamados por conta e sua diferença.
3. Recomende liberar, manter limitado ou interromper, explicitando dados ausentes.
4. Desenhe a regra do próximo teste antes de ver novos resultados.

## Resposta e rubrica — após a tentativa

Conclusão: 20% versus 24%; +4 p.p., +20% relativo. Chamados: 1% versus 4,5%; +3,5 p.p. Há 40 conclusões e 35 chamados adicionais nos grupos de mesmo tamanho, mas isso não mostra se as mesmas contas abriram chamados, nem a gravidade ou o valor econômico de cada evento.

É defensável manter B limitado enquanto se investiga suporte e incerteza do efeito, com responsável, prazo e limite de perda. Uma liberação também exigiria justificar tolerância de risco com dados; a taxa de conclusão sozinha não a justifica. O desenho de um teste real deve tratar tamanho de amostra, duração, múltiplas consultas e dependência entre observações. Esta oficina não substitui um curso de inferência estatística.

K (100): efeito absoluto/relativo 40, suporte e denominador 30, distinção observação/inferência 30. J (100): decisão 25, benefício/custo 25, dados e limites 25, regra/revisão 25. Erro crítico: afirmar causalidade de um simples antes/depois ou declarar significância apenas porque 240 é maior que 200.

Segundo caso independente: descubra que contas da mesma empresa foram distribuídas entre A e B e compartilhavam o fluxo. Discuta interferência e redesenhe a unidade de alocação antes de interpretar os totais.

## Aplicação

Escreva um PRD curto com problema, hipótese, escopo, exclusões, eventos, qualidade de dados, acessibilidade, privacidade, responsável e critério de revisão. Continue em [M3](../modules/M3-strategy-decision/module.md) para escolhas sob incerteza e [M4](../modules/M4-operating-model/module.md) para operação. Métodos e dados são simplificações didáticas autorais.
