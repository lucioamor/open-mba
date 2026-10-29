# Casos — M4

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## Caso real — GitLab Enterprise AI Operating Rhythm

Leia `SRC-OPS-GITLAB-RHYTHM`.

### Análise

1. Quais decisions pertencem à função, ao ATO, ao Hub e ao exec sponsor?
2. Por que bug/security feedback tem routing diferente de use-case request?
3. Onde existe risco de bottleneck?
4. Que SLAs ou limites você precisaria para operar o modelo?
5. Que elementos são específicos da GitLab e não devem ser copiados?
6. Desenhe um teste para saber se a interface realmente funciona.

## CENÁRIO SINTÉTICO — Orbe Brasil

Orbe vende uma plataforma AI B2B global. No Brasil:

- 1 Country Lead;
- 2 AEs;
- 1 Solutions Engineer;
- 1 Partner Manager;
- CS, Product, Security, Legal e Finance ficam fora do país;
- 12 oportunidades enterprise;
- 4 parceiros ativos;
- 3 pedidos de localização;
- 1 incidente de exposição de dado ainda não classificado.

### Sintomas

- toda oportunidade entra por canal diferente;
- Country Lead aprova qualquer desconto;
- parceiro promete roadmap;
- AE pede Security review quando o cliente já marcou go-live;
- HQ diz que Brasil “escala exceptions”;
- time local diz que HQ “não entende o Brasil”;
- não há previsão vintage nem decision log.

### Tarefa

Em 120 minutos:

1. defina seis resultados;
2. inventarie 12 decisões;
3. atribua responsável, decider, contributors, boundary e escalation;
4. desenhe quatro interface contracts HQ↔Brasil;
5. construa cadence semanal/mensal/trimestral;
6. trate o incidente sem improvisar parecer;
7. retire o Country Lead de pelo menos cinco passos;
8. escreva três mecanismos e respectivos controls/evidence.
