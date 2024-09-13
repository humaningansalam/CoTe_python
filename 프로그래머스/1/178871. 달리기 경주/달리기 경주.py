def solution(players, callings):

    player_index = {player: i for i, player in enumerate(players)}

    for calling in callings:
        index = player_index[calling] 
        

        if index > 0:
            previous_player = players[index - 1]
            

            players[index], players[index - 1] = players[index - 1], players[index]
            

            player_index[calling] = index - 1
            player_index[previous_player] = index

    return players