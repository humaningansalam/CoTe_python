from collections import deque

def solution(bridge_length, weight, truck_weights):
    answer = 0
    
    bridge= deque([0] * bridge_length)
    current_weight= 0
    trucks= deque(truck_weights)
    
    #print(bridge_length)
    #print(weight)
    #print(truck_weights)
    
    while trucks or current_weight > 0:
        answer += 1
        current_weight -= bridge.popleft()
        
        if trucks:
            if current_weight + trucks[0] <= weight:
                truck= trucks.popleft()
                bridge.append(truck)
                current_weight += truck
            else:
                bridge.append(0)
        #print(bridge)
    
    return answer