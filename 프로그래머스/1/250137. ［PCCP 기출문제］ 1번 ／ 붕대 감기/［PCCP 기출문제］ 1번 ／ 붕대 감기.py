def solution(bandage, health, attacks):
    max_health = health

    attacks_dict= {key: value for key, value in attacks}
    print(attacks_dict)
    
    seq = 0
    for i in range(1, attacks[-1][0]+1, 1):

        if i in attacks_dict:
            seq = 0
            health -= attacks_dict[i]
        else:
            seq += 1
            if bandage[0] <= seq:
                health = min(health + bandage[2], max_health)
                seq = 0
            health = min(health + bandage[1], max_health)
                
        print(f'i={i}, health={health}')
        
        if health <= 0:
            return -1
    
    return health