from itertools import product
def solution(word):
    answer = 0
    al= [ 'A', 'E', 'I', 'O', 'U']
    
    al_words = []
    for i in range(1,6):
        al_words += [''.join(p) for p in product(al, repeat=i)]

    al_words.sort()
    return al_words.index(word) + 1