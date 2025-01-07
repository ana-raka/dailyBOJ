# 알고리즘: 해시
# 시간복잡도: O(N*M), M의 최대값 = 20 --> O(N)
# 자료구조: 딕셔너리

def solution(phone_book):
    phone_dict = {}
    for number in phone_book:
        phone_dict[number] = 1
    for number in phone_book:
        temp = ""
        for num in number:
            temp += num
            if temp in phone_dict and temp != number:
                return False
    return True
                