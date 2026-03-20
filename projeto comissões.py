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
tabs = st.tabs(["01. CONCEITO", "02. MERCADO", "03. FLUXO & SISTEMA (QUIVER)", "04. ESGOTAMENTO & ESTORNO", "05. GOVERNANÇA"])

# --- CAPÍTULO 1 ---
with tabs[0]:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: 'Montserrat'; color: #FFFFFF;">O Alicerce Estratégico</h2>
        <p>A <b>tabela de comissão</b> define os percentuais que o corretor recebe por cada apólice vendida. Organiza os repasses e prevê ganhos.</p>
    </div>
    """, unsafe_allow_html=True)
    st.info("**Pelas Corretoras:** Padronização interna. \n\n **Pelas Seguradoras:** Definição de custos de aquisição.")

# --- CAPÍTULO 2 ---
with tabs[1]:
    st.markdown('<div class="ebook-section"><h2 style="font-family: Montserrat; color: #FFFFFF;">Benchmark de Mercado 2026</h2>', unsafe_allow_html=True)
    dados_m = [{"Ramo": "Vida", "M": 30}, {"Ramo": "Saúde", "M": 25}, {"Ramo": "Auto", "M": 20}]
    for i in dados_m:
        st.markdown(f"**{i['Ramo']}**")
        st.progress(i['M']/30)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 3 ---
with tabs[2]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("<h2 style='font-family: Montserrat; color: #FFFFFF;'>Fluxo de Recebimento no Sistema (Quiver)</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    ### 1. O Gatilho da "Comissão Prevista"
    No **Quiver**, ao cadastrar a apólice com comissão antecipada/esgotamento, o sistema calcula o valor anual total e aguarda a baixa do primeiro extrato.
    
    ### 2. A Regra do "Prêmio Líquido da Parcela" (Lastro)
    A comissão paga não pode ser maior que o prêmio líquido pago pelo cliente na parcela.
    - **Cenário X e Y:** Se a comissão total for R$ 500 mas a parcela for R$ 300, a seguradora paga R$ 300 no Mês 1 (**Valor X**) e os R$ 200 restantes no Mês 2 (**Valor Y**) conforme as parcelas entram.
    """)

    st.markdown("---")
    st.markdown("### Simulação de Esgotamento com Trava de Lastro")
    
    c_s1, c_s2 = st.columns([1, 2])
    with c_s1:
        p_mensal = st.number_input("Valor da Parcela do Cliente (R$)", value=400.0)
        p_com = st.slider("Percentual de Comissão (%)", 0, 50, 20)
        v_previsto = (p_mensal * 12) * (p_com / 100)
        
        st.write(f"**Comissão Prevista Total: R$ {v_previsto:,.2f}**")
        lastro_on = st.checkbox("Respeitar Limite da Parcela (Lógica Quiver)", value=True)
    
    fluxo_q = []
    restante = v_previsto
    for m in range(1, 13):
        if lastro_on:
            # Paga o máximo possível limitado ao valor da parcela do cliente
            pago_no_mes = min(restante, p_mensal)
        else:
            # Esgotamento Total puro (tudo no mês 1)
            pago_no_mes = restante if m == 1 else 0
            
        restante -= pago_no_mes
        fluxo_q.append({
            "Mês": f"Mês {m:02d}", 
            "Recebimento": pago_no_mes, 
            "Fase": "Pico (X)" if m == 1 and pago_no_mes > 0 else ("Valor Y" if pago_no_mes > 0 else "Silêncio")
        })
    
    with c_s2:
        st.markdown(f'<div class="metric-card"><p class="metric-label">Total Liquidado no Ciclo</p><p class="metric-val">R$ {v_previsto:,.2f}</p></div>', unsafe_allow_html=True)
        st.write("")
        st.data_editor(pd.DataFrame(fluxo_q), hide_index=True, use_container_width=True, disabled=True,
                       column_config={"Recebimento": st.column_config.NumberColumn(format="R$ %.2f")})
        
        if v_previsto > p_mensal and lastro_on:
            st.warning(f"⚠️ **Falta de Lastro:** A comissão (R$ {v_previsto:,.2f}) é maior que a parcela (R$ {p_mensal:,.2f}). Por isso você vê o valor distribuído em mais de um mês.")
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- CAPÍTULO 4 ---
with tabs[3]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("<h2 style='font-family: Montserrat; color: #FFFFFF;'>Engenharia de Esgotamento & Estorno</h2>", unsafe_allow_html=True)
    
    st.markdown("### 1. Normas da SUSEP")
    st.write("A **Circular SUSEP nº 612/2020** garante o Direito ao Estorno proporcional ao tempo restante (Pro-rata) em caso de cancelamento.")

    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.latex(r"C_e = C_a \times \frac{T_r}{T_t}")
    st.caption("Ce: Estorno | Ca: Comissão Recebida | Tr: Tempo Restante | Tt: Tempo Total")
    st.markdown('</div>', unsafe_allow_html=True)

    ce1, ce2 = st.columns([1, 2])
    with ce1:
        c_a_in = st.number_input("Comissão Total Recebida (R$)", value=240.0, key="ca_4")
        t_d_in = st.slider("Mês do Cancelamento", 0, 12, 3)
        c_e_res = c_a_in * ((12 - t_d_in) / 12)
    with ce2:
        st.markdown(f'<div class="metric-card" style="border-color: #F87171;"><p class="metric-label">Valor a Estornar</p><p class="metric-val" style="color: #F87171;">R$ {c_e_res:,.2f}</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 5 ---
with tabs[4]:
    st.markdown('<div class="ebook-section"><h2>Governança</h2><p>Esgotamento é ferramenta de liquidez.</p></div>', unsafe_allow_html=True)
    if st.button("CONCLUIR"): st.balloons()

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align: center; color: #475569; font-size: 0.8rem;">© 2026 | INTELIGÊNCIA EM SEGUROS • PADRÃO PROFISSIONAL GLOBUS</p>', unsafe_allow_html=True)
