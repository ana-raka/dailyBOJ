# 알고리즘: 정렬 
# 시간복잡도:
# 자료구조:

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
                