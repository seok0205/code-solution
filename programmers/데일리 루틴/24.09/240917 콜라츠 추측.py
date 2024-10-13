def solution(num):
    count = 0 #반복문 반복 횟수
    while num != 1: #1이 될 때까지 반복
        if num % 2 == 0:    #짝수라면 2 나눔
            num /= 2
            count += 1  #실행 횟수 1 증가
        elif num % 2 == 1:  #홀수라면 3 곱하고 1 더함
            num = num * 3 + 1
            count += 1  #실행 횟수 1 증가
    
    if count > 500: #반복 횟수가 500번이 넘을 시 -1 출력
        count = -1
    return count

num = int(input())
print(solution(num))