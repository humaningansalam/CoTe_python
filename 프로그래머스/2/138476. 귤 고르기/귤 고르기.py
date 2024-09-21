def solution(k, tangerine):
    answer = 0
    
    tmp = {}
    for i in tangerine:
        if i in tmp:
            tmp[i] += 1
        else:
            tmp[i] = 1

    sort_tmp = sorted(tmp.values(), reverse=True)
    #print(sort_tmp)

    total= 0
    for i in sort_tmp:
        total += i
        answer +=1
        if total >= k:
            break
    
    return answer