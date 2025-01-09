# 알고리즘: 
# 시간복잡도: O()
# 자료구조: 스택

def solution(prices):
    answer = [0 for _ in range(len(prices))]
    stack = []
    for i, price in enumerate(prices):
        while stack and stack[-1][1] > price:
            idx, _ = stack.pop()
            answer[idx] = i - idx
        stack.append((i,price))
        
    end_time = len(prices) - 1 
    while stack:
        idx, _ = stack.pop()
        answer[idx] = end_time - idx
        
    return answer