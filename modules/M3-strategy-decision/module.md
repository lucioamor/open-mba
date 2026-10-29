# M3 — Estratégia como escolha e decisão sob incerteza

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## 1. Decisão executiva central

Escolher onde jogar, como vencer, o que não financiar e quais sinais obrigam revisão, redução ou encerramento.

## 2. Como escolher a profundidade

Este módulo não presume experiência, senioridade ou lacunas do aluno. Use o diagnóstico por competência e o objetivo escolhido para decidir o que estudar. Sem avaliação, a recomendação é provisória: estudar ou fazer a prova de entrada. Cargo, tempo de carreira e autoavaliação não dispensam conteúdo. As regras da edição pública em `diagnostic/README.md` prevalecem sobre referências legadas a placement, test-out ou M0.

## 3. Pré-requisitos e test-out

Pré-requisito: separar fato, hipótese e premissa. Test-out exige 80/100 em M3-A1, nenhum erro fatal e uma defesa oral de dez minutos. Resultado altera apenas K/J; P permanece pendente de decisão real atestada.

## 4. Learning outcomes

- M3-O1/C09: produzir strategy kernel com diagnóstico causal, política-guia e ações coerentes.
- M3-O2/C10: comparar opções por expected value, reversibilidade, valor da informação e custo de atraso.
- M3-O3/C11: definir kill criteria observáveis, owner, data de revisão e regra de realocação.

Cobertura: `competency_id → lesson → guided practice → assessment`: C09→L1/L2→GP1→M3-A1; C10→L3/L4→GP2→M3-A1; C11→L5/L6→GP2→M3-A1.

## 5. Mapa de conceitos

`evidência → diagnóstico → escolhas/renúncias → opções → compromisso → sinais antecedentes → atualização → scale/hold/kill → postmortem`.

## 6. Lições

### L1 — Estratégia não é ambição

Um kernel útil tem diagnóstico do obstáculo, uma política-guia que concentra esforço e ações coerentes. Meta, slogan ou lista de iniciativas não substituem escolha. Aplicação: escrever o obstáculo Brasil em uma frase causal, não como “falta de awareness”. [SRC-M3-RUMELT]

### L2 — Escolha implica renúncia

Cada “onde jogar” consome capacidade e exclui outra aposta. Registre cinco escolhas e cinco renúncias com consequência econômica. Se tudo é prioridade, o portfolio não existe. [SRC-M3-RUMELT]

### L3 — Reversibilidade muda o processo

Decisões “two-way door” pedem velocidade e limite de perda; “one-way door” pedem evidência, revisão e autoridade maiores. Não confunda tamanho financeiro com irreversibilidade. [SRC-M3-AMAZON]

### L4 — Informação tem preço e prazo

Calcule expected value por cenário. Compre informação apenas se ela puder mudar a decisão antes do prazo. Base rate ancora; evidência específica atualiza. Probabilidade é posição revisável, não decoração matemática. [SRC-M3-GJOPEN][SRC-M3-MIT]

### L5 — Premortem e dissent

Antes do commitment, suponha que a tese falhou e liste causas observáveis. Designe red team, preserve dissenso e registre qual evidência faria mudar de opinião. [SRC-M3-KLEIN]

### L6 — Kill não é derrota

Kill criteria devem ter métrica, threshold, janela, owner, resposta e exceção autorizável. Sunk cost não entra no valor futuro. Encerrar libera capital para opção melhor. O postmortem avalia processo com informação disponível à época. [SRC-M3-GJOPEN]

## 7. Exemplos resolvidos

### Exemplo 1 — Duas wedges

**CENÁRIO SINTÉTICO.**

Opção A: 40% de chance de R$ 12 mi de valor, 60% de perda de R$ 2 mi. EV = `0,40×12 − 0,60×2 = R$ 3,6 mi`. Opção B: 70% de R$ 5 mi, 30% de perda de R$ 1 mi. EV = `R$ 3,2 mi`. A tem EV maior, mas exige compromisso irreversível. Um piloto de R$ 300 mil que discrimine demanda antes do contrato preserva option value; escolha: piloto A, não rollout A.

### Exemplo 2 — Kill criterion

**CENÁRIO SINTÉTICO.**

Hipótese: partner-led alcança 12 clientes em seis meses. Leading indicators: 30 oportunidades qualificadas até D90 e 20% de conversão até D150. Se oportunidades <18 em D90, congelar enablement; se conversão <12% em D150, encerrar e realocar dois FTE para direct. Owner: Country Lead; exceção: só CRO, com memo de evidência e nova data.

## 8. Casos

Caso real documentado: a carta da Amazon de 2016 descreve dois tipos de decisão e alerta para tratar decisões reversíveis como irreversíveis. Leia SRC-M3-AMAZON e identifique mecanismo, não imite a empresa.

Cenário sintético: `Aurora AI Brasil`, todos os números e pessoas são fictícios. A empresa deve escolher direct enterprise, partner-led ou espera de 12 meses. Dataset completo em `cases.md`.

## 9. Erros e alertas

- Diagnóstico é sintoma; ações não atacam a causa.
- Nenhuma alternativa rejeitada.
- Probabilidade sem base rate ou fonte.
- Métrica de vaidade no lugar de leading indicator.
- Kill criterion reescrito depois do resultado.
- “Piloto” com custo irreversível ou sem pergunta decisória.

## 10. Checklist

Problema causal? Alternativas comparáveis? Renúncias explícitas? Tipo de door? EV e downside? Evidência capaz de mudar a decisão? Premortem? Owner? Threshold e prazo? Regra de realocação? Trigger de revisão?

## 11. Exercício Brasil

Complete o caso Aurora. Entregue: kernel; cinco escolhas e cinco renúncias; árvore de opções; memo de uma página; register com três kill criteria; journal com prior, evidência, posterior e ação.

## 12. Avaliação e rubrica

M3-A1, 100 pontos. `K=35`: opções/números 20 e evidência/atualização 15. `J=65`: diagnóstico 15, escolhas/renúncias 15, kill/reallocation 20 e comunicação 15. Mínimo 80 e pelo menos 60% em cada dimensão. Fatal: fato inventado sobre empresa real; opção ausente; kill criterion não observável; cálculo que inverte a recomendação.

## 13. Artefato para o capstone

`Strategic choices memo` e `kill-criteria register`, versionados com `as_of_date`, alimentam os itens 2, 10 e 11 do capstone.

## 14. Leituras

Essenciais: SRC-M3-RUMELT (25 min, kernel); SRC-M3-AMAZON (15 min, reversibilidade); SRC-M3-KLEIN (15 min, premortem). Opcionais: SRC-M3-GJOPEN (60 min, forecasting); SRC-M3-MIT (90 min, options/capital budgeting).

Tempo: leitura 3h; exemplos e práticas guiadas 4h; caso independente 6h; avaliação/defesa/revisão 3h.

## 15. Fontes e limitações

Referências completas em `sources.md`. Os exemplos numéricos e Aurora são sintéticos. Expected value organiza premissas, não elimina ambiguidade. Nenhuma simulação certifica P ou field readiness.
