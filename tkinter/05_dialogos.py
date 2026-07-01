import tkinter as tk
from tkinter import messagebox, filedialog, simpledialog

janela = tk.Tk()
janela.title("Diálogos")
janela.geometry("300x220")

def abrir_info():
    messagebox.showinfo("Info", "Operação concluída!")

def abrir_erro():
    messagebox.showerror("Erro", "Algo deu errado.")

def confirmar():
    ok = messagebox.askyesno("Confirmar", "Deseja sair?")
    resultado.config(text="Sim" if ok else "Não")

def abrir_arquivo():
    caminho = filedialog.askopenfilename(
        title="Escolha um arquivo",
        filetypes=[("Texto", "*.txt"), ("Todos", "*.*")]
    )
    resultado.config(text=caminho or "Cancelado")

def pedir_texto():
    nome = simpledialog.askstring("Nome", "Qual seu nome?")
    resultado.config(text=nome or "Cancelado")

for txt, fn in [
    ("showinfo", abrir_info), ("showerror", abrir_erro),
    ("askyesno", confirmar), ("askopenfilename", abrir_arquivo),
    ("askstring", pedir_texto),
]:
    tk.Button(janela, text=txt, command=fn, width=20).pack(pady=2)

resultado = tk.Label(janela, text="", fg="navy")
resultado.pack(pady=6)
janela.mainloop()
