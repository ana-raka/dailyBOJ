import sys
input = sys.stdin.readline

n, m = map(int,input().split())
numl = [True for i in range(n + 1)]
cnt = 0
flag = False
for i in range(2, n + 1):
    for j in range(i, n + 1, i):
        if numl[j]:
            numl[j] = False
            cnt += 1
        if cnt == m:
            print(j)
            flag = True
            break
    if flag:
        break