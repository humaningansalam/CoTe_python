def solution(today, terms, privacies):
    answer = []
    today = today.split('.')
    term = {}
    for i in range(len(terms)):
        x, y = terms[i].split(' ')
        term[x] = y
    
    for i in range(len(privacies)):
        temp_y, temp_m, temp_d = int(today[0]), int(today[1]), today[2]
        
        x = privacies[i].split(' ')
        p_day = x[0].split('.')
        p_y, p_m , p_d = int(p_day[0]), int(p_day[1]), p_day[2]
        
        p_m += int(term[x[1]])
        if p_m > 12:
            p_y += (p_m-1) // 12
            p_m = (p_m-1) % 12 + 1
            
        temp_day = f'{temp_y}{temp_m:02d}{temp_d}'
        #print(temp_day)
        p_day= f'{p_y}{p_m:02d}{p_d}'
        #print(p_day)
        
        if int(p_day) <= int(temp_day):
            answer.append(i+1)
            
        print(answer)
    return answer