def solution(my_string, overwrite_string, s):
    answer = ''
    
    n = len(my_string)
    over_ = -1
    i=0
    
    while i < n:

        if over_ == -1 and i >= s:
            for j in overwrite_string:
                answer += j
                i += 1
            over_ = 1
        else:
            answer += my_string[i]
            i += 1
            

    
    return answer