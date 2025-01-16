# 알고리즘: BFS
# 시간복잡도: O(N^2)
# 자료구조: 큐
from collections import deque

def solution(n, computers):
    visited = [False] * n
    que = deque()
    answer = 0
    for i in range(n):
        if not visited[i]:
            visited[i] = True
            que.append(i)
            while que:
                y = que.popleft()
                for idx, is_connect in enumerate(computers[y]):
                    if is_connect == 1 and visited[idx] == False:
                        visited[idx] = True
                        que.append(idx)
            answer += 1
    return answer