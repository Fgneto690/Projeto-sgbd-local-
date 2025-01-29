from .conexao import executar_consulta, conectar_banco

def listar_produtos():
    query = "SELECT * FROM produtos"
    return executar_consulta(query)

def adicionar_produto(nome, preco, estoque):
    query = "INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)"
    executar_consulta(query, (nome, preco, estoque))

def editar_produtos(nome, preco):
        campos = []
        valores = []
        if nome:
            campos.append("nome = ?")
            valores.append(nome)
        if preco:
            campos.append("preco = ?")
            valores.append(preco)

        if not campos:
            return
        valores.append(id)
        query = f"UPDATE produtos SET {', '.join(campos)} WHERE id = ?"
        executar_consulta(query, valores)

def excluir_produtos(ids):
     placeholder = ', '.join('?' * len(ids))
     query = f"DELETE FROM produtos WHERE id IN ({placeholder})"
     executar_consulta(query, ids)

def autalizar_estoque(id_produto, quantidade):
    try:
        query_verificar = "SELECT estoque FROM produtos WHERE id = ?"
        produto = executar_consulta(query_verificar, (id_produto,))
        if not produto:
            return f"Error: Produto não encontrado"
        
        estoque_atual = produto[0][0]

        novo_estoque = estoque_atual + quantidade
        if novo_estoque < 0:
            return f'Error: Estoque insuficiente. Estoque atual: {estoque_atual}'
        
        query_atualizada = "UPDATE produtos SET estoque = ? WHERE id = ?"
        executar_consulta(query_atualizada, (quantidade, id_produto))
        return "Estoque atualizado com sucesso"

    except Exception as e:
        return f'Error: {e}'