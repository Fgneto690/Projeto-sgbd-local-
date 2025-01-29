import tkinter as tk
from ui.tela_produtos import tela_adicionar_produtos, tela_listar_produtos, tela_editar_produto, tela_excluir_produtos
from ui.tela_vendas import registrar_vendas, tela_listar_vendas

def tela_principal(root):
    frame = tk.Frame(root)
    frame.pack(padx=10, pady=10)

    tk.Label(frame, text="Sistema de Gerenciamento de Loja", font=("Arial", 16)).pack(pady=10)

    # Botões para gerenciar produtos
    tk.Button(frame, text="Adicionar Produto", command=lambda: tela_adicionar_produtos(root)).pack(fill="x", pady=5)
    tk.Button(frame, text="Listar Produtos", command=lambda: tela_listar_produtos(root)).pack(fill="x", pady=5)
    tk.Button(frame, text="Editar Produto", command=lambda: tela_editar_produto(root)).pack(fill="x", pady=5)
    tk.Button(frame, text="Excluir Produto", command=lambda: tela_excluir_produtos(root)).pack(fill="x", pady=5)

    # Botões para gerenciar vendas
    tk.Button(frame, text="Registrar Venda", command=lambda: registrar_vendas(root)).pack(fill="x", pady=5)
    tk.Button(frame, text="Listar Vendas", command=lambda: tela_listar_vendas(root)).pack(fill="x", pady=5)

    # Botão para sair
    tk.Button(frame, text="Sair", command=root.quit).pack(fill="x", pady=5)
