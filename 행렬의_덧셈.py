def solution(arr1, arr2):
    answer = [[]]
    row_num, col_num = len(arr1), len(arr1[0])
    answer = [[0] * col_num for _ in range(row_num)]
    
    for row_idx in range(row_num):
        for col_idx in range(col_num):
            answer[row_idx][col_idx] = arr1[row_idx][col_idx] + arr2[row_idx][col_idx]
    return answer