import streamlit as st
from datetime import datetime
import pandas as pd
import plotly.express as px
from banco import Banco  # Importe a classe Banco

banco = Banco()

# Configuração da página
st.set_page_config(page_title="BI STEAM GAMES", layout="wide")

# Menu lateral
st.sidebar.title("Menu")
opcao = st.sidebar.radio("Selecione o Dashboard", ["Analise Games"])

# Função para carregar e consolidar as bases de vendas
@st.cache_data
def carrega_dados():
    base = banco.viewer()
    base['taxa_aceitacao'] = (base['total_positivo'] / base['total_reviews']) * 100
    return base

def mostrar_filtros_aplicados(filtro_desenvolvedor):
    filtros = []
    if filtro_desenvolvedor:
        filtros.append(f"Desenvolvedor: {', '.join(filtro_desenvolvedor)}")
    if filtros:
        st.write(f"**Filtros aplicados:** {', '.join(filtros)}")
    else:
        st.write("**Filtros aplicados:** Nenhum")

def dashboard_games():
    st.title("Dashboard Games Steam")
    
    # Carregar base consolidada
    base = carrega_dados()

    # Verificar coluna price_initial_usd
    if 'price_initial_usd' not in base.columns:
        st.error("Coluna 'price_initial_usd' não encontrada.")
        return
    base['price_initial_usd'] = pd.to_numeric(base['price_initial_usd'], errors='coerce').fillna(0)
    base['price_initial_usd'] = round(base['price_initial_usd'], 2)
    base['review_score'] = pd.to_numeric(base['review_score'], errors='coerce').fillna(0)

    # --- Submenu de Filtros ---
    st.sidebar.header("Filtros")

    # Filtro de desenvolvedor
    desenvolvedores = base['desenvolvedor'].unique() if 'desenvolvedor' in base.columns else []
    filtro_desenvolvedor = st.sidebar.multiselect(
        "Selecione o Desenvolvedor",
        options=desenvolvedores,
        key="filter_desenvolvedor"
    )

    mostrar_filtros_aplicados(filtro_desenvolvedor)

    # --- Aplicar Filtros ---
    base_filtrada = base.copy()
    if filtro_desenvolvedor:
        base_filtrada = base_filtrada.loc[base_filtrada['desenvolvedor'].isin(filtro_desenvolvedor)]
    
    # Ordenar os jogos pela taxa de aceitação (do maior para o menor) e pegar os top 15
    top_15_jogos = base_filtrada.sort_values(by='taxa_aceitacao', ascending=False).head(15)

    st.header("Análise dos Top 15 Jogos por Taxa de Aceitação")

    # ============= KPIs =============
    try:
        col1, col2, col3, col4 = st.columns(4)
        
        # KPI 1 - Valor Total de Reviews
        total_reviews = top_15_jogos['total_reviews'].sum()
        col1.metric(
            label="💰 Total de Reviews",
            value=f"{total_reviews:,.0f}".replace(",", "v").replace(".", ",").replace("v", "."),
            help="Valor total de Reviews"
        )

        # KPI 2 - Reviews positivos
        reviews_positivo = top_15_jogos['total_positivo'].sum()
        col2.metric(
            label="📦 Total de Reviews Positivos",
            value=f"{reviews_positivo:,}".replace(",", "."),
            help="Total Reviews Positivos"
        )

        # KPI 3 - Reviews Negativos
        reviews_negativos = top_15_jogos['total_negativo'].sum()
        col3.metric(
            label="📦 Total de Reviews Negativos",
            value=f"{reviews_negativos:,}".replace(",", "."),
            help="Total Reviews Negativos"
        )

        # KPI 4 - Taxa de Aceitação Média
        taxa_media = top_15_jogos['taxa_aceitacao'].mean()
        col4.metric(
            label="📊 Taxa de Aceitação Média",
            value=f"{taxa_media:.2f}%",
            help="Taxa de Aceitação Média dos Top 15 Jogos"
        )

    except KeyError as e:
        st.error(f"Erro ao calcular KPIs: Coluna não encontrada - {e}")
    # ============= FIM DOS KPIs =============

    # Gráfico de barras horizontais com Plotly Express
    fig = px.bar(
        top_15_jogos,
        y='jogo',  # Jogos no eixo Y
        x='taxa_aceitacao',  # Taxa de aceitação no eixo X
        title='Top 15 Jogos por Taxa de Aceitação',
        labels={'jogo': 'Jogo', 'taxa_aceitacao': 'Taxa de Aceitação (%)'},
        text='taxa_aceitacao',  # Exibe os valores nas barras
        color='jogo',  # Colora as barras por jogo
        orientation='h',  # Barras horizontais
    )
    fig.update_traces(texttemplate='%{text:.2f}%', textposition='outside')  # Formatação dos valores
    fig.update_layout(
        xaxis_title="Taxa de Aceitação (%)",
        yaxis_title="Jogo",
        showlegend=False,  # Remove a legenda desnecessária
    )

    # Exibir gráfico no Streamlit
    st.plotly_chart(fig, use_container_width=True)

    # Exibir tabela com os top 15 jogos
    st.write("Dados dos Top 15 Jogos:")
    st.dataframe(top_15_jogos[['jogo', 'desenvolvedor', 'taxa_aceitacao', 'total_reviews', 'total_positivo', 'total_negativo']])

# Navegação entre os dashboards
if opcao == "Analise Games":
    dashboard_games()