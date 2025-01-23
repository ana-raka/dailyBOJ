# 알고리즘: DP
# 시간복잡도: 
# 자료구조: 집합, 리스트
def solution(N, number):
    if N == number:
        return 1
    answer = 0
    dp = [set() for _ in range(9)]
    dp[1].add(N)
    
    for k in range(2, 9): 
        dp[k].add(int(str(N) * k))
        
        for i in range(1, k):
            for op1 in dp[i]:
                for op2 in dp[k - i]:
                    dp[k].add(op1 + op2)
                    dp[k].add(op1 - op2)
                    dp[k].add(op1 * op2)
                    if op2 != 0:
                        dp[k].add(op1 // op2)
                        
        if number in dp[k]:
            return k
    return -1