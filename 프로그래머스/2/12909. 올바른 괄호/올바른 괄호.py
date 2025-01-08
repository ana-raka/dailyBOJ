# 알고리즘: 
# 시간복잡도: O(N)
# 자료구조: 스택

def solution(s):
    stack = []
    for char in s:
        if char == "(":
            stack.append(char)
        else:
            if not stack:
                return False
            stack.pop()
            
    return len(stack) == 0