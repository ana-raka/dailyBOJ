# 알고리즘: 
# 시간복잡도: O(N)
# 자료구조: 큐
from collections import deque

def solution(arr):
    que = deque(arr)
    answer = [-1]
    for number in que:
        if number != answer[-1]:
            answer.append(number)
    answer.pop(0)
    return answer