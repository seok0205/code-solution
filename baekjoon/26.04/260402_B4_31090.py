'''
B4 31090 2023은 무엇이 특별할까?

문제 설명:
2024는 2023의 끝 두자리인 23으로 나누어 떨어짐.
다음은 6뒤인 2029와 2030.

양의 정수 N이 주어질때, N과 N+1이 이런 조건을 만족하는 관계인지 판별하는 문제.

입력:
T 개수.
TC당 양의 정수 N.
(1 <= T <= 8910, 1000 <= N <= 9999)
N은 100의 배수가 아님.

출력:
나누어 떨어지면 Good, 아니면 Bye 출력. 한줄에 하나씩.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

T = int(input())
for _ in range(T):
    N = int(input())
    new_n = int(str(N)[-2:])
    past = N + 1

    if past % new_n == 0:
        print('Good')
    else:
        print('Bye')