import streamlit as st
import pandas as pd

# 1. Configuração de Estética e Layout High-End
st.set_page_config(page_title="Gestão de Comissões | Padrão Globus", layout="wide", page_icon="💎")

# CSS Customizado Ultra-Premium (Foco em Experiência de E-book e Usabilidade)
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

    .concept-card {
        background: rgba(255, 255, 255, 0.03);
        padding: 20px; border-radius: 15px;
        border-left: 4px solid #3B82F6; margin-bottom: 20px;
    }

    .metric-card {
        background: linear-gradient(135deg, rgba(30, 41, 59, 0.8) 0%, rgba(15, 23, 42, 0.8) 100%);
        padding: 25px; border-radius: 20px; border: 1px solid rgba(59, 130, 246, 0.3);
        text-align: center; height: 100%;
    }
    .metric-val { font-size: 2.2rem; font-weight: 700; color: #FFFFFF; margin: 0; }
    .metric-label { font-size: 0.7rem; color: #94A3B8; text-transform: uppercase; letter-spacing: 2px; }

    .formula-box {
        background: rgba(0,0,0,0.2);
        padding: 25px; border-radius: 12px;
        border: 1px dashed rgba(255,255,255,0.1);
        margin: 20px 0;
    }

    .stTabs [data-baseweb="tab-list"] { gap: 20px; }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background: transparent !important; color: #94A3B8 !important;
        font-family: 'Montserrat', sans-serif; font-size: 0.8rem; border: none !important;
    }
    .stTabs [aria-selected="true"] { color: #FFFFFF !important; border-bottom: 2px solid #3B82F6 !important; }

    h2, h3 { font-family: 'Montserrat', sans-serif; color: #FFFFFF; }
    p, li { color: #CBD5E1; line-height: 1.8; font-size: 1rem; }
    b, strong { color: #FFFFFF; }
    
    .stNumberInput div div input { background-color: #1E293B !important; color: white !important; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<h1 class="main-title">A Bíblia da Comissão</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Inteligência Financeira, Sistemas & Engenharia de Recebimento</p>', unsafe_allow_html=True)

# --- CAPÍTULOS ---
tabs = st.tabs(["01. CONCEITO DETALHADO", "02. MERCADO", "03. FLUXO & SISTEMA QUIVER", "04. SIMULADOR COMPARATIVO", "05. ESGOTAMENTO & ESTORNO", "06. GOVERNANÇA & ESCALA"])

# --- CAPÍTULO 1: CONCEITO ---
with tabs[0]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("## 01. O Conceito de Comissão em Seguros")
    st.write("""
    A comissão de corretagem não é apenas uma remuneração de vendas; é o **combustível financeiro** que sustenta a operação de uma corretora. Ela representa o valor pago pela seguradora ao corretor pela intermediação, assessoria técnica e gestão de riscos do cliente.
    """)
    
    col_c1, col_c2 = st.columns(2)
    with col_c1:
        st.markdown('<div class="concept-card">', unsafe_allow_html=True)
        st.markdown("### A Natureza Jurídica")
        st.write("""
        Amparada pelo Decreto-Lei nº 73/66, a comissão é devida sempre que houver a mediação de um corretor habilitado. Ela incide sobre o **Prêmio Líquido** (o valor do seguro antes de IOF e juros de parcelamento).
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
    with col_c2:
        st.markdown('<div class="concept-card">', unsafe_allow_html=True)
        st.markdown("### O Papel do Prêmio Líquido")
        st.write("""
        Para o cálculo de comissão, ignoramos o custo de apólice e o imposto (IOF). Se um cliente paga R$ 1.100,00, mas o prêmio líquido é R$ 1.000,00 e a comissão é 20%, o corretor recebe R$ 200,00.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    st.markdown("### Tipos de Remuneração")
    st.markdown("""
    * **Comissão Mensal (Recorrência):** Pagamento proporcional às parcelas do cliente. Ideal para estabilidade.
    * **Agenciamento:** Verba paga na primeira parcela pela captação do novo risco (comum em Saúde e Vida).
    * **Esgotamento (Antecipação):** Recebimento da comissão anual projetada logo no início da vigência.
    """)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 2: MERCADO ---
with tabs[1]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("## Benchmark de Mercado 2026")
    st.write("Valores médios praticados no Brasil para corretoras de alta performance:")
    
    dados_m = [
        {"Ramo": "Seguro de Vida (Individual)", "M": 30, "Obs": "Foco em proteção familiar."},
        {"Ramo": "Seguro Saúde (PME)", "M": 25, "Obs": "Baseado na primeira fatura."},
        {"Ramo": "Seguro Automóvel", "M": 20, "Obs": "Commodity de alta rotatividade."},
        {"Ramo": "Seguro Empresarial", "M": 25, "Obs": "Ticket médio elevado."},
        {"Ramo": "Seguro Residencial", "M": 15, "Obs": "Excelente para fidelização."}
    ]
    for i in dados_m:
        st.markdown(f"**{i['Ramo']}** — Teto: **{i['M']}%**")
        st.progress(i['M']/30)
        st.caption(i['Obs'])
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 3: FLUXO & SISTEMA QUIVER ---
with tabs[2]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("## Fluxo & Sistema: A Lógica Quiver")
    
    col_q1, col_q2 = st.columns([1, 1.5])
    
    with col_q1:
        st.markdown("### Configurações de Cadastro")
        p_mensal_q = st.number_input("Valor da Parcela do Cliente (R$)", value=400.0, step=50.0)
        # Parte percentual para digitar (%)
        p_perc_q = st.number_input("Percentual de Comissão (%)", value=20.0, step=0.1)
        
        v_total_prev = (p_mensal_q * 12) * (p_perc_q / 100)
        st.markdown(f"**Comissão Prevista no Sistema:** R$ {v_total_prev:,.2f}")
        lastro_check = st.checkbox("Respeitar Regra de Lastro (Prêmio Líquido)", value=True)

    with col_q2:
        st.markdown("### O Gatilho do Recebimento")
        st.write("""
        O **Quiver** aguarda a baixa do extrato. Se a comissão prevista for R$ 1.000, mas a parcela do cliente for R$ 400:
        1. O sistema baixa R$ 400 no Mês 01 (**Valor X**).
        2. O sistema deixa R$ 600 pendente para os próximos meses (**Valor Y**).
        """)
        
        fluxo_q = []
        rest_q = v_total_prev
        for m in range(1, 13):
            pago = min(rest_q, p_mensal_q) if lastro_check else (rest_q if m==1 else 0)
            rest_q -= pago
            fluxo_q.append({"Mês": f"Mês {m:02d}", "Recebimento": pago, "Status": "Pico (X)" if m==1 else ("Residual (Y)" if pago > 0 else "Silêncio")})
        
        df_q = pd.DataFrame(fluxo_q)
        st.data_editor(df_q, hide_index=True, use_container_width=True, disabled=True,
                       column_config={"Recebimento": st.column_config.NumberColumn(format="R$ %.2f")})
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 4: NOVO SIMULADOR COMPARATIVO ---
with tabs[3]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("## Simulação: Valor Total vs. Valor Parcelado")
    st.write("Compare como o seu fluxo de caixa se comporta em cada modelo de recebimento.")
    
    c_comp1, c_comp2 = st.columns([1, 2])
    with c_comp1:
        val_premio = st.number_input("Prêmio Líquido Anual (R$)", value=5000.0, step=100.0)
        val_com_perc = st.number_input("Comissão do Corretor (%)", value=20.0, step=1.0, key="sim_comp")
        com_total_anual = val_premio * (val_com_perc / 100)
        
    with c_comp2:
        col_m1, col_m2 = st.columns(2)
        with col_m1:
            st.markdown(f'<div class="metric-card"><p class="metric-label">Esgotamento (Total)</p><p class="metric-val">R$ {com_total_anual:,.2f}</p><p style="font-size:0.7rem">No 1º Mês</p></div>', unsafe_allow_html=True)
        with col_m2:
            st.markdown(f'<div class="metric-card"><p class="metric-label">Parcelado (Mensal)</p><p class="metric-val">R$ {com_total_anual/12:,.2f}</p><p style="font-size:0.7rem">Por Mês</p></div>', unsafe_allow_html=True)

    st.markdown("### Projeção Anual de Caixa")
    comp_data = []
    for m in range(1, 13):
        comp_data.append({
            "Mês": f"Mês {m:02d}",
            "Fluxo Esgotamento (R$)": com_total_anual if m == 1 else 0.0,
            "Fluxo Parcelado (R$)": com_total_anual / 12
        })
    st.table(pd.DataFrame(comp_data).style.format({"Fluxo Esgotamento (R$)": "R$ {:.2f}", "Fluxo Parcelado (R$)": "R$ {:.2f}"}))
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 5: ESGOTAMENTO & ESTORNO ---
with tabs[4]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("## Engenharia de Estorno (Pro-rata Temporis)")
    st.write("O esgotamento é um adiantamento. Se o cliente cancela, o valor não 'vivido' deve ser devolvido.")
    
    st.markdown('<div class="formula-box">', unsafe_allow_html=True)
    st.latex(r"C_e = C_a \times \frac{T_r}{T_t}")
    st.caption("Ce: Estorno | Ca: Comissão Antecipada | Tr: Tempo Restante | Tt: Tempo Total")
    st.markdown('</div>', unsafe_allow_html=True)

    col_e1, col_e2 = st.columns([1, 2])
    with col_e1:
        c_recebida = st.number_input("Comissão Recebida (R$)", value=1200.0)
        m_decorridos = st.slider("Meses que o cliente pagou", 1, 12, 4)
        estorno_calc = c_recebida * ((12 - m_decorridos) / 12)
    with col_e2:
        st.markdown(f'<div class="metric-card" style="border-color: #F87171;"><p class="metric-label">Valor do Estorno</p><p class="metric-val" style="color: #F87171;">R$ {estorno_calc:,.2f}</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 6: GOVERNANÇA ---
with tabs[5]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("## 06. Governança e Escala Operacional")
    st.write("""
    A governança de comissões é o que separa uma corretora amadora de uma empresa de alta performance. Sem processos claros, o esgotamento pode se tornar uma armadilha de fluxo de caixa.
    """)
    
    st.markdown("### Pilares da Governança Financeira")
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown('<div class="concept-card">', unsafe_allow_html=True)
        st.markdown("#### 1. Conciliação Bancária Automatizada")
        st.write("""
        É mandatório o uso de arquivos **PDF ou Excel de extratos de comissão** importados diretamente no Quiver. A conferência manual gera erros de até 5% na receita total.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="concept-card">', unsafe_allow_html=True)
        st.markdown("#### 2. Reserva de Estorno")
        st.write("""
        Para corretoras que usam esgotamento total, é prudente manter **15% a 20%** da receita em fundo de reserva para absorver picos de estorno sem comprometer a folha de pagamento.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    with col_g2:
        st.markdown('<div class="concept-card">', unsafe_allow_html=True)
        st.markdown("#### 3. Auditoria de Repasses")
        st.write("""
        A tabela de comissão deve ser integrada ao contrato dos produtores. A regra de esgotamento deve ser clara: o produtor recebe antecipado, mas também sofre o estorno proporcional se o cliente cancelar.
        """)
        st.markdown('</div>', unsafe_allow_html=True)
        
        st.markdown('<div class="concept-card">', unsafe_allow_html=True)
        st.markdown("#### 4. Compliance SUSEP")
        st.write("""
        Manter a transparência total. Conforme a Circular 612, a corretora deve estar pronta para apresentar o valor da comissão ao segurado, garantindo ética na negociação.
        """)
        st.markdown('</div>', unsafe_allow_html=True)

    st.info("💡 **Dica Master:** Use o esgotamento para investir em prospecção, mas nunca para custeio fixo de longo prazo.")
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align: center; color: #475569; font-size: 0.8rem;">© 2026 | INTELIGÊNCIA EM SEGUROS • PADRÃO PROFISSIONAL GLOBUS</p>', unsafe_allow_html=True)
