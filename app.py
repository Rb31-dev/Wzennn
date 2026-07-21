import streamlit as st

# Configuração da página
st.set_page_config(page_title="10% Off na primeira compra", page_icon="👟", layout="wide")

# Inicializa o carrinho de compras no estado da sessão
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

# Base de dados simples de tênis
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
