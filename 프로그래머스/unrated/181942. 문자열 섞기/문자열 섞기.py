def solution(str1, str2):
    answer = ''
    n = len(str1)
    for i in range(n):
        answer += str1[i]
        answer += str2[i]
    return answer