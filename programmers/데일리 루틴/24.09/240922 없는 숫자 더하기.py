def solution(numbers):
    num = []    #존재하지 않는 수 저장하는 배열.
    for i in range(10): #10번 반복
        if i not in numbers:    #i가 numbers에 존재하지 않으면
            num.append(i)   #num에 추가.
    return sum(num) #num의 총합을 반환.