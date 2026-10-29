# OpenMBA

**Aprenda a construir, operar e decidir sobre negócios de tecnologia.**

Um currículo aberto em português, com fundamentos, casos, exercícios, arguição e trilhas que partem do que você precisa aprender. Criado por Lucio Amorim.

Você pode chegar como profissional técnico, fundador, líder funcional ou gestor experiente. O programa não presume que todos tenham as mesmas lacunas. Objetivo define relevância; avaliação define profundidade; experiência real é registrada separadamente.

**[Comece aqui](START-HERE.md)** · [Currículo](CURRICULUM.md) · [Diagnóstico](diagnostic/README.md) · [Trilhas](tracks/README.md) · [Estudar com IA](prompts/tutor.md) · [Contribuir](CONTRIBUTING.md)

Se prefere áudio, voz ou grupo de estudo, veja as [formas de estudar](docs/STUDY-MODES.md).

## O que você encontra

- Quatro módulos introdutórios: negócio, cliente, growth e produto/dados.
- Oito módulos avançados: finanças, unit economics, estratégia, operação, pessoas, expansão, risco e comunicação.
- Casos sintéticos, análises de fontes públicas, exercícios, gabaritos e templates.
- Um diagnóstico por competência, com regras transparentes para estudar, comprimir ou dispensar conteúdo.
- Um capstone ajustável ao objetivo e um protocolo de prática no mundo real.
- Prompts portáveis para tutor, examinador e parceiro de decisão; nenhum serviço pago é obrigatório.

## Experimente em 30 minutos

Abra [F1 — Fundamentos de negócio](foundations/F1-business.md), resolva o caso sem olhar a resposta e escreva a decisão em cinco linhas. Depois compare com a rubrica. Para adaptar o restante, siga o [guia de entrada](START-HERE.md).

## Três dimensões diferentes

| Dimensão | O que observar | Como desenvolver |
|---|---|---|
| K — conhecimento | Você calcula e explica? | Aulas, exercícios e provas |
| J — julgamento | Você escolhe, explicita renúncias e revê decisões? | Casos, memos e defesa |
| P — prática documentada | Você já fez isso com responsabilidade real? | Trabalho, projeto real e revisão de evidências |

Simulação pode desenvolver K e J. Não comprova P. O projeto não concede diploma, certificação profissional ou equivalência acadêmica a um MBA.

## Estado da edição

**v0.1.0 — edição inicial, 29 de outubro de 2026.** O núcleo avançado foi adaptado de um programa pessoal; os fundamentos são uma introdução, com menor profundidade. Esta é uma proposta curricular para negócios de tecnologia e IA, com casos brasileiros, não uma cobertura completa de todas as áreas de administração.

O método de roteamento e seus limiares são convenções do projeto, ainda sem validação pedagógica externa. Notas de IA são sugestões para revisão. As referências herdadas têm revisão pública pendente: veja [fontes e limites](SOURCES.md), [proveniência](docs/MIGRATION.md) e [roadmap](ROADMAP.md).

## Usar localmente

A leitura exige apenas um navegador. Para gerar um plano ou verificar o projeto, use Python 3.11+ sem dependências externas:

```sh
python scripts/plan.py --profile examples/technical-builder.json
python scripts/validate.py
python -m unittest discover -s tests
python scripts/build.py
```

O plano vai para a saída do terminal. Para salvar um plano pessoal, use `--output learner/plan.md`. A pasta `learner/` é ignorada pelo Git; revise seus arquivos antes de qualquer publicação.

## Licença

Textos autorais, adaptações autorais e código deste repositório estão sob [Apache-2.0](LICENSE). Fontes externas, marcas e materiais apenas referenciados conservam seus próprios direitos. Não há afiliação ou endosso das empresas citadas. Consulte [SOURCES.md](SOURCES.md).

## Authorship and maintenance

This project was created by [Lucio Amorim](https://linkedin.com/in/lucioamorim).

When reusing, redistributing, or citing this work, keep the attribution credits and include a link to this repository.
