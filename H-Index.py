def solution(citations):
    answer = 0
    
    citations.sort()
        
    prev = -1
    for i in range(len(citations) // 2 + 1):
        for num in range(prev + 1, citations[i] + 1):
            if i <= num <= len(citations) - i:
                answer = num
        prev = citations[i]
    
    return answer