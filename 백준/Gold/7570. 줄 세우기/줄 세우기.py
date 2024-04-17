import sys
input = sys.stdin.readline


n = int(input().rstrip())
numl = list(map(int,input().split()))
num_idx = [0 for _ in range(n+1)]
res = 1
max_leng = 0
for idx in range(1,len(numl)+1):
    num_idx[numl[idx-1]] = idx
for i in range(1,n):
    if num_idx[i] < num_idx[i+1]:
        res += 1
    else:
        max_leng = max(max_leng,res)
        res = 1
print(n - max_leng if n != 1 else 0)