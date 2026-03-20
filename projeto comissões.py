import streamlit as st
import pandas as pd
import plotly.express as px
import plotly.graph_objects as go

# 1. Configuração de Estética e Layout High-End
st.set_page_config(page_title="Gestão de Comissões | Padrão Globus", layout="wide", page_icon="💎")

# CSS Customizado para Visual E-book de Mercado (Grupo Maldivas / Globus Style)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Montserrat:wght@300;400;700&family=Inter:wght@300;400;600&display=swap');
    
    html, body, [class*="css"] { font-family: 'Inter', sans-serif; background-color: #0F172A; }
    .stApp { background: radial-gradient(circle at top right, #1E293B, #0F172A); color: #F8FAFC; }
    
    /* Header Estilizado */
    .main-title { 
        font-family: 'Montserrat', sans-serif; 
        font-weight: 700; font-size: 3.2rem; 
        background: linear-gradient(90deg, #FFFFFF, #94A3B8);
        -webkit-background-clip: text; -webkit-text-fill-color: transparent;
        margin-bottom: 5px;
    }
    .sub-title { color: #60A5FA; font-size: 0.9rem; letter-spacing: 3px; text-transform: uppercase; margin-bottom: 40px; font-weight: 600; }

    /* Cards de Conteúdo Estilo Glassmorphism */
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
        transition: transform 0.3s ease;
    }
    .regra-card:hover { transform: translateY(-5px); background: rgba(255, 255, 255, 0.05); }
    .regra-card h4 { color: #3B82F6; margin-top: 0; font-family: 'Montserrat', sans-serif; text-transform: uppercase; font-size: 0.9rem; }
    
    /* Tabs Customizadas */
    .stTabs [data-baseweb="tab-list"] { gap: 40px; border-bottom: 1px solid rgba(255,255,255,0.1); }
    .stTabs [data-baseweb="tab"] {
        height: 60px; background: transparent !important; color: #94A3B8 !important;
        font-family: 'Montserrat', sans-serif; font-size: 0.85rem; border: none !important;
        letter-spacing: 1px;
    }
    .stTabs [aria-selected="true"] { color: #FFFFFF !important; border-bottom: 2px solid #3B82F6 !important; font-weight: 700; }
    
    /* Ajuste de Texto */
    p { color: #CBD5E1; line-height: 1.6; }
    li { color: #CBD5E1; margin-bottom: 8px; }
    b, strong { color: #FFFFFF; }
    </style>
    """, unsafe_allow_html=True)

# --- CABEÇALHO ---
st.markdown('<h1 class="main-title">A Bíblia da Comissão</h1>', unsafe_allow_html=True)
st.markdown('<p class="sub-title">Inteligência Financeira & Estratégia de Recebimento</p>', unsafe_allow_html=True)

# --- CONTEÚDO EM CAPÍTULOS ---
tab1, tab2, tab3, tab4 = st.tabs(["01. CONCEITO", "02. MERCADO", "03. FLUXO DE CAIXA", "04. GOVERNANÇA"])

with tab1:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: 'Montserrat';">O Alicerce Estratégico</h2>
        <p>A <b>tabela de comissão de corretora de seguros</b> define os percentuais que o corretor recebe por cada apólice vendida. 
        Estes valores variam conforme o ramo (vida, automóvel, empresarial, saúde etc.), de acordo com a seguradora e o modelo de atuação do corretor.</p>
        <p>Ela é essencial para <b>organizar os repasses</b>, prever ganhos e manter a gestão financeira da corretora em dia, funcionando como um GPS de rentabilidade.</p>
        <div style="display: flex; gap: 20px; margin-top: 20px;">
            <div style="flex: 1; padding: 15px; background: rgba(59, 130, 246, 0.1); border-radius: 10px;">
                <span style="color: #3B82F6; font-weight: bold;">Pelas Corretoras:</span> Para padronizar repasses e acompanhar o desempenho comercial.
            </div>
            <div style="flex: 1; padding: 15px; background: rgba(16, 185, 129, 0.1); border-radius: 10px;">
                <span style="color: #10B981; font-weight: bold;">Pelas Seguradoras:</span> Para definir percentuais autorizados e controlar o canal de distribuição.
            </div>
        </div>
    </div>
    """, unsafe_allow_html=True)

with tab2:
    st.markdown('<div class="ebook-section"><h2 style="font-family: Montserrat;">Percentuais Médios 2026</h2>', unsafe_allow_html=True)
    
    # Dados baseados no seu texto original
    dados_mercado = {
        'Tipo de Seguro': ['Automóvel', 'Vida', 'Saúde', 'Empresarial', 'Residencial'],
        'Min %': [10, 20, 15, 15, 10],
        'Max %': [20, 30, 25, 25, 15],
        'Perfil': ['Alta Renovação', 'Alta Margem', 'Recorrência Mensal', 'Contratos Robustos', 'Complementar']
    }
    df_m = pd.DataFrame(dados_mercado)

    c1, c2 = st.columns([2, 1])
    with c1:
        fig_m = go.Figure()
        fig_m.add_trace(go.Bar(name='Mínimo', x=df_m['Tipo de Seguro'], y=df_m['Min %'], marker_color='#1E40AF'))
        fig_m.add_trace(go.Bar(name='Máximo', x=df_m['Tipo de Seguro'], y=df_m['Max %'], marker_color='#3B82F6'))
        fig_m.update_layout(barmode='group', template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)', height=400)
        st.plotly_chart(fig_m, use_container_width=True)
    
    with c2:
        st.markdown("### Mix de Carteira")
        st.write("Entender estes percentuais é vital para o planejamento estratégico. Seguros de **Vida** e **Saúde** costumam oferecer as melhores margens e estabilidade.")
        st.table(df_m[['Tipo de Seguro', 'Max %']])
    st.markdown('</div>', unsafe_allow_html=True)

with tab3:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: Montserrat;">As 3 Regras de Recebimento</h2>
        <p>O fluxo de caixa da corretora é determinado pela forma como a comissão é liberada pela seguradora:</p>
    </div>
    """, unsafe_allow_html=True)

    r1, r2, r3 = st.columns(3)
    with r1:
        st.markdown('<div class="regra-card"><h4>TOTAL (Upfront)</h4>Recebimento integral da comissão no início da vigência. Traz liquidez imediata para reinvestir na aquisição de novos clientes.</div>', unsafe_allow_html=True)
    with r2:
        st.markdown('<div class="regra-card" style="border-top-color: #60A5FA;"><h4>PARCELADO (Pro-rata)</h4>A comissão é diluída durante os meses de pagamento. Garante previsibilidade e protege contra estornos por cancelamento.</div>', unsafe_allow_html=True)
    with r3:
        st.markdown('<div class="regra-card" style="border-top-color: #93C5FD;"><h4>ESGOTAMENTO</h4>Foco total de recebimento nas primeiras parcelas da apólice, antecipando o lucro sem depender de todo o período contratual.</div>', unsafe_allow_html=True)

    st.markdown("<br><br>", unsafe_allow_html=True)
    
    # SIMULADOR DINÂMICO
    with st.container():
        st.markdown('<div class="ebook-section">', unsafe_allow_html=True)
        st.subheader("Simulador de Engenharia Financeira")
        cs1, cs2 = st.columns([1, 2])
        
        with cs1:
            valor_total = st.number_input("Comissão Total Estimada (R$)", value=3600.0, step=100.0)
            regra_sel = st.selectbox("Escolha a Regra de Fluxo", ["Total", "Parcelado", "Esgotamento"])
            
            # Dinâmica do Esgotamento Flexível
            if regra_sel == "Esgotamento":
                n_meses_esg = st.number_input("Esgotar o valor em quantos meses?", min_value=1, value=3)
                vigencia = st.number_input("Vigência total da apólice (Meses)", min_value=n_meses_esg, value=12)
            else:
                vigencia = st.number_input("Vigência total da apólice (Meses)", min_value=1, value=12)
                n_meses_esg = 1

        # Lógica de Fluxo
        meses_lista = list(range(1, vigencia + 1))
        fluxo_caixa = [0.0] * vigencia
        
        if regra_sel == "Total":
            fluxo_caixa[0] = valor_total
        elif regra_sel == "Parcelado":
            fluxo_caixa = [valor_total / vigencia] * vigencia
        elif regra_sel == "Esgotamento":
            for i in range(n_meses_esg):
                fluxo_caixa[i] = valor_total / n_meses_esg
        
        with cs2:
            fig_fluxo = go.Figure()
            fig_fluxo.add_trace(go.Bar(x=meses_lista, y=fluxo_caixa, marker_color='#3B82F6', name="Receita Bruta"))
            fig_fluxo.update_layout(
                title=f"Projeção de Entrada de Receita ({regra_sel})",
                template='plotly_dark', paper_bgcolor='rgba(0,0,0,0)', plot_bgcolor='rgba(0,0,0,0)',
                xaxis=dict(title="Mês da Vigência"), yaxis=dict(title="R$")
            )
            st.plotly_chart(fig_fluxo, use_container_width=True)
        st.markdown('</div>', unsafe_allow_html=True)

with tab4:
    st.markdown("""
    <div class="ebook-section">
        <h2 style="font-family: Montserrat;">Governança & Escala</h2>
        <p>O valor da comissão vai além da tabela fixa. O corretor estratégico atua sobre 4 variáveis de crescimento:</p>
        <ol>
            <li><b>Volume de Produção:</b> Metas atingidas geram bônus progressivos junto às seguradoras.</li>
            <li><b>Tipo de Apólice:</b> Contratos corporativos e frotas geram comissões robustas e negociáveis.</li>
            <li><b>Experiência:</b> Uma base sólida de clientes permite negociar condições diferenciadas.</li>
            <li><b>Automação:</b> Utilizar tecnologia para conferir repasses evita a perda de até 15% da receita por erros operacionais.</li>
        </ol>
        <p style="margin-top: 20px;"><b>Conclusão:</b> A comissão é o combustível, mas a gestão é o motor que transforma esforço em patrimônio.</p>
    </div>
    """, unsafe_allow_html=True)
    
    if st.button("FINALIZAR E-BOOK E GERAR RELATÓRIO"):
        st.balloons()
        st.success("Jornada concluída. Aplique a inteligência de fluxo de caixa para escalar seus resultados.")

# --- FOOTER ---
st.markdown("---")
st.markdown('<p style="text-align: center; color: #475569; font-size: 0.8rem;">© 2026 | Inteligência em Seguros - Padrão de Gestão Profissional</p>', unsafe_allow_html=True)