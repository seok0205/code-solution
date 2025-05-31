'''
S3 1463 1로 만들기

정수 X에 사용할 수 있는 연산은 다음과 같이 세가지

1. X가 3으로 나누어 떨어지면, 3으로 나눈다.
2. X가 2로 나누어 떨어지면, 2로 나눈다.
3. 1을 뺀다.

정수 N이 주어질 때, 위 연산 세개 활용해 1을 만들려고 함. 연산을 사용하는 최대 횟수 최솟값 구하는 문제.

입력은 1보다 크가나 같고, 10의 6승보다 작거나 작은 정수 N
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def cal(num, cnt):
    global result

    if num == 1:            # 목표 값 만들면 최솟값인지 확인 후 종료
        result = min(result, cnt)
        return
    
    if cnt >= result:       # 구한 최솟값 보다 커지면 끝
        return
    
    if num % 3 == 0:        # 나눌수 있거나 뺄수 있는 상태에서만 연산 실행
        cal(num//3, cnt + 1)
    if num % 2 == 0:
        cal(num//2, cnt + 1)
    cal(num-1, cnt + 1)


N = int(input())
result = float('inf')

cal(N, 0)

print(result)