# M7 — Fontes, locators e direitos

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

**Checked at:** 2026-07-23\
**Policy:** regras legais/regulatórias usam T0 oficial. O catálogo público está em `sources/catalog.json`; a política vigente está em `SOURCES.md`.

## Fontes essenciais

### Governança e controles

#### SRC-OECD-CG-2023 — G20/OECD Principles of Corporate Governance 2023

- URL: https://www.oecd.org/corporate/principles-corporate-governance/
- Tier/type: T2 / institutional synthesis.
- Locator: publication landing page and board responsibilities.
- Uso: board, accountability e informação.
- Limite: referência internacional; direito brasileiro e documentos societários controlam.
- Direitos: termos OECD aplicáveis ao item; atribuição obrigatória.

#### SRC-CGU-THREE-LINES — Sistema de Controle Interno

- URL: https://www.gov.br/cgu/pt-br/assuntos/auditoria-e-fiscalizacao/sistema-de-controle-interno
- Tier/type: T0 / official guidance.
- Locator: itens 1–3 sob IN MP/CGU nº 01/2016.
- Claim: CLM-M7-THREE-LINES.
- Uso: analogia de primeira, segunda e terceira linha.
- Limite: a norma citada rege o Executivo federal, não empresa privada.
- Direitos: CC BY-ND 3.0; atribuir e não apresentar adaptação como texto oficial.

### IA

#### SRC-NIST-AI-RMF — Artificial Intelligence Risk Management Framework

- URL: https://www.nist.gov/itl/ai-risk-management-framework
- Tier/type: T0 / official guidance.
- Locator: AI RMF Core — Govern, Map, Measure, Manage.
- Claim: CLM-NIST-AIRMF-CORE.
- Uso: inventário, risk mapping, evaluation, monitoring e response.
- Limite: voluntário e geral; não é safe harbor.
- Direitos: NIST-authored technical content; conferir elementos de terceiros.

#### SRC-CAMARA-PL2338-STATUS — PL 2338/2023

- URL: https://dadosabertos.camara.leg.br/api/v2/proposicoes/2487262
- Tier/type: T0 / official legislative data.
- Locator: `statusProposicao.descricaoSituacao` e `dataHora`.
- Claim: CLM-M7-AI-BILL-STATUS.
- Estado verificado: `Aguardando Parecer`, as of 2026-07-23.
- Limite: projeto não é lei; status volátil.
- Recheck: 2026-08-22 e imediatamente antes do build.

### LGPD, transferência e incidente

#### SRC-BR-LGPD — Lei nº 13.709/2018

- URL: https://www.planalto.gov.br/ccivil_03/_ato2015-2018/2018/lei/l13709compilado.htm
- Tier/type: T0 / law.
- Locator: arts. 1, 5, 6, 7, 11, 18, 33–36, 37 e 46–50.
- Claim: CLM-M7-LGPD-APPLICABILITY.
- Limite: Planalto apresentou timeout/decoding nesta verificação; DOU controla.
- Recheck: 2026-07-24.
- Direitos: texto legal oficial; citar lei/artigo, sem snapshot nesta execução.

#### SRC-ANPD-RCIS-15-2024 — Comunicação de Incidente de Segurança

- URL: https://www.gov.br/anpd/pt-br/canais_atendimento/agente-de-tratamento/comunicado-de-incidente-de-seguranca-cis
- Tier/type: T0 / regulation and official operational guidance.
- Locator: FAQ e arts. 6, 9, 16 e 17 da Resolução CD/ANPD nº 15/2024.
- Claims: CLM-M7-INCIDENT-DEADLINE; CLM-M7-INCIDENT-RECORD.
- Limite: prazo setorial específico pode prevalecer.
- Recheck: 2026-07-24.
- Direitos: CC BY-ND 3.0; DOU controla.

#### SRC-ANPD-TID-19-2024 — Transferência Internacional de Dados

- URL: https://www.gov.br/anpd/pt-br/acesso-a-informacao/institucional/atos-normativos/regulamentacoes_anpd/resolucao-cd-anpd-no-19-de-23-de-agosto-de-2024
- Tier/type: T0 / regulation.
- Locator: arts. 1–2, 7–9, 10–33 e Anexo II.
- Claim: CLM-M7-TRANSFER-MECHANISMS.
- Limite: página registra retificação de 2025-08-18; texto atual controla.
- Recheck: 2026-07-24.
- Direitos: CC BY-ND 3.0; atribuir.

#### SRC-ANPD-SES-SC-SANCTION — Caso SES-SC

- URL: https://www.gov.br/anpd/pt-br/assuntos/noticias/anpd-sanciona-mais-um-orgao-publico
- Tier/type: T0 / official enforcement communication.
- Locator: achados ligados aos arts. 38, 48 e 49 e medidas corretivas.
- Claim: CLM-M7-SES-SC-ENFORCEMENT.
- Limite: browser/search oficial disponível; curl 401. Não extrapolar para empresa privada.
- Direitos: CC BY-ND 3.0; usar resumo factual curto.

### Estrutura e trabalho

#### SRC-DREI-LTDA-GUIDE — Sociedade Limitada

- URL: https://www.gov.br/empresas-e-negocios/pt-br/drei/orientacoes-de-abertura/tipos-de-pessoas-juridicas
- Tier/type: T0 / official guidance.
- Locator: heading `Sociedade Limitada`.
- Claim: CLM-M7-LTDA-REGISTRATION.
- Limite: orientação registral geral; não seleciona estrutura.
- Recheck: 2026-07-24.
- Direitos: CC BY-ND 3.0.

#### SRC-BR-CLT — Decreto-Lei nº 5.452/1943

- URL: https://www.planalto.gov.br/ccivil_03/decreto-lei/del5452compilado.htm
- Tier/type: T0 / law.
- Locator: arts. 2, 3, 6, 442 e 442-B.
- Claim: CLM-M7-EMPLOYMENT-TEST.
- Limite: Planalto apresentou timeout/decoding; classificação exige fatos, instrumento coletivo e jurisprudência atual.
- Recheck: 2026-07-24.
- Direitos: texto legal oficial; sem snapshot.

### Tributário, FX e intercompany

#### SRC-RFB-RTC-2026 — Reforma Tributária do Consumo

- URL: https://www.gov.br/receitafederal/pt-br/acesso-a-informacao/acoes-e-programas/programas-e-atividades/reforma-tributaria-do-consumo/entenda
- Tier/type: T0 / official guidance.
- Locator: `Transição — 2026`; página atualizada em 2026-07-03.
- Claim: CLM-M7-RTC-2026.
- Limite: resumo; LC 214/2025, LC 227/2026 e atos implementadores controlam.
- Recheck: 2026-07-24.
- Direitos: CC BY-ND 3.0.

#### SRC-BR-TRANSFER-PRICING-14596 — Lei nº 14.596/2023

- URL: https://www.planalto.gov.br/ccivil_03/_ato2023-2026/2023/lei/l14596.htm
- Tier/type: T0 / law.
- Locator: arts. 1–3; arm's length e transações controladas.
- Claim: CLM-M7-TRANSFER-PRICING.
- Limite: Planalto apresentou timeout/decoding; método e documentação exigem tax counsel.
- Recheck: 2026-07-24.
- Direitos: texto legal oficial; sem snapshot.

#### SRC-RFB-TRANSFER-PRICING-2161 — IN RFB nº 2.161/2023

- URL: https://www.gov.br/receitafederal/pt-br/assuntos/noticias/2023/setembro/receita-federal-edita-novas-regras-para-tributacao-de-multinacionais-com-presenca-no-pais
- Tier/type: T0 / official guidance.
- Locator: scope and application of IN RFB nº 2.161/2023.
- Claim: CLM-M7-TRANSFER-PRICING-REG.
- Limite: página explicativa; instrução consolidada e fatos controlam.
- Recheck: 2026-07-24.
- Direitos: CC BY-ND 3.0.

#### SRC-BCB-FX-277 — Resolução BCB nº 277/2022

- URL: https://www.bcb.gov.br/estabilidadefinanceira/exibenormativo?tipo=Resolu%C3%A7%C3%A3o%20BCB&numero=277
- Tier/type: T0 / regulation.
- Locator: art. 1; versão consolidada atualizada em 2026-06-23.
- Claim: CLM-M7-FX-SCOPE.
- Limite: confirmar finalidade, documentação e reporting com instituição autorizada e advisors.
- Recheck: 2026-07-24.
- Direitos: norma oficial; citação curta.

## Direitos e integridade

- Nenhuma fonte com proibição de ingestão foi copiada para o módulo.
- Não houve bypass de login, paywall, robots ou restrição.
- Snapshots não foram persistidos.
- Conteúdo gov.br é usado sob o aviso CC BY-ND 3.0; paráfrases do módulo não são apresentadas como texto oficial.
- Textos do Planalto são citados por lei/artigo e exigem recheck por instabilidade de acesso.
- Claims legais/regulatórias expiram no `recheck_by`.

## Escalonamento

Corporate, privacy, labor, tax, FX, sector e AI counsel devem trabalhar sobre fatos e documentos atuais. Este módulo fornece issues e perguntas; advisors fornecem advice.
