def solution(clothes):
    answer = 0
    
    tmp = {}
    
    for i in range(len(clothes)):
        if clothes[i][1] in tmp:
            tmp[clothes[i][1]] += 1
        else:
            tmp[clothes[i][1]] = 1
    
    product = 1
    for value in tmp.values():
        product *= (value+1)
        
    
    
    return product - 1