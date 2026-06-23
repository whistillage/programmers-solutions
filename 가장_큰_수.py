def solution(numbers):
    answer = ''
    
    strings = [str(num) for num in numbers]
    
    def pad(str):
        str = str * 4
        return str
    
    padded_strings = [pad(string) for string in strings]
    indices = [i for i in range(len(numbers))]
    indices.sort(key=lambda x: padded_strings[x], reverse=True)
        
    for idx in indices:
        answer += strings[idx]
    
    # exception handling: "0000" => "0"
    isZero = True
    for num in answer:
        if num != "0":
            isZero = False
            break
    if isZero:
        answer = "0"
    
    return answer