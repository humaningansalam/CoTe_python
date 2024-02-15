def solution(sizes):

    max_value = 0
    min_value = 0
    for size in sizes:
        a, b = size[0], size[1]
        if a < b:
            max_value = max(b, max_value)
            min_value = max(a, min_value)
        else:
            max_value = max(a, max_value)
            min_value = max(b, min_value)
    
    return max_value * min_value