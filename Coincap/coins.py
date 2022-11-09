# Importar biblioteca após a instalação (pip install pulp)
import pulp
from help import *

fornecedor = -1
festa = -1
valormax = -1

info()

# Inputs do usuário
while (fornecedor < 1 or fornecedor > 4):
    fornecedor = int(input("Qual fornecedor você vai querer contratar?\n(1)Fornecedor 1: entregará a compra em 1 dia\n(2)Fornecedor 2: entregará a compra em 3 dias\n(3)Fornecedor 3: entregará a compra em 5 dias\n(4)Fornecedor 4: entregará a compra em 6 dias\n-> "))
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
    indexs=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], cat=pulp.LpContinuous, lowBound=0, name='x')

# Adicionar restrições de acordo com o fornecedor
match fornecedor:
    case 1:
        model.addConstraint(12 * x[1] + 13 * x[2] + 12 * x[3] + 10 * x[4] + 8 *
                            x[5] + 5 * x[6] + 5 * x[7] + 8 * x[8] + 4 * x[9] + 5 * x[10] <= valormax, 'restricao_0')
        model.addConstraint(12 * x[1] + 13 * x[2] + 12 * x[3] + 10 * x[4] + 8 *
                            x[5] + 5 * x[6] + 5 * x[7] + 8 * x[8] + 4 * x[9] + 5 * x[10] >= valormax / 2, 'restricao_1')
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
        model.addConstraint(x[1] <= 20, 'restricao_a1')
        model.addConstraint(x[2] <= 20, 'restricao_a2')
        model.addConstraint(x[3] <= 20, 'restricao_a3')
        model.addConstraint(x[4] <= 20, 'restricao_a4')
        model.addConstraint(x[5] <= 20, 'restricao_a5')
        model.addConstraint(x[9] <= 20, 'restricao_a9')
        model.addConstraint(x[6] <= 20, 'restricao_a6')
        model.addConstraint(x[7] <= 20, 'restricao_a7')
        model.addConstraint(x[8] <= 20, 'restricao_a8')
        model.addConstraint(x[10] <= 20, 'restricao_a10')
        # Função Objetiva
        model.setObjective(12 * x[1] + 13 * x[2] + 12 * x[3] + 10 * x[4] + 8 *
                           x[5] + 5 * x[6] + 5 * x[7] + 8 * x[8] + 4 * x[9] + 5 * x[10])

    case _:
        pass

# Otimizar
model.solve()

# Obter e imprimir a solução
x_sol = {i: x[i].value() for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
print(f'x= {x_sol}')
