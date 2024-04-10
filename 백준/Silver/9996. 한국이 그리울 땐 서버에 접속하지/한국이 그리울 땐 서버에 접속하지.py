import sys
input = sys.stdin.readline
from collections import deque

n = int(input().rstrip())
pat = list(input().rstrip().split("*"))
for _ in range(n):
    target = input().rstrip()
    if len(target) >= len("".join(pat)):
        if target[0:len(pat[0])] + target[-len(pat[1]):] == "".join(pat):
            print("DA")
        else:
            print("NE")
    else:
        print("NE")