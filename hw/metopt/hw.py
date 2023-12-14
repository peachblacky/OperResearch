import gurobipy as gp
from gurobipy import GRB

try:
    # номер варианта - 53
    model = gp.Model('Gomory_53')

    x_1 = model.addVar(vtype=GRB.INTEGER, name="x_1")
    x_2 = model.addVar(vtype=GRB.INTEGER, name="x_2")

    model.setObjective(x_1 + x_2, GRB.MAXIMIZE)

    model.addConstr(-3*x_1+8*x_2 <= -2, "c0")
    model.addConstr(-6*x_1+3*x_2 <= 7, "c1")
    model.addConstr(2*x_1-2*x_2 <= 6, "c2")

    model.setParam(GRB.Param.PreCrush, 0)
    model.setParam(GRB.Param.Presolve, 0)
    model.setParam(GRB.Param.Cuts, 0)
    model.setParam(GRB.Param.Heuristics, 0)
    model.setParam(GRB.Param.GomoryPasses, 2)

    model.optimize()

    for v in model.getVars():
        print(f"{v.VarName} {v.X:g}")

    print(f"Obj: {model.ObjVal:g}")

except gp.GurobiError as e:
    print(f"Error message: {e.message}: {e}")

except AttributeError:
    print("Encountered an attribute error")
