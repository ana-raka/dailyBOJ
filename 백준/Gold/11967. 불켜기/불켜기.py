import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    global cnt
    while q:
        x,y = q.popleft()
        for switch_x, switch_y in switch_list[y][x]:
            if mage[switch_y][switch_x] == 0:
                find(switch_x,switch_y)

        for i in range(4):
            mvy = y + my[i]
            mvx = x + mx[i]
            if 0 <= x + mx[i] <= n - 1 and 0 <= y + my[i] <= n - 1:
                if mage[mvy][mvx] == 1:
                    q.append((mvx, mvy))
                    mage[mvy][mvx] = 2

def find(a,b):
    global cnt
    if mage[b][a] == 0:
        mage[b][a] = 1
        cnt += 1
    for i in range(4):
        mvy = b + my[i]
        mvx = a + mx[i]
        if 0 <= a + mx[i] <= n - 1 and 0 <= b + my[i] <= n - 1:
            if mage[mvy][mvx] == 2:
                q.append((a, b))
                mage[b][a] = 2
                return

n, m = map(int,input().split())
cnt = 0
mx = [1,-1,0,0]
my = [0,0,1,-1]
mage = [[0 for _ in range(n)] for _ in range(n)]
switch_list = [[[] for _ in range(n)] for _ in range(n)]
q = deque()
for _ in range(m):
    x,y,a,b = map(int,input().split())
    switch_list[y-1][x-1].append([a-1,b-1])
mage[0][0] = 2
q.append((0,0))
bfs()
print(cnt+1)