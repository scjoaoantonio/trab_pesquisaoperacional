# Importar biblioteca após a instalação (pip install pulp)
import pulp

# Definir o modelo de PL (Maximize ou Minimize)
model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)

# Adicionar variáveis
x = pulp.LpVariable.dicts(
    indexs=[1, 2, 3, 4, 5], cat=pulp.LpContinuous, lowBound=0, name='x')

# Adicionar as Restrições
model.addConstraint(2*x[1]+4*x[2]+x[3] == 10, name='restricao_1')
model.addConstraint(6*x[1]+x[4] == 20, name='restricao_2')
model.addConstraint(x[1]-x[2]+x[5] == 30, name='restricao_3')

# Função Objetiva
model.setObjective(3 * x[1] + 5 * x[2])

# Otimizar
model.solve()

# Obter e imprimir a solução
x_sol = {i: x[i].value() for i in [1, 2, 3, 4, 5]}
print(f'x= {x_sol}')
