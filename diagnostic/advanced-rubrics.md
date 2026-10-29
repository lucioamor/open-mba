# M0 — rubricas, placement engine e chaves de calibração

`audience: evaluator_only`\
`version: 1.0`\
`learner_status: awaiting learner results`

## 1. Política da edição pública

Este arquivo contém escalas e chaves dos instrumentos avançados. Para roteamento, prevalece [README.md](README.md). P não é nota; as classificações históricas P0–P3 abaixo são descritores qualitativos e não correspondem automaticamente aos status do perfil público. Não há resultado de aluno preenchido.

## 2. Escalas analíticas

### K — knowledge

| Faixa | Descritor |
|---:|---|
| 90–100 | Calcula e explica sem erro material; reconcilia modelos; distingue conceitos vizinhos; identifica limites. |
| 85–89 | Domínio forte; pequenas falhas não alteram decisão ou resultado. |
| 70–84 | Conhecimento utilizável, mas incompleto; requer apoio em caso novo ou sob choque. |
| 50–69 | Lacunas materiais; acerta partes, mas erra integração, definição ou cálculo relevante. |
| 0–49 | Não demonstra o conceito ou produz conclusão incompatível com os dados. |

### J — judgment

| Faixa | Descritor |
|---:|---|
| 90–100 | Escolha clara; alternativa rejeitada; escolha e renúncia; consequência econômica; risco; responsável; limite e revisão. |
| 80–89 | Boa decisão e defesa; uma dimensão secundária fica incompleta. |
| 70–79 | Recomendação plausível, mas gates, renúncia ou consequências permanecem genéricos. |
| 50–69 | Lista ações sem priorização; confunde análise com decisão; não governa incerteza. |
| 0–49 | Escolha contradiz dados, excede autoridade ou oculta risco material. |

### P — proof status

Avalie seis critérios:

1. autoridade formal ou decision rights;
2. escopo econômico/organizacional;
3. consequência real da decisão;
4. recorrência em mais de um ciclo;
5. independência da execução pessoal do participante;
6. documentação ou atribuição verificável.

| Status | Regra |
|---|---|
| `P0_absent` | nenhum artefato suficiente ou apenas narrativa |
| `P1_candidate` | evidência parcial; claim continua self-reported/inferred |
| `P2_moderate` | os critérios 1–3 estão documentados; recorrência ou independência ainda limitada |
| `P3_strong` | critérios 1–3 e pelo menos dois de 4–6; evidência revisável e atribuição clara |

Sem os critérios 1, 2 e 3, nunca classificar P como forte. Documento produzido apenas para este diagnóstico não prova experiência passada.

## 3. Competências canônicas e instrumentos

As letras identificam os instrumentos avançados. Use as questões específicas do módulo para isolar cada competência; um resultado agregado não é copiado para todos os IDs. Os fundamentos F1–F4 têm casos e rubricas nas próprias oficinas.

| ID | Competência | Instrumento complementar |
|---|---|---|
| FIN-01 | Regime de competência, caixa e reconhecimento | B |
| FIN-02 | Três demonstrações integradas | B |
| FIN-03 | Resultado de país e centros de responsabilidade | B |
| FIN-04 | Budget, rolling previsão e variance bridge | B |
| FIN-05 | Fôlego de caixa, capital de giro e câmbio | B |
| UE-01 | Receita recorrente, retenção e economia de coortes | B/C/D |
| UE-02 | Custo completo de aquisição, valor do cliente e prazo de recuperação | B/C/D |
| UE-03 | Pricing por consumo e margem por carga de trabalho | B/C/D |
| CAP-01 | Alocação de capital, retorno mínimo e critérios de encerramento | B/C/D |
| STR-01 | Escolhas, renúncias e vantagem | D |
| STR-02 | Taxas-base, cenários e valor da informação | D |
| STR-03 | Reversibilidade e diário de decisões | D |
| OPS-01 | Modelo operacional e mecanismos | E |
| OPS-02 | Direitos de decisão, interfaces e escalonamento | E |
| OPS-03 | Cadência de revisões e responsabilidade com acompanhamento | E |
| ORG-01 | Desenho organizacional, amplitude, camadas e sequência | E |
| ORG-02 | Hiring scorecards e gestor selection | E |
| ORG-03 | Desempenho, incentivos e manipulação de métricas | E |
| ORG-04 | Succession e liderança por gestores | E |
| CTY-01 | Tese Brasil, segmento inicial e modo de entrada | D/F |
| CTY-02 | Modelo de operação de receita e direito de investir | D/F |
| CTY-03 | Acordo matriz-local e diplomacia corporativa | D/F |
| GOV-01 | Governança do conselho e controles internos | F |
| RSK-01 | Risco empresarial, limites e resposta | F |
| BRL-01 | Identificação de questões de LGPD e regulação de IA | F |
| BRL-02 | Tributário, trabalhista, cambial e entidade | F |
| COM-01 | Memorando ao conselho e pedido de investimento | B–F |
| COM-02 | Revisão trimestral de desvio e comunicação sob questionamento | B–F |
| COM-03 | Defesa oral e síntese executiva | B–F |

## 4. Componentes por instrumento

As proporções abaixo organizam a correção dentro do instrumento. Não existe nota geral que dispense uma competência. Registre K e J separadamente nas tarefas correspondentes.

| Instrumento | Componentes de correção |
|---|---|
| B — finance | três demonstrações 35; P&L/cash 25; scenario/bridge 20; decisão 20 |
| C — revenue | higiene/previsão 35; capacity/quota 20; conceitos revenue 20; ações 25 |
| D — investment memo | escolhas 25; economics 25; entry/HQ 20; gates/kill 20; escalonamento 10 |
| E — organization | org/decision rights 30; capacity/cost 20; gestores 25; incentivos/sucessão 25 |
| F — governance | realidade/previsão 20; risco/controles 30; escalonamento 25; defesa 25 |

## 5. Erros críticos locais

| ID | Fatal error | Subcompetência bloqueada |
|---|---|---|
| FE-FIN-01 | balanço não fecha e o aluno o apresenta como reconciliado | FIN-02, FIN-03 |
| FE-FIN-02 | confundir lucro, EBITDA ou bookings com caixa | FIN-01, FIN-03, UE-01 |
| FE-FIN-03 | erro de sinal ou fórmula que altera materialmente runway, caixa ou decisão e não é detectado | FIN-03, FIN-04 |
| FE-UE-01 | incluir oportunidade sem evidência crítica em commit ou tratar pipeline como receita | UE-01, CTY-02 |
| FE-CTY-02 | usar probabilidade do CRM como única base de previsão | CTY-02 |
| FE-STR-01 | recomendar investimento sem renúncia, gate ou kill criterion | STR-01, CTY-01 |
| FE-OPS-01 | operating model mantém decisões críticas integralmente no Country Lead sem plano de remoção | OPS-01, ORG-01 |
| FE-ORG-01 | promover performance tóxica ou desconto não autorizado apenas porque quota foi batida | ORG-02 |
| FE-GOV-01 | omitir do board incidente, exposição financeira ou risco material conhecido | GOV-01 |
| FE-BRL-01 | emitir certeza jurídica/regulatória ou assinar claim sem fonte/revisão competente | BRL-01 |
| FE-COM-01 | alterar número, atribuição ou status de evidência durante a defesa para fortalecer a narrativa | COM-01 e claim afetado |
| FE-P-01 | transformar simulação, currículo ou autodeclaração em prova operacional forte | P de todo domínio afetado |

`Material` significa que o erro muda recomendação, viola limite, desloca em ≥5% uma saída crítica ou oculta risco que exigiria escalonamento. Pequeno erro aritmético isolado pode ser corrigido na defesa se o método estiver correto e a decisão não mudar.

## 6. Roteamento público

Veja [README.md](README.md). A rubrica dos casos profissionais do autor foi excluída.

## 8. Chave do instrumento B

### Fórmulas obrigatórias

```text
Revenue = subscription revenue + consumption revenue
Hosting = Revenue × hosting %
HQ charge = 35 × FX
EBITDA = Revenue - Hosting - Support - Payroll - S&M - G&A - HQ charge
Depreciation = 16 + prior capex / 36
EBT = EBITDA - Depreciation
Tax expense = max(EBT, 0) × 25%
Net income = EBT - Tax expense
CFO = Net income + Depreciation
      - ΔAR - ΔPrepaid + ΔAP + ΔAccrued payroll
      + ΔTax payable + ΔDeferred revenue
Closing cash = Opening cash + CFO - Capex + Equity contribution + Debt movement
```

### Checkpoints do base case

Tolerância de arredondamento: R$ 2 mil por célula; diferença do balanço deve ser zero, salvo arredondamento inferior a R$ 1 mil.

| Checkpoint | Resultado |
|---|---:|
| Y1 revenue | 7.655,00 |
| Y1 EBITDA | (6.689,55) |
| Y1 CFO | (5.979,55) |
| M12 closing cash | 4.200,45 |
| Y2 revenue | 21.165,00 |
| Y2 EBITDA | (4.162,55) |
| Y2 CFO | (2.992,55) |
| M18 closing cash — base | 3.819,75 |
| M24 closing cash — base | 2.327,90 |
| M24 EBITDA mensal | (133,50) |

O base case já viola o piso de M18 de R$ 4.000 mil. Portanto, a resposta “nenhuma ação” é incorreta antes mesmo do downside.

### Cinco movimentos EBITDA↔caixa aceitáveis

Reconhecimento vs cobrança; AR/DSO; receita diferida/billings; AP/provisões; capex; aporte/dívida; impostos pagos vs provisionados. O aluno deve explicar cinco com sinal e consequência.

### Downside

O aluno deve recalcular M13–M18. Aceite diferentes ações, mas exija:

- queda de consumption revenue de 20%;
- payroll adicional de 140/mês;
- AR final +300 em M13–M18;
- câmbio da tabela preservado;
- bridge separado entre EBITDA e caixa;
- ações suficientes para elevar M18 acima de 4.000, sem dupla contagem.

Checkpoints antes das ações de mitigação:

| Checkpoint downside | Resultado |
|---|---:|
| M13 EBITDA | (738,76) |
| M13 closing cash | 5.111,69 |
| M18 EBITDA | (509,94) |
| M18 closing cash | 2.356,71 |
| Delta de caixa M18 vs base | (1.463,04) |

Qualquer plano de mitigação precisa produzir pelo menos R$ 1.643,29 mil de caixa incremental até M18 para superar, e não apenas alcançar, o piso de R$ 4.000 mil. Validar timing: economia posterior a M18 não resolve o gate.

## 9. Chave do instrumento C

### Checkpoints

- Pipeline bruto: **R$ 9.790 mil**, cobertura bruta **2,72×** a quota.
- Capacidade: Carla tem 4 deals para capacidade 3; Diego tem 3 para capacidade 2.
- Commit defensável mínimo: O1, O7, O10, O13 e O16, total **R$ 2.090 mil**, sujeito a aprovações indicadas.
- O5 não entra em best case: sem próximo passo datado e procurement travado.
- O8 não entra em commit: security pendente crítica.
- Descontos O1 (12%), O5 (18%) e O15 (15%) exigem Country Lead + Finance; O5 também exige CFO por exceder 15%.

O2, O6, O8, O12 e O15 podem variar entre best case e upside conforme a justificativa. Não pontue a categoria isolada; pontue a evidência, dependência e ação necessária. O previsão deve mostrar gap para R$ 3.600 e não inventar cobertura.

### Fatal conceptual distinctions

- ARR contratado não é receita reconhecida no trimestre.
- Bookings não é caixa.
- Pipeline ponderado não é commit.
- Coverage não resolve capacity nem sales cycle.

## 10. Chave do instrumento D

Não existe uma única escolha correta. A resposta de domínio precisa:

- priorizar um segmento e adiar dois;
- escolher um entry mode e rejeitar outro;
- respeitar R$ 7 milhões até M12 e R$ 12 milhões até M24;
- respeitar seis pessoas até M12;
- escolher dois itens de produto e recusar dois;
- demonstrar gross margin local e efeito de margem do parceiro;
- usar os sinais fornecidos sem convertê-los em demanda comprovada;
- incluir quatro gates e pelo menos um kill criterion objetivo;
- separar issue-spotting de parecer jurídico;
- adaptar a recomendação aos dois choques escolhidos.

Resposta que declara TAM, lei, benchmark ou comportamento de empresa real não fornecido perde crédito de evidência e pode receber erro crítico.

## 11. Chave do instrumento E

O desenho não precisa usar todos os papéis. Deve:

- mostrar capacidade e custo, sem exceder R$ 720 mil/mês em M12;
- respeitar span 4–7 para gestores;
- remover aprovação universal, revisão universal e presença universal do Country Lead;
- manter roadmap, security policy e treasury no HQ;
- tratar desconto >10%, claim regulatório e incidente crítico como escalonáveis;
- não premiar o AE de 140% sem consequência e correção de controle;
- nomear sucessor interino, backup e decision rights por 30 dias;
- declarar que simulação não prova líder de gestores real.

## 12. Chave do instrumento F

Prioridade esperada:

1. conter/preservar evidência do incidente e acionar security/privacy;
2. impedir carta jurídica feita por IA e escalar revisão;
3. reconhecer serviços não faturados e impacto financeiro;
4. corrigir previsão/discount authority;
5. avaliar parceria sem aceitar pipeline não especificado;
6. ajustar OPEX/meta com bridge e escolha explícita.

Outras ordenações são aceitáveis se urgência, dano, reversibilidade e obrigação de escalonamento forem defendidos. Ocultar os eventos 1–4 do board ou tratá-los como resolvidos sem investigação é fatal.

## 13. Reteste

| Resultado | Remediação mínima | Reteste |
|---|---|---|
| K ou J 70–84 | revisão dirigida + uma prática equivalente | forma B da subcompetência |
| K ou J <70 | lição DEEP + duas práticas guiadas | forma B integral do bloco |
| erro crítico | análise de causa + cálculo/decisão refeito + checklist | forma B integral após ≥72h |
| autoria duvidosa | defesa oral sem material + reprodução do cálculo | nova forma supervisionada |
| P0/P1 | não é reteste acadêmico | field practicum ou nova evidência real |

Para aprovação no reteste:

- SKIP continua exigindo K ≥85, J ≥80, dois casos e zero erro crítico.
- COMPRESS exige ambos ≥70 e zero erro crítico.
- Nova falha crítica mantém DEEP.
- Registrar as duas tentativas; nunca sobrescrever a primeira.

## 14. Formas B seladas

Entregar somente a forma do bloco reprovado. Os casos continuam sintéticos.

### B-FIN — integração e caixa, 12 meses

Tempo: 100 minutos. Balanço M0:

| Conta | Valor |
|---|---:|
| Caixa | 5.000 |
| AR | 800 |
| Prepaid | 120 |
| PPE bruto | 360 |
| Depreciação acumulada | (60) |
| **Ativos** | **6.220** |
| AP | 350 |
| Payroll provisionado | 250 |
| Receita diferida | 500 |
| Tributos a pagar | 20 |
| Dívida | 800 |
| Patrimônio líquido | 4.300 |
| **Passivo + PL** | **6.220** |

Regras: hosting sobre revenue; HQ charge = `US$ 20 mil × FX`; depreciação de abertura R$ 10 mil/mês; capex novo em 24 meses a partir do mês seguinte; imposto 25% do EBT positivo; prepaid consumido em R$ 20 mil/mês M1–M6, já incluído em G&A; fluxo indireto; saldos finais abaixo.

| M | Revenue | Hosting % | Support | Payroll | S&M | G&A | FX | AR fim | Diferida fim | AP fim | Payroll fim | Tax fim | Capex | Aporte | Dívida +/- |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|
| 1 | 500 | 24% | 45 | 280 | 120 | 80 | 5,20 | 860 | 560 | 370 | 260 | 10 | 30 | 0 | 0 |
| 2 | 560 | 24% | 45 | 280 | 125 | 80 | 5,25 | 920 | 620 | 390 | 270 | 0 | 0 | 0 | 0 |
| 3 | 620 | 24% | 50 | 340 | 130 | 85 | 5,30 | 990 | 690 | 420 | 280 | 0 | 40 | 0 | 0 |
| 4 | 690 | 23% | 50 | 340 | 135 | 85 | 5,35 | 1.060 | 770 | 440 | 290 | 0 | 0 | 1.200 | 0 |
| 5 | 760 | 23% | 55 | 340 | 140 | 90 | 5,40 | 1.140 | 850 | 460 | 300 | 0 | 20 | 0 | 0 |
| 6 | 840 | 23% | 60 | 420 | 150 | 90 | 5,45 | 1.230 | 940 | 490 | 315 | 0 | 0 | 0 | 0 |
| 7 | 920 | 22% | 60 | 420 | 155 | 95 | 5,90 | 1.380 | 1.030 | 540 | 330 | 0 | 50 | 0 | 700 |
| 8 | 1.000 | 22% | 65 | 420 | 160 | 95 | 5,80 | 1.490 | 1.130 | 570 | 340 | 10 | 0 | 0 | 0 |
| 9 | 1.080 | 22% | 70 | 500 | 170 | 100 | 5,70 | 1.610 | 1.240 | 600 | 355 | 20 | 30 | 0 | 0 |
| 10 | 1.160 | 21% | 70 | 500 | 180 | 100 | 5,60 | 1.730 | 1.360 | 630 | 365 | 30 | 0 | 0 | 0 |
| 11 | 1.240 | 21% | 75 | 500 | 190 | 105 | 5,50 | 1.860 | 1.490 | 660 | 375 | 40 | 40 | 0 | 0 |
| 12 | 1.320 | 21% | 80 | 580 | 200 | 105 | 5,40 | 2.000 | 1.630 | 690 | 390 | 50 | 0 | 0 | (200) |

Tarefas: três demonstrações, reconciliação mensal, Y1, bridge EBITDA→cash e choque M7–M12 com revenue -12%, AR +180 e payroll +60. Recomendar ação para caixa mínimo M12 de R$ 4.500.

Checkpoints: base Y1 revenue 10.690,00; EBITDA (1.608,10); CFO (1.048,10); caixa M12 5.441,90. Choque: Y1 revenue 9.883,60; EBITDA (2.601,56); CFO (2.221,56); caixa M12 4.268,44. A mitigação precisa gerar mais de R$ 231,56 mil até M12.

### C-REV — previsão alternativo

Tempo: 50 minutos. Quota: R$ 2.400 mil. Dois reps, quota 1.200 cada, capacidade 4 deals cada.

| ID | ARR | Stage | Dias | Buyer | Security | Procurement | Próximo passo | Desconto |
|---|---:|---|---:|---|---|---|---|---:|
| R1 | 620 | Negotiation | 12 | sim | ok | em curso | redline 05/abr | 8% |
| R2 | 540 | Security | 31 | sim | crítico | não | call 07/abr | 0% |
| R3 | 280 | Proposal | 18 | não | n/a | não | demo 06/abr | 0% |
| R4 | 760 | Negotiation | 9 | sim | ok | aprovado | assinatura 08/abr | 12% |
| R5 | 220 | Negotiation | 40 | sim | n/a | travado | sem data | 18% |
| R6 | 680 | Proposal | 14 | sim | ok | não | business case 10/abr | 5% |
| R7 | 310 | Negotiation | 6 | sim | n/a | aprovado | assinatura 04/abr | 0% |
| R8 | 900 | Discovery | 5 | não | não | não | discovery 12/abr | 0% |

Política idêntica à forma A. Entrega: commit/best/upside, coverage, capacity, descontos, gap e plano de 15 dias.

### D-STR/CTY — investment memo alternativo

Tempo: 120 minutos. `Helix Cloud`, sintética, tem R$ 8 milhões por 18 meses. Três segmentos:

| Segmento | Contas | ARR médio | Ciclo | Win rate | GM | CAC |
|---|---:|---:|---:|---:|---:|---:|
| SMB técnico | 1.200 | 60 | 35d | 18% | 82% | 28 |
| Mid-market | 350 | 220 | 95d | 22% | 74% | 130 |
| Enterprise | 80 | 850 | 240d | 12% | 66% | 510 |

Escolher entre cross-border (R$ 1,2M fixo), dois parceiros não exclusivos (R$ 2,0M + 20% da receita) ou entidade local (R$ 4,4M; 120 dias). Máximo quatro FTE até M9. Gate: caixa comprometido ≤R$ 5M e GM ≥68% em M9. Entrega: wedge, renúncias, entry mode, P&L, quatro gates e kill criterion. Choque obrigatório: ciclo +45 dias e FX +10%.

### E-ORG — organização alternativa

Tempo: 60 minutos. Um Country Lead com sete reports diretos aprova propostas, incidentes e hiring. O time crescerá de 8 para 24 em nove meses; budget R$ 650 mil/mês; dois melhores ICs querem virar gestores, mas nenhum avaliou performance. Entrega: spans/layers, dez contratações, decision rights, scorecards, incentivo, caso de performance e sucessão. Deve remover três dependências do Country Lead e nomear backup para funções single-point-of-failure.

### F-GOV — QBR alternativo

Tempo: 50 minutos. Plano/real: ARR 1.800/1.250; GM 72%/65%; DSO 40/68; previsão accuracy 80%/54%; incidentes 0/1. Eventos: invoice duplicada de R$ 210 mil; claim de compliance sem revisão; parceiro promete R$ 3 milhões sem account list; incidente ainda não contido; headcount contratado fora do budget. Entrega: QBR, registro de riscos, comunicação ao board, controles e escalonamento. Omissão de incidente ou claim jurídico continua fatal.

## 15. Template de quadro de indicadores

| ID canônico | K | J | Revisão | Casos independentes | Erro crítico | Prática | Remediação/reteste |
|---|---|---|---|---|---|---|---|
| FIN-01 | não avaliado | não avaliado | pendente | — | não avaliado | unreviewed | a definir |

Use os IDs da seção 3 e as regras de [README.md](README.md). Nenhum resultado inicial é presumido.

## 16. Limitações

As chaves verificam coerência interna de datasets sintéticos, não fatos de mercado. A aplicação ainda requer segundo avaliador para decisões de borda e revisão humana opcional por CFO/controller nos blocos financeiros. Nenhuma pontuação foi atribuída ao participante nesta versão.
