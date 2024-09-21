
from collections import Counter


def solution(want, number, discount):
    answer = 0
    
    last= 10
    want_dict= dict(zip(want, number))
    #print(want_dict)
    for i in range(len(discount)-9):
        #print(i)
        item_count= Counter(discount[i:last+i])
        #print(item_count)
        
        match = True
        for item in want:
            if item_count[item] < want_dict[item]:
                match= False
                break
                
        if match:
            answer +=1
                
            
        
        #print(i)
    
    return answer