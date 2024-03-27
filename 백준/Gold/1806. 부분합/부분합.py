import sys
input = sys.stdin.readline

n, m = map(int,input().split())
numl = list(map(int,input().split()))
left = right = 0
res = idx = 0
is_add = True
res_cnt = 100001
while right != n:
    if is_add:
        idx += 1
        res += numl[right]
    if res >= m:
        res -= numl[left]
        left += 1
        res_cnt = min(res_cnt,idx)
        idx -= 1
        is_add = False
        continue
    elif res < m:
        right += 1
    is_add = True

if res_cnt == 100001:
    print(0)
else:
    print(res_cnt)