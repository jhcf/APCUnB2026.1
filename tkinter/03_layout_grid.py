import tkinter as tk

janela = tk.Tk()
janela.title("Layout com grid")
janela.geometry("300x180")

# grid organiza em linhas e colunas
campos = ["Nome", "Email", "Telefone"]
entradas = {}

for i, campo in enumerate(campos):
    tk.Label(janela, text=campo + ":").grid(
        row=i, column=0, sticky="e", padx=8, pady=4
    )
    e = tk.Entry(janela, width=22)
    e.grid(row=i, column=1, padx=8)
    entradas[campo] = e

# sticky="e" alinha o Label à direita (East)
# columnspan junta colunas
tk.Button(janela, text="Enviar").grid(
    row=len(campos), column=0, columnspan=2, pady=10
)

janela.mainloop()
