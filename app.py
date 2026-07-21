import streamlit as st

# Configuração da página
st.set_page_config(page_title="Sneaker Vault", page_icon="👟", layout="wide")

# CSS para o visual Clássico / Rústico Elegante (Bordas marcadas e alto contraste)
st.markdown("""
<style>
    /* Forçar fundo claro na aplicação inteira */
    .stApp {
        background-color: #FAFAFA !important;
    }
    
    /* Fontes e Títulos em Preto Profundo */
    h1, h2, h3, h4, h5, h6, label, p, span {
        color: #111111 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    .secondary-text {
        color: #555555 !important;
        font-size: 0.9em;
        font-weight: 500;
    }

    /* Cards dos Tênis (Estilo Rústico Elegante - Bordas sólidas e bem definidas) */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 4px !important;
        border: 2px solid #111111 !important;
        background-color: #FFFFFF !important;
        box-shadow: 4px 4px 0px #111111 !important;
        padding: 12px;
        transition: transform 0.2s ease;
    }

    /* Estilo dos Botões - Marcados e Táteis */
    div.stButton > button {
        background-color: #1B2A4A !important;
        color: #FFFFFF !important;
        border: 2px solid #111111 !important;
        border-radius: 4px !important;
        font-weight: 700 !important;
        letter-spacing: 0.5px;
        box-shadow: 3px 3px 0px #111111 !important;
        transition: all 0.1s ease-in-out;
    }

    div.stButton > button:hover {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        transform: translate(-1px, -1px);
        box-shadow: 4px 4px 0px #1B2A4A !important;
    }

    /* Inputs de Pesquisa e Filtro */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        border: 2px solid #111111 !important;
        border-radius: 4px !important;
        background-color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

# Estado do carrinho
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

# Base de produtos
tenis_db = [
    {
        "id": 1,
        "nome": "Air Jordan 1 Retro High",
        "marca": "Nike",
        "preco": 1299.90,
        "imagem": "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500",
    },
    {
        "id": 2,
        "nome": "Adidas Yeezy Boost 350",
        "marca": "Adidas",
        "preco": 1499.90,
        "imagem": "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=500",
    },
    {
        "id": 3,
        "nome": "Puma Suede Classic",
        "marca": "Puma",
        "preco": 399.90,
        "imagem": "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=500",
    },
    {
        "id": 4,
        "nome": "New Balance 550",
        "marca": "New Balance",
        "preco": 899.90,
        "imagem": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=500",
    },
]

# --- SIDEBAR (Carrinho) ---
st.sidebar.title("🛒 SEU CARRINHO")
st.sidebar.write("---")

if not st.session_state.carrinho:
    st.sidebar.info("O carrinho está vazio.")
else:
    total = 0
    for item in st.session_state.carrinho:
        st.sidebar.markdown(f"**{item['nome']}**")
        st.sidebar.markdown(f"<span class='secondary-text'>R$ {item['preco']:.2f}</span>", unsafe_allow_html=True)
        st.sidebar.write("---")
        total += item["preco"]
    
    st.sidebar.markdown(f"### Total: R$ {total:.2f}")
    if st.sidebar.button("FINALIZAR COMPRA", use_container_width=True):
        st.sidebar.balloons()
        st.sidebar.success("Pedido realizado com sucesso!")
        st.session_state.carrinho = []

# --- CABEÇALHO ---
st.title("SNEAKER VAULT")
st.markdown("<p class='secondary-text' style='font-size: 1.1em;'>Modelos clássicos & atemporais</p>", unsafe_allow_html=True)
st.write("")

# --- BARRA DE BUSCA E FILTROS NO TOPO ---
col_busca, col_filtro = st.columns([2, 1])

with col_busca:
    busca = st.text_input("Buscar por modelo", placeholder="Digite o nome do tênis...")

with col_filtro:
    marca_selecionada = st.selectbox("Marca", ["Todas", "Nike", "Adidas", "Puma", "New Balance"])

st.write("---")

# --- FILTRAGEM ---
produtos_filtrados = tenis_db

if marca_selecionada != "Todas":
    produtos_filtrados = [t for t in produtos_filtrados if t["marca"] == marca_selecionada]

if busca:
    produtos_filtrados = [t for t in produtos_filtrados if busca.lower() in t["nome"].lower()]

# --- VITRINE DE PRODUTOS ---
if not produtos_filtrados:
    st.warning("Nenhum modelo encontrado.")
else:
    cols = st.columns(3)
    for idx, tenis in enumerate(produtos_filtrados):
        col = cols[idx % 3]
        
        with col:
            with st.container(border=True):
                st.image(tenis["imagem"], use_container_width=True)
                st.markdown(f"### {tenis['nome']}")
                st.markdown(f"<span class='secondary-text'>Marca: {tenis['marca']}</span>", unsafe_allow_html=True)
                st.markdown(f"<h4 style='color: #111111; margin-top: 8px;'>R$ {tenis['preco']:.2f}</h4>", unsafe_allow_html=True)
                
                if st.button("ADICIONAR AO CARRINHO", key=f"btn_{tenis['id']}", use_container_width=True):
                    st.session_state.carrinho.append(tenis)
                    st.toast(f"{tenis['nome']} adicionado!", icon="✅")
                    st.rerun()
