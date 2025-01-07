# 알고리즘: 해시
# 시간 복잡도: O(N)
# 자료구조: 디폴트 딕셔너리

from collections import defaultdict

def solution(clothes):
    clothes_dict = defaultdict(int)
    answer = 1
    for cloth, category in clothes:
        clothes_dict[category] += 1
    for count in clothes_dict.values():
        answer *= (count + 1)
        
    return answer - 1