def solution(n, left, right):
    answer = []
    
    for index in range(left, right+1):
        row = index // n + 1
        col = index % n
        answer.append(max(row,col + 1))
    
    return answer