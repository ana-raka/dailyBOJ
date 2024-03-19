import sys, math
input = sys.stdin.readline
def solution(num):
    cnt = 0
    ck_left = ck_right = num
    while ck_left > 0:
        if ck_left in numl:
            break
        ck_left -= 1
        cnt += 1

    left = cnt - 1
    cnt = 0

    while ck_right < 1001:
        if ck_right in numl:
            break
        ck_right += 1
        cnt += 1
    right = cnt - 1
    if left == -1 or right == -1:
        print(0)
        exit()
    print(left * (right + 1) + right)

input()
numl = list(map(int,input().split()))
n = int(input().rstrip())
solution(n)