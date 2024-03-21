from collections import deque
import sys
input = sys.stdin.readline

def find(val):
    global is_pyu
    temp = []
    while q:
        y3,x3 = q.popleft()
        temp.append((y3, x3))
        for i in range(4):
            mvx = x3 + mx[i]
            mvy = y3 + my[i]
            if mvx > 5 or mvy > 11 or mvy < 0 or mvx < 0:
                continue
            if mage[mvy][mvx] == val and visit[mvy][mvx] == 0:
                q.append((mvy,mvx))
                visit[mvy][mvx] = 1
    if len(temp) >= 4:
        while temp:
            stack.append(temp.pop())
        is_pyu = True
def down():
    idx_cnbheck = [0 for _ in range(6)]
    while stack:
        y, x = stack.pop()
        mage[y][x] = '.'
        idx_cnbheck[x] = 1
    for num in range(6):
        down_cnt = idx_cnbheck[num]
        if down_cnt == 0:
            continue
        ent = 11
        for j in range(11,-1,-1):
            if mage[j][num] != ".":
                    mage[ent][num] = mage[j][num]
                    if j != ent:
                        mage[j][num] = "."
                    ent -= 1
mx = [1,-1,0,0]
my = [0,0,-1,1]

mage = []
q = deque()
for _ in range(12):
    mage.append(list(input().rstrip()))
cnt = 0
is_pyu = True
while True:
    if is_pyu == False:
        break
    is_pyu = False
    stack = []
    visit = [[0 for _ in range(6)] for i in range(12)]
    for i in range(12):
        for j in range(6):
            if mage[i][j] != '.' and visit[i][j] != 1:
                q.append((i, j))
                visit[i][j] = 1
                find(mage[i][j])
    if is_pyu:
        down()
        cnt += 1
print(cnt)