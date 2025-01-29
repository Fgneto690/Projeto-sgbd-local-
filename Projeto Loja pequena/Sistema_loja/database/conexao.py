import sqlite3

DB_PATH = 'E:/Projeto Loja pequena/banco.db'

def conectar_banco():
    """Estabelece uma conexão com o banco de dados."""
    return sqlite3.connect(DB_PATH)

def executar_consulta(query, params=()):
    """Executa uma consulta no banco de dados."""
    try:
        conexao = conectar_banco()
        cursor = conexao.cursor()
        cursor.execute(query, params)
        conexao.commit()
        return cursor
    except Exception as e:
        raise e
    finally:
        cursor.close()
        conexao.close()
