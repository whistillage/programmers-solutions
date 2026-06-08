import math

def solution(n):
    answer = 0
    
    for i in range(1, int(math.sqrt(n)) + 1):
        if n % i == 0:
            d, q = i, n / i
            answer += d
            if d != q:
                answer += q
    
    return answer