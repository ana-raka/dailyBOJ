def solution(phone_number):
    numberLength = len(phone_number)
    return "*" * (numberLength - 4) + phone_number[-4:]