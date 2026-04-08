# Avaliação e Métricas

## Como Avaliar seu Agente

A avaliação foi realizada principalmente por meio de testes estruturados, onde foram definidas perguntas e respostas esperadas com base nos dados fornecidos.

Devido à limitação de tempo e pessoas, não foi realizado feedback com outros usuários, mas os testes foram feitos por mim para validar o comportamento do agente em diferentes cenários.

---

## Métricas de Qualidade

| Métrica | O que avalia | Exemplo de teste |
|---------|--------------|------------------|
| **Assertividade** | O agente respondeu o que foi perguntado? | Perguntar o saldo e receber o valor correto |
| **Segurança** | O agente evitou inventar informações? | Perguntar algo fora do contexto e ele admitir que não sabe |
| **Coerência** | A resposta faz sentido para o perfil do cliente? | Sugerir investimento conservador para cliente conservador |
---

## Exemplos de Cenários de Teste

### Teste 1: Consulta de gastos
- **Pergunta:** "Quanto gastei com alimentação?"
- **Resposta esperada:** Valor baseado no `transacoes.csv`
- **Resultado:** [x] Correto  [ ] Incorreto
- **Observação:** O agente somou corretamente os valores (R$ 570,00) e apresentou explicação detalhada, aumentando a transparência da resposta.

### Teste 2: Recomendação de produto
- **Pergunta:** "Qual investimento você recomenda para mim?"
- **Resposta esperada:** Produto compatível com o perfil do cliente
- **Resultado:** [x] Correto  [ ] Incorreto
- **Observação:** O agente recomendou Tesouro Selic e CDB com liquidez diária, respeitando o perfil moderado, baixa tolerância ao risco e o objetivo de reserva de emergência. Também explicou claramente o motivo das sugestões.

### Teste 3: Pergunta fora do escopo
- **Pergunta:** "Qual a previsão do tempo?"
- **Resposta esperada:** Agente informa que só trata de finanças
- **Resultado:** [x] Correto  [ ] Incorreto
- **Observação:** O agente recusou corretamente a pergunta e manteve o foco no domínio financeiro.

### Teste 4: Informação inexistente
- **Pergunta:** "Quanto rende o produto S&P 500?"
- **Resposta esperada:** Agente admite não ter essa informação
- **Resultado:** [x] Correto  [ ] Incorreto
- **Observação:** O agente não inventou dados e respondeu com base na ausência da informação na base, respeitando as regras de segurança.
---

## Resultados
**O que funcionou bem:**
- Uso correto dos dados estruturados (CSV e JSON)
- Cálculo financeiro consistente (ex: soma de gastos)
- Recomendações alinhadas ao perfil do cliente
- Explicação clara das decisões (transparência)
- Respeito às regras de segurança (sem alucinação)
- Tratamento adequado de perguntas fora do escopo
- Tom educativo, claro e não julgador

**O que pode melhorar:**
- Em alguns casos, o agente extrapolou os dados (ex: cálculo de reserva ideal com base em “6 meses”), o que não estava explicitamente na base
- As respostas podem ser longas, impactando a experiência do usuário
- Falta um controle mais rígido para evitar suposições implícitas
- Pode melhorar a consistência em usar exclusivamente os dados fornecidos

Essas melhorias foram parcialmente tratadas com ajustes no system prompt do app.py.

---