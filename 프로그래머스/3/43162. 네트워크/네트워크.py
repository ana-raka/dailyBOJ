# 알고리즘: BFS
# 시간복잡도: 
# 자료구조: 큐
from collections import deque

def solution(n, computers):
    que = deque()
    answer = 0
    for i in range(n):
        for j in range(n):
            if computers[i][j] == 1:
                computers[i][j] == 0
                que.append(i)
                while que:
                    y = que.popleft()
                    for idx in range(n):
                        if computers[y][idx] == 1:
                            computers[y][idx] = 0
                            computers[idx][y] = 0
                            que.append(idx)
                answer += 1
    return answer