def solution(a, b):
    answer = 0
    if a <= b:  #a가 b보다 작으면 a부터 b까지 증가시키며 덧셈 연산
        for i in range(a, b+1):
            answer += i
    elif a > b: #a가 b보다 크면 a부터 b까지 감소시키며 덧셈 연산
        for i in range(a, b-1, -1):
            answer += i
    return answer

a, b = map(int, input().split())
print(solution(a, b))