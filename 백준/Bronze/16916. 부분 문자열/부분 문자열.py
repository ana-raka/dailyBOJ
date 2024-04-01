import sys
input = sys.stdin.readline
from collections import deque

stl = input().rstrip()
P = input().rstrip()
if P in stl:
    print(1)
else:
    print(0)
