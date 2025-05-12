'''
G4 16234 인구 이동

NxN 크기 땅이 존재. 각각의 땅에는 나라가 하나씩 존재. r행 c열에 있는 나라엔 A[r][c]명이 살고 있음.
인접한 나라 사이에는 국경선이 존재함. 모든나라는 1x1 크기라서 모든 국경선은 정사각형 형태.

인구 이동은 하루 동안 다음과 같이 진행. 이동이 없을 때까지 지속됨.

1. 국경선을 공유하는 두 나라의 인구 차이가 L명 이상, R명 이하라면, 두 나라가 공유하는 국경선을 오늘 하루 동안 연다.
2. 위의 조건에 의해 열어야하는 국경선이 모두 열렸다면, 인구 이동 시작.
3. 국경선이 열려 있어 인접한 칸만을 이용해 이동할 수 있으면, 그 나라를 오늘 하루 동안은 연합이라 함.
4. 연합을 이루고 있는 각 칸의 인구수는 (연합의 인구수) / (연합을 이루고 있는 칸의 개수)가 된다. 소수점 버림.
5. 연합을 해체 후, 모든 국경선을 닫음.

각 나라 인구수가 주어질 때, 인구 이동이 며칠 동안 발생하는지 구하는 문제.

입력:
N, L, R : N은 1이상 50이하, L, R은 1이상 100이하
N개의 줄에 각 나라 인구수. r행 c열에 주어지는 정수는 A[r][c]의 값.
인구 이동이 발생하는 일수가 2,000번 보다 작거나 같은 입력만 주어짐.
'''

import sys
sys.stdin = open('tc.txt', 'r')
from collections import deque

dir_dic = {0: (0, 1), 1: (1, 0), 2: (0, -1), 3: (-1, 0)}


def check(x, y):
    q = deque([(x, y)])
    visit[x][y] = 1
    population = worlds[x][y]

    while q:
        x, y = q.popleft()

        for k in range(4):
            nx = x + dir_dic[k][0]
            ny = y + dir_dic[k][1]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue

            if visit[nx][ny]:
                continue

            differ = abs(worlds[x][y] - worlds[nx][ny])
            if differ < L and differ > R:
                continue

            visit[nx][ny] = 1
            population += worlds[nx][ny]
            q.append((nx, ny))
    
    return population


N, L, R = map(int, input().split())

worlds = [list(map(int, input().split())) for _ in range(N)]
result = 0

while True:
    visit = [[0] * N for _ in range(N)]
    sub = 0

    for i in range(N):
        for j in range(N):
            if visit[i][j] != 1:
                population = check(i, j)
                sub += 1

    if sub == 0:
        break

print(population)