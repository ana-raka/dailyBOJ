def solution(name):
    front = ord('A')
    back = ord('Z')
    change_count = 0
    for ch in name:
        change_count += min(ord(ch) - front, (back - ord(ch)) + 1)
        
    n = len(name)
    move_count = n - 1 
    for i in range(n):
        next_i = i + 1
        while next_i < n and name[next_i] == 'A':
            next_i += 1
        move_count = min(move_count, 2 * i + n - next_i, i + 2 * (n - next_i))
    
    return change_count + move_count