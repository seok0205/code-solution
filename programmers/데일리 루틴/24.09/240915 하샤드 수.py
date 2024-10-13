def solution(x):
    num = 0
    x_list = list(str(x))   #입력받은 x를 리스트로 만듦
    for i in range(len(str(x))):
        num += int(x_list[i])   #자릿수를 모두 더한다
    if x % num == 0:    #나누어 떨어지면 true
        answer = True
    else:     #그렇지 않으면 false
        answer = False
    return answer

x = int(input())
print(solution(x))