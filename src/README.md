# Código da Aplicação
Esta pasta contém o código do agente financeiro GRIOF (Gestão Responsável de Investimento e Organização Financeira).

## Estrutura do Projeto

```
src/
├── app.py              # Aplicação principal (Streamlit)
├── requirements.txt    # Dependências
data/
├── perfil_investidor.json
├── produtos_financeiros.json
├── transacoes.csv
├── historico_atendimento.csv
```
## Setup do Ollama

```bash
# Instalar o Ollama
Baixe e instale em: https://ollama.com

# Baixar o modelo
ollama run gpt-oss:120b-cloud

# Testar o modelo
ollama run gpt-oss:120b-cloud "Olá"
```

## Como Rodar

```bash
# Instalar dependências
pip install -r requirements.txt

# Garantir que o Ollama está rodando
ollama serve

# Rodar a aplicação
streamlit run app.py
ou
python -m streamlit run src/app.py
```
## Evidência de execução
![alt text](<Captura de tela 2026-04-08 101459.png>)
