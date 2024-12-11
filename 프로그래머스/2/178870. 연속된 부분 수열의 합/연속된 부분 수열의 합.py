def solution(sequence, k):
    left, right = 0, 0
    current_sum = sequence[0]
    answer = []
    min_length = float('inf')  # 최소 길이를 추적
    
    while right < len(sequence):
        if current_sum == k:
            # 길이가 짧거나, 길이가 같으면 더 작은 인덱스를 선택
            if right - left < min_length:
                min_length = right - left
                answer = [left, right]
        if current_sum < k:
            # 현재 합이 k보다 작으면 오른쪽 포인터 이동
            right += 1
            if right < len(sequence):
                current_sum += sequence[right]
        else:
            # 현재 합이 k 이상이면 왼쪽 포인터 이동
            current_sum -= sequence[left]
            left += 1
    
    return answer