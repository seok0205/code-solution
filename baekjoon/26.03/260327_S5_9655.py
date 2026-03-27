'''
S5 9655 돌 게임

문제 설명:
돌 게임은 둘(상근, 창영)이서 하는 게임.
탁자 위에 N개의 돌이 있다.
턴을 번갈아가며 돌을 가져가고, 돌 1개 혹은 3개 가져갈 수 있음. 마지막 돌을 가져가는 사람이 이김.
두사람이 완벽하게 게임을 했을때, 이기는 사람을 구하는 프로그램 작성.
게임은 상근이가 먼저 시작.

입력:
첫째 줄 - N (1 <= N <= 1000)

출력:
상근이가 이기면 SK, 창영이가 이기면 CY 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())

dp = [0] * (N+1)
if N >= 1:
    dp[1] = 1
if N >= 2:
    dp[2] = 0
if N >= 3:
    dp[3] = 1

for i in range(4, N+1):
    if dp[i-1] == 0 or dp[i-3] == 0:
        dp[i] = 1
    else:
        dp[i] = 0

if dp[N]:
    print('SK')
else:
    print('CY')