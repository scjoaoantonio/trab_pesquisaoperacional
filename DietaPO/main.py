from help import *
# Importar biblioteca após a instalação (pip install pulp)
import pulp

info()
print("\nPreencha as lacunas com a quantidade de calorias necessárias diariamente na sua dieta de acordo com a  recomendação de um nutricionista:")
calorias = 0
while(calorias < 2000 or calorias > 2500):
    calorias = int(input("Calorias: "))

# Definir o modelo de PL (Maximize ou Minimize)
model = pulp.LpProblem('Dieta', sense=pulp.LpMinimize)

# Adicionar variáveis
x = pulp.LpVariable.dicts(
    indexs=[1, 2, 3, 4, 5, 6, 7, 8, 9, 10], cat=pulp.LpContinuous, lowBound=0, name='x')

# Adicionar as Restrições
model.addConstraint(2.7 * x[1] + 24.2 * x[2] + 0 * x[3] + 1.4 * x[4] + 0.49 *
                    x[5] + 26 * x[6] + 26 * x[7] + 0.9 * x[8] + 0.9 * x[9] + 3.4 * x[10] == (calorias/30), 'restricao_1')
model.addConstraint(x[1] >= 1, 'restricao_a2')
model.addConstraint(x[2] >= 1, 'restricao_a3')
model.addConstraint(x[3] >= 1, 'restricao_a4')
model.addConstraint(x[4] >= 1, 'restricao_a5')
model.addConstraint(x[5] >= 1, 'restricao_a6')
model.addConstraint(x[6] + x[7] == 1, 'restricao_a7')
model.addConstraint(x[8] >= 1, 'restricao_a9')
model.addConstraint(x[9] + x[10] == 1, 'restricao_a10')
model.addConstraint(x[1] <= 3, 'restricao_b2')
model.addConstraint(x[2] <= 3, 'restricao_b3')
model.addConstraint(x[3] <= 3, 'restricao_b4')
model.addConstraint(x[4] <= 3, 'restricao_b5')
model.addConstraint(x[5] <= 3, 'restricao_b6')
model.addConstraint(x[6] <= 3, 'restricao_b7')
model.addConstraint(x[7] <= 3, 'restricao_b8')
model.addConstraint(x[8] <= 3, 'restricao_b9')
model.addConstraint(x[9] <= 3, 'restricao_b10')
model.addConstraint(x[10] <= 3, 'restricao_b11')

# Função Objetiva
model.setObjective(0.99 * x[1] + 2.90 * x[2] + 0.79 * x[3] + 0.95 * x[4] + 0.49 *
                   x[5] + 2.49 * x[6] + 2.00 * x[7] + 0.33 * x[8] + 0.83 * x[9] + 1.40 * x[10])

# Otimizar
model.solve()

# Obter e imprimir a solução
x_sol = {i: x[i].value() for i in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]}
print(f'x= {x_sol}')
