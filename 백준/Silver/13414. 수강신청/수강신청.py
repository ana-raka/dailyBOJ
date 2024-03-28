import sys
input = sys.stdin.readline

n, m = map(int,input().split())
dic = {}
for i in range(m):
    stdid = input().rstrip()
    dic[stdid] = i
cnt = 0
stdlist = sorted(dic.items(), key= lambda x : x[1])
for stdid, val in stdlist:
    print(stdid)
    cnt += 1
    if cnt == n:
        exit()