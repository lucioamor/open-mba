# Caderno de exercícios — M1

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## Instruções

Faça sem IA. Use calculadora e planilha. Declare moeda, unidade, período e arredondamento. Não consulte `answer-key.md` antes da entrega.

## A1 — Fechamento das três demonstrações

`CENÁRIO SINTÉTICO`, R$ mil.

Balanço inicial: cash 500; AR 100; equipment net 200; AP 80; debt 120; equity 600.

Eventos do mês:

1. revenue de 300, sendo 180 faturado e recebido e 120 faturado a prazo;
2. COGS de 90, dos quais 60 pagos e 30 em AP;
3. opex de 110, sendo 20 de D&A e 90 pagos;
4. capex à vista de 50;
5. collection de 70 do AR inicial;
6. principal de debt pago: 20; interest pago e reconhecido: 5;
7. ignore impostos.

Entregue income statement, cash flow indireto, ending balance sheet e checks.

## A2 — Previsão e decisão

Use `../../templates/pnl-forecast.xlsx`. O arquivo contém todos os inputs sintéticos, fórmulas e doze meses de actuals necessários; não substitua valores.

1. Recalcule Base, Upside e Downside.
2. Para cada cenário, reporte revenue, gross margin, operating income e ending cash de M24.
3. Na aba Variance, explique M1–M12 por volume/mix, timing, COGS e OPEX; o bridge deve somar.
4. Calcule previsão error absoluto e bias de revenue em Q1–Q4.
5. Recomende `scale/hold/repair/kill` em no máximo 250 palavras, com alternativa rejeitada e gatilho.

Os três ciclos de `cases.md` são práticas guiadas. Não fazem parte da A2 porque exigem decisões adicionais de modelagem; qualquer uso avaliativo requer um dataset versionado próprio.

## A3 — Perguntas de julgamento

1. Revenue bateu o budget, mas AR vencido dobrou e deferred revenue caiu. Quais cinco diagnósticos você testa primeiro?
2. CFO positivo por atraso de pagamento a fornecedores é sinal de melhora? Defenda.
3. HQ oferece financiamento, mas exige quota 40% maior. Que informações tornam a decisão aceitável ou recusável?
4. Qual diferença entre cortar headcount aberto, aprovado e iniciado?
5. Quando FX deve ser escalado para treasury em vez de absorvido no P&L local?

## Entregáveis

- arquivo de modelo;
- checks;
- bridge;
- QBR;
- decision log;
- disclosure de qualquer assistência depois da avaliação.
