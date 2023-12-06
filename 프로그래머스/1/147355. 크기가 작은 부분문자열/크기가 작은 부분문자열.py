def solution(t, p):
    answer = 0
    
    len_t = len(str(t))
    len_p = len(str(p))

    print(len_t)
    print(len_p)
    
    for i in range(len_t - len_p + 1):
        if int(p) >= int(str(t)[i:i+len_p]):
                 answer += 1

                            
                             
    
    return answer