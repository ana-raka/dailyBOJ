# 알고리즘: DP
# 시간복잡도: O(N^2)
# 자료구조: 그래프
def solution(m, n, puddles):
    graph = [[0 for _ in range(n+1)] for _ in range(m+1)]
    puddle_graph = [[False for _ in range(n+1)] for _ in range(m+1)]
    for y,x in puddles:
        puddle_graph[y][x] = True
        
    graph[1][1] = 1
    for y in range(1,m+1):
        for x in range(1, n+1):
            if not puddle_graph[y][x]:
                graph[y][x] += graph[y-1][x] + graph[y][x-1]
    return graph[m][n] % 1000000007