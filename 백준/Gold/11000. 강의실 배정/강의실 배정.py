import sys
input = sys.stdin.readline
from queue import PriorityQueue

numl = []
for i in range(int(input().rstrip())):
    numl.append(list(map(int,input().split())))
numl.sort(key=lambda x : (x[0],x[1]))
res = PriorityQueue()
for new_lect in numl:
    if res.qsize() == 0:
        res.put(new_lect[1])
        continue
    min_val = res.get()
    if min_val > new_lect[0]:
        res.put(min_val)
    res.put(new_lect[1])
print(res.qsize())