def solution(answers):
    answer = [0,0,0]
    a = [ 1, 2, 3, 4, 5]
    b = [2, 1, 2, 3, 2, 4, 2, 5]
    c = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    for i, value in enumerate(answers):
        
        if value == a[i % len(a)]:
            answer[0] += 1
        if value == b[i % len(b)]:
            answer[1] += 1
        if value == c[i % len(c)]:
            answer[2] += 1
            
    
    max_indices = [i+1 for i, value in enumerate(answer) if value == max(answer)]
            
    

    return max_indices