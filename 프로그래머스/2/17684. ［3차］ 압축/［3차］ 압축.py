def solution(msg):
    answer = []

    letters={}
    for i in range(26):
        letters[chr(65 + i)] = i+1
        
    #print(letters)
    
    index = 0
    while index < len(msg):
        word = msg[index]
        ii = 1
        #print( msg[index:index+ii])
        while index + ii <= len(msg) and msg[index:index+ii] in letters:
            word = msg[index:index+ii]
            ii += 1
        
        answer.append(letters[word])
        
        if index + ii - 1 < len(msg):
            new_word = msg[index:index+ii]
            letters[new_word] = len(letters) + 1
        
        index += len(word)

    return answer