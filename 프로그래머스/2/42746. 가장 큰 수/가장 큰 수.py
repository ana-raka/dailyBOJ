# 알고리즘: 정렬, 문자열
# 시간복잡도: O(NlongN)
# 자료구조: 리스트
def solution(numbers):
    numbers = list(map(str, numbers))
    numbers.sort(key=lambda x: x * 10, reverse=True) 
    answer = ''.join(numbers)
    return answer if answer[0] != '0' else '0'