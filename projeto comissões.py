import streamlit as st
import pandas as pd

# 1. Configuração de Estética e Layout High-End
st.set_page_config(page_title="Gestão de Comissões | Padrão Globus", layout="wide", page_icon="💎")

# CSS Customizado Ultra-Premium (Foco em Experiência de E-book)
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
    .sub-title { color: #64748B; font-size: 0.8rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 40px; font-weight: 600; }

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
    
    .metric-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.8) 100%);
        padding: 25px; border-radius: 20px; border: 1px solid rgba(59, 130, 246, 0.3);
        text-align: center;
    }
    .metric-val { font-size: 2.2rem; font-weight: 700; color: #FFFFFF; margin: 0; }
    .metric-label { font-size: 0.7rem; color: #94A3B8; text-transform: uppercase; letter-spacing: 2px; }

    .formula-box {
        background: rgba(0,0,0,0.2);
        padding: 20px; border-radius: 12px;
        border: 1px dashed rgba(255,255,255,0.1);
        text-align: center; margin: 20px 0;
    }

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
tabs = st.tabs(["01. CONCEITO", "02. MERCADO", "03. FLUXO & MANUTENÇÃO", "04. ESGOTAMENTO & ESTORNO", "05. GOVERNANÇA"])

# --- CAPÍTULO 1 ---
with tabs[0]:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: 'Montserrat'; color: #FFFFFF;">O Alicerce Estratégico</h2>
        <p>A <b>tabela de comissão de corretora de seguros</b> define os percentuais que o corretor recebe por cada apólice vendida. 
        Estes valores variam conforme o ramo, a seguradora e o modelo de atuação.</p>
        <p>Ela é essencial para <b>organizar os repasses</b>, prever ganhos e manter a gestão financeira da corretora em dia, funcionando como um GPS de rentabilidade.</p>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    with col1:
        st.info("**Pelas Corretoras:** Para padronizar repasses internos e acompanhar o desempenho comercial.")
    with col2:
        st.success("**Pelas Seguradoras:** Para definir os percentuais autorizados e controlar os repasses às corretoras.")

# --- CAPÍTULO 2 ---
with tabs[1]:
    st.markdown('<div class="ebook-section"><h2 style="font-family: Montserrat; color: #FFFFFF;">Benchmark de Mercado 2026</h2>', unsafe_allow_html=True)
    dados_m = [
        {"Ramo": "Seguro de Vida", "Máx": 30, "Obs": "Margem estratégica."},
        {"Ramo": "Seguro Saúde", "Máx": 25, "Obs": "Recorrência mensal."},
        {"Ramo": "Seguro Empresarial", "Máx": 25, "Obs": "Ticket elevado."},
        {"Ramo": "Seguro Automóvel", "Máx": 20, "Obs": "Alto giro."},
        {"Ramo": "Seguro Residencial", "Máx": 15, "Obs": "Fidelização."}
    ]
    for i in dados_m:
        c1, c2 = st.columns([1, 4])
        with c1: st.markdown(f"**{i['Ramo']}**")
        with c2: 
            st.progress(i['Máx']/30)
            st.caption(f"Teto: {i['Máx']}% — {i['Obs']}")
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 3 ---
with tabs[2]:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: Montserrat; color: #FFFFFF;">O Cálculo de Manutenção (Fluxo Constante)</h2>
        <p>Se o cliente é fiel e paga tudo, o cálculo que a seguradora faz internamente para te pagar é baseado no prêmio anualizado:</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.latex(r"V_{total} = (P_{mensal} \times 12) \times \%com")
    st.caption("P_mensal: Prêmio pago pelo cliente por mês | %com: Seu percentual de comissão")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("""
    - **Esgotamento Total:** Você recebe $V_{total}$ integralmente no **mês 1**.
    - **Esgotamento Parcial:** A seguradora pode dividir esse $V_{total}$ em **3 ou 4 parcelas fixas** no início da vigência.
    """)

    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    col_s1, col_s2 = st.columns([1, 2])
    with col_s1:
        p_mensal = st.number_input("Prêmio Mensal do Cliente (R$)", value=400.0)
        perc_com = st.slider("Percentual de Comissão (%)", 0, 40, 20)
        v_anual_com = (p_mensal * 12) * (perc_com / 100)
        
        regra_m = st.selectbox("Regra de Esgotamento", ["Total (Mês 1)", "Parcial (3 Parcelas)", "Parcial (4 Parcelas)"])
        n_p = 1 if "Total" in regra_m else (3 if "3" in regra_m else 4)

    fluxo_m = []
    for m in range(1, 13):
        val = v_anual_com / n_p if m <= n_p else 0
        fluxo_m.append({"Mês": f"Mês {m:02d}", "Recebimento": val})

    with col_s2:
        st.markdown(f'<div class="metric-card"><p class="metric-label">V_total Anual Estimado</p><p class="metric-val">R$ {v_anual_com:,.2f}</p></div>', unsafe_allow_html=True)
        st.write("")
        st.data_editor(pd.DataFrame(fluxo_m), hide_index=True, use_container_width=True, disabled=True,
                       column_config={"Recebimento": st.column_config.NumberColumn(format="R$ %.2f")})
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 4 ---
with tabs[3]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("<h2 style='font-family: Montserrat; color: #FFFFFF;'>Engenharia de Esgotamento & Estorno</h2>", unsafe_allow_html=True)
    
    st.markdown("### 1. O Conceito de Esgotamento")
    st.write("Diferente da comissão mensal, no modelo de esgotamento a seguradora paga uma porcentagem sobre o prêmio anual de uma só vez. A regra entra em vigor no cancelamento antecipado: o corretor devolve a parte proporcional.")
    
    st.markdown("### 2. Normas da SUSEP")
    st.write("A **Circular SUSEP nº 612/2020** garante transparência ao cliente e o **Direito ao Estorno** às seguradoras em caso de inadimplência.")

    st.markdown("### 3. Cálculo de Estorno (Pro-rata Temporis)")
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.latex(r"C_e = C_a \times \frac{T_r}{T_t}")
    st.caption("Ce: Estorno | Ca: Comissão Recebida | Tr: Tempo Restante | Tt: Tempo Total")
    st.markdown('</div>', unsafe_allow_html=True)

    ce1, ce2 = st.columns([1, 2])
    with ce1:
        c_a_in = st.number_input("Comissão Recebida Antecipada (R$)", value=240.0, key="ca_4")
        t_t_in = st.number_input("Vigência (Meses)", value=12, key="tt_4")
        t_d_in = st.slider("Meses Decorridos", 0, 12, 3)
        c_e_res = c_a_in * ((t_t_in - t_d_in) / t_t_in) if t_t_in > 0 else 0
    with ce2:
        st.markdown(f'<div class="metric-card" style="border-color: #F87171;"><p class="metric-label">Estorno a Devolver</p><p class="metric-val" style="color: #F87171;">R$ {c_e_res:,.2f}</p></div>', unsafe_allow_html=True)
        st.info(f"O corretor devolve R$ {c_e_res:,.2f} referente aos {t_t_in - t_d_in} meses não decorridos.")

    st.markdown("### 4. Pontos de Atenção")
    st.warning("- **Gatilho:** Algumas seguradoras cessam o estorno após 24 meses. \n- **Impostos:** O estorno é sobre o bruto. \n- **Previdência:** Comum em aportes únicos.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 5 ---
with tabs[4]:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: Montserrat; color: #FFFFFF;">Governança & Escala</h2>
        <p>A comissão é o resultado de uma engenharia bem executada. Foque em volume, mix de carteira e tecnologia.</p>
        <p><i>"No mercado de alta performance, o esgotamento é uma ferramenta de liquidez, não apenas um ganho antecipado."</i></p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("CONCLUIR JORNADA"):
        st.balloons()
        st.toast("E-book Master Finalizado!", icon="💎")

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align: center; color: #475569; font-size: 0.8rem;">© 2026 | INTELIGÊNCIA EM SEGUROS • PADRÃO PROFISSIONAL GLOBUS</p>', unsafe_allow_html=True)
