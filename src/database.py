import sqlite3 

DB_PATH = "bot_database.db"

def iniciar_banco():

    conexao = sqlite3.connect(DB_PATH)

    cursor = conexao.cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS pendencias (
        id INTEGER PRIMARY KEY,
        titulo TEXT NOT NULL
    )
""")

    conexao.commit()
    conexao.close()

def pendencias_ja_processadas(item_id):

    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()
    cursor.execute("SELECT 1 FROM pendencias WHERE id = ?", (item_id,))
    resultado = cursor.fetchone()
    conexao.close()
    return resultado is not None
    

def salvar_pendencias(item_id, titulo):

    conexao = sqlite3.connect(DB_PATH)
    cursor = conexao.cursor()
    cursor.execute("INSERT INTO pendencias (id, titulo) VALUES (?, ?)", (item_id, titulo))
    conexao.commit()
    conexao.close()
    