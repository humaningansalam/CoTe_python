def solution(absolutes, signs):
    answer = 0
    for idx, value in enumerate(signs):
        tmp_abs = absolutes[idx]
        if value:
            answer += tmp_abs * 1
        else:
            answer += tmp_abs * -1
    
    return answer