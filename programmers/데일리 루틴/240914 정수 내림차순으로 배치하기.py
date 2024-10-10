def solution(n):
    a = list(str(n))    #입력 받은 n를 리스트화.
    a.sort(reverse = True)  #정렬하고, reverse까지.
    answer = 0
    for i in range(len(a)): #리스트 길이만큼 반복
        answer += int(a[i]) #1의 자리에 더해 넣음.
        if i != len(a) - 1:
            answer *= 10    #10을 곱해서 1의 자리를 0으로 만듬.
    return answer