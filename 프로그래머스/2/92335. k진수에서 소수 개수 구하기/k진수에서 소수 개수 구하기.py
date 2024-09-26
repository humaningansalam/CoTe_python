def to_n(num, n):
    if num == 0:
        return '0'
    
    digits= []
    while num:
        convert = num % n
        digits.append(str(convert))
        num //= n
    return ''.join(digits[::-1])

def is_prime(n):
    if n< 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

def solution(n, k):
    answer = 0
    
    #print(to_n(n, k))
    split_n = to_n(n, k).split('0')
    #print(split_n)
    
    for i in split_n:
        if i and is_prime(int(i)):
            answer  += 1

        
    return answer