def solution(n):
    answer = []

    re_n = str(n)
    k = len(re_n)
    
    for i in range(k-1, -1 ,-1):
        answer.append(int(re_n[i]))
    
    return answer