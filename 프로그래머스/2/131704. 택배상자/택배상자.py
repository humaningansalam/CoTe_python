def solution(order):
    answer = 0
    stack = []
    box = 1  

    for o in order:
        while box <= o:
            stack.append(box)
            box += 1
        
        if stack and stack[-1] == o:
            stack.pop()
            answer += 1
        else:
            break  
                         
    return answer