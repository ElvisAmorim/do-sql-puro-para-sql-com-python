from dotenv import load_dotenv
import os
import cx_Oracle
import pandas as pd
# Carrega as variáveis do arquivo .env
load_dotenv()

# Acessa os valores
usuario = os.getenv("MASTER_DB_USER")
senha = os.getenv("MASTER_DB_PASSWORD")
host = os.getenv("MASTER_DB_HOST")
porta = os.getenv("MASTER_DB_PORT")
service = os.getenv("MASTER_DB_SERVICE")


def get_db_connection():
    try:
        dsn = cx_Oracle.makedsn(
            host=os.getenv("MASTER_DB_HOST"),
            port=os.getenv("MASTER_DB_PORT"),
            service_name=os.getenv("MASTER_DB_SERVICE")
        )

        connection = cx_Oracle.connect(
            user=os.getenv("MASTER_DB_USER"),
            password=os.getenv("MASTER_DB_PASSWORD"),
            dsn=dsn
        )

        print("Conexão estabelecida com sucesso!")
        return connection

    except cx_Oracle.DatabaseError as e:
        print(f"Erro ao conectar ao banco de dados Oracle: {e}")
        return None

def execultar_sql(query):
    try:
        df = pd.read_sql(query, conn)
        print(f"[OK] Consulta executada com sucesso. Linhas retornadas: {len(df)}")
        return df
    except Exception as e:
        print(f"[ERRO] Falha ao executar SQL:\n{e}")
        return pd.DataFrame()  # Retorna DF vazio se falhar
    
    
# Testando a função no Jupyter Notebook
conn = get_db_connection()

if conn:
    print("Você pode agora usar a variável `conn` para executar consultas.")
else:
    print("Verifique os parâmetros de conexão ou a rede.")
    
    
