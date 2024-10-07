import re
def split_number(s):
    match = re.search(r'\d+', s)
    if match:
        start, end = match.span()
        # 숫자를 기준으로 문자열을 분할
        left = s[:start]
        middle = s[start:end]
        right = s[end:]
        return left, middle, right
    return s, '', ''

def solution(files):
    # 각 파일을 (HEAD, NUMBER, TAIL)로 분리
    split_files = [split_number(file) for file in files]
    
    # 정렬: HEAD는 대소문자 구분 없이, NUMBER는 정수로 변환하여 비교
    sorted_files = sorted(split_files, key=lambda x: (x[0].lower(), int(x[1])))
    
    # 원래 파일 형식으로 다시 결합하여 반환
    answer = [''.join(file) for file in sorted_files]
    
    return answer