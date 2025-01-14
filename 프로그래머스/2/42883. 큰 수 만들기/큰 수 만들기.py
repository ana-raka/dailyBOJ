# 알고리즘: 스택, 그리디
# 시간복잡도: O(N)
# 자료구조: 스택
def solution(number, k):
    number_list = []
    for num in number:
        while number_list and k > 0 and number_list[-1] < num:
            number_list.pop()
            k -= 1
        number_list.append(num)
    if k > 0:
        number_list = number_list[:-k]
    return ''.join(number_list)
    