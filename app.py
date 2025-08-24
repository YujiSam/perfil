import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy import stats

# ======================
# Configuração inicial
# ======================
st.set_page_config(page_title="Meu Dashboard Profissional", layout="wide")

# ======================
# Menu de navegação
# ======================
menu = st.sidebar.radio("Navegação", ["Home", "Formação e Experiência", "Skills", "Análise de Dados"])

# ======================
# Aba Home
# ======================
if menu == "Home":
    st.title("Bem-vindo ao meu Dashboard 🚀")
    st.subheader("Apresentação Pessoal")
    st.write("""
    Olá, meu nome é Gustavo Yuji Osugi.  
    Este dashboard foi desenvolvido em Python + Streamlit para apresentar meu perfil profissional e realizar uma análise de dados aplicada.
    """)
    st.markdown("**Objetivo profissional:** Aqui você descreve em poucas linhas seu objetivo.")

# ======================
# Aba Formação e Experiência
# ======================
elif menu == "Formação e Experiência":
    st.title("🎓 Formação Acadêmica e Experiência")
    st.write("- Graduando na FIAP em Engenharia de Software (2024 - 2027)")
    st.write("- Cursos relevantes: Alura Javascript")

# ======================
# Aba Skills
# ======================
elif menu == "Skills":
    st.title("💡 Minhas Skills")
    st.write("**Tecnologias:** Python, Javascript, HTML, CSS, Streamlit, etc.")
    st.write("**Ferramentas:** Git, Vscode, PyCharm")
    st.write("**Soft Skills:** Comunicação, Trabalho em equipe, Resolução de problemas")

# ======================
# Aba Análise de Dados
# ======================
elif menu == "Análise de Dados":
    st.title("📊 Análise de Dados")

    st.subheader("1. Carregando os dados")
    uploaded_file = st.file_uploader("Envie um arquivo CSV para análise", type="csv")

    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        st.write("Visualização inicial dos dados:")
        st.dataframe(df.head())

        # Tipos de variáveis
        st.subheader("Tipos de variáveis")
        st.write(df.dtypes)

        # Medidas centrais
        st.subheader("2. Medidas centrais e análise inicial")
        st.write("Descrição estatística dos dados numéricos:")
        st.write(df.describe())

        # Distribuição de uma variável numérica
        col_num = st.selectbox("Escolha uma coluna numérica para visualizar a distribuição:", df.select_dtypes(include=np.number).columns)
        fig, ax = plt.subplots()
        sns.histplot(df[col_num], kde=True, ax=ax)
        st.pyplot(fig)

        # Correlação
        st.subheader("Correlação entre variáveis")
        corr = df.corr()
        fig, ax = plt.subplots(figsize=(6,4))
        sns.heatmap(corr, annot=True, cmap="coolwarm", ax=ax)
        st.pyplot(fig)

        # Teste de hipótese
        st.subheader("3. Intervalo de Confiança e Teste de Hipótese")
        st.write("Exemplo: Testar se a média de uma variável é igual a um valor hipotético.")

        col_test = st.selectbox("Escolha uma coluna numérica para o teste:", df.select_dtypes(include=np.number).columns)
        hipotese = st.number_input("Digite o valor da média hipotética:", value=0.0)

        # t-test
        t_stat, p_value = stats.ttest_1samp(df[col_test].dropna(), hipotese)

        st.write(f"Estatística t: {t_stat:.4f}")
        st.write(f"p-valor: {p_value:.4f}")

        if p_value < 0.05:
            st.success("Rejeitamos a hipótese nula: a média é diferente do valor hipotético.")
        else:
            st.info("Não rejeitamos a hipótese nula: não há evidência suficiente para dizer que a média é diferente.")

