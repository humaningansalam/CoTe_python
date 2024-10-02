def solution(numbers):
    answer = [-1] * len(numbers)  # 결과 리스트를 -1로 초기화
    stack = []  # 인덱스를 저장하는 스택

    for i in range(len(numbers)):
        # 스택에 값이 있고, 현재 숫자가 스택 상단 숫자보다 클 때
        while stack and numbers[stack[-1]] < numbers[i]:
            index = stack.pop()  # 스택에서 인덱스를 꺼내서
            answer[index] = numbers[i]  # 그 인덱스의 값을 현재 숫자로 변경

        stack.append(i)  # 현재 인덱스를 스택에 추가

    return answer