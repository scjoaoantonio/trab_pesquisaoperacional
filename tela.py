# from main import *
import pandas as pd
import pulp
from tkinter import *
from tkinter import messagebox
from tkinter import Tk, ttk

co5 = "#e06636"

# Criar janela
app = Tk()
app.title("Otimização")
app.geometry("700x330")
app.resizable(width=FALSE, height=TRUE)
style = ttk.Style(app)
style.theme_use("clam")

# Mostrar planilha
t = Text(app, font="arial 11", width="1080", height="6")
t.pack()
tabela = pd.read_excel(r"./valores.xlsx")
qtd_fornecedores = tabela['Fornecedor'].count()
qtd_colunas = len(tabela.columns)
t.insert(0.0, tabela, )

space = Label(app)
space.pack()

# Adicionar Inputs
addfornecedor = Label(
    app, text="Qual fornecedor você quer contratar?", font="Arial 10 bold")
addfornecedor.pack()
e_fornecedor = Entry(app, width=24)
e_fornecedor.pack()

listfesta = ["Festa de adultos", "Festa de crianças"]
addfesta = Label(
    app, text="Qual o tipo de evento você irá fazer?", font="Arial 10 bold")
addfesta.pack()
e_festa = ttk.Combobox(app, values=listfesta)
e_festa.pack()


addvalormax = Label(
    app, text="Quanto, no máximo, você quer gastar para compras as bebidas?", font="Arial 10 bold")
addvalormax.pack()
e_valormax = Entry(app, width=24)
e_valormax.pack()

space = Label(app)
space.pack()


# Função de otimização
def otimizar():
    tabela = pd.read_excel(r"./valores.xlsx")
    qtd_fornecedores = tabela['Fornecedor'].count()

    fornecedor = int(e_fornecedor.get())
    valormax = int(e_valormax.get())

    festa = e_festa.get()
    if (festa == "Festa de crianças"):
        festa = 1
    elif (festa == "Festa de adultos"):
        festa = 2
    else:
        messagebox.showerror('Erro', 'Seleciona um dos dados na tabela')

    model = pulp.LpProblem('Festa', sense=pulp.LpMaximize)

    # Adicionar variáveis
    x = pulp.LpVariable.dicts(
        indexs=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], cat='Integer', lowBound=0, name='x')

    # Adicionar restrições de acordo com o fornecedor
    f = fornecedor
    t = tabela

    model.addConstraint(x[1] * int(t.iat[f, 1]) + x[2] * int(t.iat[f, 2]) + x[3] * int(
        t.iat[f, 3]) + x[4] * int(t.iat[f, 4]) + x[5] * int(t.iat[f, 5]) + x[6]*int(t.iat[f, 6]) + x[7]*int(t.iat[f, 7]) + x[8]*int(t.iat[f, 8]) + x[9]*int(t.iat[f, 9]) + x[10]*int(t.iat[f, 10]) == valormax, 'restricao_1')
    model.addConstraint(x[1] + x[2] + x[3] + x[4] >= 1, 'restricao_2')
    model.addConstraint(x[5] + x[6] + x[7] + x[8] >= 1, 'restricao_3')
    model.addConstraint(x[9] >= 1, 'restricao_4')
    model.addConstraint(x[10] >= 1, 'restricao_5')
    model.addConstraint(x[9] + x[10] <= (x[1] + x[2] +
                        x[3] + x[4] + x[5] + x[6] + x[7] + x[8]) / 2, 'restricao_6')
    model.addConstraint(x[1] <= valormax/20, 'restricao_a1')
    model.addConstraint(x[2] <= valormax/20, 'restricao_a2')
    model.addConstraint(x[3] <= valormax/20, 'restricao_a3')
    model.addConstraint(x[4] <= valormax/20, 'restricao_a4')
    model.addConstraint(x[5] <= valormax/20, 'restricao_a5')
    model.addConstraint(x[9] <= valormax/20, 'restricao_a9')
    model.addConstraint(x[6] <= valormax/20, 'restricao_a6')
    model.addConstraint(x[7] <= valormax/20, 'restricao_a7')
    model.addConstraint(x[8] <= valormax/20, 'restricao_a8')
    model.addConstraint(x[10] <= valormax/20, 'restricao_a10')
    if (festa == 1):
        # criança
        model.addConstraint(x[1] + x[2] + x[3] + x[4] >=
                            x[5] + x[6] + x[7] + x[8], 'restricao_7')
    elif (festa == 2):
        # adulto
        model.addConstraint(x[1] + x[2] + x[3] + x[4] <=
                            x[5] + x[6] + x[7] + x[8], 'restricao_7')

    # Função Objetiva
    model.setObjective(x[1] * int(t.iat[f, 1]) + x[2] * int(t.iat[f, 2]) + x[3] * int(
        t.iat[f, 3]) + x[4] * int(t.iat[f, 4]) + x[5] * int(t.iat[f, 5]) + x[6]*int(t.iat[f, 6]) + x[7]*int(t.iat[f, 7]) + x[8]*int(t.iat[f, 8]) + x[9]*int(t.iat[f, 9]) + x[10]*int(t.iat[f, 10]))

    # Otimizar
    model.solve()

    # Obter e imprimir a solução
    itens = list(tabela.columns)
    for i in range(1, 11):
        if (x[i].value() < 0):
            print("\n\nERRO! Digite um valor maior para a compra.\n\n")
            exit()
    resultado(itens, x)


def resultado(itens, x):
    tela_result = Tk()
    tela_result.title("Otimização")
    tela_result.geometry("200x350")
    tela_result.resizable(width=FALSE, height=TRUE)

    t = Text(tela_result, font="arial 11", width="1080")
    t.pack()
    for i in range(1, 11):
        t.insert(0.0, "\n" + itens[i] + " = " + str(x[i].value()) + "\n")


# Botão de otimização
btn_link = Button(app, text="Otimizar",
                  command=otimizar, width=20, bg=co5)
btn_link.pack()
space = Label(app)
space.pack()


app.mainloop()
