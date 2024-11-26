import streamlit as st

# Configuração inicial do layout e estilo
st.set_page_config(page_title="Hubot", layout="centered")

# Aplicando estilo customizado
st.markdown(
    """
    <style>
    body {
        background-color: white;
    }
    .titulo {
        font-size: 3em;
        font-weight: bold;
        color: blue;
        text-align: center;
        margin-bottom: 20px;
    }
    .container {
        background-color: #E3F2FD;
        padding: 20px;
        border-radius: 10px;
        margin-bottom: 20px;
    }
    .item-titulo {
        font-size: 1.5em;
        font-weight: bold;
        color: #1565C0;
        margin-bottom: 10px;
    }
    .horario {
        color: black;
        font-size: 1em;
        margin-bottom: 10px;
    }
    .duvidas-container {
        background-color: #FFEBEE;
        padding: 20px;
        border-radius: 10px;
        margin: 20px 0;
        text-align: center;
    }
    .duvidas-title {
        font-size: 1.5em;
        font-weight: bold;
        color: #B71C1C;
        margin-bottom: 10px;
    }
    .descricao {
        font-size: 1em;
        color: #424242;
        margin-bottom: 10px;
        font-style: italic;
    }
    </style>
    """,
    unsafe_allow_html=True,
)

# Título principal
st.markdown('<div class="titulo">Hubot</div>', unsafe_allow_html=True)

# Função para renderizar Locais Ocupados
def render_locais_ocupados(local, horario, descricao, participantes):
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown(f'<div class="item-titulo">Reservada</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="horario">{local}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="horario">{horario}</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="descricao">Assunto: {descricao}</div>', unsafe_allow_html=True)
    with st.expander("Visualizar Participantes", expanded=False):
        for participante in participantes:
            st.write(participante)
    st.markdown('</div>', unsafe_allow_html=True)

# Função para renderizar Locais Disponíveis com a opção de "Reservar Sala"
def render_locais_disponiveis(local, reservas):
    st.markdown('<div class="container">', unsafe_allow_html=True)
    st.markdown(f'<div class="item-titulo">Reservar Sala</div>', unsafe_allow_html=True)
    st.markdown(f'<div class="horario">{local}</div>', unsafe_allow_html=True)
    
    # Formulário para marcar horário
    with st.form(key=f"form_{local}"):
        data = st.text_input("Data (DD/MM/AAAA):", placeholder="Ex: 25/11/2024")
        horario = st.text_input("Horário (HH:MM-HH:MM):", placeholder="Ex: 14:00-15:00")
        titulo = st.text_input("Título da Reunião:", placeholder="Ex: Planejamento Semestral")
        submitted = st.form_submit_button("Marcar Horário")
        
        if submitted:
            if data and horario and titulo:
                reservas.append(f"{data}, {horario} - {titulo}")
                st.success(f"Reserva feita para {local}: {titulo} em {data} das {horario}.")
            else:
                st.error("Por favor, preencha todos os campos.")
    
    # Exibindo reservas salvas
    if reservas:
        st.markdown("#### Reservas:")
        for reserva in reservas:
            st.markdown(f"- {reserva}")
    st.markdown('</div>', unsafe_allow_html=True)

# Dados de exemplo
locais_ocupados = [
    {"local": "Sala de Reunião 2", "horario": "19h-20h", "descricao": "Feedback de Projeto", "participantes": ["Manoela", "Camila", "Diego"]},
    {"local": "Sala de Reunião 3", "horario": "15h-16h", "descricao": "Reunião Semanal", "participantes": ["Carol", "Laura", "Amanda"]},
    {"local": "Sala de Reunião 5", "horario": "10h15-12h20", "descricao": "Treinamento de Equipe", "participantes": ["Vivian", "Diego", "Rogério"]}
]

locais_disponiveis = [
    {"local": "Sala de Reunião 4", "reservas": []},
    {"local": "Sala de Reunião 1", "reservas": []},
    {"local": "Sala de Reunião Principal", "reservas": []}
]

# Dividindo em duas colunas
col1, col2 = st.columns(2)

# Renderizando Locais Ocupados na coluna da esquerda
with col1:
    st.markdown("### Locais Ocupados")
    for local in locais_ocupados:
        render_locais_ocupados(local["local"], local["horario"], local["descricao"], local["participantes"])

# Renderizando Locais Disponíveis na coluna da direita
with col2:
    st.markdown("### Locais Disponíveis")
    for local in locais_disponiveis:
        render_locais_disponiveis(local["local"], local["reservas"])
