def solution(k, m, score):
    answer = 0
    
    #print(len(score)//m)
    score.sort(reverse=True)
    #print(score)
    
    for i in range(0, len(score) - len(score) % m, m):
        tmp = score[i:i + m]
        answer += min(tmp) * m
        
    
    return answer