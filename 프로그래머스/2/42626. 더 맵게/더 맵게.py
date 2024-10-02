import heapq

def solution(scoville, K):
    answer = 0
    heapq.heapify(scoville)    

    while scoville:
        # 가장 낮은 스코빌 지수를 가진 두 음식을 꺼냄
        first = heapq.heappop(scoville)
        
        # 만약 첫 번째 음식이 K 이상이라면 반복 종료
        if first >= K:
            return answer
        
        # 두 번째 음식이 없으면 -1 반환
        if not scoville:
            return -1
            
        second = heapq.heappop(scoville)
        
        # 새로운 스코빌 지수 계산
        new_scoville = first + (second * 2)
        
        # 새로운 스코빌 지수를 힙에 추가
        heapq.heappush(scoville, new_scoville)
        
        # 섞은 횟수 증가
        answer += 1

    return -1  