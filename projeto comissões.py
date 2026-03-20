import streamlit as st
import pandas as pd

# 1. Configuração de Estética e Layout High-End
st.set_page_config(page_title="Gestão de Comissões | Padrão Globus", layout="wide", page_icon="💎")

# CSS Customizado Ultra-Premium (Dark Mode & Glassmorphism)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0F172A; }
    .stApp { background: radial-gradient(circle at top right, #1E293B, #0F172A); color: #F8FAFC; }
    
    .main-title { 
        font-family: 'Montserrat', sans-serif; 
        font-weight: 700; font-size: 3.2rem; 
        background: linear-gradient(90deg, #FFFFFF, #60A5FA);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .sub-title { color: #64748B; font-size: 0.9rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 40px; font-weight: 600; }

    .ebook-section {
        background: rgba(30, 41, 59, 0.4);
        padding: 40px; border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px); margin-bottom: 30px;
    }

    .regra-card {
        padding: 25px; border-radius: 16px;
        background: rgba(255, 255, 255, 0.03);
        border-top: 4px solid #3B82F6; height: 100%;
    }
    .regra-card h4 { color: #3B82F6; margin-top: 0; font-family: 'Montserrat', sans-serif; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; }
    
    /* Tabela Customizada Estilo Globus */
    .stDataFrame { background: transparent !important; border-radius: 15px; }
    
    /* Métricas Minimalistas */
    .metric-box {
        background: rgba(255, 255, 255, 0.05);
        padding: 20px; border-radius: 12px; text-align: center;
        border: 1px solid rgba(255, 255, 255, 0.1);
    }
    .metric-val { font-size: 1.8rem; font-weight: 700; color: #FFFFFF; }
    .metric-label { font-size: 0.8rem; color: #94A3B8; text-transform: uppercase; }

    p, li { color: #CBD5E1; line-height: 1.6; }
    b, strong { color: #FFFFFF; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<h1 class="main-title">A Bíblia da Comissão</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Inteligência Financeira & Engenharia de Recebimento</p>', unsafe_allow_html=True)

# --- CONTEÚDO EM CAPÍTULOS ---
tab1, tab2, tab3, tab4 = st.tabs(["01. CONCEITO", "02. MERCADO", "03. FLUXO DE CAIXA", "04. GOVERNANÇA"])

with tab1:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: 'Montserrat';">O Alicerce Estratégico</h2>
        <p>A <b>tabela de comissão de corretora de seguros</b> define os percentuais que o corretor recebe por cada apólice vendida. 
        Estes valores variam conforme o ramo (vida, automóvel, empresarial, saúde etc.), de acordo com a seguradora e o modelo de atuação do corretor.</p>
        <p>Ela é essencial para <b>organizar os repasses</b>, prever ganhos e manter a gestão financeira da corretora em dia, funcionando como um GPS de rentabilidade.</p>
    </div>
    """, unsafe_allow_html=True)
    
    c1, c2 = st.columns(2)
    with c1:
        st.markdown("""
        ### Pelas Corretoras
        Utilizada para padronizar repasses internos, acompanhar o desempenho comercial e manter a saúde do fluxo de caixa sob controle rigoroso.
        """)
    with c2:
        st.markdown("""
        ### Pelas Seguradoras
        Serve para definir percentuais autorizados em cada produto e controlar os repasses às corretoras parceiras conforme o volume de produção.
        """)

with tab2:
    st.markdown('<div class="ebook-section"><h2 style="font-family: Montserrat;">Benchmark de Mercado 2026</h2>', unsafe_allow_html=True)
    st.write("Percentuais médios praticados por tipo de seguro:")

    # Dados originais do texto
    dados = [
        {"Ramo": "Seguro de Vida", "Perc": 30, "Cor": "#3B82F6", "Desc": "Maior margem e foco em previdência."},
        {"Ramo": "Seguro Saúde", "Perc": 25, "Cor": "#60A5FA", "Desc": "Recorrência mensal constante."},
        {"Ramo": "Seguro Empresarial", "Perc": 25, "Cor": "#93C5FD", "Desc": "Contratos robustos e negociáveis."},
        {"Ramo": "Seguro Automóvel", "Perc": 20, "Cor": "#2563EB", "Desc": "Alta renovação e giro."},
        {"Ramo": "Seguro Residencial", "Perc": 15, "Cor": "#1D4ED8", "Desc": "Porta de entrada para cross-selling."}
    ]

    for item in dados:
        col_r1, col_r2 = st.columns([1, 3])
        with col_r1:
            st.markdown(f"**{item['Ramo']}** \n<small>{item['Perc']}% (Máx)</small>", unsafe_allow_html=True)
        with col_r2:
            st.progress(item['Perc'] / 30) # Normalizado pelo máximo de 30%
            st.caption(item['Desc'])
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: Montserrat;">As 3 Regras de Recebimento</h2>
        <p>A engenharia financeira da corretora depende de como a receita é distribuída no tempo:</p>
    </div>
    """, unsafe_allow_html=True)

    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown('<div class="regra-card"><h4>TOTAL (Upfront)</h4>Recebimento integral no primeiro mês. Ideal para crescimento acelerado.</div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="regra-card" style="border-top-color: #60A5FA;"><h4>PARCELADO (Pro-rata)</h4>Comissão diluída conforme o pagamento do cliente. Segurança contra estornos.</div>', unsafe_allow_html=True)
    with r3:
        st.markdown('<div class="regra-card" style="border-top-color: #93C5FD;"><h4>ESGOTAMENTO</h4>Foco nas parcelas iniciais da apólice, acelerando o retorno do lucro.</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # SIMULADOR SEM PLOTLY (USANDO MÉTRICAS E TABELAS DINÂMICAS)
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.subheader("Simulador de Engenharia Financeira")
    
    cs1, cs2 = st.columns([1, 2])
    with cs1:
        valor_total = st.number_input("Comissão Total (R$)", value=3600.0, step=100.0)
        regra_sel = st.selectbox("Regra de Fluxo", ["Total", "Parcelado", "Esgotamento"])
        
        if regra_sel == "Esgotamento":
            n_esg = st.number_input("Esgotar em quantos meses?", min_value=1, value=3)
            vigencia = st.number_input("Vigência total (Meses)", min_value=n_esg, value=12)
        else:
            vigencia = st.number_input("Vigência total (Meses)", min_value=1, value=12)
            n_esg = 1

    # Cálculos de Fluxo
    fluxo_data = []
    for m in range(1, vigencia + 1):
        if regra_sel == "Total":
            val = valor_total if m == 1 else 0
        elif regra_sel == "Parcelado":
            val = valor_total / vigencia
        elif regra_sel == "Esgotamento":
            val = valor_total / n_esg if m <= n_esg else 0
        fluxo_data.append({"Mês": f"Mês {m}", "Recebimento": val})

    df_fluxo = pd.DataFrame(fluxo_data)

    with cs2:
        # Exibição de Resumo de Caixa em cards
        m1, m2 = st.columns(2)
        with m1:
            st.markdown(f'<div class="metric-box"><p class="metric-label">Entrada no 1º Mês</p><p class="metric-val">R$ {fluxo_data[0]["Recebimento"]:,.2f}</p></div>', unsafe_allow_html=True)
        with m2:
            avg = valor_total / vigencia
            st.markdown(f'<div class="metric-box"><p class="metric-label">Média por Mês</p><p class="metric-val">R$ {avg:,.2f}</p></div>', unsafe_allow_html=True)
        
        st.write("")
        st.dataframe(df_fluxo, use_container_width=True, hide_index=True)
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: Montserrat;">Governança & Escala</h2>
        <p>O corretor estratégico foca em 4 pilares para escalar os ganhos:</p>
        <ol>
            <li><b>Volume:</b> Metas que geram bonificações progressivas.</li>
            <li><b>Tipo de Apólice:</b> Seguros corporativos geram comissões robustas.</li>
            <li><b>Negociação:</b> Experiência de mercado abre portas para percentuais diferenciados.</li>
            <li><b>Tecnologia:</b> Automatizar a conferência para evitar perdas operacionais.</li>
        </ol>
        <p style="margin-top: 20px;"><b>Conclusão:</b> A comissão é o combustível, mas a gestão profissional é o motor do seu patrimônio.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("FINALIZAR JORNADA"):
        st.balloons()

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align: center; color: #475569; font-size: 0.8rem;">© 2026 | Gestão de Alta Performance para Corretores Profissionais</p>', unsafe_allow_html=True)
