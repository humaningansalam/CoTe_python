def solution(k, score):
    answer = []
    hall = []
    for x in score:
        hall.append(x)
        hall.sort(reverse=True)  # 리스트 정렬

        if len(hall) >= k:
            hall[:] = hall[:k]  

        answer.append(hall[-1])
        
    return answer