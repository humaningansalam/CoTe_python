def get_lotto_rank(matched_count):
    return min(7 - matched_count, 6) if matched_count > 1 else 6

def solution(lottos, win_nums):
    zero_count = lottos.count(0)
    match_count = sum(num in win_nums for num in lottos)
    
    max_rank = get_lotto_rank(match_count + zero_count)
    min_rank = get_lotto_rank(match_count)
    
    return [max_rank, min_rank]