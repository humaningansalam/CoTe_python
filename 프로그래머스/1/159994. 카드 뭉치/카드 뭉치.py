def solution(cards1, cards2, goal):

    i=0
    j=0
    for x in goal:
        if i < len(cards1) and cards1[i] == x:
            i += 1
        elif j < len(cards2) and cards2[j] == x:
            j += 1
        else:
            return 'No'
            
    return 'Yes'

