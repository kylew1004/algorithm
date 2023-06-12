# https://school.programmers.co.kr/learn/courses/30/lessons/178871

def solution(players, callings):
    idx_dict = {i : player for i, player in enumerate(players)}
    player_dict = {player : i for i, player in enumerate(players)}
    
    for call in callings:
        up_idx = player_dict[call]
        down_player = idx_dict[up_idx - 1]
        
        player_dict[call], player_dict[down_player] = player_dict[down_player], player_dict[call]
        idx_dict[up_idx], idx_dict[up_idx - 1] = idx_dict[up_idx - 1], idx_dict[up_idx]

    answer = [player for player in idx_dict.values()]

    return answer