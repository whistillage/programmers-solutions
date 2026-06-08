def solution(spell, dic):
    answer = 0
    len_spell = len(spell)
    
    candidates = [word for word in dic if len(word) == len_spell]
    for c in spell:
        candidates = [word for word in candidates if c in word]
    
    if len(candidates) >= 1:
        answer = 1
    else:
        answer = 2
    
    return answer