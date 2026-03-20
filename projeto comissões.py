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
tabs = st.tabs(["01. CONCEITO", "02. MERCADO", "03. FLUXO & SISTEMA (QUIVER)", "04. ESGOTAMENTO & ESTORNO", "05. GOVERNANÇA"])

# --- CAPÍTULO 1 ---
with tabs[0]:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: 'Montserrat'; color: #FFFFFF;">O Alicerce Estratégico</h2>
        <p>A <b>tabela de comissão de corretora de seguros</b> define os percentuais que o corretor recebe por cada apólice vendida. Estes valores variam conforme o ramo, a seguradora e o modelo de atuação.</p>
        <p>Ela é essencial para <b>organizar os repasses</b>, prever ganhos e manter a gestão financeira da corretora em dia.</p>
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
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("<h2 style='font-family: Montserrat; color: #FFFFFF;'>Fluxo de Recebimento no Sistema (Quiver)</h2>", unsafe_allow_html=True)
    
    st.markdown("""
    ### 1. O Gatilho da "Comissão Prevista"
    No **Quiver**, ao cadastrar uma apólice, você informa o Percentual de Comissão e a Forma de Pagamento. O sistema calcula automaticamente a **Comissão Prevista**.
    Se você marcar como antecipada/esgotamento, o sistema espera receber o "bolo" total no primeiro extrato baixado da seguradora.
    
    ### 2. A Regra do "Prêmio Líquido da Parcela"
    Uma lógica técnica fundamental: **A comissão paga no esgotamento não pode ser maior que o prêmio líquido pago pelo cliente na parcela.**
    
    - **O que acontece:** Se a comissão total for R$ 500,00, mas a 1ª parcela for de R$ 300,00, a seguradora não tem "lastro" para pagar os R$ 500,00 de uma vez.
    - **No Sistema:** Você verá o recebimento de R$ 300,00 no Mês 1 (**Valor X**) e os R$ 200,00 restantes no Mês 2 (**Valor Y**) assim que a segunda parcela entrar.
    """)

    st.markdown("---")
    st.markdown("### 3. Dinâmica de Pico e Silêncio (Se não houver cancelamento)")
    st.write("O cálculo interno para pagamento total é:")
    st.latex(r"V_{total} = (P_{mensal} \times 12) \times \%com")
    
    st.markdown("""
    - **Esgotamento Total:** Recebimento integral no **Mês 1** (desde que respeite o lastro da parcela).
    - **Esgotamento Parcial/Escalonado:** Dividido para mitigar risco de estorno imediato ou por falta de lastro no prêmio da parcela.
    """)

    # Simulador de Fluxo Quiver
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    c_s1, c_s2 = st.columns([1, 2])
    with c_s1:
        p_mensal_cli = st.number_input("Valor da Parcela do Cliente (R$)", value=300.0)
        p_comissao = st.slider("Comissão (%)", 0, 40, 20)
        v_total_previsto = (p_mensal_cli * 12) * (p_comissao / 100)
        
        st.write(f"**Comissão Prevista Total:** R$ {v_total_previsto:,.2f}")
        
        lastro = st.checkbox("Limitar pelo Prêmio Líquido da Parcela (Lógica Quiver)", value=True)
    
    fluxo_quiver = []
    saldo_a_receber = v_total_previsto
    for m in range(1, 13):
        if lastro:
            # Paga o máximo possível limitado à parcela do cliente
            pagamento_m = min(saldo_a_receber, p_mensal_cli)
        else:
            # Esgotamento total sem trava
            pagamento_m = saldo_a_receber if m == 1 else 0
            
        saldo_a_receber -= pagamento_m
        fluxo_quiver.append({"Mês": f"Mês {m:02d}", "Recebimento": pagamento_m, "Fase": "Pico (X)" if m==1 else ("Residual (Y)" if pagamento_m > 0 else "Silêncio")})
    
    with c_s2:
        st.markdown(f'<div class="metric-card"><p class="metric-label">Total Liquidado no Ciclo</p><p class="metric-val">R$ {sum(d["Recebimento"] for d in fluxo_quiver):,.2f}</p></div>', unsafe_allow_html=True)
        st.write("")
        st.data_editor(pd.DataFrame(fluxo_quiver), hide_index=True, use_container_width=True, disabled=True,
                       column_config={"Recebimento": st.column_config.NumberColumn(format="R$ %.2f")})
    st.markdown('</div></div>', unsafe_allow_html=True)

# --- CAPÍTULO 4 ---
with tabs[3]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("<h2 style='font-family: Montserrat; color: #FFFFFF;'>Engenharia de Esgotamento & Estorno</h2>", unsafe_allow_html=True)
    
    st.markdown("### 1. O Conceito de Esgotamento")
    st.write("Diferente da comissão mensal, no modelo de esgotamento a seguradora antecipa o prêmio anual de uma só vez. A regra de estorno entra em vigor quando o contrato é cancelado antes do período previsto.")
    
    st.markdown("### 2. Normas da SUSEP")
    st.write("""
    - **Circular SUSEP nº 612/2020:** O corretor deve informar o montante da comissão se solicitado.
    - **Direito ao Estorno:** Respaldo legal para recuperar valores antecipados em inadimplência ou cancelamento.
    """)

    st.markdown("### 3. Cálculo do Estorno (Pro-rata Temporis)")
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.latex(r"C_e = C_a \times \frac{T_r}{T_t}")
    st.caption("Ce: Estorno | Ca: Comissão Antecipada | Tr: Tempo Restante | Tt: Tempo Total")
    st.markdown('</div>', unsafe_allow_html=True)

    ce1, ce2 = st.columns([1, 2])
    with ce1:
        c_a_val = st.number_input("Comissão Total Recebida (R$)", value=240.0, key="ca_4")
        t_t_val = st.number_input("Vigência (Meses)", value=12, key="tt_4")
        t_d_val = st.slider("Meses Decorridos", 0, 12, 3)
        c_e_res = c_a_val * ((t_t_val - t_d_val) / t_t_val) if t_t_val > 0 else 0
    with ce2:
        st.markdown(f'<div class="metric-card" style="border-color: #F87171;"><p class="metric-label">Valor do Estorno (A Devolver)</p><p class="metric-val" style="color: #F87171;">R$ {c_e_res:,.2f}</p></div>', unsafe_allow_html=True)

    st.warning("**Atenção:** O estorno é sobre o bruto. Cuidado com impostos já pagos sobre o Pico (X) do Mês 1.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 5 ---
with tabs[4]:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: Montserrat; color: #FFFFFF;">Governança & Escala</h2>
        <p>A comissão é o resultado de uma engenharia bem executada. Foque em volume, mix de carteira e tecnologia.</p>
        <p><i>"No mercado de alta performance, o esgotamento é uma ferramenta de liquidez estratégica."</i></p>
    </div>
    """, unsafe_allow_html=True)
    if st.button("CONCLUIR JORNADA"):
        st.balloons()
        st.toast("E-book Master Finalizado!", icon="💎")

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align: center; color: #475569; font-size: 0.8rem;">© 2026 | INTELIGÊNCIA EM SEGUROS • PADRÃO PROFISSIONAL GLOBUS</p>', unsafe_allow_html=True)
