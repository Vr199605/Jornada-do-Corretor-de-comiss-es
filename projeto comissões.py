import streamlit as st
import pandas as pd

# 1. Configuração de Estética e Layout High-End
st.set_page_config(page_title="Gestão de Comissões | Padrão Globus", layout="wide", page_icon="💎")

# CSS Customizado Ultra-Premium
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
        Para o cálculo de comissão, ignoramos o custo de apólice e o imposto (IOF). Se um cliente paga **R$ 1.100,00**, mas o prêmio líquido é **R$ 1.000,00** e a comissão é **20%**, o corretor recebe **R$ 200,00**.
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
    dados_m = [
        {"Ramo": "Seguro de Vida (Individual)", "M": 30, "Obs": "Foco em proteção familiar."},
        {"Ramo": "Seguro Saúde (PME)", "M": 25, "Obs": "Baseado na primeira fatura."},
        {"Ramo": "Seguro Automóvel", "M": 20, "Obs": "Commodity de alta rotatividade."}
    ]
    for i in dados_m:
        st.markdown(f"**{i['Ramo']}** — Teto: **{i['M']}%**")
        st.progress(i['M']/30)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 3: FLUXO & SISTEMA QUIVER ---
with tabs[2]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("## Fluxo & Sistema: A Lógica Quiver")
    
    col_q1, col_q2 = st.columns([1, 1.5])
    
    with col_q1:
        st.markdown("### Configurações de Cadastro")
        p_mensal_q = st.number_input("Valor da Parcela do Cliente (R$)", value=400.0, step=50.0)
        p_perc_q = st.number_input("Percentual de Comissão (%)", value=20.0, step=0.1, key="q_perc")
        
        v_total_prev = (p_mensal_q * 12) * (p_perc_q / 100)
        st.markdown(f"**Comissão Prevista no Sistema:** R$ {v_total_prev:,.2f}")
        lastro_check = st.checkbox("Respeitar Regra de Lastro (Prêmio Líquido)", value=True)

    with col_q2:
        st.markdown("### O Gatilho do Recebimento")
        st.write("""
        O **Quiver** aguarda a baixa do extrato. Se a comissão prevista for **R$ 1.000,00**, mas a parcela do cliente for **R$ 400,00**:
        1. O sistema baixa **R$ 400,00** no Mês 01 (**Valor X**).
        2. O sistema deixa **R$ 600,00** pendentes para os meses subsequentes (**Valor Y**).
        """)
        
        fluxo_q = []
        rest_q = v_total_prev
        for m in range(1, 13):
            pago = min(rest_q, p_mensal_q) if lastro_check else (rest_q if m==1 else 0)
            rest_q -= pago
            fluxo_q.append({"Mês": f"Mês {m:02d}", "Recebimento": pago, "Status": "Pico (X)" if m==1 else ("Residual (Y)" if pago > 0 else "Silêncio")})
        
        st.data_editor(pd.DataFrame(fluxo_q), hide_index=True, use_container_width=True, disabled=True,
                       column_config={"Recebimento": st.column_config.NumberColumn(format="R$ %.2f")})
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 4: SIMULADOR COMPARATIVO (ATUALIZADO) ---
with tabs[3]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("## Simulação: Valor Total vs. Valor Parcelado")
    
    c_comp1, c_comp2 = st.columns([1, 2])
    with c_comp1:
        val_premio_anual = st.number_input("Prêmio Líquido Anual (R$)", value=5000.0, step=100.0)
        val_com_perc_sim = st.number_input("Comissão do Corretor (%)", value=20.0, step=1.0, key="sim_comp_perc")
        com_total_anual_sim = val_premio_anual * (val_com_perc_sim / 100)
        
        # ESCOLHA DA OPÇÃO
        modelo_pagto = st.radio("Escolha o Modelo de Recebimento:", ["Total (Esgotamento no Mês 1)", "Parcelado"])
        
        if modelo_pagto == "Parcelado":
            qtd_parcelas = st.number_input("Em quantas vezes foi parcelado?", min_value=2, max_value=12, value=12)
        else:
            qtd_parcelas = 1

    with c_comp2:
        val_por_parcela = com_total_anual_sim / qtd_parcelas
        st.markdown(f'<div class="metric-card"><p class="metric-label">Valor por Recebimento</p><p class="metric-val">R$ {val_por_parcela:,.2f}</p><p style="font-size:0.7rem">Distribuído em {qtd_parcelas}x</p></div>', unsafe_allow_html=True)

        st.markdown("### Cronograma de Recebimento")
        comp_data_sim = []
        for m in range(1, 13):
            valor_m_sim = val_por_parcela if m <= qtd_parcelas else 0.0
            comp_data_sim.append({
                "Mês": f"Mês {m:02d}",
                "Fluxo de Caixa": valor_m_sim
            })
        st.table(pd.DataFrame(comp_data_sim).style.format({"Fluxo de Caixa": "R$ {:.2f}"}))
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 5: ESGOTAMENTO & ESTORNO ---
with tabs[4]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("## Engenharia de Estorno (Pro-rata Temporis)")
    st.latex(r"C_e = C_a \times \frac{T_r}{T_t}")
    col_e1, col_e2 = st.columns([1, 2])
    with col_e1:
        c_recebida_e = st.number_input("Comissão Recebida (R$)", value=1200.0)
        m_vividos = st.slider("Meses Decorridos (Pagos)", 1, 12, 4)
        estorno_final = c_recebida_e * ((12 - m_vividos) / 12)
    with col_e2:
        st.markdown(f'<div class="metric-card" style="border-color: #F87171;"><p class="metric-label">Valor do Estorno</p><p class="metric-val" style="color: #F87171;">R$ {estorno_final:,.2f}</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- CAPÍTULO 6: GOVERNANÇA ---
with tabs[5]:
    st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
    st.markdown("## 06. Governança e Escala Operacional")
    st.write("A governança de comissões separa corretoras amadoras de empresas de alta performance.")
    
    col_g1, col_g2 = st.columns(2)
    with col_g1:
        st.markdown('<div class="concept-card"><h4>1. Conciliação Automatizada</h4><p>Importar arquivos de extratos diretamente no Quiver elimina erros manuais que podem custar até 5% da receita.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="concept-card"><h4>2. Reserva de Estorno</h4><p>Manter de 15% a 20% da receita em fundo de reserva protege o fluxo de caixa contra cancelamentos inesperados.</p></div>', unsafe_allow_html=True)
    with col_g2:
        st.markdown('<div class="concept-card"><h4>3. Auditoria de Repasses</h4><p>Garantir que produtores parceiros também sigam a regra de estorno proporcional conforme o contrato estabelecido.</p></div>', unsafe_allow_html=True)
        st.markdown('<div class="concept-card"><h4>4. Compliance SUSEP</h4><p>Transparência total conforme a Circular 612, mantendo os valores de corretagem disponíveis ao segurado.</p></div>', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align: center; color: #475569; font-size: 0.8rem;">© 2026 | INTELIGÊNCIA EM SEGUROS • PADRÃO PROFISSIONAL GLOBUS</p>', unsafe_allow_html=True)
