import sys
input = sys.stdin.readline
from collections import deque

def bfs():
    while q:
        y, x, w  = q.popleft()
        if x == m-1 and y == n-1:
            print(visit[y][x][w])
            exit()
        for i in range(4):
            mvx = x + mx[i]
            mvy = y + my[i]
            if 0<= mvx <= m-1 and 0<= mvy <= n -1:
                if visit[mvy][mvx][w] == 0 and mage[mvy][mvx] == 0:
                    q.append((mvy, mvx, w))
                    visit[mvy][mvx][w] = visit[y][x][w] + 1
                elif mage[mvy][mvx] == 1 and w == 0:
                    q.append((mvy, mvx, w + 1))
                    visit[mvy][mvx][w + 1] = visit[y][x][w] + 1

n,m = map(int,input().split())
mx = [-1,1,0,0]
my = [0,0,-1,1]
mage = []
for _ in range(n):
    mage.append(list(map(int,input().rstrip())))

visit = [[[0,0] for i in range(m)] for j in range(n)]
q = deque()
q.append((0, 0, 0))
visit[0][0][0] = 1
bfs()
print(-1)