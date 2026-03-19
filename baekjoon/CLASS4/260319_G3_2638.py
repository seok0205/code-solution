'''
G3 2638 치즈

문제 설명:
N x M 모눈종이 위에 치즈가 표시되어 있음.
N은 세로, M은 가로 격자 수.
치즈는 4변중 2변 이상이 실내온도의 공기와 접촉하면 한시간만에 녹음.
치즈 내부에 있는 공간은 외부 공기와 접촉되지 않는 것으로 간주됨.
내부에 있는 공기는 외부 공기로 안친다는 뜻.
따라서 4방향중 2방향 이상 치즈가 없으면 녹는 것임.
입력으로 주어진 치즈가 모두 녹아 없어지는 데 걸리는 시간을 구하는 문제.

입력:
N, M (5 <= N, M <= 100)
N개의 줄동안 치즈 상태 표시.
1은 치즈, 0은 공기.
각 0과 1은 공백으로 구분지어 입력됨.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

from collections import deque

N, M = map(int, input().split())
cheeses = [list(map(int, input().split())) for _ in range(N)]

di = [0, 0, 1, -1]
dj = [1, -1, 0, 0]


def bfs(board):
    visit = [[0] * M for _ in range(N)]
    q = deque([(0, 0)])

    while q:
        x, y = q.popleft()
        visit[x][y] = 1

        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]

            if 0 <= nx < N and 0 <= ny < M and visit[nx][ny] != 1 and board[nx][ny] == 0:
                visit[nx][ny] = 1
                q.append((nx, ny))

    return visit


def func(cheeses, cnt):
    amount = sum(map(sum, cheeses))
    if amount == 0:
        output(str(cnt))
        return

    visit = [[0] * M for _ in range(N)]
    air = bfs(cheeses)

    for i in range(N):
        for j in range(M):
            if cheeses[i][j]:
                temp = 0
                for k in range(4):
                    ni = i + di[k]
                    nj = j + dj[k]

                    if air[ni][nj]:
                        temp += 1
                    
                    if temp >= 2:
                        visit[i][j] = 1
                        break
    
    for i in range(N):
        for j in range(M):
            if visit[i][j]:
                cheeses[i][j] = 0
    
    func(cheeses, cnt + 1)

func(cheeses, 0)