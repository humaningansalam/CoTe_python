from datetime import datetime


def solution(data, ext, val_ext, sort_by):
    answer = [[]]
    col = {
            'code':0,
            'date':1,
            'maximum':2,
            'remain':3,
            }
    print(col[ext])
    print(col[sort_by])


    for i in range(len(data)-1, -1, -1):
        data[i][0] = int(data[i][0])
        data[i][1] = int(data[i][1])
        data[i][2] = int(data[i][2])
        data[i][3] = int(data[i][3])
        
        if col[ext] == 0:
            if val_ext < data[i][0]:
                data.pop(i)
        elif col[ext] == 1:
            if val_ext < data[i][1]:
                data.pop(i)
        elif col[ext] == 2:
            if val_ext < data[i][2]:
                data.pop(i)
        elif col[ext] == 3:
            if val_ext < data[i][3]:
                data.pop(i)
        
    answer  = sorted(data, key= lambda x: x[col[sort_by]])
    
    return answer