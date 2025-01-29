# Projeto-sgbd-local-
Um estudo de como criar um banco de dados pequeno e local através do python. A finalidade desse projeto é aprender a estruturar um programa e entender melhor os conceitos de CRUD através da linguagem de programação escolhida.

Sistema de Loja

Este projeto é um Sistema de Loja desenvolvido em Python com interface gráfica usando Tkinter e banco de dados SQLite3. Ele permite o gerenciamento de produtos e vendas, com funcionalidades como cadastro, edição, exclusão e listagem de produtos e vendas.

📌 Funcionalidades

📦 Gerenciamento de Produtos

Adicionar produtos (nome, preço, estoque)

Editar produtos

Listar produtos cadastrados

Excluir produtos

Atualizar estoque (adicionar ou remover itens)

💰 Gerenciamento de Vendas

Registrar vendas

Listar vendas realizadas

🏗 Estrutura do Projeto

Sistema_loja/
│── app.py                 # Arquivo principal
│
├── database/              # Módulo de banco de dados
│   ├── __init__.py        # Inicializador do pacote
│   ├── conexao.py         # Configuração do SQLite3
│   ├── produtos.py        # Funções de manipulação de produtos
│   ├── vendas.py          # Funções de manipulação de vendas
│
├── ui/                    # Interface gráfica (Tkinter)
│   ├── __init__.py        # Inicializador do pacote
│   ├── tela_produtos.py   # Tela para gerenciar produtos
│   ├── tela_vendas.py     # Tela para gerenciar vendas
│   ├── tela_principal.py  # Tela principal do sistema
│
├── README.md              # Documentação do projeto

🚀 Instalação e Uso

1️⃣ Pré-requisitos

Python 3.10+

SQLite3 (já incluído no Python por padrão)

2️⃣ Execute o sistema atraves do arquivo App.py
 
 python .py

🔧 Melhorias Futuras

Criar uma API REST para integrar com um site/e-commerce

Melhorar a interface gráfica com Tkinter ou PyQt

Implementar um relatório de vendas

Adicionar suporte a múltiplos usuários com autenticação

Migrar o banco de dados para MySQL/PostgreSQL para escalabilidade

📜 Licença

Este projeto é de código aberto e pode ser modificado conforme necessário.

Desenvolvido por Francisco Soares 🚀

