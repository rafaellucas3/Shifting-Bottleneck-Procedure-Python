from classes import Job, Jobshop
import networkx as nx
from pulp import *

jobs = {}
jobs[1] = Job(1, [1, 2, 3], [10, 8, 4])
jobs[2] = Job(2, [2, 1, 4, 3], [8, 3, 5, 6])
jobs[3] = Job(3, [1, 2, 4], [4, 7, 3])

def LP(jobs):
    """
    A function that computes the linear programming optimization procedure for the Jobshop Scheduling Problem.
    This is the disjunctive programming formulation.
    Formulation from Pinedo 2009.
    """
    js = Jobshop()
    js.addJobs(jobs)

    prob = LpProblem("Job shop", LpMinimize)

    H = sum(js.node[j]['p'] for j in js)
    T = range(H + 1)

    x = LpVariable.dicts("x", [(ij, t) for ij in js for t in T], 0, 1, cat=LpInteger)

    C = LpVariable.dicts("C", [ij for ij in js])
    for ij in js:
        prob += C[ij] == lpSum([t * x[(ij, t)] for t in T])

    prob += C["V"]

    for ij in js:
        prob += lpSum([x[(ij, t)] for t in T]) == 1

    for ij in js:
        prob += C[ij] >= js.node[ij]['p']

    for ij in js:
        for k in js. predecessors(ij):
            prob += C[ij] >= C[k] + js.node[ij]['p']

    p = lambda ij, t: lpSum([x[(ij, u)] for u in range(t, t + js.node[ij]['p'])])

    for i in js.machines:
        for t in T:
            prob += lpSum([p(ij, t) for ij in js.machines[i] if t <= H - js.node[ij]['p'] + 1]) <= 1

    prob.solve(GUROBI())
    #prob.solve()

    print("status", LpStatus[prob.status])
    print("objective", value(prob.objective))

    for j in js:
        for t in T:
            if x[j, t].varValue > 0:
                js.add_node(j, C=t)

    js.output()

LP(jobs)