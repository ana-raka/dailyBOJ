# 알고리즘: BFS
# 시간복잡도: O(2^N)
# 자료구조: 큐

from collections import deque

def solution(numbers, target):
    que = deque([0])
    for num in numbers:
        next_que = deque() 
        while que:
            prev = que.popleft()
            next_que.append(prev - num)
            next_que.append(prev + num)
        que = next_que  
    return que.count(target)