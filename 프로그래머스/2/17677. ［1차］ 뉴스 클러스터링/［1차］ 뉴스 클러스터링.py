def solu_dict(str):
    
    tmp_dict = {}
    for i in range(0, len(str) - 1 ):
        #print(str[i:i+2])
        if str[i:i+2].isalpha():
            if str[i:i+2].upper() in tmp_dict:
                tmp_dict[str[i:i+2].upper()] += 1
            else:
                tmp_dict[str[i:i+2].upper()] = 1   
    return tmp_dict
    
def solution(str1, str2):
    answer = 0
    one = {}
    two = {}
        
    one = solu_dict(str1)
    two = solu_dict(str2)

    #print(one)
    #print(two)
    
    inter = {}
    union = {}
    
    #교
    for key in one:
        if key in two:
            inter[key] = min(one[key], two[key])
            
    #합        
    for key, value in one.items():
        union[key] = value
        
    for key, value in two.items():
        if key not in union:
            union[key] = value
        elif key in union:
            union[key] = max(union[key] , value)
    
    #print(inter)
    #3print(union)
    
    if len(union) == 0:
        return 65536
    
    #print(sum(inter.values())/sum(union.values()))
    
    return int(sum(inter.values())/sum(union.values()) * 65536)