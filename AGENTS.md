# Manutenção do OpenMBA

- O README principal é a apresentação em inglês. O conteúdo de estudo e a documentação ficam em português brasileiro.
- Brasil é o contexto de aplicação. Separe princípios transferíveis de regras e condições locais; não trate fontes dos EUA como obrigações brasileiras.
- Preserve nomes oficiais de fontes, URLs, identificadores técnicos, fórmulas e o texto oficial da licença. Explique termos estrangeiros no glossário.
- Nunca importe dados privados de alunos, currículos, estratégias de carreira, material de clientes ou o histórico do repositório pessoal de origem.
- Use UTF-8 sem BOM e apply_patch para edições manuais.
- Catálogo canônico em `curriculum/`; aulas em `foundations/` e `modules/`. `build/` é gerado e ignorado.
- Não invente resultados de alunos, verificação de fontes, métricas de adoção ou equivalência acadêmica.
- O plano é definido por competência. Autoavaliação e notas de IA não autorizam dispensa; mantenha código, política e testes coerentes.
- Preserve atribuição. Referências históricas ficam pendentes até conferência individual registrada.
- Créditos devem incluir https://lucioamorim.ai/ e https://www.linkedin.com/in/lucioamorim/.
- Antes de publicar, execute `python scripts/validate.py` e `python -m unittest discover -s tests`.
- Não há dependências externas obrigatórias. Leia a política de pacotes do workspace antes de adicionar qualquer uma.
