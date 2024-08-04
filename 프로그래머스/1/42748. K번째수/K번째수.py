def solution(array, commands):
    
    answer = []

    for x in commands:
        i, j, y = x
        tmp = []
        for index, z in enumerate(array):
            if index >= i-1  and index < j:
                tmp.append(z)

        tmp.sort()

        answer.append(tmp[y-1])

    return answer