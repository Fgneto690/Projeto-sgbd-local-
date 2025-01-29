import sqlite3

#conexões com o banco de dados

conexao = sqlite3.connect('banco.db')
cursor = conexao.cursor()

#criando a tabela de produtos

cursor.execute('''
    CREATE TABLE IF NOT EXISTS produtos (
        Id INTEGER PRIMARY KEY AUTOINCREMENT,
        nome TEXT NOT NULL,
        preco REAL NOT NULL,
        estoque INTEGER NOT NULL
    ) 
''')

#criando a tabela de vendas

cursor.execute('''
    CREATE TABLE IF NOT EXISTS vendas (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        id_produto INTEGER NOT NULL,
        quantidade INTEGER NOT NULL,
        data text not NULL,
       foreign key (id_produto) references produtos(id)
    )
''')

print('Tabelas criadas com sucesso')
#fechando a conexão com o banco de dados

cursor.execute('''CREATE TABLE IF NOT EXISTS log_estoque (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    id_produto INTEGER NOT NULL,
    name_produto TEXT NOT NULL,
    quantidade INTEGER NOT NULL,
    operacao TEXT NOT NULL,
    data TEXT NOT NULL,
    FOREIGN KEY (id_produto) REFERENCES produtos(id)
    )
''')

print("Tabela log_estoque criada com sucesso")

conexao.commit()

cursor.close()
conexao.close()
