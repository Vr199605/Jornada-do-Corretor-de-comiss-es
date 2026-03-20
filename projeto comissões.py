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
    
    /* Títulos */
    .main-title { 
        font-family: 'Montserrat', sans-serif; 
        font-weight: 700; font-size: 3.2rem; 
        background: linear-gradient(90deg, #FFFFFF, #60A5FA);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .sub-title { color: #64748B; font-size: 0.8rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 40px; font-weight: 600; }

    /* Cards Estilo Glassmorphism */
    .ebook-section {
        background: rgba(30, 41, 59, 0.4);
        padding: 40px; border-radius: 24px;
        border: 1px solid rgba(255, 255, 255, 0.08);
        backdrop-filter: blur(12px); margin-bottom: 30px;
    }

    /* Regras de Comissão */
    .regra-card {
        padding: 25px; border-radius: 16px;
        background: rgba(255, 255, 255, 0.03);
        border-top: 4px solid #3B82F6; height: 100%;
    }
    .regra-card h4 { color: #3B82F6; margin-top: 0; font-family: 'Montserrat', sans-serif; text-transform: uppercase; font-size: 0.8rem; letter-spacing: 1px; }
    
    /* Métricas Customizadas */
    .metric-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.8) 100%);
        padding: 25px; border-radius: 20px; border: 1px solid rgba(59, 130, 246, 0.3);
        text-align: center; box-shadow: 0 10px 15px -3px rgba(0, 0, 0, 0.3);
    }
    .metric-val { font-size: 2.2rem; font-weight: 700; color: #FFFFFF; margin: 0; }
    .metric-label { font-size: 0.7rem; color: #94A3B8; text-transform: uppercase; letter-spacing: 2px; margin-bottom: 5px; }

    /* Tabs Customizadas */
    .stTabs [data-baseweb="tab-list"] { gap: 30px; }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background: transparent !important; color: #94A3B8 !important;
        font-family: 'Montserrat', sans-serif; font-size: 0.85rem; border: none !important;
    }
    .stTabs [aria-selected="true"] { color: #FFFFFF !important; border-bottom: 2px solid #3B82F6 !important; }

    p, li { color: #CBD5E1; line-height: 1.6; }
    b, strong { color: #FFFFFF; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<h1 class="main-title">A Bíblia da Comissão</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Inteligência Financeira & Engenharia de Recebimento</p>', unsafe_allow_html=True)

# --- CAPÍTULOS ---
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
    
    col_a, col_b = st.columns(2)
    with col_a:
        st.info("**Pelas Corretoras:** Para padronizar repasses internos e acompanhar o desempenho comercial.")
    with col_b:
        st.success("**Pelas Seguradoras:** Para definir os percentuais autorizados em cada produto e controlar canais.")

with tab2:
    st.markdown('<div class="ebook-section"><h2 style="font-family: Montserrat;">Benchmark de Mercado 2026</h2>', unsafe_allow_html=True)
    st.write("Percentuais médios praticados de acordo com o tipo de seguro:")

    dados_mercado = [
        {"Ramo": "Seguro de Vida", "Mín": 20, "Máx": 30, "Nota": "Maior margem estratégica."},
        {"Ramo": "Seguro Saúde", "Mín": 15, "Máx": 25, "Nota": "Recorrência mensal estável."},
        {"Ramo": "Seguro Empresarial", "Mín": 15, "Máx": 25, "Nota": "Contratos de alto ticket."},
        {"Ramo": "Seguro Automóvel", "Mín": 10, "Máx": 20, "Nota": "Alta renovação e giro."},
        {"Ramo": "Seguro Residencial", "Mín": 10, "Máx": 15, "Nota": "Fidelização de carteira."}
    ]

    for item in dados_mercado:
        c_r1, c_r2 = st.columns([1, 4])
        with c_r1:
            st.markdown(f"**{item['Ramo']}**")
        with c_r2:
            st.progress(item['Máx'] / 30)
            st.caption(f"Faixa: {item['Mín']}% a {item['Máx']}% — {item['Nota']}")
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: Montserrat;">As 3 Regras de Recebimento</h2>
        <p>A engenharia financeira da corretora é ditada por como a comissão entra no caixa:</p>
    </div>
    """, unsafe_allow_html=True)

    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown('<div class="regra-card"><h4>TOTAL (Upfront)</h4>Comissão integral na primeira parcela. Foco em liquidez imediata.</div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="regra-card" style="border-top-color: #60A5FA;"><h4>PARCELADO (Pro-rata)</h4>Comissão diluída conforme o pagamento do cliente. Segurança de longo prazo.</div>', unsafe_allow_html=True)
    with r3:
        st.markdown('<div class="regra-card" style="border-top-color: #93C5FD;"><h4>ESGOTAMENTO</h4>Antecipação total da receita concentrada nos meses iniciais da vigência.</div>', unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    
    # SIMULADOR INTELIGENTE (SEM PLOTLY)
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.subheader("Simulador de Engenharia Financeira")
    
    cs1, cs2 = st.columns([1, 2])
    with cs1:
        v_total = st.number_input("Comissão Total (R$)", value=4800.0, step=100.0)
        regra_f = st.selectbox("Selecione a Regra", ["Total", "Parcelado", "Esgotamento"])
        
        if regra_f == "Esgotamento":
            n_esg = st.number_input("Esgotar em quantos meses?", min_value=1, value=4)
            vig = st.number_input("Vigência (Meses)", min_value=n_esg, value=12)
        else:
            vig = st.number_input("Vigência (Meses)", min_value=1, value=12)
            n_esg = 1

    # Cálculos
    fluxo = []
    for m in range(1, vig + 1):
        if regra_f == "Total":
            v = v_total if m == 1 else 0
        elif regra_f == "Parcelado":
            v = v_total / vig
        else: # Esgotamento
            v = v_total / n_esg if m <= n_esg else 0
        fluxo.append({"Mês": f"Mês {m:02d}", "Recebimento": v, "Percentual": (v/v_total)*100})

    df_f = pd.DataFrame(fluxo)

    with cs2:
        # Métricas Estilizadas
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown(f'<div class="metric-card"><p class="metric-label">Entrada Inicial</p><p class="metric-val">R$ {fluxo[0]["Recebimento"]:,.2f}</p></div>', unsafe_allow_html=True)
        with col_m2:
            st.markdown(f'<div class="metric-card"><p class="metric-label">Período de Receita</p><p class="metric-val">{n_esg if regra_f=="Esgotamento" else (1 if regra_f=="Total" else vig)} Meses</p></div>', unsafe_allow_html=True)
        
        st.write("")
        # Tabela com Gráfico Nativo (BarChartColumn)
        st.data_editor(
            df_f,
            column_config={
                "Recebimento": st.column_config.NumberColumn("Valor (R$)", format="R$ %.2f"),
                "Percentual": st.column_config.BarChartColumn("Peso no Caixa (%)", y_min=0, y_max=100)
            },
            hide_index=True, use_container_width=True, disabled=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: Montserrat;">Governança & Escala</h2>
        <p>Entender a tabela é o primeiro passo. Escalar exige foco em 4 fatores que influenciam o valor final:</p>
        <ol>
            <li><b>Volume de Produção:</b> Bonificações por metas atingidas junto às seguradoras.</li>
            <li><b>Mix de Carteira:</b> Equilibrar produtos massificados (Auto) com alto valor agregado (Vida/Empresarial).</li>
            <li><b>Negociação:</b> Corretores experientes com baixa sinistralidade negociam 'over-comission'.</li>
            <li><b>Tecnologia:</b> A conferência automática evita perdas que chegam a 15% do faturamento anual.</li>
        </ol>
        <p><i>"No mercado de alta performance, a comissão é o resultado de uma engenharia bem executada."</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("FINALIZAR JORNADA E GERAR INSIGHTS"):
        st.balloons()
        st.toast("E-book Master Concluído!", icon="💎")

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align: center; color: #475569; font-size: 0.8rem; letter-spacing: 1px;">© 2026 | INTELIGÊNCIA EM SEGUROS • PADRÃO PROFISSIONAL</p>', unsafe_allow_html=True)
