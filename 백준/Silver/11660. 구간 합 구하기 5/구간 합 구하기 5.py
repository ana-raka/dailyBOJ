#알고리즘: 누적합
#시간복잡도: O(N*M)
#자료구조: 리스트

import sys
input = sys.stdin.readline

def make_prefixSum():
    for i in range(1,n+1):
        for j in range(1,n+1):
            prefixSum[i][j] = prefixSum[i-1][j] + prefixSum[i][j-1] - prefixSum[i-1][j-1] + arr[i-1][j-1]

def get_prefixSum(x1, y1, x2, y2):
    return prefixSum[x2][y2] - prefixSum[x2][y1-1] - prefixSum[x1-1][y2] + prefixSum[x1-1][y1-1]


n, m = map(int, input().split())
arr = []
prefixSum = [[0 for j in range(n+1)] for i in range(n+1)]
for _ in range(n):
    arr.append(list(map(int,input().split())))
make_prefixSum()
for _ in range(m):
    x1, y1, x2, y2 = map(int,input().split())
    print(get_prefixSum(x1,y1,x2,y2))