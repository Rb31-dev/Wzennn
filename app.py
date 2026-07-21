import streamlit as st

# 1. Configuração da página
st.set_page_config(page_title="Sneaker Vault", page_icon="👟", layout="wide")

# 2. Injeção de CSS para o estilo rústico clássico
st.markdown("""
<style>
    /* Força fundo claro global */
    .stApp, [data-testid="stAppViewContainer"], [data-testid="stHeader"] {
        background-color: #FAFAFA !important;
    }
    
    /* Barra Lateral Clara */
    [data-testid="stSidebar"] {
        background-color: #F0F0F0 !important;
        border-right: 2px solid #111111 !important;
    }

    /* Textos padrão do site */
    h1, h2, h3, h4, h5, h6, label, p, span {
        color: #111111 !important;
        font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    }

    .secondary-text {
        color: #555555 !important;
        font-size: 0.9em;
        font-weight: 600;
    }

    /* Cards e Caixas na Sidebar e Vitrine */
    div[data-testid="stVerticalBlockBorderWrapper"] {
        border-radius: 6px !important;
        border: 2px solid #111111 !important;
        background-color: #FFFFFF !important;
        box-shadow: 4px 4px 0px #111111 !important;
        padding: 14px;
        margin-bottom: 15px;
    }

    /* Estilo dos Botões */
    div.stButton > button {
        background-color: #1B2A4A !important;
        border: 2px solid #111111 !important;
        border-radius: 4px !important;
        box-shadow: 3px 3px 0px #111111 !important;
        padding: 8px 16px !important;
        transition: all 0.1s ease !important;
    }

    /* Texto interno dos Botões em Branco Puro */
    div.stButton > button p, 
    div.stButton > button span, 
    div.stButton > button div {
        color: #FFFFFF !important;
        font-weight: 700 !important;
        font-size: 0.9em !important;
        letter-spacing: 0.5px !important;
    }

    /* Hover dos Botões */
    div.stButton > button:hover {
        background-color: #111111 !important;
        box-shadow: 4px 4px 0px #1B2A4A !important;
    }

    div.stButton > button:hover p,
    div.stButton > button:hover span {
        color: #FFFFFF !important;
    }

    /* Inputs e Selects */
    div[data-baseweb="input"], div[data-baseweb="select"] {
        border: 2px solid #111111 !important;
        border-radius: 4px !important;
        background-color: #FFFFFF !important;
    }
</style>
""", unsafe_allow_html=True)

# 3. Estado da Aplicação (Carrinho e Produtos)
if "carrinho" not in st.session_state:
    st.session_state.carrinho = []

# Função para resetar os produtos para o padrão atualizado
def resetar_produtos():
    st.session_state.produtos = [
        {
            "id": 1,
            "nome": "Air Jordan 1 Retro High",
            "marca": "Nike",
            "cor": "Vermelho",
            "tamanhos": [39, 40, 41, 42],
            "preco": 1299.90,
            "imagem": "https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500",
        },
        {
            "id": 2,
            "nome": "Adidas Yeezy Boost 350",
            "marca": "Adidas",
            "cor": "Preto",
            "tamanhos": [38, 39, 40, 41, 42, 43],
            "preco": 1499.90,
            "imagem": "https://images.unsplash.com/photo-1584735935682-2f2b69dff9d2?w=500",
        },
        {
            "id": 3,
            "nome": "Puma Suede Classic",
            "marca": "Puma",
            "cor": "Preto",
            "tamanhos": [37, 38, 39, 40],
            "preco": 399.90,
            "imagem": "https://images.unsplash.com/photo-1608256246200-53e635b5b65f?w=500",
        },
        {
            "id": 4,
            "nome": "New Balance 550",
            "marca": "New Balance",
            "cor": "Verde",
            "tamanhos": [40, 41, 42, 43, 44],
            "preco": 899.90,
            "imagem": "https://images.unsplash.com/photo-1539185441755-769473a23570?w=500",
        },
    ]

# Garante que a lista de produtos exista no estado
if "produtos" not in st.session_state:
    resetar_produtos()

# --- SIDEBAR (BARRA LATERAL COM CAIXAS) ---
with st.sidebar:
    st.title("🛒 SEU CARRINHO")
    
    # CAIXA 1: Conteúdo do Carrinho
    with st.container(border=True):
        if not st.session_state.carrinho:
            st.markdown("<p class='secondary-text' style='margin:0;'>O carrinho está vazio.</p>", unsafe_allow_html=True)
        else:
            total = 0
            for item in st.session_state.carrinho:
                st.markdown(f"**{item['nome']}**")
                st.markdown(f"<span class='secondary-text'>R$ {item['preco']:.2f}</span>", unsafe_allow_html=True)
                total += item["preco"]
                st.write("---")
            
            st.markdown(f"#### Total: R$ {total:.2f}")
            if st.button("FINALIZAR COMPRA", use_container_width=True):
                st.balloons()
                st.success("Pedido realizado!")
                st.session_state.carrinho = []
                st.rerun()

    st.write("")
    st.title("⚡ FILTROS")

    # Tratamento seguro (.get) para evitar KeyError com produtos antigos
    marcas_opts = ["Todas"] + sorted(list(set([t.get("marca", "Outra") for t in st.session_state.produtos])))
    cores_opts = ["Todas"] + sorted(list(set([t.get("cor", "Única") for t in st.session_state.produtos])))
    
    # Busca de tamanhos com segurança
    todos_tamanhos = set()
    for t in st.session_state.produtos:
        tams = t.get("tamanhos", [])
        if isinstance(tams, list):
            for tam in tams:
                todos_tamanhos.add(tam)
    
    tamanhos_opts = ["Todos"] + [str(tam) for tam in sorted(list(todos_tamanhos))]

    # Faixa de preço com segurança
    precos = [t.get("preco", 0.0) for t in st.session_state.produtos]
    min_p_db = float(min(precos)) if precos else 0.0
    max_p_db = float(max(precos)) if precos else 2000.0

    # CAIXA 2: Painel de Filtros Avançados
    with st.container(border=True):
        st.subheader("Filtrar Tênis")
        
        f_marca = st.selectbox("Marca", marcas_opts)
        f_cor = st.selectbox("Cor", cores_opts)
        f_tamanho = st.selectbox("Tamanho", tamanhos_opts)
        
        st.write("---")
        st.markdown("**Faixa de Preço (R$)**")
        f_preco = st.slider(
            "Selecione o limite",
            min_value=0.0,
            max_value=float(max(max_p_db, 2000.0)),
            value=(min_p_db, max_p_db),
            step=50.0
        )

# --- CABEÇALHO DA PÁGINA PRINCIPAL ---
col_head1, col_head2 = st.columns([3, 1])
with col_head1:
    st.title("SNEAKER VAULT")
    st.markdown("<p class='secondary-text' style='font-size: 1.1em;'>Vitrine clássica & acervo de sneakers</p>", unsafe_allow_html=True)

with col_head2:
    st.write("")
    # Botão de emergência para recarregar o banco de dados limpo
    if st.button("🔄 Resetar Catálogo", use_container_width=True):
        resetar_produtos()
        st.toast("Catálogo atualizado para a nova versão!", icon="✅")
        st.rerun()

st.write("")

# --- PAINEL DE CADASTRO DE NOVOS PRODUTOS ---
with st.expander("➕ Adicionar Novo Tênis ao Catálogo"):
    with st.form("form_novo_tenis", clear_on_submit=True):
        st.subheader("Cadastrar Produto")
        novo_nome = st.text_input("Nome do Tênis", placeholder="Ex: Nike Dunk Low")
        
        col_m, col_c, col_p = st.columns(3)
        with col_m:
            nova_marca = st.selectbox("Marca", ["Nike", "Adidas", "Puma", "New Balance", "Outra"])
        with col_c:
            nova_cor = st.text_input("Cor Principal", value="Preto")
        with col_p:
            novo_preco = st.number_input("Preço (R$)", min_value=0.0, value=299.90, step=10.0)

        novos_tams = st.multiselect("Tamanhos Disponíveis", [36, 37, 38, 39, 40, 41, 42, 43, 44], default=[39, 40, 41])
        nova_imagem = st.text_input("URL da Imagem", value="https://images.unsplash.com/photo-1552346154-21d32810aba3?w=500")
        
        btn_cadastrar = st.form_submit_button("CADASTRAR TÊNIS", use_container_width=True)
        
        if btn_cadastrar:
            if novo_nome and nova_cor:
                novo_id = len(st.session_state.produtos) + 1
                novo_item = {
                    "id": novo_id,
                    "nome": novo_nome,
                    "marca": nova_marca,
                    "cor": nova_cor,
                    "tamanhos": novos_tams if novos_tams else [40],
                    "preco": novo_preco,
                    "imagem": nova_imagem
                }
                st.session_state.produtos.append(novo_item)
                st.success(f"Tênis '{novo_nome}' adicionado com sucesso!")
                st.rerun()
            else:
                st.error("Por favor, preencha o nome e a cor do tênis.")

st.write("---")

# --- BARRA DE BUSCA RÁPIDA ---
busca = st.text_input("🔍 Buscar por modelo", placeholder="Digite o nome do tênis...")

st.write("---")

# --- LÓGICA DE FILTRAGEM SEGURA ---
produtos_filtrados = st.session_state.produtos

# Filtro por Marca
if f_marca != "Todas":
    produtos_filtrados = [t for t in produtos_filtrados if t.get("marca") == f_marca]

# Filtro por Cor
if f_cor != "Todas":
    produtos_filtrados = [t for t in produtos_filtrados if t.get("cor") == f_cor]

# Filtro por Tamanho
if f_tamanho != "Todos":
    produtos_filtrados = [
        t for t in produtos_filtrados 
        if int(f_tamanho) in t.get("tamanhos", [])
    ]

# Filtro por Faixa de Preço
produtos_filtrados = [
    t for t in produtos_filtrados 
    if f_preco[0] <= t.get("preco", 0.0) <= f_preco[1]
]

# Filtro por Texto da Busca
if busca:
    produtos_filtrados = [
        t for t in produtos_filtrados 
        if busca.lower() in t.get("nome", "").lower()
    ]

# --- VITRINE DE PRODUTOS ---
if not produtos_filtrados:
    st.info("Nenhum tênis encontrado com esses filtros.")
else:
    cols = st.columns(3)
    for idx, tenis in enumerate(produtos_filtrados):
        col = cols[idx % 3]
        
        with col:
            with st.container(border=True):
                st.image(tenis.get("imagem", ""), use_container_width=True)
                st.markdown(f"### {tenis.get('nome', 'Sem Nome')}")
                
                marca_str = tenis.get('marca', 'Indefinida')
                cor_str = tenis.get('cor', 'Padrão')
                st.markdown(f"<span class='secondary-text'>Marca: {marca_str} | Cor: {cor_str}</span>", unsafe_allow_html=True)
                
                tams_list = tenis.get('tamanhos', [])
                tams_str = ', '.join(map(str, tams_list)) if tams_list else 'Consulte'
                st.markdown(f"<span class='secondary-text'>Tamanhos: {tams_str}</span>", unsafe_allow_html=True)
                
                preco_val = tenis.get('preco', 0.0)
                st.markdown(f"<h4 style='color: #111111; margin-top: 8px;'>R$ {preco_val:.2f}</h4>", unsafe_allow_html=True)
                
                if st.button("ADICIONAR AO CARRINHO", key=f"btn_{tenis.get('id', idx)}", use_container_width=True):
                    st.session_state.carrinho.append(tenis)
                    st.toast(f"{tenis.get('nome')} adicionado ao carrinho!", icon="✅")
                    st.rerun()
