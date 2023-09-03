def solution(seoul):
    answer = ''
    
    for key ,value in enumerate(seoul):

        if value == 'Kim':
            answer = f'김서방은 {key}에 있다'
    return answer