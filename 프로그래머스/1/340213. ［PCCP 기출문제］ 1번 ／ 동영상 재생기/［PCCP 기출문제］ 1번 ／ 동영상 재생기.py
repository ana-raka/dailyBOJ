# 알고리즘: 구현
# 시간복잡도: O()
# 자료구조: 리스트
def solution(video_len, pos, op_start, op_end, commands):
    video_len = list(map(int,video_len.split(":")))
    video_len = video_len[0] * 60 + video_len[1]
    pos = list(map(int,pos.split(":")))
    pos = pos[0] * 60 + pos[1]
    op_start = list(map(int,op_start.split(":")))
    op_start = op_start[0] * 60 + op_start[1]
    op_end = list(map(int,op_end.split(":")))
    op_end = op_end[0] * 60 + op_end[1]
    for command in commands:
        if op_start <= pos <= op_end:
            pos = op_end
        if command == "prev":
            pos -= 10
            if pos < 0:
                pos = 0
        else:
            pos += 10
            if pos > video_len:
                pos = video_len
    if op_start <= pos <= op_end:
        pos = op_end
    mm = pos // 60
    ss = pos % 60
    return f"{mm:02}:{ss:02}"