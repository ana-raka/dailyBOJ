# 알고리즘: DFS
# 시간복잡도: O(NlongN)
# 자료구조: 스택, 리스트
from collections import defaultdict, deque

def solution(tickets):
    flight = defaultdict(list)
    for fr, to in tickets:
        flight[fr].append(to)
    
    for key in flight:
        flight[key].sort(reverse=True)

    stack = ["ICN"]
    path = []

    while stack:
        while flight[stack[-1]]:
            stack.append(flight[stack[-1]].pop())
        path.append(stack.pop())

    return path[::-1]