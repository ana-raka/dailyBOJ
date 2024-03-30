import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())
numl = list(map(int,input().split()))
left = right = cnt = 0
dic = [0 for i in range(100001)]
while right < n:
    if dic[numl[right]] == 0:
        dic[numl[right]] = 1
        right += 1
    elif dic[numl[right]] == 1:
        while True:
            if numl[left] == numl[right]:
                cnt += right - left
                dic[numl[left]] = 0
                left += 1
                break
            cnt += right - left
            dic[numl[left]] = 0
            left += 1
else:
    while left != right:
        cnt += right - left
        left += 1
print(cnt)