import streamlit as st
import pandas as pd

# 1. Configuração de Estética e Layout High-End
st.set_page_config(page_title="Gestão de Comissões | Padrão Globus", layout="wide", page_icon="💎")

# CSS Customizado Ultra-Premium (Foco em Experiência de E-book de Mercado)
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
    
    .estorno-card { border: 1px solid rgba(248, 113, 113, 0.4); }
    .estorno-val { color: #F87171 !important; }

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
tab1, tab2, tab3, tab4, tab5 = st.tabs(["01. CONCEITO", "02. MERCADO", "03. FLUXO DE CAIXA", "04. ESGOTAMENTO & ESTORNO", "05. GOVERNANÇA"])

with tab1:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: 'Montserrat'; color: #FFFFFF;">O Alicerce Estratégico</h2>
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
    st.markdown('<div class="ebook-section"><h2 style="font-family: Montserrat; color: #FFFFFF;">Benchmark de Mercado 2026</h2>', unsafe_allow_html=True)
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
        <h2 style="font-family: Montserrat; color: #FFFFFF;">As 3 Regras de Recebimento</h2>
        <p>A engenharia financeira da corretora depende de como a receita entra no caixa:</p>
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
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.subheader("Simulador de Fluxo de Caixa (Pico e Silêncio)")
    
    cs1, cs2 = st.columns([1, 2])
    with cs1:
        v_total_sim = st.number_input("Comissão Total Anual (R$)", value=4800.0, step=100.0, key="v_sim")
        regra_sim = st.selectbox("Escolha a Regra", ["Total", "Parcelado", "Esgotamento"], key="r_sim")
        
        if regra_sim == "Esgotamento":
            n_esg_sim = st.number_input("Esgotar em quantos meses?", min_value=1, value=3, help="Define em quanto tempo a comissão anual será consumida.")
            vig_sim = st.number_input("Vigência total (Meses)", min_value=n_esg_sim, value=12)
        else:
            vig_sim = st.number_input("Vigência total (Meses)", min_value=1, value=12)
            n_esg_sim = 1

    fluxo_sim = []
    for m in range(1, vig_sim + 1):
        if regra_sim == "Total":
            val_m = v_total_sim if m == 1 else 0
        elif regra_sim == "Parcelado":
            val_m = v_total_sim / vig_sim
        else:
            val_m = v_total_sim / n_esg_sim if m <= n_esg_sim else 0
        fluxo_sim.append({"Mês": f"Mês {m:02d}", "Valor": val_m, "Status": "Pico" if val_m > 0 and regra_sim == "Esgotamento" else ("Silêncio" if regra_sim == "Esgotamento" else "Regular")})

    with cs2:
        st.data_editor(
            pd.DataFrame(fluxo_sim),
            column_config={
                "Valor": st.column_config.NumberColumn("Recebimento (R$)", format="R$ %.2f"),
                "Status": st.column_config.TextColumn("Fase do Fluxo")
            },
            hide_index=True, use_container_width=True, disabled=True
        )
    st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("<h2 style='font-family: Montserrat; color: #FFFFFF;'>Engenharia de Esgotamento & Estorno</h2>", unsafe_allow_html=True)
    
    st.markdown("### 1. O Conceito de Esgotamento")
    st.write("""
    Diferente da comissão mensal (onde o corretor recebe conforme o cliente paga), no modelo de esgotamento a seguradora paga uma porcentagem sobre o prêmio anual de uma só vez. 
    A **regra de esgotamento** entra em vigor quando o contrato é cancelado antes do período previsto. Como a corretora recebeu por um serviço que "não se completou", ela deve devolver a parte proporcional à seguradora.
    """)
    
    st.markdown("### 2. Normas da SUSEP")
    st.write("""
    A SUSEP não define um percentual fixo de comissão (livre negociação). No entanto, regula a transparência e o estorno:
    - **Circular SUSEP nº 612/2020:** O corretor deve informar ao cliente o montante da comissão, se solicitado.
    - **Direito ao Estorno:** Respaldo legal para recuperar valores antecipados em caso de inadimplência ou cancelamento.
    """)

    st.markdown("### 3. Como é feito o cálculo? (Pro-rata Temporis)")
    st.write("O cálculo baseia-se no conceito de proporcionalidade ao tempo. Se o corretor recebeu por 12 meses e o cliente cancelou no 4º mês, o corretor 'não fez jus' aos 8 meses restantes.")
    
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.latex(r"C_e = C_a \times \frac{T_r}{T_t}")
    st.caption("Onde: Ce = Estorno | Ca = Comissão Antecipada | Tr = Tempo Restante | Tt = Tempo Total")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🧪 Simulador de Estorno Pro-rata")
    
    ce1, ce2 = st.columns([1, 2])
    with ce1:
        c_a_in = st.number_input("Comissão Recebida Antecipada (R$)", value=240.0)
        t_t_in = st.number_input("Vigência Total do Contrato (Meses)", value=12)
        t_d_in = st.slider("Mês do Cancelamento", 0, int(t_t_in), 3)
        t_r_in = t_t_in - t_d_in
        
        # Cálculo da Fórmula
        c_e_res = c_a_in * (t_r_in / t_t_in) if t_t_in > 0 else 0
        
    with ce2:
        st.markdown(f"""
        <div class="metric-card estorno-card">
            <p class="metric-label">Valor do Estorno (A devolver)</p>
            <p class="metric-val estorno-val">R$ {c_e_res:,.2f}</p>
        </div>
        """, unsafe_allow_html=True)
        st.markdown(f"""
        **Exemplo Prático:**
        - Comissão: R$ {c_a_in} | Vigência: {t_t_in} meses.
        - Cancelamento no mês {t_d_in}.
        - Cálculo: {c_a_in} × ({t_r_in}/{t_t_in}) = **R$ {c_e_res:,.2f}**.
        - *O valor costuma ser descontado em conta corrente das próximas comissões.*
        """)

    st.markdown("### 4. Pontos de Atenção")
    st.warning("""
    - **Prazo de Gatilho:** Algumas seguradoras têm cláusulas de comissão irretratável após certo período (ex: 24 meses).
    - **Impostos:** O estorno é sobre o valor bruto. O corretor deve atentar à contabilidade de impostos já pagos no Mês 1.
    - **Previdência Privada:** Esgotamento é padrão em aportes únicos ou planos com carregamento na saída.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab5:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: Montserrat; color: #FFFFFF;">Governança & Escala</h2>
        <p>A comissão é o combustível, mas a gestão profissional é o motor. Fatores de escala:</p>
        <ol>
            <li><b>Volume de Produção:</b> Bonificações progressivas por metas.</li>
            <li><b>Tipo de Apólice:</b> Mix entre massificados e alto ticket (Vida/Empresarial).</li>
            <li><b>Experiência:</b> Histórico de baixa sinistralidade gera melhores acordos.</li>
            <li><b>Automação:</b> Tecnologia para conferir repasses e evitar perdas operacionais.</li>
        </ol>
        <p><i>"No mercado de alta performance, a comissão é uma engenharia de resultados."</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("FINALIZAR JORNADA"):
        st.balloons()
        st.toast("E-book Concluído com Sucesso!", icon="💎")

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align: center; color: #475569; font-size: 0.8rem; letter-spacing: 1px;">© 2026 | GESTÃO DE ALTA PERFORMANCE • PADRÃO GLOBUS</p>', unsafe_allow_html=True)
