def solution(n):
    temp = n ** 0.5
    if temp == int(temp):
        return (temp+1) ** 2
    else:
        return -1