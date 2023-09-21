def solution(n):
    su = '수'
    subak = '수박'
    answer = ''
    if n%2 == 1:
        answer = subak * ((n-1)//2)
        answer += su
    else:
        answer = subak * (n//2)
    return answer