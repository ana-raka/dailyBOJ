def solution(numbers):
    sumValue = 0
    for i in range(10):
        if not i in numbers:
            sumValue += i
    return sumValue
            