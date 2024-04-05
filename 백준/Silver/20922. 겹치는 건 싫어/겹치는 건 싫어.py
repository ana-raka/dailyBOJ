import sys
input = sys.stdin.readline

n, k = map(int,input().split())
numl = list(map(int,input().split()))
res = []
num_cnt = [0 for i in range(100001)]
max_leng = 0
for num in numl:
    if num_cnt[num] == k:
        while res[0] != num:
            num_cnt[res.pop(0)] -= 1
        else:
            num_cnt[res.pop(0)] -= 1
    res.append(num)
    num_cnt[num] += 1
    max_leng = max(max_leng, len(res))
print(max_leng)