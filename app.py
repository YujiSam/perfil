import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats
import plotly.express as px

# ======================
# Configuração inicial
# ======================
st.set_page_config(
    page_title="Meu Dashboard Profissional",
    layout="wide",
    page_icon="🚀"
)

# ======================
# Sidebar personalizada
# ======================
st.sidebar.header("📌 Navegação")
menu = st.sidebar.radio("", ["Home", "Formação e Experiência", "Skills", "Análise de Dados"])

# ======================
# Aba Home
# ======================
if menu == "Home":
    st.markdown("<h1 style='text-align: center; color: #4B8BBE;'>Bem-vindo ao meu Dashboard 🚀</h1>", unsafe_allow_html=True)
    st.subheader("Apresentação Pessoal")
    st.write("""
    Olá, meu nome é **Gustavo Yuji Osugi**.  
    Este dashboard foi desenvolvido em Python + Streamlit para apresentar meu perfil profissional e realizar análises de dados aplicadas.
    """)
    st.markdown("**Objetivo profissional:** Aprender com desenvolvedores experientes e evoluir minhas habilidades em desenvolvimento Full-Stack.")

# ======================
# Aba Formação e Experiência
# ======================
elif menu == "Formação e Experiência":
    st.markdown("## 🎓 Formação Acadêmica e Experiência")
    st.write("- Graduando na **FIAP** em Engenharia de Software (2024 - 2027)")
    st.write("- Cursos relevantes: Javascript - Alura, Design Thinking - FIAP")

# ======================
# Aba Skills
# ======================
elif menu == "Skills":
    st.markdown("## 💡 Minhas Skills")
    col1, col2, col3 = st.columns(3)
    col1.subheader("Tecnologias")
    col1.write("Python, Javascript, C++, HTML, CSS, Streamlit, React.js, Node.js, Tailwind CSS")
    col2.subheader("Ferramentas")
    col2.write("Git, VSCode, PyCharm")
    col3.subheader("Soft Skills")
    col3.write("Comunicação, Trabalho em equipe, Resolução de problemas")

# ======================
# Aba Análise de Dados
# ======================
elif menu == "Análise de Dados":
    st.markdown("## 📊 Análise de Dados")
    
    st.subheader("1. Carregando os dados")
    uploaded_file = st.file_uploader("Envie um arquivo CSV para análise", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("### Visualização inicial dos dados")
        st.dataframe(df.head(), use_container_width=True)

        # Tipos de variáveis
        st.subheader("Tipos de variáveis")
        st.write(df.dtypes)

        # Métricas resumidas
        numeric_cols = df.select_dtypes(include=np.number).columns
        if len(numeric_cols) > 0:
            st.subheader("📈 Métricas rápidas")
            col1, col2, col3 = st.columns(3)
            col1.metric("Número de linhas", df.shape[0])
            col2.metric("Número de colunas", df.shape[1])
            col3.metric("Colunas numéricas", len(numeric_cols))

        # Distribuição de uma variável numérica
        if len(numeric_cols) > 0:
            st.subheader("2. Distribuição de uma variável numérica")
            col_num = st.selectbox("Escolha uma coluna numérica:", numeric_cols)
            
            # Histograma interativo
            fig = px.histogram(df, x=col_num, nbins=20, title=f"Distribuição de {col_num}", marginal="box")
            st.plotly_chart(fig, use_container_width=True)
            
            # Heatmap de correlação
            st.subheader("3. Correlação entre variáveis")
            corr = df[numeric_cols].corr()
            fig, ax = plt.subplots(figsize=(8,5))
            sns.set_style("whitegrid")
            sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
            st.pyplot(fig)

            # Teste de hipótese
            st.subheader("4. Intervalo de Confiança e Teste de Hipótese")
            st.write("Teste se a média de uma coluna numérica é igual a um valor hipotético.")
            col_test = st.selectbox("Escolha a coluna para o teste:", numeric_cols)
            hipotese = st.number_input("Digite o valor da média hipotética:", value=0.0)

            t_stat, p_value = stats.ttest_1samp(df[col_test].dropna(), hipotese)
            col1, col2 = st.columns(2)
            col1.metric("Estatística t", round(t_stat, 4))
            col2.metric("p-valor", round(p_value, 4))

            if p_value < 0.05:
                st.success("Rejeitamos a hipótese nula: a média é diferente do valor hipotético.")
            else:
                st.info("Não rejeitamos a hipótese nula: não há evidência suficiente para dizer que a média é diferente.")
