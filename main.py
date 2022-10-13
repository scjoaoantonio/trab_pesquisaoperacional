# Importar biblioteca após a instalação (pip install pulp)
import pulp

# Definir o modelo de PL (Maximize ou Minimize)
model = pulp.LpProblem('Exemplo', sense=pulp.LpMaximize)

# Adicionar variáveis
x = pulp.LpVariable.dicts(
    indexs=[1, 2, 3, 4, 5], cat=pulp.LpContinuous, lowBound=0, name='x')

# Adicionar as Restrições
model.addConstraint(x[1] >= 0.25*(x[1] + x[2]), name='restricao_1')
model.addConstraint(x[2] <= 0.5*(x[1] + x[2]), name='restricao_2')
model.addConstraint(x[1] >= 0.5*x[2], name='restricao_3')
model.addConstraint(x[1] + x[2] <= 5000, name='restricao_4')

# Função Objetiva
model.setObjective(0.05 * x[1] + 0.08 * x[2])

# Otimizar
model.solve()

# Obter e imprimir a solução
x_sol = {i: x[i].value() for i in [1, 2]}
print(f'x= {x_sol}')
