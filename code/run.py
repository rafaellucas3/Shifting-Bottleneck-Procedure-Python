from classes import Job, Jobshop, Shift

js = Shift()

jobs = {}
jobs[1] = Job(1, [1,2,3], [10, 8, 4])
jobs[2] = Job(2, [2,1,4,3], [8,3,5,6])
jobs[3] = Job(3, [1,2,4], [4,7,3])

js.addJobs(jobs)

js.criticalPath
js.output()

js.computeLmax()

js.add_edges_from([((1,1), (1,2)), ((1,2),(1,3))])

js.criticalPath
print(js.makespan)

js = Shift()
jobs = {}
jobs[1] = Job(1, [1,2], [3,4])
jobs[2] = Job(2, [1,2], [6,5])
jobs[3] = Job(3, [1,2], [4,5])
jobs[4] = Job(4, [1,2], [3,2])
jobs[11] = Job(11, [1,2], [12,2])

js.addJobs(jobs)
js.criticalPath
js.output()
print(sum(js.node[ij]['p'] for ij in js.machines[1]))
print(sum(js.node[ij]['p'] for ij in js.machines[2]))

seq = (3,2,1,11,4)
for j1, j2 in zip(seq[:-1], seq[1:]):
    js.add_edge((1,j1), (1,j2))

js.criticalPath
js.output()