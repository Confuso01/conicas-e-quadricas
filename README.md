# 📐 Visualizador de Cônicas e Quádricas

Aplicação desktop desenvolvida em Python para visualização interativa de **cônicas** (figuras planas 2D) e **quádricas** (superfícies 3D), com parâmetros totalmente ajustáveis pelo usuário.

---

## ✨ Funcionalidades

### 📏 Figuras 2D (Cônicas)
| Figura | Parâmetros |
|---|---|
| Parábola | a, b, c |
| Elipse | a, b |
| Hipérbole | a, b |
| Círculo | r |
| Ponto | x₀, y₀ |
| Par de retas | m₁, b₁, m₂, b₂ |

### 🌐 Superfícies 3D (Quádricas)
| Figura | Parâmetros |
|---|---|
| Elipsoide | a, b, c |
| Paraboloide Elíptico | a, b |
| Paraboloide Hiperbólico | a, b |
| Hiperboloide de 1 folha | a, b, c |
| Hiperboloide de 2 folhas | a, b, c |
| Cone Quádrico | a, b, c |
| Cilindro | a, b |

---

## 🖥️ Interface

- Seleção da figura via **Combobox** com atualização dinâmica dos campos de parâmetro
- Campos com **valores padrão** pré-preenchidos para facilitar o uso
- Plotagem 2D para cônicas e **3D interativo** para quádricas (rotação com o mouse)
- Títulos automáticos com a equação da figura selecionada

---

## 🚀 Como Executar

### Pré-requisitos

```bash
pip install matplotlib numpy
```

> `tkinter` já vem incluso na instalação padrão do Python.

### Execução

```bash
python algebra_vetorial.py
```

---

## 📦 Dependências

| Biblioteca | Uso |
|---|---|
| `tkinter` / `ttk` | Interface gráfica (GUI) |
| `matplotlib` | Plotagem 2D e 3D |
| `numpy` | Geração dos dados das figuras |
| `mpl_toolkits.mplot3d` | Renderização das superfícies 3D |

---

## 🎓 Contexto

Desenvolvido como ferramenta de apoio à disciplina de **Álgebra Vetorial e Geometria Analítica** do curso de Engenharia Elétrica da **UFCG** (Universidade Federal de Campina Grande).

---

## 📄 Licença

MIT License
