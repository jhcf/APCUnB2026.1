import tkinter as tk

janela = tk.Tk()
janela.title("Eventos")
janela.geometry("380x220")

log = tk.Text(janela, height=8, width=44, state="disabled")
log.pack(padx=10, pady=10)

def registrar(msg):
    log.config(state="normal")
    log.insert(tk.END, msg + "\n")
    log.config(state="disabled")
    log.see(tk.END)  # rola para o fim

# Eventos de mouse no widget log
log.bind("<Button-1>",
    lambda e: registrar(f"Clique em ({e.x}, {e.y})"))

log.bind("<Motion>",
    lambda e: registrar(f"Mouse em ({e.x}, {e.y})"))

# Evento de teclado na janela inteira
janela.bind("<Key>",
    lambda e: registrar(f"Tecla: {e.keysym}"))

registrar("Clique aqui, mova o mouse ou pressione uma tecla!")
janela.mainloop()
