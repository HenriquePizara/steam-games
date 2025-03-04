import sqlite3 as sq
import pandas as pd
class Banco(object):
    def __init__(self):
        self.path_base = '../data/'
        self.nm_banco = 'base.db'
        self.nm_arquivo = 'steam_games'
        self.nm_tabela = 'steam'
        self.conn = sq.connect(f'{self.path_base}{self.nm_banco}')
        self.cursor = self.conn.cursor()
    def create_table(self):
            
            self.cursor.execute(f'''
            CREATE TABLE IF NOT EXISTS {self.nm_tabela} (
    steam_appid INT PRIMARY KEY,
    jogo VARCHAR(255),
    desenvolvedor VARCHAR(255),
    publishers VARCHAR(255),
    categoria VARCHAR(255),
    genero VARCHAR(255),
    idade_min INT,
    n_achievements INT,
    plataforma VARCHAR(255),
    is_released VARCHAR(255),
    data_lancamento DATE,
    additional_content BOOLEAN,
    total_reviews INT,
    total_positivo INT,
    total_negativo INT,
    review_score FLOAT,
    review_score_desc VARCHAR(255),
    positive_percentual FLOAT,
    metacritic INT,
    free_to_play BOOLEAN,
    price_initial_usd FLOAT
)''')
    def read(self):
        pass
    def insert(self,df):
        try:
            # joga o nome das colunas em uma lista
            nm_colunas = df.columns.to_list()
            #aqui ele cria pra cada nome de coluna uma virgula e um '?'
            placeholders = ','.join(['?' for _ in nm_colunas])
            #comando insert sql , aqui vc tem q ja ter criado a tabela
            #no meu caso a tabela é 'info_vendas
            #if tp =='loja':
            cmd_sql = f"INSERT INTO {self.nm_tabela} ({', '.join(nm_colunas)}) VALUES ({placeholders}) ON CONFLICT (Pedido_Venda) DO NOTHING"
            # ele faz um join do nome da coluna,VALUES e  os placeholders 
            cmd_sql = f"INSERT INTO {self.nm_tabela} ({', '.join(nm_colunas)}) VALUES ({placeholders})"
            #aqui ele joga todas as linhas em uma lista
            rows_to_insert = df.values.tolist()
            #aqui ele execulta o insert , inserirndo os valores
            self.cursor.executemany(cmd_sql, rows_to_insert)
            self.conn.commit()
            self.conn.close()
            #return opcional, no meu caso queria ver a api p teste 
            #
        except Exception as e:
            print(f"Error inserting data: {str(e)}")
            self.conn.rollback()
        finally:
            self.conn.close()
    def viewer(self):
        query =  f'SELECT * FROM steam '#WHERE DataEmissaoNota BETWEEN {dt_inicio} AND  {dt_fim}
        df =pd.read_sql_query(query, self.conn)
        #results = self.cursor.fetchall()
        #self.conn.close()
        return df
