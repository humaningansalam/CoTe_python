
def solution(elements):
    n = len(elements)
    answer = set()
    
    circular_elements = elements * 2

    for length in range(1, n + 1): 
        current_sum = sum(circular_elements[:length])
        answer.add(current_sum)

        for j in range(length, n + length):
            current_sum += circular_elements[j] - circular_elements[j - length]
            answer.add(current_sum)

    return len(answer) 