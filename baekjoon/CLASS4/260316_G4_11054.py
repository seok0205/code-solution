'''
G4 11054 가장 긴 바이토닉 부분 수열

문제 설명:
수열 S가 어떤 수 Sk를 기준으로 S1 < S2 < ... Sk-1 < Sk > Sk+1 > ... SN-1 > SN을 만족한다면, 그 수열을 바이토닉 수열이라고 한다.

예를 들어, {10, 20, 30, 25, 20}과 {10, 20, 30, 40}, {50, 40, 25, 10} 은 바이토닉 수열이지만, {1, 2, 3, 2, 1, 2, 3, 2, 1}과 {10, 20, 30, 40, 20, 30} 은 바이토닉 수열이 아니다.

수열 A가 주어졌을 때, 그 수열의 부분 수열 중 바이토닉 수열이면서 가장 긴 수열의 길이를 구하는 프로그램을 작성하시오.

입력:
첫째 줄 - N (수열 A의 크기, 1 <= N <= 1000)
둘째 줄 - 수열 A를 이루고 있는 Aj (1 <= Aj <= 1000)

출력:
수열 A의 부분 수열 중 가장 긴 바이토닉 수열 길이 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
A = list(map(int, input().split()))

dp_up = [1] * N
dp_down = [1] * N

for i in range(N):
    for j in range(i):
        if A[i] > A[j]:
            dp_up[i] = max(dp_up[i], dp_up[j] + 1)

for i in range(N-1, -1, -1):
    for j in range(N-1, i, -1):
        if A[i] > A[j]:
            dp_down[i] = max(dp_down[i], dp_down[j] + 1)

result = 0
for i in range(N):
    if result < dp_down[i] + dp_up[i] - 1:
        result = dp_down[i] + dp_up[i] - 1

output(str(result))