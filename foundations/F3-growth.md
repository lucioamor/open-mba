# F3 — Distribuição, aquisição e retenção

**Competência:** FND-03. **Pré-requisitos:** F1 e F2. **Entrega:** funil definido e experimento de canal. Oficina introdutória, cerca de 6 horas com prática.

## Decisão

Qual gargalo do percurso do cliente merece o próximo experimento?

## Lição

Defina etapas por eventos observáveis: visita elegível, cadastro, primeira entrega de valor, retorno e pagamento. “Ativo” precisa de evento e janela. Não confunda pessoas, sessões, contas e empresas no mesmo denominador.

Um funil descreve transições. Uma coorte acompanha um grupo com o mesmo evento de entrada durante o tempo. Crescimento de novos usuários pode esconder queda de retenção. Canais diferentes podem trazer pessoas com intenção e custo distintos; compare qualidade além de volume.

Para priorizar, estime alcance × melhoria plausível × valor, custo e confiança. A estimativa serve para escolher o teste, não para prometer resultado. Inclua um limite de perda e uma métrica que proteja contra efeitos indesejados.

## Exemplo resolvido — cenário sintético

De 1.000 contas novas, 300 completam a primeira tarefa e 120 dessas retornam na semana seguinte. Ativação: 30% das novas contas. Retorno entre ativadas: 40%. Retorno entre todas as novas: 12%. São três métricas com denominadores diferentes; nenhuma deve receber apenas o nome “retenção” sem definição.

## Faça antes de ler a resposta

Dados sintéticos de duas coortes observadas pela mesma janela, sem sobreposição ou atribuição multicanal neste exercício:

| Canal | Custo | Novas contas | Primeira tarefa | Retorno na semana seguinte | Pagantes |
|---|---:|---:|---:|---:|---:|
| A | R$2.000 | 400 | 80 | 20 | 10 |
| B | R$3.000 | 200 | 100 | 60 | 20 |

1. Calcule custo por conta, por ativada e por pagante.
2. Calcule ativação e retorno entre ativadas.
3. Escolha o próximo teste com orçamento adicional de R$1.000.
4. Identifique duas informações ausentes que podem mudar a decisão.

## Resposta e rubrica — após a tentativa

A: R$5/conta, R$25/ativada, R$200/pagante; ativação 20%; retorno entre ativadas 25%. B: R$15/conta, R$30/ativada, R$150/pagante; ativação 50%; retorno entre ativadas 60%. Os custos representam somente o gasto fornecido, não CAC fully-loaded.

B parece melhor por pagante e retorno, mas faltam margem, ticket, prazo de conversão, capacidade e estabilidade ao escalar. É defensável testar mais B com perda limitada ou melhorar a ativação de A, desde que formule uma hipótese e compare com uma alternativa. Não multiplique a eficiência observada por dez como se fosse constante.

K (100): custos 40, taxas/denominadores 40, escopo dos custos 20. J (100): escolha e comparação 25, hipótese 25, limites econômicos 25, regra de continuidade e proteção 25. Erro crítico: selecionar A somente por cadastro barato ou chamar gasto de mídia de CAC total sem ressalva.

Segundo caso independente: B tem custo de atendimento de R$250 por pagante e A de R$20, com mesma receita por pagante de R$300. Reavalie contribuição antes de continuar. Separe aquisição de atendimento.

## Aplicação

Escreva um cartão: segmento, canal, evento de valor, janela, custo máximo, métrica principal, proteção, resultado que refuta a aposta e data de revisão. Continue em [M2](../modules/M2-unit-economics-pricing-capital/module.md) para coortes e economia mais completa. Todos os dados desta oficina são fictícios.
