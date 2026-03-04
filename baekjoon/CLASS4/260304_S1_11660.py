'''
S1 11660 구간 합 구하기 5

문제 설명:
NxN개의 수가 NxN 크기의 표에 채워져있음.
주어진 x1,y1 부터 x2,y2까지 합을 구하는 프로그램 작성
표에 채워져있는 수와 합을 구하는 연산이 주어짐.

입력:
첫째 줄에 표의 크기 N과 합을 구해야하는 횟수 M 주어짐. (1 <= N <= 1024, 1 <= M <= 100,000)
둘째 줄부터 N개의 줄에 표에 채워져 있는 수가 1행부터 주어짐.
다음 M개의 줄에는 네 개의 정수 x1, y1, x2, y2가 주어짐. (x1 <= x2, y1 <= y2)
(x1, y1) 부터 (x2, y2)의 합을 구해 출력.
표에 채워진 수는 1,000보다 작거나 같은 자연수.
'''

import sys

# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().split())
chart = []

for _ in range(N):
    temp = list(map(int, input().split()))
    chart.append(temp)

dp = [[0] * (N + 1) for _ in range(N + 1)]

for i in range(1, N+1):
    for j in range(1, N+1):
        dp[i][j] = dp[i-1][j] + dp[i][j-1] - dp[i-1][j-1] + chart[i-1][j-1]

for _ in range(M):
    x1, y1, x2, y2 = map(int, input().split())
    result = dp[x2][y2] - dp[x1-1][y2] - dp[x2][y1-1] + dp[x1-1][y1-1]

    output(str(result) + '\n')