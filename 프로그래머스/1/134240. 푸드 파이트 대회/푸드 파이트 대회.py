def solution(food):
    answer = []

    for i in range(1, len(food)):
        count = food[i] // 2
        answer.append(str(i) * count)
    
    left_side = ''.join(answer)
    right_side = left_side[::-1] 
    
    answer = left_side + '0' + right_side
    
    return answer