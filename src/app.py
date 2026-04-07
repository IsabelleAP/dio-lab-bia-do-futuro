import json
import pandas as pd
import requests
import streamlit as st

# CONFIGURAÇÃO
OLLAMA_URL = "http://localhost:11434/api/generate"
MODELO = "gpt-oss:120b-cloud"

# MEMÓRIA
if "historico_chat" not in st.session_state:
    st.session_state["historico_chat"] = []

# CARREGAR DADOS
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
Apoiar o cliente de forma proativa e personalizada, utilizando dados financeiros para gerar insights, sugerir ajustes práticos e ajudar na tomada de decisões conscientes.

REGRAS:
1. Baseie respostas apenas nos dados fornecidos
2. Nunca invente informações
3. Se não souber, admita claramente
4. Não lide com dados sensíveis
5. Não recomende investimentos fora do perfil
6. Seja claro, direto e educativo
7. Explique o motivo das sugestões
8. Não responda fora do escopo financeiro
"""

def perguntar(msg):
    # Montar histórico da conversa
    historico_formatado = "\n".join(
        [f'{m["role"].upper()}: {m["content"]}' for m in st.session_state["historico_chat"]]
    )

    prompt = f"""
{SYSTEM_PROMPT}

CONTEXTO DO CLIENTE:
{contexto}

HISTÓRICO DA CONVERSA:
{historico_formatado}

PERGUNTA ATUAL: {msg}
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

# Mostrar histórico
for msg in st.session_state["historico_chat"]:
    st.chat_message(msg["role"]).write(msg["content"])

# Input do usuário
if pergunta_usuario := st.chat_input("Sua dúvida sobre finanças..."):
    # salvar pergunta
    st.session_state["historico_chat"].append({
        "role": "user",
        "content": pergunta_usuario
    })

    st.chat_message("user").write(pergunta_usuario)

    with st.spinner("Analisando suas finanças..."):
        resposta = perguntar(pergunta_usuario)

    # salvar resposta
    st.session_state["historico_chat"].append({
        "role": "assistant",
        "content": resposta
    })

    st.chat_message("assistant").write(resposta)