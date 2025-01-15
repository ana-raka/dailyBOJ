# 알고리즘: DP
# 시간복잡도: O(N^2)
# 자료구조: 리스트
def solution(triangle):
    for i in range(1, len(triangle)):
        m = len(triangle[i])
        for j in range(m):
            if j == 0:
                triangle[i][j] += triangle[i-1][0]
            elif j == m - 1:
                triangle[i][j] += triangle[i-1][-1]
            else:
                triangle[i][j] += max(triangle[i-1][j-1], triangle[i-1][j])    
    else:
        return max(triangle[i])