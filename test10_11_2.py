from gurobipy import *

# data
plants = [1, 2, 3]
retailers = ['A', 'B', 'C', 'D']
demands = {'A': 1700, 'B': 1000, 'C': 1500, 'D': 1200}
supplies = {1: 1700, 2: 2000, 3: 1700}
cost_data = [[5, 3, 2, 6], [7, 7, 8, 10], [6, 5, 3, 8]]
cost = {(plants[i], retailers[j]): cost_data[i][j]
        for i in range(len(plants))
        for j in range(len(retailers))}
m = Model('trans')

# decision
x = m.addVars(plants, retailers, name='x')
# objective

m.setObjective(x.prod(cost), sense=GRB.MINIMIZE)

m.addConstrs(sum(x[i, j] for i in plants) == demands[j] for j in retailers)
m.addConstrs(sum(x[i, j] for j in retailers) <= supplies[i] for i in plants)

m.optimize()

if m.status == GRB.OPTIMAL:
    for i in plants:
        for j in retailers:
            print(x[i, j].x, i, j)
