import sys
input = sys.stdin.readline

def solv(num):
    numl = [True for i in range(num+1)]
    primel = []
    for i in range(2,num+1):
        if numl[i]:
            primel.append(i)
            for j in range(i * 2 , num + 1, i):
                numl[j] = False
    right = left = 0
    res = cnt = 0
    while right <= len(primel):
        if res < n:
            if right < len(primel):
                res += primel[right]
            right += 1
        elif res >= n:
            if res == n:
                cnt += 1
            res -= primel[left]
            left += 1

    print(cnt)
n = int(input().rstrip())
solv(n)