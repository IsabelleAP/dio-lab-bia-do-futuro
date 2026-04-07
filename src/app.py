import json
import pandas as pd
import requests
import streamlit as st

# CONFIGURAÇÃO
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:120b-cloud"

# CARREGAR OS DADOS
with open("../data/perfil_investidor.json", "r", encoding="utf-8") as f:
    perfil = json.load(f)

with open("../data/produtos_financeiros.json", "r", encoding="utf-8") as f:
    produtos = json.load(f)

transacoes = pd.read_csv("../data/transacoes.csv")
historico = pd.read_csv("../data/historico_atendimento.csv")


# CONTEXTO
contexto = f"""
CLIENTE: {perfil["nome"]}, {perfil["idade"]} anos, perfil {perfil["perfil_investidor"]}
OBJETIVO: {perfil["objetivo_principal"]}
PATRIMÔNIO: R$ {perfil["patrimonio_total"]} | RESERVA: R$ {perfil["reserva_emergencia_atual"]}

TRANSAÇÕES RECENTES:
{transacoes.to_string(index=False)}

ATENDIMENTOS ANTERIORES:
{historico.to_string(index=False)}

PRODUTOS DISPONÍVEIS:
{json.dumps(produtos, indent=2, ensure_ascii=False)}
"""

# SYSTEM PROMPT
SYSTEM_PROMPT = """
Você é o GRIOF (Gestão Responsável de Investimento e Organização Financeira), um agente financeiro inteligente especializado em ajudar clientes a organizar suas finanças, planejar metas e identificar padrões de gastos.

OBJETIVO:
Seu objetivo é apoiar o cliente de forma proativa e personalizada, utilizando seus dados financeiros para gerar insights, sugerir ajustes práticos e ajudar na tomada de decisões mais conscientes.

REGRAS:
1. Sempre baseie suas respostas exclusivamente nos dados fornecidos
2. Nunca invente informações financeiras ou dados do cliente
3. Se não souber algo, admita claramente e ofereça alternativas
4. Não forneça ou solicite informações sensíveis (senhas, dados de outros clientes, etc.)
5. Não faça recomendações de investimentos fora do perfil do cliente
6. Seja educativo, claro, direto e não julgador
7. Explique o motivo das suas sugestões sempre que possível
8. Não responda perguntas fora do escopo, mesmo que saiba a resposta
"""

# CHAMAR OLLAMA
def perguntar(msg):
    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

Pergunta: {msg}
"""
    try:
        r = requests.post(
            OLLAMA_URL,
            json={
                "model": MODELO,
                "prompt": prompt,
                "stream": False
            },
            timeout=60
        )

        r.raise_for_status()
        return r.json().get("response", "Não consegui gerar uma resposta no momento.")

    except requests.exceptions.RequestException as e:
        return f"Erro ao conectar com o modelo: {e}"


# INTERFACE
st.title("GRIOF - Assistente Financeiro Inteligente")

if pergunta := st.chat_input("Sua dúvida sobre finanças..."):
    st.chat_message("user").write(pergunta)

    with st.spinner("Analisando suas finanças..."):
        resposta = perguntar(pergunta)
        st.chat_message("assistant").write(resposta)