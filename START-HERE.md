# Comece pelo seu objetivo

Este programa é para brasileiros e usa português brasileiro. Princípios de gestão são aplicados ao nosso contexto; casos internacionais aparecem para comparação, sem substituir regras locais. Consulte [idioma e contexto brasileiro](docs/BRASIL-E-IDIOMA.md) e o [glossário](docs/GLOSSARIO.md) quando encontrar termos técnicos.

## 1. Defina uma decisão que você precisa aprender a tomar

Escolha uma destas trilhas iniciais:

- **builder:** transformar capacidade técnica em um negócio e um produto usados.
- **founder:** validar cliente, oferta, distribuição e sustentabilidade econômica.
- **functional-lead:** assumir uma área, orçamento, processos e pessoas.
- **general-manager:** integrar estratégia, P&L, organização, expansão e risco.
- **explorer:** explorar o currículo inteiro e escolher um objetivo depois.

Essas trilhas são pontos de partida. O título do seu cargo não determina a rota. Se a meta for trabalhar em outro setor ou país, revise a aplicabilidade dos casos.

## 2. Faça um mapa de entrada de 20–30 minutos

Copie o [perfil vazio](templates/learner-profile.json) para `learner/profile.json`. Informe objetivo, horas semanais e uma decisão real ou sintética que gostaria de enfrentar. Não envie dados de clientes, contratos, senhas ou documentos de trabalho para o repositório ou para uma IA.

Para cada domínio relevante, escreva em suas notas privadas: o que você sabe explicar, o que sabe fazer e o que consegue documentar. Não converta confiança em nota. Deixe `assessments` vazio até haver resultados.

```sh
python scripts/plan.py --profile learner/profile.json --output learner/plan.md
```

Sem notas, o plano recomenda estudar ou fazer a avaliação de entrada. Isso significa **não avaliado**, não incapaz.

## 3. Teste o que já domina

Use [diagnostic/README.md](diagnostic/README.md). Faça apenas as avaliações relevantes ao objetivo. Você pode estudar diretamente se preferir não investir tempo em avaliação para dispensa. O plano não força uma prova de 13 horas para começar.

Cargo e tempo de experiência ajudam a escolher exemplos, mas não dispensam competências. Um engenheiro pode demonstrar domínio de dados e precisar estudar aquisição; uma pessoa de vendas pode demonstrar o inverso. Um executivo experiente também pode encontrar lacunas pontuais.

## 4. Estude em ciclos

1. Escolha uma decisão e leia a lição correspondente.
2. Explique o conceito com suas próprias palavras.
3. Resolva o exercício sem IA nem gabarito.
4. Defenda a escolha: alternativa rejeitada, risco, responsável e gatilho de revisão.
5. Corrija e refaça com dados diferentes.
6. Registre o que mudou no [log de aprendizagem](templates/learning-log.md).

Uma sessão de 45 minutos pode ter 15 minutos de leitura, 20 de prática e 10 de revisão. Ajuste conforme cálculo, acessibilidade e dificuldade. Não trate o tempo de leitura como carga horária do programa.

## 5. Integre e aplique

Conclua o [capstone](capstone/brief.md) da sua trilha. Depois, se houver acesso e autorização, faça um [projeto de campo](capstone/field-practicum.md). Quem está em transição de carreira pode praticar com um projeto próprio pequeno ou voluntário, sem inventar responsabilidade executiva.

O currículo pode ser usado inteiramente em Markdown. O [tutor](prompts/tutor.md) é opcional, assim como sessões por voz, um colega de estudo ou um mentor.
