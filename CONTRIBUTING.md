# Contribuir com o OpenMBA

Comece com uma correção, um caso sintético ou um exercício com solução. Explique para quem serve e que decisão treina. Mudanças grandes de escopo devem vir com uma proposta em issue antes de reestruturar o currículo.

Cada contribuição de conteúdo deve ter:

1. Objetivo de aprendizagem e pré-requisitos.
2. Explicação e exemplo resolvido.
3. Exercício independente, dados suficientes e rubrica.
4. Alternativas aceitáveis e erros críticos.
5. Fontes primárias para claims externos, conforme [SOURCES.md](SOURCES.md).
6. Disclosure do uso de IA e do que foi conferido por pessoa.

Não inclua dados pessoais, histórias de clientes, estratégias privadas de candidatura ou material de terceiros sem permissão. Novas trilhas devem partir de objetivos e diagnóstico, sem inferir deficiência de uma profissão ou senioridade.

Antes de abrir um PR:

```sh
python scripts/validate.py
python -m unittest discover -s tests
```

Revisão automática verifica estrutura, links locais e regras do plano; não substitui revisão factual, pedagógica ou de direitos. Ao contribuir, você deve ter o direito de disponibilizar seu material sob a licença do projeto.
