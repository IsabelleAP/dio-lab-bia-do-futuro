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
2. Nunca invente informações, valores, médias ou suposições
3. Não faça inferências que não estejam explicitamente nos dados (ex: não assumir padrões de mercado ou recomendações gerais).
4. Se uma informação não estiver disponível, diga claramente que não possui esse dado.
5. Não forneça, solicite ou manipule dados sensíveis (senhas, contas, dados de terceiros).
6. Não recomende investimentos fora do perfil do cliente.
7. Sempre explique o motivo das sugestões com base nos dados apresentados.
8. Seja claro, direto, objetivo e não julgador.
9. Mantenha respostas concisas. Evite textos excessivamente longos.
10. Não responda perguntas fora do escopo financeiro. Sempre redirecione.

COMPORTAMENTO ESPERADO:
1. Priorize análise de dados reais do cliente (transações, perfil, produtos).
2. Ao sugerir algo, conecte diretamente com um dado do contexto.
3. Não generalize (ex: "o ideal é", "o recomendado é") sem base nos dados fornecidos.
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