import math, itertools

def isPrime(x):
    if x == 0 or x == 1:
        return False
    for num in range(2, int(math.sqrt(x)) + 1):
        if x % num == 0:
            return False
    return True

def possibleNums(arr):
    ret = set()
    
    for l in range(1, len(arr) + 1):
        ret.update(set(int(''.join(perm)) for perm in list(itertools.permutations(arr, l))))
    
    return ret

def solution(numbers):
    answer = 0
    
    for num in possibleNums(numbers):
        if isPrime(num):
            answer += 1
    
    return answer