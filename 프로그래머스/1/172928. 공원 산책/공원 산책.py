def solution(park, routes):
    answer = []
    location = None
    fail_mov = []
    #print(len(park))
    #print(len(park[0]))
    
    for i in range(len(park)):
        for j in range(len(park[0])):
            if park[i][j] == 'S':
                location = (i, j)
            if park[i][j] == 'X':
                fail_mov.append((i,j))
                
    #print(location)
    #print(fail_mov)
    
    mov ={
    'E': (0,1),
    'S': (1,0),
    'N': (-1,0),
    'W': (0, -1),       
    }
    
    for i in routes:
        x, y = i.split(" ")
        temp_location= location
        temp_mov = mov[x]
        temp_block = []
        
        print(f'temp_location = {temp_location}')
        print(f'x = {x}')
        
        # 공원 벗어나는지
        if x == 'E':
            temp_block.append(len(park[0]) - temp_location[1])
        elif x == 'W':
            temp_block.append(temp_location[1]+1)
        elif x == 'S':
            temp_block.append(len(park) - temp_location[0])
        elif x == 'N':
            temp_block.append(temp_location[0]+1)
            
        # 방향 장애물
        for j in fail_mov:
            # E
            if x == 'E':
                if temp_location[0] == j[0]:
                    if j[1] > temp_location[1]:
                        temp_block.append(abs(j[1] - temp_location[1]))
            # W
            elif x == 'W':
                if temp_location[0] == j[0]:
                    if j[1] < temp_location[1]:
                        temp_block.append(abs(j[1] - temp_location[1] ))
            # S
            elif x == 'S':
                if temp_location[1] == j[1]:
                    if j[0] > temp_location[0]:
                        temp_block.append(abs(j[0] - temp_location[0] ))
            # N
            elif x == 'N':
                if temp_location[1] == j[1]:
                    if j[0] < temp_location[0]:
                        temp_block.append(abs(j[0] - temp_location[0] ))
        
        print(temp_block)
        
        if min(temp_block) > int(y):
            temp_mov = (temp_mov[0]*int(y), temp_mov[1]*int(y))
            temp_mov = (temp_mov[0] + temp_location[0], temp_mov[1] + temp_location[1])
            location= temp_mov
        else:
            print('pass')
            continue
   
    return location