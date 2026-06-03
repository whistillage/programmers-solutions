def solution(cards):
    answer = 0
    
    # 상자 그룹의 길이 정보 저장
    group_lens = []
    
    # 이미 오픈된 카드들
    open_cards = set()
    
    for start_idx in range(len(cards)):
        cur_idx = start_idx
        group_len = 0
        
        while cards[cur_idx] not in open_cards:
            open_cards.add(cards[cur_idx])
            group_len += 1
            cur_idx = cards[cur_idx] - 1
            
        group_lens.append(group_len)
    
    if len(group_lens) >= 2:
        group_lens.sort(reverse = True)
        answer = group_lens[0] * group_lens[1]
    
    return answer