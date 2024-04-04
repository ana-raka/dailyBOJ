import sys
input = sys.stdin.readline
from queue import PriorityQueue

def load(vil_num_load):
    global weight
    boxl[vil_num_load].sort(key=lambda x: (x[0], x[1]))
    for to_vil, val in boxl[vil_num_load]:
        if weight + val <= C:
            car[to_vil].append(val)
            weight += val
        else:
            if weight == C:
                break
            car[to_vil].append(C-weight)
            weight = C
        boxl[vil_num_load] = []
def drop(vil_num_drop):
    global res, weight
    for i in range(vil_num_drop,len(car)):
        for val in car[i]:
            if i == vil_num_drop:
                res += val
                #weight -= val
            else:
                boxl[vil_num_drop].append([i,val])
        car[i] = []
    weight = 0

N, C = map(int,input().split())
boxl = [[] for _ in range(N+1)]
car = [[] for _ in range(N+1)]
weight = 0
res = 0
for _ in range(int(input().rstrip())):
    f_vil, t_vil, val = map(int,input().split())
    boxl[f_vil].append([t_vil,val])
for vil_num in range(1,N+1):
    if vil_num == 1:
        load(vil_num)
        continue
    drop(vil_num)
    load(vil_num)
print(res)