# 알고리즘: dp
# 시간복잡도: 
# 자료구조: 리스트
def solution(money):
    n = len(money)
    
    def max_steal(sub_money):
        dp = [0] * len(sub_money)
        dp[0] = sub_money[0]
        dp[1] = max(sub_money[0], sub_money[1])
        for i in range(2, len(sub_money)):
            dp[i] = max(dp[i - 1], dp[i - 2] + sub_money[i])
        return dp[-1]
    case1 = max_steal(money[:-1])

    case2 = max_steal(money[1:])
    
    return max(case1, case2)