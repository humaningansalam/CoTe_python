def solution(numbers, target):
    answer = 0
    
    for i in range(1 << len(numbers)):  
        total = 0
        for j in range(len(numbers)):
            if i & (1 << j):
                total += numbers[j]
            else:
                total -= numbers[j]
        
        if total == target:
            answer += 1


    
    return answer