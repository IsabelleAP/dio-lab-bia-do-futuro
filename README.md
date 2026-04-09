# 🤖 GRIOF — Gestão Responsável de Investimento e Organização Financeira

Agente financeiro inteligente desenvolvido como solução para o desafio **BIA do Futuro** da [DIO](https://www.dio.me/). O GRIOF atua como um mentor financeiro proativo, ajudando clientes a organizar suas finanças, identificar padrões de gastos e planejar metas com base em seus próprios dados.

---

## O Problema

Muitas pessoas enfrentam instabilidade financeira não por falta de renda, mas por desorganização e ausência de planejamento. O GRIOF resolve isso de forma acessível e personalizada.

---

## O Agente

| Atributo | Descrição |
|---|---|
| **Nome** | GRIOF |
| **Sigla** | Gestão Responsável de Investimento e Organização Financeira |
| **Tom** | Informal, educativo, direto e não julgador |
| **Tecnologia** | LLM via Ollama + interface Streamlit |
| **Base de dados** | CSV e JSON mockados com dados do cliente |

### O que o GRIOF faz

- Analisa padrões de gastos e classifica despesas
- Sugere ajustes práticos no orçamento mensal
- Apoia o planejamento de metas financeiras
- Indica produtos compatíveis com o perfil do cliente
- Admite limitações e evita respostas fora do seu escopo

### O que o GRIOF **não** faz

- Não acessa dados bancários reais
- Não faz previsões de mercado
- Não substitui um consultor financeiro profissional
- Não responde perguntas fora do contexto financeiro

---

## Arquitetura

```
Cliente → Interface (Streamlit) → LLM (Ollama) → Base de Conhecimento (CSV/JSON)
                                       ↓
                              Validação & Resposta
```

---

## Estrutura do Repositório

```
📁 dio-lab-bia-do-futuro/
├── 📁 data/                      # Dados mockados do cliente
│   ├── transacoes.csv
│   ├── historico_atendimento.csv
│   ├── perfil_investidor.json
│   └── produtos_financeiros.json
├── 📁 docs/                      # Documentação completa
│   ├── 01-documentacao-agente.md
│   ├── 02-base-conhecimento.md
│   ├── 03-prompts.md
│   ├── 04-metricas.md
│   └── 05-pitch.md
├── 📁 src/
│   └── app.py                    # Aplicação Streamlit
└── 📁 assets/
```

---

## Segurança e Anti-Alucinação

O GRIOF responde **exclusivamente com base nos dados fornecidos**. Quando não há informação disponível, declara a limitação abertamente. Recomendações fora do perfil do cliente são bloqueadas por design no system prompt.

---

## Stack

`Python` · `Streamlit` · `Ollama` · `Prompting com few-shot`

---

## Documentação

| Doc | Conteúdo |
|---|---|
| [01 — Agente](./docs/01-documentacao-agente.md) | Caso de uso, persona e arquitetura |
| [02 — Base de Conhecimento](./docs/02-base-conhecimento.md) | Estratégia de dados |
| [03 — Prompts](./docs/03-prompts.md) | System prompt, exemplos e edge cases |
| [04 — Métricas](./docs/04-metricas.md) | Avaliação da qualidade do agente |
| [05 — Pitch](./docs/05-pitch.md) | Roteiro de apresentação |


---

*Desenvolvido por [Isabelle AP](https://github.com/IsabelleAP) · Desafio BIA do Futuro — DIO*