from .conexao import conectar_banco, executar_consulta
from datetime import datetime

def registrar_vendas(id_produto, quantidade):
        conexao = conectar_banco()
        cursor = conexao.cursor()

        cursor.execute("SELECT estoque FROM produtos WHERE id = ?", (id_produto,))
        resultado = cursor.fetchone()

        if not resultado:
            return

        estoque = resultado[0]
        if quantidade > estoque:
            return

        cursor.execute(
            "UPDATE produtos SET estoque = estoque - ? WHERE id = ?", (quantidade, id_produto)
        )
        data = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        cursor.execute(
            "INSERT INTO vendas (id_produto, quantidade, data) VALUES (?, ?, ?)",
            (id_produto, quantidade, data),
        )
        conexao.commit()
        cursor.close()
        conexao.close()

def listar_vendas():
    query = "SELECT * FROM vendas"
    return executar_consulta(query)