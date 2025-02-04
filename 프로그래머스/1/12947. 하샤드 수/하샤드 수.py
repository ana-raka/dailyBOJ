def solution(x):
    temp = list(str(x))
    answer = 0
    for i in temp:
        answer += int(i)
    if x % answer == 0:
        return True
    else:
        return False
