# Base de Conhecimento

## Dados Utilizados

Descreva se usou os arquivos da pasta `data`, por exemplo:

| Arquivo | Formato | Utilização no Agente |
|---------|---------|---------------------|
| `historico_atendimento.csv` | CSV | Contextualiza interações anteriores, permitindo respostas mais consistentes e alinhadas ao histórico do cliente. |
| `perfil_investidor.json` | JSON | Define perfil do cliente, metas financeiras, tolerância a risco e patrimônio, sendo utilizado para personalização das recomendações. |
| `produtos_financeiros.json` | JSON | Lista produtos financeiros disponíveis, permitindo sugestões compatíveis com o perfil e objetivos do cliente. |
| `transacoes.csv` | CSV | Permite análise do padrão de gastos, identificação de despesas recorrentes e organização do orçamento. |

---

## Adaptações nos Dados

> Você modificou ou expandiu os dados mockados? Descreva aqui.

[
* Inclusão de novos produtos financeiros:
Debêntures Incentivadas (renda fixa, risco médio, IPCA + 5%, aporte mínimo de R$ 1.000)
ETF Ibovespa (renda variável, alto risco, aporte mínimo de R$ 50)
* Expansão do histórico de transações:
Adição de registros entre 2025-10-26 e 2025-11-25
Inclusão de diferentes categorias (lazer, alimentação, transporte, investimento e receitas)
Manutenção da padronização das categorias para permitir análise automatizada ]

---

## Estratégia de Integração

### Como os dados são carregados?
> Descreva como seu agente acessa a base de conhecimento.

[Os arquivos JSON e CSV são carregados no início da execução da aplicação utilizando Python (pandas e json).

Após o carregamento, os dados são estruturados e inseridos diretamente no contexto enviado ao modelo de linguagem.]

### Como os dados são usados no prompt?
> Os dados vão no system prompt? São consultados dinamicamente?

[Os dados são incorporados dinamicamente no prompt a cada interação do usuário.

O contexto inclui:

* Informações do perfil do cliente
* Histórico de transações
* Interações anteriores
* Lista de produtos financeiros disponíveis

O modelo utiliza esse contexto para gerar respostas personalizadas, garantindo que:

* As recomendações sejam baseadas em dados reais
* As análises estejam alinhadas com o comportamento financeiro do cliente
* As sugestões respeitem o perfil de risco]

---

## Exemplo de Contexto Montado

> Mostre um exemplo de como os dados são formatados para o agente.

```
Dados do Cliente:
Dados do Cliente:
- Nome: João Silva
- Perfil: Moderado
- Renda mensal: R$ 5.000
- Patrimônio: R$ 15.000
- Reserva de emergência atual: R$ 10.000

Últimas transações:
- 01/10: Salário - R$ 5.000 (entrada)
- 02/10: Aluguel - R$ 1.200 (saída)
- 03/10: Supermercado - R$ 450 (saída)
- 05/10: Netflix - R$ 55,90 (saída)
- 07/10: Farmácia - R$ 89 (saída)

Metas financeiras:
- Completar reserva de emergência: R$ 15.000 até 06/2026
- Entrada do apartamento: R$ 50.000 até 12/2027

Produtos financeiros disponíveis:
- Tesouro Selic: indicado para reserva de emergência
- CDB Liquidez Diária: indicado para segurança com rendimento diário
- Fundo Multimercado: indicado para diversificação moderada
- Debêntures Incentivadas: indicado para investidores moderados
- ETF Ibovespa: indicado para exposição à bolsa
```
