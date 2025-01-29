import tkinter as tk
from tkinter import messagebox
from database.produtos import adicionar_produto, editar_produtos, listar_produtos, excluir_produtos,autalizar_estoque
 
def tela_adicionar_produtos(root):
    janela = tk.Toplevel(root)
    janela.title("Adicionar Produto")

    tk.Label(janela, text="Nome:").pack()
    nome_entry = tk.Entry(janela)
    nome_entry.pack()

    tk.Label(janela, text="Preço:").pack()
    preco_entry = tk.Entry(janela)
    preco_entry.pack()

    tk.Label(janela, text="Estoque:").pack()
    estoque_entry = tk.Entry(janela)
    estoque_entry.pack()

    def salvar():
        try:
            nome = nome_entry.get().strip()
            preco = float(preco_entry.get().strip())
            estoque = int(estoque_entry.get().strip())
            adicionar_produto(nome, preco, estoque)
            messagebox.showinfo("Sucesso", "Produto adicionado com sucesso!")
            janela.destroy()
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao adicionar produto: {e}")

    tk.Button(janela, text="Salvar", command=salvar).pack()
    tk.Button(janela, text="Fechar", command=janela.destroy).pack()

def tela_editar_produto(root):
    janela = tk.Toplevel(root)
    janela.title("Adicionar Produto")

    tk.Label(janela, text="ID:").pack()
    id_entry = tk.Entry(janela)
    id_entry.pack()

    tk.Label(janela, text="Nome:").pack()
    nome_entry = tk.Entry(janela)
    nome_entry.pack()

    tk.Label(janela, text="Preço:").pack()
    preco_entry = tk.Entry(janela)
    preco_entry.pack()

    tk.Label(janela, text="Estoque:").pack()
    estoque_entry = tk.Entry(janela)
    estoque_entry.pack()
    
    def salvar_edicao():
        try:
            id_produto = int(id_entry.get().strip())
            nome = nome_entry.get().strip()
            preco = preco_entry.get().strip()
            preco = float(preco) if preco else None
            estoque_entry = estoque_entry.get().strip()
            editar_produtos(id_produto, nome, preco)

            #chamar a função editar_produtos

            editar_produtos(id_produto, nome, preco)
            messagebox.showinfo("Sucesso", "Produto editado com sucesso!")
            janela.destroy()
        except ValueError as e:
            messagebox.showerror("Erro", f"Id do produto inválido: {e}")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao editar produto: {e}")    
        
    tk.Button(janela, text="Salvar", command=salvar_edicao).pack()
    tk.Button(janela, text="Fechar", command=janela.destroy).pack()

def tela_listar_produtos(root):
    janela = tk.Toplevel(root)
    janela.title("Listar Produtos")

    produtos = listar_produtos()
    if not produtos:
        tk.Label(janela, text="Nenhum produto cadastrado").pack()
        tk.Button(janela, text="Fechar", command=janela.destroy).pack()
        return
    
    for produto in produtos:
        tk.Label(janela, text=f"ID: {produto[0]}, Nome: {produto[1]}, Preço: {produto[2]}, Estoque: {produto[3]}").pack()

def tela_excluir_produtos(root):
    def excluir():
        try:
            entrada = id_entry.get()
            if not entrada:
                raise ValueError("Nenhum ID fornecido")

            ids = [int(id.strip()) for id in entrada.split(',')]
            if not ids:
                raise ValueError("Nenhum ID fornecido")
            excluir_produtos(ids)
            messagebox.showinfo("Sucesso", "Produtos excluídos com sucesso!")
            janela.destroy()

        except Exception as e:
            messagebox.showerror("Erro", f"Erro ao excluir produto: {e}")
        
        except ValueError:
            messagebox.showerror("Erro", "ID inválido fornecido")
    
    #configuração da janela
    janela = tk.Toplevel(root)
    janela.title("Excluir Produtos")

    tk.Label(janela, text="Insira ID dos produtos (separados por vírgula):").pack()
    id_entry = tk.Entry(janela)
    id_entry.pack()

    tk.Button(janela, text="Excluir", command=excluir).pack()
    tk.Button(janela, text="Fechar", command=janela.destroy).pack()

def tela_gerenciar_estoque(root):
    def atualizar_estoque():
        try:
            id_produto = int(id_entry.get().strip())
            quantidade = int(qtd_entry.get().strip())
            resultado = autalizar_estoque(id_produto, quantidade)
            if "Error" in resultado:
                messagebox.showerror("Erro", resultado)
            else:
                messagebox.showinfo("Sucesso", resultado)
            janela.destroy()
        except ValueError:
            messagebox.showerror("Erro", "ID ou quantidade inválidos!")
        except Exception as e:
            messagebox.showerror("Erro", f"Erro inesperado: {e}")

    janela = tk.Toplevel(root)
    janela.title("Gerenciar Estoque")

    tk.Label(janela, text="ID do Produto:").pack()
    id_entry = tk.Entry(janela)
    id_entry.pack()

    tk.Label(janela, text="Quantidade (+ para adicionar, - para remover):").pack()
    qtd_entry = tk.Entry(janela)
    qtd_entry.pack()

    tk.Button(janela, text="Atualizar Estoque", command=atualizar_estoque).pack()
    tk.Button(janela, text="Fechar", command=janela.destroy).pack()
