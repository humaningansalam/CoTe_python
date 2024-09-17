def solution(n):
    answer = 0
    
    number = bin(n)[2:]
    #print(type(number))
    number_one = number.count('1')
    #print(number_one)
    while True:
        n+= 1
        tmp_num = bin(n)[2:]
        tmp_num_one = tmp_num.count('1')
        
        if number_one == tmp_num_one:
            answer = n
            break
    
        
        
    return answer