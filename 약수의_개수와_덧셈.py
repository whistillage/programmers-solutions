import math

def solution(left, right):
    answer = 0
    
    for num in range(left, right + 1):
        isSquared = False
        for divider in range(1, int(math.sqrt(num)) + 1):
            if num == divider ** 2:
                isSquared = True
        if isSquared:
            answer -= num
        else:
            answer += num
    
    return answer