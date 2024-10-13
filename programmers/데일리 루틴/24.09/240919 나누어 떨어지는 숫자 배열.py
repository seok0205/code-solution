def solution(arr, divisor):
    answer = []
    
    for i in arr:   #arr에 저장된 값 순서대로 비교.
        if i % divisor == 0:    #i에 divisor 나누고 나누어 떨어지면 리스트에 추가.
            answer.append(i)
    
    answer.sort()   #정렬
    
    if len(answer) == 0:    #리스트에 하나의 값도 없으면 -1 리스트에 저장.
        answer.append(-1)
    
    return answer

arr_1 = [] #대입할 배열 입력.
divisor_1 = int(input())

print(solution(arr_1, divisor_1))