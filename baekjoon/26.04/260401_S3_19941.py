'''
S3 19941 햄버거 분배

문제 설명:
기다란 벤치 모양 식탁에 사람들과 햄버거가 단위 간격으로 놓여 있음.
사람들은 자신의 위치에서 거리가 K인 햄버거 먹을 수 있음.

ex)
버거/사람/버거/사람/버거/사람/버거/버거/사람/사람/버거/사람

위 상태에서 K가 1이라면 모든 사람은 자신과 인접한 햄버거만 먹을 수 있음.
식탁 길이 N, 햄버거 선택할 수 있는 거리 K, 사람 햄버거 위치가 주어질 때, 햄버거를 먹을 수 있는 사람의 최댓값을 구하는 문제.

입력:
첫 줄 - N, K (1 <= N <= 20000, 1 <= K <= 10)
둘째 줄 - P(사람), H(버거)로 이루어진 길이 N의 문자열
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
table = list(input().strip())
burger = [True] * N
result = 0

for i in range(N):
    if table[i] == 'P':
        burger[i] = False

for i in range(N):
    if table[i] == 'P':
        s = i - K if i - K >= 0 else 0
        e = i + K + 1 if i + K + 1 < N else N
        for j in range(s, e):
            if table[j] == 'P':
                continue

            if table[j] == 'H' and burger[j]:
                result += 1
                burger[j] = False
                break

print(result)