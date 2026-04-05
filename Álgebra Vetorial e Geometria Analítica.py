import tkinter as tk
from tkinter import ttk, messagebox

import numpy as np
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from mpl_toolkits.mplot3d import Axes3D

# -------------------------------------------
# Funções para gerar dados de figuras 2D
# -------------------------------------------
def desenhar_parabola(ax, a, b, c):
    x = np.linspace(-10, 10, 400)
    y = a*x**2 + b*x + c
    ax.plot(x, y)
    ax.set_title(f'Parábola: y = {a}x² + {b}x + {c}')


def desenhar_elipse(ax, a, b):
    t = np.linspace(0, 2*np.pi, 400)
    x = a*np.cos(t)
    y = b*np.sin(t)
    ax.plot(x, y)
    ax.set_aspect('equal')
    ax.set_title(f'Elipse: x²/{a}² + y²/{b}² = 1')


def desenhar_hiperbole(ax, a, b):
    t = np.linspace(-2, 2, 400)
    x1 = a*np.cosh(t)
    y1 = b*np.sinh(t)
    ax.plot(x1, y1)
    ax.plot(-x1, y1)
    ax.set_title(f'Hipérbole: x²/{a}² - y²/{b}² = 1')


def desenhar_circulo(ax, r):
    t = np.linspace(0, 2*np.pi, 400)
    x = r*np.cos(t)
    y = r*np.sin(t)
    ax.plot(x, y)
    ax.set_aspect('equal')
    ax.set_title(f'Círculo: x² + y² = {r}²')


def desenhar_ponto(ax, x0, y0):
    ax.plot(x0, y0, 'o')
    ax.set_title(f'Ponto: ({x0}, {y0})')


def desenhar_par_de_retas(ax, m1, b1, m2, b2):
    x = np.linspace(-10, 10, 400)
    y1 = m1*x + b1
    y2 = m2*x + b2
    ax.plot(x, y1, label=f'y = {m1}x + {b1}')
    ax.plot(x, y2, label=f'y = {m2}x + {b2}')
    ax.legend()
    ax.set_title('Par de retas')

# -------------------------------------------
# Funções para gerar dados de superfícies 3D
# -------------------------------------------
def desenhar_elipsoide(ax, a, b, c):
    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(0, np.pi, 50)
    x = a * np.outer(np.cos(u), np.sin(v))
    y = b * np.outer(np.sin(u), np.sin(v))
    z = c * np.outer(np.ones_like(u), np.cos(v))
    ax.plot_surface(x, y, z, alpha=0.6)
    ax.set_title(f'Elipsoide: x²/{a}² + y²/{b}² + z²/{c}² = 1')


def desenhar_paraboloide_eliptico(ax, a, b):
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = X**2/a**2 + Y**2/b**2
    ax.plot_surface(X, Y, Z, alpha=0.6)
    ax.set_title('Paraboloide Elíptico')


def desenhar_paraboloide_hiperbolico(ax, a, b):
    x = np.linspace(-5, 5, 50)
    y = np.linspace(-5, 5, 50)
    X, Y = np.meshgrid(x, y)
    Z = X**2/a**2 - Y**2/b**2
    ax.plot_surface(X, Y, Z, alpha=0.6)
    ax.set_title('Paraboloide Hiperbólico')


def desenhar_hiperboloide_uma_folha(ax, a, b, c):
    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(-1, 1, 50)
    U, V = np.meshgrid(u, v)
    X = a * np.cosh(V) * np.cos(U)
    Y = b * np.cosh(V) * np.sin(U)
    Z = c * np.sinh(V)
    ax.plot_surface(X, Y, Z, alpha=0.6)
    ax.set_title('Hiperboloide de uma folha')


def desenhar_hiperboloide_duas_folhas(ax, a, b, c):
    u = np.linspace(0, 2*np.pi, 50)
    v = np.linspace(1, 2, 50)
    U, V = np.meshgrid(u, v)
    X = a * np.cosh(V) * np.cos(U)
    Y = b * np.cosh(V) * np.sin(U)
    Z = c * np.sinh(V)
    ax.plot_surface(X, Y, Z, alpha=0.6)
    ax.set_title('Hiperboloide de duas folhas')


def desenhar_cono_quadrico(ax, a, b, c):
    u = np.linspace(0, 2*np.pi, 50)
    z = np.linspace(-5, 5, 50)
    U, Z = np.meshgrid(u, z)
    X = a * Z * np.cos(U)
    Y = b * Z * np.sin(U)
    ax.plot_surface(X, Y, Z, alpha=0.6)
    ax.set_title('Cone Quádico')


def desenhar_cilindro(ax, a, b):
    u = np.linspace(0, 2*np.pi, 50)
    z = np.linspace(-5, 5, 50)
    U, Z = np.meshgrid(u, z)
    X = a * np.cos(U)
    Y = b * np.sin(U)
    ax.plot_surface(X, Y, Z, alpha=0.6)
    ax.set_title('Cilindro')

# -------------------------------------------
# Interface Gráfica com Tkinter
# -------------------------------------------
class Aplicativo(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('Visualizador de Cônicas e Quádricas')
        self.geometry('1000x700')

        # Painel de seleção
        frame_esquerda = ttk.Frame(self)
        frame_esquerda.pack(side=tk.LEFT, fill=tk.Y, padx=5, pady=5)

        ttk.Label(frame_esquerda, text='Selecione a figura:').pack(pady=5)
        self.combo = ttk.Combobox(frame_esquerda, values=[
            'Parábola', 'Elipse', 'Hipérbole', 'Círculo',
            'Ponto', 'Par de retas',
            'Elipsoide', 'Paraboloide Elíptico', 'Paraboloide Hiperbólico',
            'Hiperboloide 1 folha', 'Hiperboloide 2 folhas', 'Cone', 'Cilindro'
        ])
        self.combo.pack(pady=5)
        self.combo.bind('<<ComboboxSelected>>', self.construir_entradas)

        self.param_frame = ttk.Frame(frame_esquerda)
        self.param_frame.pack(pady=10)

        ttk.Button(frame_esquerda, text='Plotar', command=self.plotar).pack(pady=20)

        # Área de plotagem
        self.fig = plt.Figure(figsize=(6,6))
        self.ax = self.fig.add_subplot(111)
        self.canvas = FigureCanvasTkAgg(self.fig, master=self)
        self.canvas.get_tk_widget().pack(side=tk.RIGHT, fill=tk.BOTH, expand=1)

        # Dicionário para armazenar entradas
        self.entries = {}

    def construir_entradas(self, event=None):
        # Limpar parâmetros antigos
        for widget in self.param_frame.winfo_children():
            widget.destroy()
        self.entries.clear()

        figura = self.combo.get()
        params = []
        if figura == 'Parábola': params = [('a', 1), ('b', 0), ('c', 0)]
        elif figura == 'Elipse': params = [('a', 5), ('b', 3)]
        elif figura == 'Hipérbole': params = [('a', 5), ('b', 3)]
        elif figura == 'Círculo': params = [('r', 5)]
        elif figura == 'Ponto': params = [('x0', 0), ('y0', 0)]
        elif figura == 'Par de retas': params = [('m1', 1), ('b1', 0), ('m2', -1), ('b2', 0)]
        elif figura in ['Elipsoide','Hiperboloide 1 folha','Hiperboloide 2 folhas','Cone','Cilindro']:
            params = [('a', 3), ('b', 2), ('c', 1)]
        elif figura == 'Paraboloide Elíptico': params = [('a', 1), ('b', 1)]
        elif figura == 'Paraboloide Hiperbólico': params = [('a', 1), ('b', 1)]

        for nome, padrao in params:
            ttk.Label(self.param_frame, text=nome).pack()
            ent = ttk.Entry(self.param_frame)
            ent.insert(0, str(padrao))
            ent.pack()
            self.entries[nome] = ent

    def plotar(self):
        figura = self.combo.get()
        if not figura:
            messagebox.showwarning('Aviso', 'Selecione uma figura!')
            return
        try:
            valores = {k: float(v.get()) for k, v in self.entries.items()}
        except ValueError:
            messagebox.showerror('Erro', 'Parâmetros inválidos!')
            return

        # Limpar plot anterior
        self.fig.clf()
        if figura in ['Elipsoide','Paraboloide Elíptico','Paraboloide Hiperbólico','Hiperboloide 1 folha','Hiperboloide 2 folhas','Cone','Cilindro']:
            ax = self.fig.add_subplot(111, projection='3d')
        else:
            ax = self.fig.add_subplot(111)

        # Desenhar conforme selecionado
        if figura == 'Parábola': desenhar_parabola(ax, **valores)
        elif figura == 'Elipse': desenhar_elipse(ax, **valores)
        elif figura == 'Hipérbole': desenhar_hiperbole(ax, **valores)
        elif figura == 'Círculo': desenhar_circulo(ax, **valores)
        elif figura == 'Ponto': desenhar_ponto(ax, **valores)
        elif figura == 'Par de retas': desenhar_par_de_retas(ax, **valores)
        elif figura == 'Elipsoide': desenhar_elipsoide(ax, **valores)
        elif figura == 'Paraboloide Elíptico': desenhar_paraboloide_eliptico(ax, **valores)
        elif figura == 'Paraboloide Hiperbólico': desenhar_paraboloide_hiperbolico(ax, **valores)
        elif figura == 'Hiperboloide 1 folha': desenhar_hiperboloide_uma_folha(ax, **valores)
        elif figura == 'Hiperboloide 2 folhas': desenhar_hiperboloide_duas_folhas(ax, **valores)
        elif figura == 'Cone': desenhar_cono_quadrico(ax, **valores)
        elif figura == 'Cilindro': desenhar_cilindro(ax, **valores)

        self.canvas.draw()

if __name__ == '__main__':
    app = Aplicativo()
    app.mainloop()
