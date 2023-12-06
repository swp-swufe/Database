import pandas as pd
import gurobipy as gp

# data
data = pd.read_csv('./data_portfolio.csv')
# print(data)
stocks = data.columns.values
mean = data.mean()
mean = dict(mean)
cov = data.cov()

budget = 1
target = 0.005

# model
m = gp.Model('portfolio')

x = m.addVars(stocks, name='x')

m.setObjective(gp.quicksum(cov.loc[i, j] * x[i] * x[j] for i in stocks for j in stocks), gp.GRB.MINIMIZE)
m.addConstr(x.sum() <= budget, name='budget')
m.addConstr(x.prod(mean) >= target, name='target')
m.optimize()
# analysis
if m.status == gp.GRB.OPTIMAL:
    for v in m.getVars():
        print(v.varName, '=', v.x)
    print('variance of the portfolio = ', m.objVal)
    selected = [i for i in stocks if x[i].x > 1e-3]
    print('invested stocks:\n', selected)
