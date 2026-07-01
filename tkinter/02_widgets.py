import tkinter as tk

janela = tk.Tk()
janela.title("Widgets")
janela.geometry("640x560")

# Label — texto estático
tk.Label(janela, text="Nome:").pack(pady=4)

# Entry — campo de texto de uma linha
entrada = tk.Entry(janela, width=25)
entrada.pack()

# Button — botão clicável
def saudar():
    nome = entrada.get()
    resultado.config(text=f"Olá, {nome}!")

tk.Button(janela, text="Saudar", command=saudar).pack(pady=8)

# Label que muda dinamicamente
resultado = tk.Label(janela, text="", fg="blue")
resultado.pack()

# Checkbutton — caixa de seleção
var = tk.BooleanVar()
tk.Checkbutton(janela, text="Lembrar nome", variable=var).pack(pady=4)

janela.mainloop()
