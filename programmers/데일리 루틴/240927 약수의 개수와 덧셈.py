def solution(left, right):
    result = 0
    for i in range(left, right+1):  #left에서 right까지의 수를 반복.
        count = 0   #약수의 개수
        for j in range(1, i+1): #각 수마다 약수의 개수를 구함.
            if i % j == 0:  #약수 개수 구하기.
                count += 1
        if count % 2 == 0:  #약수 개수 짝수면 result에 더함.
            result += i
        else:   #약수 개수 홀수면 result에 뺌.
            result -= i
    return result