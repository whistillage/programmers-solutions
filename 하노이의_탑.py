def myfunc(lev, source, target):
    if lev == 1:
        return [[source, target]]
    tmp = 1 + 2 + 3 - source - target
    
    return myfunc(lev-1, source, tmp) + [[source, target]] + myfunc(lev-1, tmp, target)

def solution(n):
    answer = myfunc(n, 1, 3)
    print(myfunc(3, 1, 3))
    
    return answer