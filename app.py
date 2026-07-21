Ficou ótimo ver a imagem! Dá para ajustar exatamente do jeito que você quer.

Para aplicar essa paleta de cores elegante/clean e mover a barra de pesquisa e filtros para o topo, você precisará atualizar 2 arquivos no seu projeto do GitHub:

1️⃣ Atualize a paleta de cores no arquivo .streamlit/config.toml
Substitua o conteúdo do arquivo .streamlit/config.toml por este código. Ele define o fundo claro, os textos escuros e a cor dos botões em Azul Marinho:

Ini, TOML
[theme]
primaryColor = "#1B2A4A"              # Azul marinho (botões e destaques)
backgroundColor = "#FAFAFA"           # Fundo geral off-white
secondaryBackgroundColor = "#FFFFFF"  # Fundo dos cards e barra lateral (Branco puro)
textColor = "#1A1A1A"                 # Preto profundo para o texto
font = "sans serif"
2️⃣ Atualize o código no seu app.py
Substitua o código do seu app.py pelo código abaixo. Ele move a barra de pesquisa e o filtro de marcas para o topo (usando colunas lado a lado) e aplica estilos refinados:

Python
import streamlit as st

# Configuração da página
st.set_page_config(page_title="Sneaker Vault", page_icon="👟", layout="wide")

# CSS personalizado para refinamento de cores secundárias e botões
st.markdown("""
<style>
    /* Cor dos textos secundários (Cinza Médio) */
    .stCaption, p {
        color: #1A1A1A;
    }
    .secondary-text {
        color: #8C8C8C !important;
        font-size: 0.9em;
    }
    /* Estilo dos cards */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 8px;
        border: 1px solid #E5E5E5;
        background-color: #FFFFFF;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.04);
    }
    /* Estilização do título */
    h1, h2, h3 {
        color: #1A1A1A !important;
        font-weight: 700;
    }
</style>
""", unsafe_allow_html=True)

# Inicializa o carrinho na sessão
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

# Banco de dados de tênis
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

# --- BARRA LATERAL (Apenas Carrinho) ---
st.sidebar.title("🛒 Seu Carrinho")
if not st.session_state.carrinho:
    st.sidebar.info("Seu carrinho está vazio.")
else:
    total = 0
    for item in st.session_state.carrinho:
        st.sidebar.markdown(f"**{item['nome']}**")
        st.sidebar.markdown(f"<span class='secondary-text'>R$ {item['preco']:.2f}</span>", unsafe_allow_html=True)
        st.sidebar.write("---")
        total += item["preco"]
    
    st.sidebar.subheader(f"Total: R$ {total:.2f}")
    if st.sidebar.button("Finalizar Compra", type="primary", use_container_width=True):
        st.sidebar.balloons()
        st.sidebar.success("Pedido realizado com sucesso!")
        st.session_state.carrinho = []

# --- CABEÇALHO DO SITE ---
st.title("👟 Sneaker Vault")
st.markdown("<p class='secondary-text' style='font-size: 1.1em;'>Os melhores modelos para o seu estilo</p>", unsafe_allow_html=True)
st.write("")

# --- BARRA DE PESQUISA E FILTROS NO TOPO ---
col_busca, col_filtro = st.columns([2, 1])

with col_busca:
    busca = st.text_input("🔍 Pesquisar modelo", placeholder="Digite o nome do tênis...")

with col_filtro:
    marca_selecionada = st.selectbox("Marca", ["Todas", "Nike", "Adidas", "Puma", "New Balance"])

st.write("---")

# --- LÓGICA DE FILTRAGEM ---
produtos_filtrados = tenis_db

if marca_selecionada != "Todas":
    produtos_filtrados = [t for t in produtos_filtrados if t["marca"] == marca_selecionada]

if busca:
    produtos_filtrados = [t for t in produtos_filtrados if busca.lower() in t["nome"].lower()]

# --- VITRINE (3 COLUNAS) ---
if not produtos_filtrados:
    st.warning("Nenhum tênis encontrado com esses filtros.")
else:
    cols = st.columns(3)
    for idx, tenis in enumerate(produtos_filtrados):
        col = cols[idx % 3]
        
        with col:
            with st.container(border=True):
                st.image(tenis["imagem"], use_container_width=True)
                st.markdown(f"### {tenis['nome']}")
                st.markdown(f"<span class='secondary-text'>Marca: {tenis['marca']}</span>", unsafe_allow_html=True)
                st.markdown(f"<h4 style='color: #1B2A4A; margin-top: 5px;'>R$ {tenis['preco']:.2f}</h4>", unsafe_allow_html=True)
                
                if st.button("Adicionar ao Carrinho", key=f"btn_{tenis['id']}", type="primary", use_container_width=True):
                    st.session_state.carrinho.append(tenis)
                    st.toast(f"{tenis['nome']} adicionado ao carrinho!", icon="✅")
                    st.rerun()        "preco": 899.90,
        "imagem": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=500",
    },
]

# --- BARRA LATERAL (Filtros e Carrinho) ---
st.sidebar.title("🛒 Seu Carrinho")
if not st.session_state.carrinho:
    st.sidebar.info("Seu carrinho está vazio.")
else:
    total = 0
    for item in st.session_state.carrinho:
        st.sidebar.write(f"**{item['nome']}**")
        st.sidebar.caption(f"R$ {item['preco']:.2f}")
        total += item["preco"]
    st.sidebar.divider()
    st.sidebar.subheader(f"Total: R$ {total:.2f}")
    if st.sidebar.button("Finalizar Compra", type="primary"):
        st.sidebar.balloons()
        st.sidebar.success("Pedido realizado com sucesso!")
        st.session_state.carrinho = []

st.sidebar.divider()
st.sidebar.title("🔍 Filtros")
marca_selecionada = st.sidebar.selectbox("Filtrar por Marca", ["Todas", "Nike", "Adidas", "Puma", "New Balance"])

# --- CORPO DO SITE ---
st.title("👟 Sneaker Vault")
st.subheader("Os melhores modelos para o seu estilo")
st.write("---")

# Filtragem de produtos
produtos_filtrados = tenis_db
if marca_selecionada != "Todas":
    produtos_filtrados = [t for t in tenis_db if t["marca"] == marca_selecionada]

# Exibição em Vitrine (3 colunas por linha)
cols = st.columns(3)

for idx, tenis in enumerate(produtos_filtrados):
    # Distribui os cards entre as 3 colunas
    col = cols[idx % 3]
    
    with col:
        with st.container(border=True):
            st.image(tenis["imagem"], use_container_width=True)
            st.markdown(f"### {tenis['nome']}")
            st.caption(f"Marca: {tenis['marca']}")
            st.markdown(f"**R$ {tenis['preco']:.2f}**")
            
            # Botão de compra com funcionalidade
            if st.button("Adicionar ao Carrinho", key=f"btn_{tenis['id']}"):
                st.session_state.carrinho.append(tenis)
                st.toast(f"{tenis['nome']} adicionado ao carrinho!", icon="✅")
                st.rerun()
