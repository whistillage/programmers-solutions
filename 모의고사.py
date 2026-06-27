def solution(answers):
    answer = []
    
    supo1 = [1, 2, 3, 4, 5]
    supo2 = [2, 1, 2, 3, 2, 4, 2, 5]
    supo3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    
    scores = [0, 0, 0]
    for idx in range(len(answers)):
        if answers[idx] == supo1[idx % 5]:
            scores[0] += 1
        if answers[idx] == supo2[idx % 8]:
            scores[1] += 1
        if answers[idx] == supo3[idx % 10]:
            scores[2] += 1
    
    if max(scores) == scores[0]:
        answer.append(1)
    if max(scores) == scores[1]:
        answer.append(2)
    if max(scores) == scores[2]:
        answer.append(3)
    
    return answer