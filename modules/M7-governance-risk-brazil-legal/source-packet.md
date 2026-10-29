# M7 — Referências de apoio herdadas

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

**Data de referência:** 2026-07-23\
**Uso:** executive issue-spotting. Não é aconselhamento jurídico, tributário, trabalhista, cambial ou regulatório.

## 1. Regra de admissão

- Regra legal ou regulatória: fonte T0 oficial, `checked_at`, locator e `recheck_by`.
- Framework: fonte institucional identificada; explicitar quando voluntário ou aplicável apenas ao setor público.
- Projeto legislativo não é lei.
- Página em manutenção, inacessível ou com texto oficial não confirmado não gera conclusão.
- O output executivo é: fato → issue → implicação → pergunta → advisor → decisão/controle provisório.

## 2. Claims centrais aceitas

| Claim | Uso no módulo | Fonte | Status e limite |
|---|---|---|---|
| CLM-M7-LGPD-APPLICABILITY | Escopo, papéis, princípios, bases e direitos | SRC-BR-LGPD | Verificado com limitação de acesso; recheck 2026-07-24 |
| CLM-M7-INCIDENT-DEADLINE | Relógio de comunicação | SRC-ANPD-RCIS-15-2024 | Verificado; prazo setorial pode prevalecer |
| CLM-M7-INCIDENT-RECORD | Evidência e retenção de registro | SRC-ANPD-RCIS-15-2024 | Verificado; alinhar com retention policy e litigation hold |
| CLM-M7-TRANSFER-MECHANISMS | Fluxo internacional de dados | SRC-ANPD-TID-19-2024 | Verificado; mecanismo depende dos fatos |
| CLM-M7-SES-SC-ENFORCEMENT | Caso real de incidente e resposta regulatória | SRC-ANPD-SES-SC-SANCTION | Caso público; não extrapolar sanção para empresa privada |
| CLM-M7-THREE-LINES | Ownership de risco e assurance | SRC-CGU-THREE-LINES | Analogia; norma citada é do Executivo federal |
| CLM-M7-LTDA-REGISTRATION | Mapa de questões de estrutura local | SRC-DREI-LTDA-GUIDE | Orientação geral; não escolhe entidade |
| CLM-M7-EMPLOYMENT-TEST | Issue spotting de emprego e contractor | SRC-BR-CLT | Requer counsel e análise factual/jurisprudencial |
| CLM-M7-RTC-2026 | Transição tributária em 2026 | SRC-RFB-RTC-2026 | Resumo oficial; norma e operação controlam |
| CLM-M7-TRANSFER-PRICING | Arm's length e transações controladas | SRC-BR-TRANSFER-PRICING-14596 | Método e documentação exigem tax counsel |
| CLM-M7-TRANSFER-PRICING-REG | Regulamentação pela IN RFB nº 2.161/2023 | SRC-RFB-TRANSFER-PRICING-2161 | Guidance oficial; instrução consolidada controla |
| CLM-M7-FX-SCOPE | Pagamentos, transferências e contas de não residentes | SRC-BCB-FX-277 | Norma consolidada; confirmar fluxo com instituição autorizada |
| CLM-M7-AI-BILL-STATUS | Estado da regulação geral de IA | SRC-CAMARA-PL2338-STATUS | Volátil; `Aguardando Parecer` não é lei |
| CLM-NIST-AIRMF-CORE | Govern/Map/Measure/Manage | SRC-NIST-AI-RMF | Framework voluntário; contextualizar |
| CLM-OECD-PRINCIPLES-2023 | Board e accountability | SRC-OECD-CG-2023 | Referência internacional; direito local prevalece |

## 3. Pacote por decisão

### Board e controles

- **SRC-OECD-CG-2023:** responsabilidades, informação, accountability e governança corporativa.
- **SRC-CGU-THREE-LINES:** primeira linha opera e controla; segunda orienta e monitora; terceira fornece assurance independente. Uso por analogia.
- **Pergunta executiva:** qual assunto pertence a shareholder, board, committee, CEO/GM ou management, e qual evidência deve existir antes e depois da decisão?

### Enterprise risk e IA

- **SRC-NIST-AI-RMF:** Govern, Map, Measure e Manage; framework voluntário.
- **SRC-CAMARA-PL2338-STATUS:** em 2026-07-23 o PL 2338/2023 aguardava parecer na Câmara.
- **Pergunta executiva:** qual uso de IA tem responsável, propósito, dados, avaliação, monitoramento, human oversight, fallback e stop gatilho?

### LGPD, transferência e incidente

- **SRC-BR-LGPD:** lei compilada; usar somente os artigos indicados no manifesto e revalidar.
- **SRC-ANPD-RCIS-15-2024:** critérios cumulativos, comunicação, registro e procedimento.
- **SRC-ANPD-TID-19-2024:** mecanismos de transferência internacional e cláusulas-padrão.
- **SRC-ANPD-SES-SC-SANCTION:** falha de resposta, comunicação e evidência em caso real.
- **Pergunta executiva:** quem é controlador, operador e exportador/importador em cada fluxo; qual hipótese, mecanismo, evidência e resposta?

### Estrutura, contratos e trabalho

- **SRC-DREI-LTDA-GUIDE:** registry-level facts sobre sociedade limitada.
- **SRC-BR-CLT:** conceitos legais de empregador/empregado e relação de trabalho.
- **Pergunta executiva:** a estrutura consegue contratar, faturar, pagar, assinar, receber capital e suportar o risco; o desenho de trabalho reflete os fatos?

### Tributário, FX e intercompany

- **SRC-RFB-RTC-2026:** transição do consumo; 2026 como ano-teste.
- **SRC-BR-TRANSFER-PRICING-14596** e **SRC-RFB-TRANSFER-PRICING-2161:** arm's length e regulamentação.
- **SRC-BCB-FX-277:** escopo regulatório de câmbio e transferências.
- **Pergunta executiva:** qual entidade entrega valor, assume risco, detém ativos, assina, fatura, recebe, paga, financia e documenta?

## 4. Fronteiras de conteúdo

- M1 é proprietário de P&L, caixa e três demonstrações. M7 usa materialidade para escalonamento.
- M2 é proprietário de pricing, unit economics e capital. M7 testa implicação legal/tributária e controle.
- M3 é proprietário do decision memo. M7 define issues, approvals, evidence e advisors.
- M6 é proprietário da tese de entrada e do country P&L. M7 testa se a estrutura e os fluxos são operáveis.
- M8 é proprietário da defesa executiva. M7 fornece o board pack e os challenge points.

## 5. Limitações e escalation obrigatório

| Tema | Advisor mínimo | Gatilho |
|---|---|---|
| Estrutura, poderes, contrato ou setor regulado | Corporate/regulatory counsel | Antes de constituir, assinar, representar, licenciar ou delegar |
| LGPD, fornecedor, transferência ou titular | Privacy counsel + DPO/encarregado | Antes de go-live ou mudança material de fluxo |
| Incidente | Incident commander + DPO + privacy counsel + forensics | Imediatamente após confirmação; preservar relógio e evidência |
| Tributação do consumo ou renda | Tax counsel + contador | Antes de preço, invoice, reconhecimento ou alteração de modelo |
| Intercompany/transfer pricing | Tax counsel + finance | Antes de contrato, charge, financiamento ou fechamento |
| Trabalho/contractor/EOR | Labor counsel + People | Antes de contratar, mudar fatos ou encerrar |
| FX/capital externo | Instituição autorizada + tax/FX counsel | Antes do fluxo e do registro/reporting |
| IA | Product/AI risk + privacy + sector counsel | Antes de alto impacto, dado sensível, mudança de modelo ou uso não aprovado |

## 6. Status de acesso

- Planalto para LGPD, CLT e Lei 14.596: indexado oficialmente, mas com timeout/decoding nesta verificação. `accepted_with_limitations`; recheck obrigatório.
- ANPD RCIS, transferência internacional, CGU, DREI, Receita, BCB e Câmara API: acesso oficial verificado.
- Página do caso SES-SC: browser/search oficial disponível; curl retornou 401. Nenhum detalhe além da publicação oficial foi admitido.
