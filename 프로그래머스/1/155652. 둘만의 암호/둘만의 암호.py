import string

def solution(s, skip, index):
    answer = ''
    alphabet = string.ascii_lowercase
    
    for i in s:
        count = 1
        char_index = alphabet.index(i)
        while count < index+1:
            char_index += 1
            
            if char_index >= len(alphabet):
                char_index -= len(alphabet)
            
            tmp_char = alphabet[char_index]
            if tmp_char not in skip:
                count += 1
            else:
                pass
            
        answer += tmp_char
                
        
    
    return answer