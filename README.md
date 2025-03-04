# BI STEAM GAMES

Este projeto é um dashboard interativo para análise de jogos da plataforma Steam. Ele permite visualizar métricas como taxa de aceitação, reviews positivos e negativos, e outras informações relevantes sobre os jogos. O dashboard foi desenvolvido usando **Streamlit** e **Plotly** para visualizações interativas, e os dados são armazenados em um banco de dados SQLite.

---

## **Funcionalidades**

1. **Filtros Interativos:**
   - Selecione um ou mais desenvolvedores para visualizar os **top 15 jogos** com base na taxa de aceitação.
   
2. **KPIs:**
   - Total de Reviews.
   - Total de Reviews Positivos.
   - Total de Reviews Negativos.
   - Taxa de Aceitação Média.

3. **Gráficos Interativos:**
   - Gráfico de barras horizontais mostrando a taxa de aceitação dos top 15 jogos.

4. **Tabela de Dados:**
   - Exibe os dados dos top 15 jogos, incluindo nome do jogo, desenvolvedor, taxa de aceitação, total de reviews, reviews positivos e negativos.

---

## **Tecnologias Utilizadas**

- **Python**: Linguagem de programação principal.
- **Streamlit**: Framework para criação de dashboards interativos.
- **Plotly**: Biblioteca para criação de gráficos interativos.
- **SQLite**: Banco de dados para armazenamento dos dados.
- **Pandas**: Manipulação e análise de dados.
- **link da base de dados utilizada :**
  https://www.kaggle.com/datasets/srgiomanhes/steam-games-dataset-2025
---

## **Como Executar o Projeto**

### **Pré-requisitos**

1. **Python 3.8 ou superior**: Certifique-se de ter o Python instalado.
2. **Pip**: Gerenciador de pacotes do Python.

### **Passos para Execução**

1. **Clone o repositório:**
   ```bash
   git clone https://github.com/HenriquePizara/steam-games.git
   cd bi-steam-games
2. **Crie um ambiente virtual (opcional, mas recomendado)**
   ```bash
    python -m venv venv
    source venv/bin/activate  # No Windows: venv\Scripts\activate
3. **Instale as dependências:**
   ```bash
   pip install -r requirements.txt
4. **Execute o projeto:**
   ```bash
   streamlit run viewer.py
