def solution(X, Y):
    answer = ''
    
    d_x, d_common = {}, {}
    
    for num in X:
        if num not in d_x:
            d_x[num] = 1
        else:
            d_x[num] += 1
    # print(f"d_x: {d_x}")
    
    for num in Y:
        # 공통된 문자가 있으면
        if num in d_x:
            # 공통 딕셔너리에 추가
            if num not in d_common:
                d_common[num] = 1
            else:
                d_common[num] += 1
            # d_x에 1개 차감
            if d_x[num] == 1:
                d_x.pop(num)
            else:
                d_x[num] -= 1
    # print(f"d_common: {d_common}")
    
    # 공통 문자가 없는 case 처리
    if len(d_common) == 0:
        return "-1"
    
    # 0만 있는 case 처리
    if len(d_common) == 1 and '0' in d_common:
        return "0"
    
    # 문자열 배열로 만들고 역순으로 정렬
    l = []
    for num, freq in d_common.items():
        for i in range(freq):
            l.append(num)
    l.sort(reverse=True)
    # print(l)
    
    answer = ''.join(l)
    
    return answer