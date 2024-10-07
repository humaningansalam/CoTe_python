from collections import deque

def solution(x, y, n):
    queue = deque()
    queue.append((x,0))
    visited = set()  
    visited.add(x) 
    
    while queue:
        i, j = queue.popleft()
        if i==y: 
            return j
        for k in (i*3,i*2,i+n):
            
            if k <= y and k not in visited:
                queue.append((k,j+1))    
                visited.add(k)
        
        #print(queue)
    return -1