import os
import mysql.connector
from dotenv import load_dotenv


load_dotenv()

def obter_conexao(com_banco=True):
    
    config = {
        "host": os.getenv("DB_HOST", "localhost"),
        "user": os.getenv("DB_USER", "root"),
        "password": os.getenv("DB_PASSWORD"),
        "port": int(os.getenv("DB_PORT", 3306)),
    }
    if com_banco:
        config["database"] = os.getenv("DB_NAME", "bot_rpa")
        
    return mysql.connector.connect(**config)

def iniciar_banco():
    
    try:
        conexao = obter_conexao(com_banco=False)
        cursor = conexao.cursor()
        db_name = os.getenv("DB_NAME", "bot_rpa")
        cursor.execute(f"CREATE DATABASE IF NOT EXISTS {db_name}")
        cursor.close()
        conexao.close()

        conexao = obter_conexao(com_banco=True)
        cursor = conexao.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS pendencias (
                id INT PRIMARY KEY,
                titulo VARCHAR(255) NOT NULL
            )
        """)
        conexao.commit()
        cursor.close()
        conexao.close()
        print("[DATABASE] Banco MySQL e tabela verificados com sucesso!")
    except mysql.connector.Error as err:
        print(f"[ERRO MYSQL] Falha na inicialização do banco: {err}")

def pendencias_ja_processadas(item_id):
    
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute("SELECT id FROM pendencias WHERE id = %s", (item_id,))
        resultado = cursor.fetchone()
        cursor.close()
        conexao.close()
        return resultado is not None
    except mysql.connector.Error as err:
        print(f"[ERRO MYSQL] Erro ao consultar ID {item_id}: {err}")
        return False

def salvar_pendencias(item_id, titulo):
    
    try:
        conexao = obter_conexao()
        cursor = conexao.cursor()
        cursor.execute(
            "INSERT INTO pendencias (id, titulo) VALUES (%s, %s)",
            (item_id, titulo)
        )
        conexao.commit()
        cursor.close()
        conexao.close()
    except mysql.connector.Error as err:
        print(f"[ERRO MYSQL] Erro ao salvar ID {item_id}: {err}")