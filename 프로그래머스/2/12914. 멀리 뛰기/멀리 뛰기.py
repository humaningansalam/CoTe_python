def solution(n):
    answer = 0
    
    tmp = [0] * (n+1)
    tmp[0] = 1
    tmp[1] = 2
        
    #print(tmp)
    for i in range(2,n):
        tmp[i] = tmp[i-2] + tmp[i-1]
	
    return tmp[n-1] % 1234567
