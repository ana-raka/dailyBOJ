# 알고리즘: 완전탐색, 소수 찾기
# 시간복잡도: 
# 자료구조: 집합
from itertools import permutations

def is_prime(target):
    if target < 2:
        return False
    for i in range(2, int(target ** 0.5) + 1):
        if target % i == 0:
            return False
    return True

def solution(numbers):
    num_set = set() 
    for i in range(1, len(numbers) + 1): 
        for perm in permutations(numbers, i):
            num = int("".join(perm))
            num_set.add(num)
            
    answer = sum(1 for num in num_set if is_prime(num))
    return answer