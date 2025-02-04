def solution(s):
    s = s.lower()
    pcnt = s.count("p")
    ycnt = s.count("y")
    if pcnt == ycnt:
        return True
    else:
        return False