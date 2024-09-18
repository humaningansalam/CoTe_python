
    
def solution(n):    
    
    pi= [0,1]
    for i in range(2, n+1):
        pi.append(pi[i-1] + pi[i-2])


    return pi[-1] % 1234567