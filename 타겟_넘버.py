def solution(numbers, target):
    answer = 0
    
    def dfs(idx, cur_sum):
        if idx == len(numbers):
            if target == cur_sum:
                return 1
            else:
                return 0
        return dfs(idx + 1, cur_sum + numbers[idx]) + dfs(idx + 1, cur_sum - numbers[idx])
    
    answer = dfs(0, 0)
    
    return answer