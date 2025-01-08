# 알고리즘: 정렬
# 시간복잡도: O(N)
# 자료구조: 큐
from collections import deque

def solution(priorities, location):
    deq = deque((p, i == location) for i, p in enumerate(priorities))
    sorted_priorities = sorted(priorities)
    cnt = 1
    while deq:
        priority, is_target = deq[0]
        if priority == sorted_priorities[-1]:
            if is_target:
                break
        
            deq.popleft()
            sorted_priorities.pop()
            cnt += 1
        else:
            deq.rotate(-1)        
    return cnt