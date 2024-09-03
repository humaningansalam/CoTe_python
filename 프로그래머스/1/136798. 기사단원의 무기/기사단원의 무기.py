import math

def get_d(n):
    count = 0
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            count += 1  
            if i != n // i:
                count += 1
    return count

def solution(number, limit, power):
    answer = 0
    
    for i in range(1, number + 1):
        t = get_d(i)
        if t > limit:
            answer += power
        else:
            answer += t

    
    return answer