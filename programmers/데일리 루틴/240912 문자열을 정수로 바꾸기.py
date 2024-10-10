def solution(s):
    if s[0] == '-': #입력받은 수 맨 앞이 -라면 자체를 int타입으로 바꾸고 출력
        return int(s)
    elif s[0] == '+':   #맨 앞이 +라면 +를 제외하고 int타입 변형 출력
        s = s[1:]
        return int(s)
    else:   #아무 부호도 없다면 그냥 int타입 변형 출력
        return int(s)

print(solution(input()))