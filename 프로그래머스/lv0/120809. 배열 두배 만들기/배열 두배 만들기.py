def solution(numbers):
    answer = []
    n = len(numbers)
    for i in range(n):
        answer.append(numbers[i] * 2)
    
    return answer