# etl.py
import pandas as pd
from src.banco import Banco  # Importe a classe Banco
banco = Banco()

def extract(path,nm_arquivo):
    df = pd.read_csv(f'{path}{nm_arquivo}')
    return df
def transform(df):
    # renomeia as colunas
    df = df.rename(columns={'name':'Jogo','developers':'Desenvolvedor','categories':'Categoria','genres':'Genero',
                            'required_age':'Idade_min','platforms':'Plataforma','release_date':'data_lancamento',
                            'total_positive':'Total_Positivo','total_negative':'Total_Negativo','is_free':'Free_to_play',
                            'price_initial (USD)':'price_initial_usd'})
    #df['data_lancamento'] =pd.to_datetime(df['data_lancamento'],errors='coerce')
    df['Desenvolvedor'] = df['Desenvolvedor'].astype('string')
    df['publishers'] = df['publishers'].astype('string')
    df['Categoria'] = df['Categoria'].astype('string')
    df['Genero'] = df['Genero'].astype('string')
    df['Jogo'] = df['Jogo'].astype('string')
    df['Plataforma'] = df['Plataforma'].astype('string')
    df['is_released'] = df['is_released'].astype('string')
    df = df.fillna(0)
    
    print(df.columns)
    df.info()
    return  df

def load(df):
    banco.insert(df)
    return df
def ETL(path,nm_arquivo):
    #extract
    df = extract(path,nm_arquivo)
    df = transform(df)
    df = load(df)
    #transform
   # df = pass
    #load
    return print('finalizado')