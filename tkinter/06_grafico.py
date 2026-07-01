import tkinter as tk
import matplotlib
matplotlib.use("TkAgg")           # backend que fala com Tkinter
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg,            # canvas do gráfico
    NavigationToolbar2Tk,         # barra zoom/pan
)
import numpy as np

janela = tk.Tk()
janela.title("Gráfico Interativo")
janela.geometry("600x500")

# ── Controles no topo ──────────────────────────────
frame_ctrl = tk.Frame(janela, bg="#f0f0f0", pady=4)
frame_ctrl.pack(fill="x")

tk.Label(frame_ctrl, text="Função:", bg="#f0f0f0").pack(side="left", padx=6)

tipo_var = tk.StringVar(value="seno")
for nome in ("seno", "cosseno", "tangente", "quadrática"):
    tk.Radiobutton(
        frame_ctrl, text=nome, variable=tipo_var,
        value=nome, bg="#f0f0f0",
        command=lambda: atualizar()
    ).pack(side="left")

# ── Figura Matplotlib ──────────────────────────────
fig = Figure(figsize=(6, 4), dpi=90)
ax  = fig.add_subplot(111)

# FigureCanvasTkAgg transforma a Figure num widget Tkinter
canvas = FigureCanvasTkAgg(fig, master=janela)
canvas.get_tk_widget().pack(fill="both", expand=True)

# Barra de ferramentas nativa (zoom, pan, salvar)
toolbar = NavigationToolbar2Tk(canvas, janela)
toolbar.update()

# ── Função de redesenho ────────────────────────────
x = np.linspace(-2 * np.pi, 2 * np.pi, 400)

FUNCOES = {
    "seno":      (np.sin(x),  "steelblue"),
    "cosseno":   (np.cos(x),  "tomato"),
    "tangente":  (np.clip(np.tan(x), -5, 5), "seagreen"),
    "quadrática":(x**2 / 10, "darkorchid"),
}

def atualizar():
    y, cor = FUNCOES[tipo_var.get()]
    ax.clear()
    ax.plot(x, y, color=cor, linewidth=2)
    ax.set_title(tipo_var.get().capitalize())
    ax.axhline(0, color="gray", linewidth=0.5)
    ax.grid(True, alpha=0.3)
    fig.tight_layout()
    canvas.draw()           # ← redesenha o widget

atualizar()                 # desenha ao iniciar
janela.mainloop()
