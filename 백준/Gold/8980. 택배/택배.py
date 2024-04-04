import sys
input = sys.stdin.readline
from queue import PriorityQueue

def load():
    global weight
    boxl.sort(key=lambda x: (x[0], x[1], -x[2]))
    while boxl and vil_num == boxl[0][0]:
        f_vil, t_vil, val = boxl.pop(0)
        if weight + val <= C:
            car[t_vil].append(val)
            weight += val
        else:
            if weight == C:
                continue
            car[t_vil].append(C-weight)
            weight = C

def drop(vil_num_drop):
    global res, weight
    for i in range(1,len(car)):
        for val in car[i]:
            if i == vil_num_drop:
                res += val
                #weight -= val
            else:
                boxl.append([vil_num_drop,i,val])
        car[i] = []
    weight = 0



N, C = map(int,input().split())
boxl = []
car = [[] for _ in range(N+1)]
weight = 0
res = 0
for _ in range(int(input().rstrip())):
    boxl.append(list(map(int,input().split())))
for vil_num in range(1,N+1):
    if vil_num == 1:
        load()
        continue
    drop(vil_num)
    load()
print(res)