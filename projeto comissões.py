
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
        padding: 25px; border-radius: 20px; border: 1px solid rgba(248, 113, 113, 0.3);
        text-align: center;
    }
    .metric-val { font-size: 2.2rem; font-weight: 700; color: #F87171; margin: 0; }
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
tab1, tab2, tab3, tab4, tab5 = st.tabs(["01. CONCEITO", "02. MERCADO", "03. REGRAS", "04. ESGOTAMENTO & ESTORNO", "05. GOVERNANÇA"])

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

with tab4:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("<h2 style='font-family: Montserrat; color: #FFFFFF;'>Engenharia de Esgotamento & Estorno</h2>", unsafe_allow_html=True)
    st.write("""
    No mercado de seguros e previdência, a comissão por esgotamento (ou antecipada com estorno) é uma prática onde a seguradora 
    antecipa ao corretor uma parte ou o total da comissão anual logo no início da vigência.
    """)
    
    st.markdown("### 1. O Conceito de Esgotamento")
    st.write("""
    Diferente da comissão mensal (onde o corretor recebe conforme o cliente paga), no modelo de esgotamento a seguradora paga uma porcentagem sobre o prêmio anual de uma só vez. 
    A **regra de esgotamento** entra em vigor quando o contrato é cancelado antes do período previsto.
    """)

    st.markdown("### 2. Normas da SUSEP")
    st.write("""
    A **Circular SUSEP nº 612/2020** estabelece a transparência: o corretor deve informar o montante da comissão se solicitado. 
    As seguradoras possuem respaldo legal para o **Direito ao Estorno** caso o prêmio não seja integralmente pago.
    """)

    st.markdown("### 3. Como é feito o cálculo? (Pro-rata Temporis)")
    st.write("Se o contrato é cancelado antes do período previsto, a corretora deve devolver a parte proporcional à seguradora.")
    
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.latex(r"C_e = C_a \times \frac{T_r}{T_t}")
    st.caption("Fórmula: Ce (Estorno) | Ca (Comissão Antecipada) | Tr (Tempo Restante) | Tt (Tempo Total)")
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("---")
    st.subheader("🧪 Simulador de Estorno Prático")
    
    col_e1, col_e2 = st.columns([1, 2])
    with col_e1:
        c_a = st.number_input("Comissão Total Recebida (R$)", value=240.0)
        t_t = st.number_input("Vigência Total (Meses)", value=12)
        t_d = st.slider("Meses Decorridos (até o cancelamento)", 0, int(t_t), 3)
        t_r = t_t - t_d
        
        c_e = c_a * (t_r / t_t) if t_t > 0 else 0
        
    with col_e2:
        st.markdown(f"""
        <div class="metric-card">
            <p class="metric-label">Valor a ser Devolvido (Estorno)</p>
            <p class="metric-val">R$ {c_e:,.2f}</p>
        </div>
        """, unsafe_allow_html=True)
        
        st.markdown(f"""
        **Detalhamento do Cenário:**
        - **Período de Estorno:** {t_r} meses restantes.
        - **Impacto:** O valor será descontado das suas próximas comissões ("Estorno em Conta Corrente").
        """)

    with st.expander("💡 Pontos de Atenção em Previdência e Vida"):
        st.write("""
        - **Prazo de Gatilho:** Algumas cláusulas tornam a comissão irretratável após um certo período (ex: 24 meses).
        - **Impostos:** O estorno é feito sobre o bruto; cuidado com a contabilidade de impostos já recolhidos no mês 1.
        - **Previdência:** Comum em aportes únicos ou planos com carregamento na saída.
        """)
    st.markdown('</div>', unsafe_allow_html=True)

with tab5:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: Montserrat; color: #FFFFFF;">Governança & Escala</h2>
        <p>Entender a tabela é o primeiro passo. Escalar exige foco em 4 fatores essenciais:</p>
        <ol>
            <li><b>Volume de Produção:</b> Bonificações por metas atingidas junto às seguradoras.</li>
            <li><b>Mix de Carteira:</b> Equilibrar produtos massificados (Auto) com alto valor agregado (Vida/Empresarial).</li>
            <li><b>Negociação:</b> Corretores experientes negociam 'over-comission'.</li>
            <li><b>Tecnologia:</b> A conferência automática evita perdas operacionais.</li>
        </ol>
        <p><i>"No mercado de alta performance, a comissão é o resultado de uma engenharia bem executada."</i></p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("FINALIZAR JORNADA E GERAR INSIGHTS"):
        st.balloons()
        st.toast("E-book Master Concluído!", icon="💎")

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align: center; color: #475569; font-size: 0.8rem; letter-spacing: 1px;">© 2026 | INTELIGÊNCIA EM SEGUROS • PADRÃO PROFISSIONAL GLOBUS</p>', unsafe_allow_html=True)
