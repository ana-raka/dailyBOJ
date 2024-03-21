import sys
input = sys.stdin.readline
from collections import deque

for _ in range(int(input().rstrip())):
    res = 0
    input()
    A_list = list(map(int,input().split()))
    B_list = list(map(int, input().split()))
    A_list.sort(reverse=True)
    B_list.sort(reverse=True)
    temp = 0

    for numB in A_list:
        for i in range(temp, len(B_list)):
            if numB > B_list[i]:
                res += len(B_list) - i
                break
            else:
                temp = i
    print(res)