# 알고리즘: 플로이드-와샬
# 시간복잡도: O(N^3)
# 자료구조: 그래프 

def solution(n, results):
    graph = [[False for _ in range(n+1)] for _ in range(n+1)]
    for wnode, lnode in results:
        graph[wnode][lnode] = True
    
    for k in range(1,n+1):
        for i in range(1,n+1):
            for j in range(1,n+1):
                if graph[i][k] and graph[k][j]:
                    graph[i][j] = True
    answer = 0
    for i in range(1,n+1):
        known = 0
        for j in range(1,n+1):
            if graph[i][j] or graph[j][i]:
                known += 1
        if known == n - 1:
            answer += 1
    return answer