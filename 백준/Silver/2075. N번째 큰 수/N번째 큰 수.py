import sys
input = sys.stdin.readline
from queue import PriorityQueue

n = int(input().rstrip())
numl = []
for i in range(n):
    for num in map(int,input().split()):
        numl.append(num)
    numl.sort(reverse=True)
    numl = numl[:n]
print(numl[n-1])