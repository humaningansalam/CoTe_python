def solution(phone_number):
    answer = ''

    
    for idx, value in enumerate(reversed(phone_number)):
        if idx > 3:
            answer += '*'
        else:
            answer += value
            

    return answer[::-1]