def solution(numbers):
    def get_next_number(n):
        # 0의 위치를 찾아서 처리하는 방식으로 변경
        bin_n = list('0' + bin(n)[2:])  # 앞에 0을 하나 추가
        length = len(bin_n)
        
        # 오른쪽에서부터 첫 번째 '0' 찾기
        idx = length - 1
        while idx >= 0 and bin_n[idx] == '1':
            idx -= 1
            
        # 찾은 0을 1로 바꾸기
        bin_n[idx] = '1'
        
        # 그 다음 위치부터 끝까지 중에서
        # 원래 수보다는 커야 하고
        # 비트 차이가 2 이하여야 함
        original_ones = bin(n).count('1')
        min_diff = float('inf')
        answer = n
        
        # idx+1 위치부터 모든 가능한 조합 시도
        for i in range(idx+1, length):
            bin_n[i] = '0'
        
        temp = int(''.join(bin_n), 2)
        if temp > n and bin(n ^ temp).count('1') <= 2:
            return temp
            
        for i in range(length-1, idx, -1):
            bin_n[i] = '1'
            temp = int(''.join(bin_n), 2)
            if temp > n and bin(n ^ temp).count('1') <= 2:
                return temp
    
    return [get_next_number(n) for n in numbers]