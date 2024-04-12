import sys
input = sys.stdin.readline
from collections import deque

stack = []
strs = input().rstrip()
boom = list(input().rstrip())
for i in strs:
    if len(stack)==0:
        stack += i
        continue
    stack += i
    while True:
        if stack[-len(boom):] == boom:
            for _ in range(len(boom)):
                stack.pop()
            #stack = stack[:len(stack) - len(boom)]
        else:
            break

if len(stack) == 0:
    print("FRULA")
else:
    print("".join(stack))