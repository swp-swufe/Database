from gurobipy import *

n_row = 2
n_col = 3
ubs = [10, GRB.INFINITY, GRB.INFINITY]

A = [[-1, 1, 3],
     [1, 3, -7]]
b = [-5, 10]

c = [1, 2, 5]

m = Model('LP')
# DECISION VARIABLE
# x1 = m.addVar(lb=0,ub=10,vtype=GRB.CONTINUOUS,name='x1')
# x2 = m.addVar(lb=0,ub=GRB.INFINITY,name='x2')
# x3 =m.addVar(lb=0,ub=10,name='x3')


x = m.addVars(n_col, ub=ubs, name='x')

# objective


m.setObjective(sum(c[i] * x[i] for i in range(n_col)), sense=GRB.MAXIMIZE)

m.addConstrs(sum(A[i][j] * x[j] for j in range(n_col)) <= b[i] for i in range(n_row))

# m.addConstr(-x1+x2+3*x3<=-5,name='con1')
# m.addConstr(x1+3*x2-7*x3<=10,name='con2')


m.optimize()

if m.status == GRB.OPTIMAL:
    for v in m.getVars():
        print(v.varName, '=', v.x)
    print('the object value is ', m.objVal)
