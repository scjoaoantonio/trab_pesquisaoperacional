# Importar biblioteca após a instalação (pip install pulp)
import pulp
from help import *
import pandas as pd

info()
fornecedor = -1
festa = -1
valormax = -1

# Manipulação da planilha
tabela = pd.read_excel(r"./valores.xlsx")
qtd_fornecedores = tabela['Fornecedor'].count()
qtd_colunas = len(tabela.columns)
print(tabela)


# Inputs do usuário
while (fornecedor < 0 or fornecedor > (qtd_fornecedores-1)):
    fornecedor = int(input("\nQual fornecedor você quer contratar?\n-> "))
while (festa < 1 or festa > 2):
    festa = int(input(
        "Qual o tipo de evento você irá fazer?\n(1) Festa de Criança\n(2) Festa de Adulto\n-> "))
while (valormax < 0):
    valormax = int(input(
        "Quanto, no máximo, você quer gastar para compras as bebidas?\n-> "))

# Definir o modelo de PL (Maximize ou Minimize)
model = pulp.LpProblem('Festa', sense=pulp.LpMaximize)

# Adicionar variáveis
x = pulp.LpVariable.dicts(
    indexs=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], cat='Integer', lowBound=0, name='x')

# Adicionar restrições de acordo com o fornecedor
f = fornecedor
t = tabela

model.addConstraint(x[1] * int(t.iat[f, 1]) + x[2] * int(t.iat[f, 2]) + x[3] * int(
    t.iat[f, 3]) + x[4] * int(t.iat[f, 4]) + x[5] * int(t.iat[f, 5]) + x[6]*int(t.iat[f, 6]) + x[7]*int(t.iat[f, 7]) + x[8]*int(t.iat[f, 8]) + x[9]*int(t.iat[f, 9]) + x[10]*int(t.iat[f, 10]) == valormax, 'restricao_1')
model.addConstraint(x[1] + x[2] + x[3] + x[4] +
                    x[5] >= 1, 'restricao_2')
model.addConstraint(x[6] + x[7] + x[8] >= 1, 'restricao_3')
model.addConstraint(x[9] >= 1, 'restricao_4')
model.addConstraint(x[10] >= 1, 'restricao_5')
model.addConstraint(x[9] + x[10] <= (x[1] + x[2] +
                    x[3] + x[4] + x[5] + x[6] + x[7] + x[8]) / 2, 'restricao_6')
if (festa == 1):
    # criança
    model.addConstraint(x[1] + x[2] + x[3] + x[4] +
                        x[5] >= x[6] + x[7] + x[8], 'restricao_7')
elif (festa == 2):
    # adulto
    model.addConstraint(x[1] + x[2] + x[3] + x[4] +
                        x[5] <= x[6] + x[7] + x[8], 'restricao_7')

# Função Objetiva
model.setObjective(x[1] * int(t.iat[f, 1]) + x[2] * int(t.iat[f, 2]) + x[3] * int(
    t.iat[f, 3]) + x[4] * int(t.iat[f, 4]) + x[5] * int(t.iat[f, 5]) + x[6]*int(t.iat[f, 6]) + x[7]*int(t.iat[f, 7]) + x[8]*int(t.iat[f, 8]) + x[9]*int(t.iat[f, 9]) + x[10]*int(t.iat[f, 10]))


# Otimizar
model.solve()

# Obter e imprimir a solução
itens = list(tabela.columns)
print("\nMelhor Solução: \n")
for i in range(1, 11):
    print(itens[i] + " = " + str(x[i].value()))
