from database.vendas import registrar_vendas, listar_vendas
from tkinter import messagebox
import tkinter as tk

def tela_listar_vendas(root):
    janela = tk.Toplevel(root)
    janela.title("Listar Vendas")
    
    vendas = listar_vendas()
    if not vendas:
        tk.Label(janela, text="Nenhuma venda registrada.").pack()
        return
    
    for venda in vendas:
        id_venda, id_produto, quantidade, data = venda
        tk.Label(janela, text=f"ID: {id_venda} - Produto: {id_produto} - Quantidade: {quantidade} - Data: {data}").pack()

def tela_registrar_vendas(root):
    janela = tk.Toplevel(root)
    janela.title("Registrar Venda")
    
    tk.Label(janela, text="ID do Produto:").pack()
    id_produto_entry = tk.Entry(janela)
    id_produto_entry.pack()
    
    tk.Label(janela, text="Quantidade:").pack()
    quantidade_entry = tk.Entry(janela)
    quantidade_entry.pack()
    
    def registrar():
        try:
            id_produto = int(id_produto_entry.get())
            quantidade = int(quantidade_entry.get())
            registrar_vendas(id_produto, quantidade)
            messagebox.showinfo("Sucesso", "Venda registrada com sucesso!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao registrar venda: {e}")
    
    tk.Button(janela, text="Registrar", command=registrar).pack()
    tk.Button(janela, text="Fechar", command=janela.destroy).pack()