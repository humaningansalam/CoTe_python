from collections import Counter

def solution(participant, completion):

    participant_count = Counter(participant)
    completion_count = Counter(completion)

    answer_count = participant_count - completion_count
    
    answer = list(answer_count.keys())[0]
    
    return answer