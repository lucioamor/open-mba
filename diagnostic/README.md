# Diagnóstico por competência

## Objetivo

Escolher o que estudar sem pressupor as lacunas do autor ou do aluno. O diagnóstico é educacional e não é seleção de emprego nem certificação.

O mapa inicial é qualitativo. Uma avaliação formal exige resposta produzida pelo participante, identificação do exercício e registro da revisão. Para fundamentos, use os casos F1–F4. Para o núcleo, use o avaliação para dispensa da seção 3 e a avaliação do `module.md`, os exercícios do `workbook.md` e os gabaritos depois da tentativa. Os [instrumentos avançados](advanced-assessments.md) e suas [rubricas](advanced-rubrics.md) servem como opção integrada.

Nos instrumentos avançados, o instrumento A pessoal foi excluído. Para documentar experiência, use [evidence-record.md](../templates/evidence-record.md), sem lista obrigatória de empregadores ou projetos.

## K, J e P

- **K:** cálculo, explicação e identificação de limites, 0–100.
- **J:** escolha, renúncia, risco, consequência, responsável e revisão, 0–100.
- **P:** `unreviewed`, `absent`, `documented` ou `reviewed`. Registro de prática real; não é uma nota.

Uma nota de IA ou autoavaliação é provisória. Para dispensar conteúdo, o projeto exige revisão humana dos exercícios, sem gabarito aberto durante a tentativa. Essa revisão é uma convenção de estudo entre pares/mentores, não acreditação.

## Regras públicas de roteamento — v0.1

Estas regras prevalecem sobre referências legadas a M0 ou placement nos módulos adaptados. Os limiares são escolhas de desenho, ainda sem validação externa.

| Condição por competência | Rota |
|---|---|
| Sem avaliação humana registrada | STUDY_OR_ASSESS: estudar ou avaliar |
| Erro crítico/fatal | DEEP: estudar e refazer |
| K ≥ 85, J ≥ 80, dois casos independentes, tentativa sem ajuda, revisão humana identificada | SKIP: dispensar instrução, mantendo aplicação no capstone |
| K ≥ 70, J ≥ 70, ao menos um caso, tentativa sem ajuda, revisão humana identificada | COMPRESS: revisão e caso novo |
| Demais resultados humanos | DEEP |

A rota considera cada competência. A média do módulo não dispensa uma lacuna local. No plano agregado, a competência menos demonstrada determina o esforço do módulo, sem apagar os resultados individuais. `COMPRESS` estima metade do tempo; `SKIP` não adiciona horas de instrução. Prática real é uma recomendação separada e nunca muda a rota de conhecimento automaticamente.

## Registro

No perfil JSON, registre uma entrada por ID do [catálogo](../curriculum/competencies.json):

```json
{
  "FIN-01": {
    "k": 88,
    "j": 82,
    "independent_cases": 2,
    "unassisted": true,
    "fatal_error": false,
    "review_type": "human",
    "reviewer": "mentor ou par identificado nas notas privadas",
    "assessment_ref": "exercício e data nas notas privadas",
    "proof": "unreviewed"
  }
}
```

O script verifica consistência e aplica regras ao registro fornecido; ele não comprova a identidade do avaliador ou a autenticidade dos exercícios. Não publique nomes ou evidências sem autorização. Para outra tentativa, preserve o histórico em notas privadas e atualize o resultado vigente. Use dados diferentes no reteste.

Necessidades de acessibilidade e idioma devem ser combinadas antes. Avalie a decisão e o raciocínio; velocidade de fala, sotaque e acesso a um cargo não são competências medidas aqui.

## Autoria e manutenção

Este projeto foi criado por [Lucio Amorim](https://lucioamorim.ai/). Conheça também seu [LinkedIn](https://www.linkedin.com/in/lucioamorim/).

Ao reutilizar, redistribuir ou citar este trabalho, preserve os créditos e inclua um link para este repositório.
