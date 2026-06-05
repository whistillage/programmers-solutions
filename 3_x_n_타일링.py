def solution(n): 
    answer = 0
    
    # for memoization
    memo = [3]
    
    for i in range(n // 2):
        if i >= len(memo):
            new_val = memo[i - 1] * 3 + sum(memo[:-1]) * 2 + 2
            memo.append(new_val)
    
    return memo[-1] % 1000000007