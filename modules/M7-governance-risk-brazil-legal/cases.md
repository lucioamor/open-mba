# M7 — Casos

> **Edição pública inicial.** Adaptado de material de estudo assistido por IA. Referências e locators herdados do material de julho de 2026 ainda não foram revalidados para esta edição. Trate afirmações externas como pontos a verificar, não como fatos atuais confirmados. Casos numéricos são exercícios; consulte a política de fontes em [SOURCES.md](../../SOURCES.md).

## CASE-M7-SES-SC — Caso real documentado

### Fonte e limite

Fonte oficial: **SRC-ANPD-SES-SC-SANCTION**, publicação da Agência Nacional de Proteção de Dados sobre sanção à Secretaria de Estado da Saúde de Santa Catarina.

Este caso usa somente fatos publicados pela ANPD. Não presume causa técnica, intenção, materialidade financeira, decisão de board nem resultado posterior. O órgão público está sujeito a particularidades que não podem ser transportadas para empresa privada.

### Fatos admitidos

A publicação oficial registra que:

- houve incidente de segurança;
- a comunicação aos titulares foi considerada inadequada ou intempestiva;
- a ANPD apontou issue de segurança;
- um Relatório de Impacto à Proteção de Dados Pessoais requisitado não foi apresentado;
- outras informações requisitadas não foram disponibilizadas;
- foram aplicadas advertências e medidas corretivas.

[CLM-M7-SES-SC-ENFORCEMENT; locator: findings concerning LGPD arts. 38, 48 e 49 and corrective measures]

### Questão executiva

Que sistema de governança deveria tornar detectáveis e escaláveis as quatro classes de falha: resposta ao incidente, comunicação, evidência/RIPD e atendimento à autoridade?

### Trabalho guiado — 60 minutos

Produza:

1. uma timeline apenas com fatos admitidos;
2. uma lista `known / unknown / must verify`;
3. cinco failure modes de governança;
4. um control map preventivo/detectivo/corretivo;
5. um escalation path;
6. um board update de uma página;
7. uma lista de documentos que deveriam ser preservados;
8. um after-action review sem atribuir culpa não documentada.

### Questionamento

- Qual falha é de design e qual é de execução?
- Qual evidência provaria que um controle existia e operava?
- Quem pode aceitar risco residual?
- Como manter segredo técnico sem omitir fato material?
- Que aprendizado não pode ser inferido deste caso público?

### Critério de qualidade

A resposta forte não estima multa, não inventa causa e não afirma que a empresa privada receberia a mesma sanção. Ela mostra sistema, responsável, evidence e escalation.

---

## CASE-M7-ORBE-INCIDENT — CENÁRIO SINTÉTICO

Todo o conteúdo abaixo é fictício. A Orbe AI não representa Lovable, Anthropic, OpenAI nem qualquer empresa real.

### Contexto

Orbe AI, Inc. é uma empresa fictícia estrangeira de software. Ela vende um workspace de IA para equipes de atendimento. O board realizará reunião extraordinária em 24 horas.

O country lead pede autorização para:

1. manter o lançamento de um assistente de tickets;
2. escolher estrutura operacional para os próximos 12 meses;
3. contratar equipe local;
4. financiar a operação brasileira;
5. responder a um incidente confirmado em fornecedor.

### Anexo A — Desempenho

- previsão trimestral: USD 2,50 milhões;
- previsão revisado: USD 2,05 milhões;
- miss: `2,50 − 2,05 = USD 0,45 milhão`;
- miss percentual: `0,45 / 2,50 = 18%`;
- runway global: não informado ao aluno;
- dois contratos enterprise dependem da feature de IA;
- HQ quer manter a data pública de lançamento.

### Anexo B — Incidente

- fornecedor de suporte confirmou acesso não autorizado na segunda-feira às 09:00;
- export de tickets contém até 18.400 registros;
- os campos possíveis incluem nome, e-mail, texto livre do ticket e ID de conta;
- não há confirmação sobre exfiltração total;
- parte dos tickets pode conter dado inserido livremente por usuário;
- logs brutos existem, mas a retenção padrão do fornecedor é de sete dias;
- o fornecedor afirma que “investiga” e não forneceu lista de subprocessors;
- a Orbe não localizou data-processing addendum assinado;
- customer support quer avisar todos imediatamente;
- sales quer esperar para não afetar as duas renovações.

### Anexo C — IA e produto

- o assistente resume tickets e sugere resposta;
- treinamento usa dados sintéticos, segundo Product, mas a afirmação ainda não foi documentada;
- prompts de produção passam por API de terceiro;
- região de processamento não foi confirmada;
- há revisão humana opcional;
- não existe kill switch por tenant;
- teste mostrou duas respostas com referência a conta errada em 2.000 execuções;
- Product propõe aceitar o risco por 30 dias.

### Anexo D — Pessoas

- 14 pessoas trabalham no Brasil;
- seis estão em EOR;
- oito são pessoas jurídicas contratadas diretamente por HQ;
- os oito contractors têm metas semanais, gestor de HQ, acesso a sistemas, reuniões diárias e bônus por performance;
- não existe people-facts review por labor counsel;
- HQ quer contratar mais cinco pessoas no mesmo desenho.

### Anexo E — Estrutura e contratos

- clientes assinam com a entidade estrangeira;
- parte paga em USD por wire; parte paga em BRL via intermediário;
- country lead negocia descontos, mas sua autoridade de assinatura não está documentada;
- parceiro local pediu exclusividade e direito de revenda;
- não há matriz de reserved matters;
- não há entidade brasileira;
- DREI, tax e corporate counsel ainda não receberam facts pack.

### Anexo F — Operações entre empresas do grupo, tributos e câmbio

- HQ pretende enviar USD 1 milhão para “Brazil operations”;
- não há entidade destinatária nem contrato de financiamento;
- custos locais são reembolsados por expense reports;
- não há intercompany agreement;
- pricing e invoice não foram revisitados para a transição tributária de 2026;
- finance não mapeou finalidade cambial, retenções ou evidência contábil;
- um executivo sugeriu dividir o fluxo em parcelas “para simplificar”.

### Anexo G — Informação imperfeita

Não estão disponíveis:

- conteúdo final dos logs;
- país/região de todos os subprocessors;
- opinião jurídica;
- tratamento tributário;
- análise trabalhista;
- classificação setorial dos clientes;
- decisão sobre notificabilidade;
- runway;
- ata de approval anterior.

O aluno não pode preencher essas lacunas com suposição.

### Decisões exigidas

1. Continuar, condicionar ou interromper o lançamento?
2. Que ação de incidente ocorre nas próximas 24 horas?
3. Que estrutura entra em diligence e qual bridge provisório é aceitável?
4. Que contratações ficam bloqueadas?
5. Que fluxo de financiamento fica bloqueado?
6. Que assuntos sobem ao board e quais ficam com management?
7. Que advisors são acionados, com quais perguntas?
8. O que comunicar internamente, a clientes e externamente — e quem decide?

### Entregáveis

- board memo de duas páginas;
- registro de riscos com oito riscos;
- control map;
- incident decision log;
- data/vendor map;
- structure options matrix;
- people-facts sheet;
- flow-of-funds map;
- advisor brief;
- compliance roadmap 30/60/90.

### Restrições

- não emitir conclusão jurídica;
- não afirmar que o PL 2338/2023 é lei;
- não concluir notificabilidade sem análise;
- não dividir pagamentos para evitar processo;
- não chamar revisão humana opcional de controle efetivo sem teste;
- não aprovar novo contractor sem facts review;
- não inventar informação ausente;
- toda regra externa deve apontar fonte e locator.

### Questionamento oral

O avaliador escolherá três:

1. “O incidente ainda não está quantificado; por que envolver o board?”
2. “Se o vendor assume responsabilidade, por que parar?”
3. “O PL de IA ainda não virou lei; por que criar controles?”
4. “O country lead precisa de autonomia; por que exigir delegation matrix?”
5. “Por que não enviar o financiamento agora e documentar depois?”
6. “Contractors aceitaram o contrato; qual é o issue?”
7. “Qual controle você removeria se o prazo cair pela metade?”
8. “Qual decisão é reversível e qual cria lock-in?”

---

## ASSESS-M7-FORM-B — CENÁRIO SINTÉTICO DE RETEST

Todo o conteúdo abaixo é fictício. Vela Grid não representa empresa real. Esta forma é reservada ao retest e não pode ser usada como prática.

**Pacote regulatório fechado:** as of 2026-07-23. Regras legais/regulatórias devem citar T0 deste módulo: SRC-BR-LGPD, SRC-ANPD-RCIS-15-2024, SRC-ANPD-TID-19-2024, SRC-DREI-LTDA-GUIDE, SRC-BR-CLT, SRC-RFB-RTC-2026, SRC-BR-TRANSFER-PRICING-14596, SRC-RFB-TRANSFER-PRICING-2161, SRC-BCB-FX-277 e SRC-CAMARA-PL2338-STATUS. NIST é framework voluntário. O avaliador atualiza somente o status volátil antes de aplicar.

### Contexto independente

Vela Grid, Inc. vende analytics e recomendação de contratação para operadores de logística. Considera adquirir 40% de um parceiro brasileiro e conceder-lhe exclusividade comercial. Um diretor da Vela investiu pessoalmente em fundo que detém participação no parceiro, mas ainda não registrou conflito.

### Dados B

- orçamento anual da operação: USD 4,00 milhões;
- gasto revisado: USD 5,08 milhões;
- overrun: `5,08 − 4,00 = USD 1,08 milhão`, ou `1,08 / 4,00 = 27%`;
- o parceiro recebe currículo, avaliação e histórico de candidatos;
- um bucket de teste com 9.600 perfis ficou acessível por link público durante seis horas;
- o acesso foi confirmado; download por terceiros ainda está em apuração;
- security desativou o link, mas não preservou cópia integral do access log;
- o modelo recomenda shortlist e o recruiter pode aceitar sem justificar;
- não há teste documentado por subgrupo nem appeal path;
- contrato com o parceiro não define papéis de dados, subprocessor, transferência, auditoria ou retorno/deleção;
- a Vela pretende cobrar royalty de IP e management fee da futura sociedade;
- não há functional analysis nem intercompany agreements;
- o financiamento seria em EUR, embora orçamento, contrato comercial e contabilidade usem moedas diferentes;
- 22 trabalhadores locais seriam transferidos do parceiro; não há labor due diligence;
- a reunião de board ocorre em 36 horas.

### Decisões

1. Suspender, condicionar ou continuar a feature de recomendação?
2. Como operar o incidente e a lacuna de logs?
3. Como tratar o conflito do diretor?
4. Que diligence precede aquisição, exclusividade e transferência de trabalhadores?
5. Que facts pack precede royalty, management fee e financiamento?
6. Que decisões pertencem ao board, committee ou management?

### Entregáveis

Novo board memo, registro de riscos, control map, incident log, structure/JV map, people-facts sheet, data-flow, intercompany/FX map e advisor brief.

### Regra de independência

- arquivo novo, não revisão da Form A;
- dataset e decision memo novos;
- mesmos resultados e rubrica K45/J55;
- proibição de IA generativa;
- nenhuma resposta da Orbe pode ser copiada sem adaptação factual.
- erro crítico ocorrido na Form B reprova o retest e não pode ser compensado por ponto ou trecho aprovado da Form A.
