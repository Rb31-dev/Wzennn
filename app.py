import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Sneaker Vault", page_icon="👟", layout="wide")

# 2. Injeção de CSS para garantir o tema claro + estilo rústico elegante
st.markdown("""
<style>
    /* Força fundo claro e remove sombras escuras padrão */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FAFAFA !important;
    }
    
    /* Barra Lateral Clara */
    [data-testid="stSidebar"] {
        background-color: #F0F0F0 !important;
        border-right: 2px solid #111111 !important;
    }

    /* Textos sempre escuros e visíveis */
    h1, h2, h3, h4, h5, h6, label, p, span, div {
        color: #111111 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    .secondary-text {
        color: #555555 !important;
        font-size: 0.9em;
        font-weight: 600;
    }

    /* Cards dos Tênis - Bordas bem marcadas e rústicas */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 6px !important;
        border: 2px solid #111111 !important;
        background-color: #FFFFFF !important;
        box-shadow: 4px 4px 0px #111111 !important;
        padding: 12px;
    }

    /* Botões em Azul Marinho com alto contraste */
    div.stButton > button {
        background-color: #1B2A4A !important;
        color: #FFFFFF !important;
        border: 2px solid #111111 !important;
        border-radius: 4px !important;
        font-weight: 700 !important;
        box-shadow: 3px 3px 0px #111111 !important;
        transition: all 0.1s ease;
    }

    div.stButton > button:hover {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        box-shadow: 4px 4px 0px #1B2A4A !important;
    }

    /* Ajuste para botões dentro de formulários */
    div.stFormSubmitButton > button {
        background-color: #111111 !important;
        color: #FFFFFF !important;
        border: 2px solid #111111 !important;
        box-shadow: 3px 3px 0px #1B2A4A !important;
    }

    /* Caixas de texto e seleções */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        border: 2px solid #111111 !important;
        border-radius: 4px !important;
        background-color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Gerenciamento do Estado (Produtos e Carrinho)
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

# Lista inicial de produtos salva na sessão para permitir novos cadastros
if "produtos" not in st.session_state:
    st.session_state.produtos = [
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

# --- SIDEBAR (Carrinho de Compras) ---
st.sidebar.title("🛒 SEU CARRINHO")
st.sidebar.write("---")

if not st.session_state.carrinho:
    st.sidebar.write("O carrinho está vazio.")
else:
    total = 0
    for idx, item in enumerate(st.session_state.carrinho):
        st.sidebar.markdown(f"**{item['nome']}**")
        st.sidebar.markdown(f"<span class='secondary-text'>R$ {item['preco']:.2f}</span>", unsafe_allow_html=True)
        total += item["preco"]
        st.sidebar.write("---")
    
    st.sidebar.markdown(f"### Total: R$ {total:.2f}")
    if st.sidebar.button("FINALIZAR COMPRA", use_container_width=True):
        st.sidebar.balloons()
        st.sidebar.success("Pedido realizado com sucesso!")
        st.session_state.carrinho = []
        st.rerun()

# --- CABEÇALHO ---
st.title("SNEAKER VAULT")
st.markdown("<p class='secondary-text' style='font-size: 1.1em;'>Vitrine clássica & acervo de sneakers</p>", unsafe_allow_html=True)
st.write("")

# --- ÁREA DE CADASTRO DE NOVOS PRODUTOS ---
with st.expander("➕ Adicionar Novo Tênis ao Catálogo"):
    with st.form("form_novo_tenis", clear_on_submit=True):
        st.subheader("Cadastrar Produto")
        novo_nome = st.text_input("Nome do Tênis", placeholder="Ex: Nike Dunk Low")
        
        col_m, col_p = st.columns(2)
        with col_m:
            nova_marca = st.selectbox("Marca", ["Nike", "Adidas", "Puma", "New Balance", "Outra"])
        with col_p:
            novo_preco = st.number_input("Preço (R$)", min_value=0.0, value=299.90, step=10.0)
            
        nova_imagem = st.text_input("URL da Imagem (Link da foto)", value="https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500")
        
        btn_cadastrar = st.form_submit_button("CADASTRAR TÊNIS", use_container_width=True)
        
        if btn_cadastrar:
            if novo_nome:
                novo_id = len(st.session_state.produtos) + 1
                novo_item = {
                    "id": novo_id,
                    "nome": novo_nome,
                    "marca": nova_marca,
                    "preco": novo_preco,
                    "imagem": nova_imagem
                }
                st.session_state.produtos.append(novo_item)
                st.success(f"Tênis '{novo_nome}' adicionado com sucesso!")
                st.rerun()
            else:
                st.error("Por favor, digite o nome do tênis.")

st.write("---")

# --- BARRA DE BUSCA E FILTROS ---
col_busca, col_filtro = st.columns([2, 1])

# Extrai marcas dinamicamente para o filtro
marcas_disponiveis = ["Todas"] + sorted(list(set([t["marca"] for t in st.session_state.produtos])))

with col_busca:
    busca = st.text_input("Buscar por modelo", placeholder="Digite o nome do tênis...")

with col_filtro:
    marca_selecionada = st.selectbox("Filtrar por Marca", marcas_disponiveis)

st.write("---")

# --- LÓGICA DE FILTRAGEM ---
produtos_filtrados = st.session_state.produtos

if marca_selecionada != "Todas":
    produtos_filtrados = [t for t in produtos_filtrados if t["marca"] == marca_selecionada]

if busca:
    produtos_filtrados = [t for t in produtos_filtrados if busca.lower() in t["nome"].lower()]

# --- VITRINE DE PRODUTOS ---
if not produtos_filtrados:
    st.info("Nenhum tênis encontrado.")
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
                    st.toast(f"{tenis['nome']} adicionado ao carrinho!", icon="✅")
                    st.rerun()
