import tkinter as tk
from ui.tela_principal import tela_principal

if __name__ == "__main__":
    root = tk.Tk()
    root.title("Sistema de Gerenciamento de Loja")
    tela_principal(root)
    root.mainloop()
