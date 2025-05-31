'''
S3 1003 피보나치 함수

피보나치 함수 f(3)은 f(2)와 f(1)을 호출.
f(2)는 f(1), f(0)을 호출.
두번째 호출의 f(1)은 1을 출력, 1 리턴
f(0)은 0 출력, 0 리턴
f(2)는 f(1)과 f(0)의 결과를 얻고, 1 리턴.
첫 번째 호출한 f(1)은 1출력, 1 리턴
f(3)은 f(2)와 f(1)의 결과 얻고, 2 리턴

피보나치 함수 f(N)을 호출했을 때, 0과 1이 각각 몇 번 출력되는지 구하는 문제.

첫 줄에 테스트 케이스 개수
각 테스트 케이스는 한 줄로 이루어져 있고, N이 주어짐. N은 40보다 작거나 같은 자연수 혹은 0임.

각 테스트 케이스 마다 0이 출력되는 횟수, 1이 출력되는 횟수를 공백으로 구분해 출력.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

def fibonacci(num):     # 피보나치 함수는 규칙이 있음. 2일때부터
    if num == 0:        # num0은 이전 num1의 값이고, num1은 이전 num1에 이전 num0을 더한 값임
        return 1, 0
    elif num == 1:
        return 0, 1
    
    num0, num1 = 0, 1

    for i in range(num-1):  # 위에서 발견한 규칙을 식으로 표현
        new_num0 = num1
        new_num1 = num0 + num1

        num0 = new_num0
        num1 = new_num1

    return num0, num1

T = int(input())

for _ in range(T):
    num = int(input())

    result_num0, result_num1 = fibonacci(num)

    print(result_num0, result_num1)