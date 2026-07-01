import tkinter as tk

# 1. Cria a janela raiz (a "tela em branco")
janela = tk.Tk()

# 2. Configura propriedades
janela.title("Minha Primeira Janela")
janela.geometry("400x200")   # largura x altura em pixels

# 3. Inicia o loop de eventos — SEMPRE no final
janela.mainloop()
