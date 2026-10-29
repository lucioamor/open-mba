> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../SOURCES.md).

# Avaliações avançadas — casos sintéticos

## Instrumento B — caso financeiro integrado de 24 meses

**Tempo:** 150 minutos.\
**Mede:** três demonstrações, accrual vs cash, P&L, previsão, working capital, FX e reação a choque.\
**Empresa:** `Aster AI Brasil Ltda.` — cenário sintético.

### Situação

A Aster vende assinatura anual e consumo de uma plataforma de IA. O HQ avalia continuar financiando a operação brasileira. Você recebeu o balanço de abertura e um previsão operacional de 24 meses. Deve construir as três demonstrações integradas, identificar a necessidade de caixa e recomendar ações.

### Balanço de abertura — fim de M0

| Conta | Valor |
|---|---:|
| Caixa | 8.000 |
| Contas a receber | 1.200 |
| Despesas antecipadas | 240 |
| Imobilizado bruto | 600 |
| Depreciação acumulada | (120) |
| **Total de ativos** | **9.920** |
| Fornecedores | 500 |
| Salários provisionados | 400 |
| Receita diferida | 900 |
| Tributos a pagar | 100 |
| Empréstimo intercompany | 1.500 |
| Capital social + lucros acumulados | 6.520 |
| **Passivo + patrimônio líquido** | **9.920** |

### Regras contábeis e de modelagem

1. Receita é a soma de assinatura reconhecida e consumo reconhecido da tabela.
2. Hosting é percentual da receita total.
3. O suporte, payroll, S&M, G&A e HQ charge são despesas operacionais.
4. HQ charge mensal = `US$ 35 mil × câmbio da tabela`.
5. Depreciação do imobilizado de abertura: R$ 16 mil/mês. Capex novo deprecia em 36 meses, linha reta, a partir do mês seguinte.
6. Imposto gerencial: 25% do EBT positivo mensal; prejuízo não gera ativo fiscal.
7. Despesas antecipadas são consumidas linearmente em 12 meses: R$ 20 mil/mês de M1 a M12, já incluídos em G&A. Portanto, reduza `prepaid` sem duplicar despesa.
8. Contas a receber, receita diferida, fornecedores, salários provisionados e tributos a pagar fecham nos saldos fornecidos.
9. Variações desses saldos entram no fluxo de caixa operacional pelo método indireto.
10. Capex é fluxo de investimento.
11. Aporte aumenta caixa e patrimônio; dívida sacada aumenta caixa e empréstimo; amortização reduz ambos.
12. Não há dividendos, goodwill, outros ativos, outros passivos ou juros.
13. Caixa fecha por roll-forward; não é plug arbitrário. O balanço deve reconciliar a cada mês.

### Dados mensais

| Mês | Assinatura | Consumo | Hosting % | Suporte | Payroll | S&M | G&A | FX | AR fim | Diferida fim | AP fim | Salários fim | Tributos fim | Capex | Aporte | Dívida +/- |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| M1 | 250 | 60 | 20% | 35 | 320 | 180 | 100 | 5,00 | 1.280 | 980 | 520 | 410 | 80 | 40 | 0 | 0 |
| M2 | 280 | 70 | 20% | 35 | 320 | 180 | 100 | 5,05 | 1.360 | 1.050 | 540 | 420 | 60 | 0 | 0 | 0 |
| M3 | 320 | 80 | 20% | 40 | 320 | 190 | 105 | 5,10 | 1.450 | 1.120 | 560 | 425 | 40 | 60 | 0 | 0 |
| M4 | 360 | 90 | 20% | 45 | 440 | 200 | 105 | 5,15 | 1.530 | 1.210 | 590 | 440 | 20 | 0 | 0 | 0 |
| M5 | 400 | 105 | 20% | 45 | 440 | 205 | 110 | 5,20 | 1.620 | 1.300 | 610 | 450 | 10 | 40 | 0 | 0 |
| M6 | 450 | 120 | 19% | 50 | 440 | 210 | 110 | 5,25 | 1.720 | 1.400 | 640 | 460 | 0 | 0 | 0 | 0 |
| M7 | 500 | 135 | 19% | 55 | 560 | 220 | 115 | 5,30 | 1.820 | 1.510 | 670 | 480 | 0 | 80 | 2.500 | 0 |
| M8 | 560 | 150 | 19% | 55 | 560 | 230 | 115 | 5,35 | 1.930 | 1.630 | 700 | 490 | 0 | 0 | 0 | 0 |
| M9 | 620 | 170 | 19% | 60 | 560 | 240 | 120 | 5,40 | 2.040 | 1.760 | 730 | 500 | 0 | 40 | 0 | 0 |
| M10 | 690 | 190 | 19% | 65 | 700 | 250 | 120 | 5,45 | 2.160 | 1.900 | 760 | 520 | 0 | 0 | 0 | 0 |
| M11 | 760 | 215 | 18% | 70 | 700 | 260 | 125 | 5,50 | 2.280 | 2.050 | 790 | 530 | 0 | 60 | 0 | 0 |
| M12 | 840 | 240 | 18% | 75 | 700 | 270 | 125 | 5,55 | 2.410 | 2.210 | 820 | 540 | 10 | 0 | 0 | 0 |
| M13 | 920 | 265 | 18% | 80 | 820 | 280 | 130 | 6,20 | 2.620 | 2.360 | 900 | 570 | 10 | 100 | 0 | 2.000 |
| M14 | 1.000 | 290 | 18% | 85 | 820 | 290 | 130 | 6,10 | 2.780 | 2.520 | 940 | 580 | 20 | 0 | 0 | 0 |
| M15 | 1.080 | 315 | 18% | 85 | 820 | 300 | 135 | 6,00 | 2.950 | 2.690 | 980 | 590 | 30 | 40 | 0 | 0 |
| M16 | 1.160 | 340 | 18% | 90 | 960 | 310 | 135 | 5,90 | 3.120 | 2.870 | 1.020 | 610 | 40 | 0 | 0 | 0 |
| M17 | 1.240 | 365 | 18% | 95 | 960 | 320 | 140 | 5,80 | 3.290 | 3.060 | 1.060 | 620 | 60 | 60 | 0 | 0 |
| M18 | 1.320 | 390 | 17% | 95 | 960 | 330 | 140 | 5,70 | 3.460 | 3.260 | 1.100 | 630 | 80 | 0 | 0 | 0 |
| M19 | 1.400 | 415 | 17% | 100 | 1.100 | 340 | 145 | 5,65 | 3.640 | 3.470 | 1.140 | 650 | 100 | 80 | 0 | 0 |
| M20 | 1.480 | 440 | 17% | 100 | 1.100 | 350 | 145 | 5,60 | 3.820 | 3.690 | 1.180 | 660 | 120 | 0 | 0 | 0 |
| M21 | 1.560 | 465 | 17% | 105 | 1.100 | 360 | 150 | 5,55 | 4.000 | 3.920 | 1.220 | 670 | 140 | 40 | 0 | 0 |
| M22 | 1.640 | 490 | 17% | 105 | 1.240 | 370 | 150 | 5,50 | 4.190 | 4.160 | 1.260 | 690 | 160 | 0 | 0 | 0 |
| M23 | 1.720 | 520 | 17% | 110 | 1.240 | 380 | 155 | 5,45 | 4.380 | 4.410 | 1.300 | 700 | 180 | 60 | 0 | 0 |
| M24 | 1.800 | 550 | 17% | 110 | 1.240 | 390 | 155 | 5,40 | 4.580 | 4.670 | 1.340 | 710 | 200 | 0 | 0 | (500) |

### Choque a aplicar após o base case

No início de M13:

- câmbio segue a tabela;
- consumo realizado fica 20% abaixo do previsão de M13–M18;
- uma contratação planejada para M16 ocorre em M13, adicionando R$ 140 mil/mês a payroll;
- clientes atrasam recebíveis: AR final de M13–M18 aumenta em R$ 300 mil sobre a tabela;
- HQ exige preservar caixa final de M18 acima de R$ 4.000 mil.

### Tarefas

1. Construir P&L, balanço e fluxo de caixa mensais, M1–M24.
2. Mostrar annual view de Y1 e Y2.
3. Reconciliar caixa e explicar, em cinco movimentos, por que EBITDA e caixa divergem.
4. Calcular gross profit, EBITDA, margem EBITDA, burn ou geração de caixa e runway quando aplicável.
5. Construir base case e downside M13–M18.
6. Produzir bridge de EBITDA e caixa entre base e downside.
7. Recomendar três ações priorizadas para respeitar o piso de caixa, com efeito, escolha e renúncia e gatilho.
8. Escrever memo de uma página para HQ: situação, implicação, opções, recomendação, riscos e ask.

---

## Instrumento C — simulação da operação de receita

**Tempo:** 90 minutos.\
**Mede:** pipeline, capacity, quota, previsão, discount governance e miss management.\
**Empresa:** Aster AI Brasil — cenário sintético.\
**Data de corte:** 30 de setembro; Q4 tem 92 dias.

### Definições fornecidas

- `Pipeline`: oportunidades abertas; não é receita.
- `Bookings`: valor contratado; não é automaticamente receita reconhecida nem caixa.
- `Commit`: alta confiança, com evidência de comprador, processo e data.
- `Best case`: pode fechar no trimestre, mas mantém dependência material.
- `Upside`: possível, porém não deve sustentar o plano.

### Meta e capacidade

Meta Q4 de new ARR: **R$ 3.600 mil**.

| Rep | Ramp em Q4 | Quota Q4 | Capacidade máxima de deals ativos | Deals ativos |
|---|---:|---:|---:|---:|
| Ana | 100% | 1.200 | 5 | 5 |
| Bruno | 100% | 1.200 | 5 | 4 |
| Carla | 60% | 720 | 3 | 4 |
| Diego | 40% | 480 | 2 | 3 |

### Oportunidades abertas

| ID | Rep | Segmento | ARR | Stage | Prob. CRM | Dias no stage | Close CRM | Champion | Economic buyer | Security | Procurement | Próximo passo datado | Desconto pedido |
|---|---|---|---:|---|---:|---:|---|---|---|---|---|---|---:|
| O1 | Ana | Enterprise | 900 | Negotiation | 80% | 18 | 15/out | forte | confirmado | aprovado | em curso | redline 04/out | 12% |
| O2 | Ana | Enterprise | 700 | Security | 60% | 35 | 31/out | forte | confirmado | 2 pendências | não iniciado | workshop 07/out | 5% |
| O3 | Ana | Mid | 320 | Proposal | 50% | 12 | 20/out | médio | não | n/a | não iniciado | demo CFO 06/out | 0% |
| O4 | Ana | Enterprise | 1.100 | Discovery | 20% | 8 | 15/dez | fraco | não | não iniciado | não iniciado | discovery 05/out | 0% |
| O5 | Ana | Mid | 280 | Negotiation | 80% | 42 | 10/out | forte | confirmado | n/a | travado | sem data | 18% |
| O6 | Bruno | Enterprise | 1.200 | Proposal | 50% | 16 | 30/nov | forte | confirmado | aprovado | não iniciado | business case 10/out | 8% |
| O7 | Bruno | Mid | 450 | Negotiation | 80% | 9 | 25/out | forte | confirmado | n/a | aprovado | assinatura 11/out | 3% |
| O8 | Bruno | Enterprise | 850 | Security | 60% | 28 | 15/nov | médio | confirmado | pendência crítica | não iniciado | security call 08/out | 0% |
| O9 | Bruno | Mid | 260 | Proposal | 50% | 47 | 20/out | fraco | não | n/a | não iniciado | sem data | 10% |
| O10 | Carla | Mid | 380 | Negotiation | 80% | 7 | 18/out | forte | confirmado | n/a | aprovado | assinatura 09/out | 0% |
| O11 | Carla | Enterprise | 950 | Discovery | 20% | 14 | 15/dez | médio | não | não iniciado | não iniciado | tech discovery 12/out | 0% |
| O12 | Carla | Mid | 300 | Proposal | 50% | 21 | 10/nov | forte | confirmado | n/a | não iniciado | proposal review 06/out | 6% |
| O13 | Carla | SMB | 120 | Negotiation | 80% | 30 | 07/out | médio | confirmado | n/a | cartão falhou | nova tentativa 03/out | 0% |
| O14 | Diego | Enterprise | 1.400 | Discovery | 20% | 5 | 20/dez | fraco | não | não iniciado | não iniciado | discovery 14/out | 0% |
| O15 | Diego | Mid | 340 | Proposal | 50% | 10 | 30/nov | médio | confirmado | n/a | não iniciado | ROI review 13/out | 15% |
| O16 | Diego | Mid | 240 | Negotiation | 80% | 25 | 20/out | forte | confirmado | n/a | aprovado | assinatura 05/out | 4% |

Política: desconto acima de 10% exige Country Lead + Finance; acima de 15% exige CFO. Security pendente crítica não pode entrar em commit. Oportunidade sem próximo passo datado não entra em best case.

### Tarefas

1. Higienizar o pipeline e marcar evidência ausente.
2. Produzir previsão `commit / best case / upside`, sem usar apenas probabilidade do CRM.
3. Calcular cobertura total, cobertura qualificada e gap para quota.
4. Avaliar capacidade por rep e propor redistribuição ou desqualificação.
5. Aprovar, negar ou condicionar cada desconto acima de 10%.
6. Produzir plano de 30 dias com responsáveis, métricas leading, limites e ações.
7. Simular QBR: explique o miss provável sem culpar mercado ou pipeline genérico.
8. Identificar diferenças entre bookings, ARR, receita reconhecida e caixa.

---

## Instrumento D — memorando de investimento no Brasil

**Tempo:** 240 minutos.\
**Mede:** estratégia, market entry, alocação, P&L de país e diplomacia HQ↔local.\
**Empresa:** `Northstar AI` — cenário sintético, sem relação com empresa real.

### Mandato

O board disponibiliza no máximo **R$ 12 milhões por 24 meses**. A continuidade após M12 depende de evidência. O produto já funciona em inglês; localização e presença local ainda não existem.

### Segmentos candidatos

| Segmento | Contas acessíveis | ARR médio | Ciclo | Win rate após oportunidade qualificada | Gross margin | Churn anual esperado | CAC fully-loaded | Fricção principal |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| Digital-native mid-market | 600 | 180 | 75 dias | 24% | 78% | 14% | 110 | integração e suporte |
| Enterprise regulada | 120 | 720 | 210 dias | 16% | 68% | 6% | 420 | security, procurement, DPA |
| Setor público | 45 | 1.100 | 330 dias | 9% | 64% | 4% | 760 | contratação, policy, prazo |

Todos os valores monetários da tabela estão em R$ mil. Esses números são inputs sintéticos, não benchmarks.

### Opções de entrada

| Opção | Custo fixo 12m | Tempo para operar | Margem cedida | Controle | Limitação |
|---|---:|---:|---:|---|---|
| A — venda cross-border | 1.800 | imediato | 0% | alto no produto | cobrança, suporte e procurement |
| B — parceiro mestre | 2.600 | 60 dias | 24% da receita | médio | dependência e conflito de canal |
| C — subsidiária enxuta | 5.400 | 150 dias | 0% | alto | execução legal, fiscal e hiring |

### Recursos e restrições

- O HQ aceita contratar no máximo seis pessoas até M12.
- Engineering global oferece 1.200 horas de localização no ano.
- Produto pode cumprir dois, e apenas dois, destes itens até M9: PT-BR, billing local, integração de identidade enterprise, conector de dados local.
- O board exige gross margin local ≥ 65% no M12.
- Caixa comprometido até M12 não pode superar R$ 7 milhões.
- Um lighthouse logo não conta como repeatability.
- O HQ não autoriza afirmar compliance ou adequação jurídica sem revisão especialista.

### Sinais disponíveis

| Sinal | Digital-native | Enterprise | Público |
|---|---:|---:|---:|
| Discovery calls concluídas | 18 | 14 | 5 |
| Problema confirmado | 12 | 11 | 4 |
| Piloto aceito | 5 | 5 | 1 |
| Economic buyer envolvido | 3 | 4 | 0 |
| Processo de compra mapeado | 2 | 3 | 0 |
| Contrato assinado | 0 | 0 | 0 |

### Choques

Use o base case e escolha dois:

- `FX`: BRL desvaloriza 15%, elevando HQ charges.
- `Delay`: subsidiária atrasa 90 dias.
- `Security`: duas oportunidades enterprise exigem conector local antes do piloto.
- `Partner`: parceiro pede 32% de margem e exclusividade de 18 meses.

### Entrega — memo máximo de seis páginas

1. Recomendação e ask.
2. Por que Brasil agora — somente com os inputs fornecidos.
3. Segmento e wedge; dois segmentos explicitamente adiados.
4. Entry mode e alternativa rejeitada.
5. Dois itens de produto priorizados e dois recusados.
6. Headcount e sequência até M12.
7. P&L simplificado 24 meses, base/downside.
8. Gates M3, M6, M9 e M12; cada um com métrica, limite, responsável e ação.
9. Critérios de encerramento e capital realocado se o investimento parar.
10. Riscos, informação ausente e escalonamento a CFO/controller/advogado.
11. Mensagem de cinco linhas ao HQ defendendo a decisão sem excepcionalismo brasileiro.

---

## Instrumento E — caso de organização 0–5 / 5–20 / 20–50

**Tempo:** 120 minutos.\
**Mede:** operating model, org design, gestores, incentivos, performance e sucessão.\
**Empresa:** Northstar AI Brasil — cenário sintético.

### Situação inicial

Time atual: Country Lead, 2 AEs, 1 Solutions Engineer e 1 Community/Growth Lead. O Country Lead aprova todo desconto, revisa toda proposta, entra em todo discovery enterprise e resolve incidentes de clientes.

### Demanda projetada para M12

| Trabalho | Volume mensal | Capacidade por FTE/mês | Observação |
|---|---:|---:|---|
| Oportunidades enterprise qualificadas | 18 | 6 por AE | exige SE em 60% |
| Oportunidades mid-market qualificadas | 35 | 12 por AE | ciclo mais curto |
| Implementações novas | 12 | 5 por implementation lead | duas complexas |
| Contas ativas high-touch | 45 | 25 por CSM | expansão incluída |
| Incidentes críticos | 6 | 12 por support lead | on-call necessário |
| Partner reviews | 10 | 15 por partner gestor | conflito potencial |

### Restrições

- Limite de payroll fully-loaded: R$ 720 mil/mês em M12.
- Custos mensais por papel, em R$ mil: gestor 75; AE 55; SE 60; CSM 42; implementation 48; growth 45; ops/finance 50; support 38; partner gestor 52.
- Span-alvo para gestor: 4–7 reports.
- Nenhuma função pode ter só uma pessoa sem backup nomeado após 20 FTEs.
- O HQ retém product roadmap, security policy e treasury.
- O país decide contratação dentro do budget, segment sequencing e parceiros não exclusivos.
- Desconto >10%, claim regulatório e incidente crítico exigem escalonamento.

### Tarefas

1. Desenhar organizações 0–5, 5–20 e 20–50.
2. Sequenciar as primeiras dez contratações, com gatilho e custo.
3. Definir decision rights: país, HQ e compartilhado.
4. Remover pelo menos três dependências do Country Lead.
5. Criar quadro de indicadores de dois gestores: resultados, leading indicators, comportamentos e erros críticos.
6. Definir incentivo que não premie receita ruim, desconto excessivo ou churn futuro.
7. Especificar cadência: weekly, monthly e quarterly.
8. Resolver um caso de performance: o melhor AE bate 140% da quota, mas usa descontos não aprovados e deteriora handoffs.
9. Definir sucessor interino e plano de continuidade de 30 dias.
10. Indicar o que o desenho ainda não prova no mundo real.

---

## Instrumento F — simulação de governança

**Tempo:** 90 minutos.\
**Mede:** QBR, risco, board, controles, issue-spotting e comunicação sob challenge.\
**Empresa:** Northstar AI Brasil — cenário sintético.

### Pacote da revisão trimestral

| Métrica Q3 | Plano | Real | Observação |
|---|---:|---:|---|
| New ARR | 2.400 | 1.620 | um deal de 700 escorregou |
| Gross margin | 70% | 63% | uso acima do previsto |
| Burn | 1.800 | 2.350 | contratação antecipada |
| Pipeline qualificado Q4 | 7.200 | 5.100 | CRM total mostra 9.800 |
| Previsão accuracy | 85% | 58% | commit incluiu security pendente |
| NRR | 108% | 96% | downsell de duas contas |
| DSO | 45 dias | 71 dias | três invoices contestadas |
| Incidentes críticos | 0 | 2 | um ainda aberto |

### Eventos recebidos 24 horas antes do board

1. Um prospect pede declaração formal de adequação à LGPD. O time comercial quer assinar uma carta preparada por IA.
2. Um incidente expôs metadados de 240 usuários por 36 horas. Não há confirmação de acesso malicioso.
3. O parceiro mestre quer exclusividade em troca de pipeline de R$ 4 milhões, sem lista de contas.
4. Finance encontrou R$ 380 mil de serviços consumidos e não faturados.
5. O melhor AE aprovou desconto de 18% sem alçada.
6. O HQ pede manter a meta anual e cortar 15% do OPEX.

### Tarefas

1. Produzir QBR de uma página: realidade, causas, previsão revisado, ações e asks.
2. Criar registro de riscos com responsável, leading indicator, limite, response e escalation.
3. Priorizar os seis eventos em uma matriz de urgência/impacto/reversibilidade.
4. Decidir o que comunicar imediatamente ao board e o que investigar antes.
5. Recusar ou escalar afirmações jurídicas sem parecer paralisado.
6. Propor três controles preventivos e três detectivos.
7. Responder oralmente, em até três minutos cada:
   - “Por que devemos confiar no seu novo previsão?”
   - “Você está escondendo um problema de produto atrás do Brasil?”
   - “Qual investimento você mata hoje?”
   - “O que exige advogado, controller, security ou HQ?”

### Limite de autoridade

O aluno não deve emitir parecer jurídico, tributário ou de segurança. Deve identificar problema, preservar evidência, conter dano, nomear responsável, definir limite e escalar ao especialista adequado.

---

## Formas paralelas de reteste

As formas abaixo são especificações, não atalhos. O avaliador deve trocar números e nomes mantendo dificuldade e blueprint.

| Bloco | Forma B obrigatória |
|---|---|
| B | balanço de abertura e 18 meses novos; choque de churn + collections; três demonstrações continuam obrigatórias |
| C | 14–18 oportunidades novas; stages e policy equivalentes; quota gap diferente |
| D | empresa sintética diferente; três segmentos, três entry modes e capital cap equivalente |
| E | capacidade e custo novos; mesmo problema de centralização e gestor misconduct |
| F | QBR novo; um incidente, um risco jurídico, um miss de previsão e um conflito de canal |

Não reutilizar respostas, números, planilhas ou gabarito da tentativa anterior.

## Fontes e limitações

Os instrumentos B–F usam dados sintéticos para avaliação. Não incluem casos pessoais do autor. Nenhum benchmark, lei atual ou estatística externa é afirmado neste arquivo.
