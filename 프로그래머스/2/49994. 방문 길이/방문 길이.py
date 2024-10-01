def solution(dirs):
    answer = 0
    pos = (0, 0)  # 좌표는 (0, 0)에서 시작
    visited_paths = set()  # 지나간 길을 저장할 set
    
    # 이동 방향 정의
    mov = {
        'U': (0, 1),
        'D': (0, -1),
        'L': (-1, 0),
        'R': (1, 0),
    }
    
    for direction in dirs:
        # 현재 좌표
        x, y = pos
        # 이동할 좌표
        nx, ny = x + mov[direction][0], y + mov[direction][1]
        
        # 좌표평면의 경계를 벗어나는 경우 무시
        if nx < -5 or nx > 5 or ny < -5 or ny > 5:
            continue
        
        # 경로 저장 (시작점, 끝점)
        path = (pos, (nx, ny))
        reverse_path = ((nx, ny), pos)  # 역방향도 동일한 경로로 취급
        
        # 처음 지나가는 길이라면 경로 추가
        if path not in visited_paths and reverse_path not in visited_paths:
            visited_paths.add(path)
            visited_paths.add(reverse_path)
            answer += 1
        
        # 좌표 업데이트
        pos = (nx, ny)
    
    return answer
