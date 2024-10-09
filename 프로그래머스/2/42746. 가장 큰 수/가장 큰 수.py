

def solution(numbers):
    answer = ''
    
    numbers = list(map(str, numbers))
    
    numbers.sort(key=lambda x: x*6, reverse=True)
    

    answer = str(int(''.join(numbers)))

    return answer