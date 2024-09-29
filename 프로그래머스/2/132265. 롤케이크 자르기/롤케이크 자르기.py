def solution(topping):
    answer = 0
    
    l_dict= {}
    r_dict = {}
    for i in topping:
        if i in l_dict:
            l_dict[i] += 1
        else:
            l_dict[i] = 1
    
    for i in topping:
        
        if i in r_dict:
            r_dict[i] += 1
        else:
            r_dict[i] = 1
            
        l_dict[i] -= 1
        if l_dict[i] == 0:
            del l_dict[i]
        
        if len(l_dict) == len(r_dict):
            answer += 1
        
    return answer