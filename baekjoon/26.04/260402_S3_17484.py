'''
S3 17484 진우의 달 여행 (Small)

문제 설명:
지구와 우주 사이는 NxM 행렬로 나타냄.
각 원소의 값은 우주선이 그 공간을 지날 때 소모되는 연료 양.

우주선의 특징
1. 지구 -> 달로 가는 경우 우주선이 움직일 수 있는 방향은 대각선 양쪽 아래, 아래 방향이다.
2. 우주선은 전에 움직인 방향으로 움직일 수 없다. 즉, 같은 방향으로 두 번연속 못 감.

연료를 최대한 아끼며 지구의 어느위치에서든 출발해 달의 어느 위치든 착륙하는 것.
필요한 연료의 최솟값을 계산.

입력:
첫 줄에 지구와 달 사이 공간을 나타내는 행렬의 크기 N, M주어짐 (2 <= N, M <= 6)
다음 N줄 동안 각 행렬의 원소 값이 주어짐. 각 행렬의 원소값은 100이하의 자연수.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
space = [list(map(int, input().split())) for _ in range(N)]
visit = [[[float('inf') for _ in range(3)] for _ in range(M)] for _ in range(N)]

for i in range(M):
    for j in range(3):
        visit[0][i][j] = space[0][i]

for i in range(1, N):
    for j in range(M):
        if j > 0:
            visit[i][j][0] = space[i][j] + min(visit[i-1][j-1][1], visit[i-1][j-1][2])
        visit[i][j][1] = space[i][j] + min(visit[i-1][j][0], visit[i-1][j][2])
        if j < M - 1:
            visit[i][j][2] = space[i][j] + min(visit[i-1][j+1][0], visit[i-1][j+1][1])

result = float('inf')
for i in range(M):
    for j in range(3):
        result = min(result, visit[N-1][i][j])

print(result)