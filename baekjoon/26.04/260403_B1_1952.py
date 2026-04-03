'''
B1 1952 달팽이2

문제 설명:
M줄 N칸으로 되어 있는 표 위에, 달팽이 모양으로 선을 그리려고 함.
표 왼쪽 위칸에서 시작, 오른쪽으로 선을 그려 나감.
표의 바깥 또는 이미 그려진 칸에 닿아서 이동못하면 시계방향으로 꺾음.
선이 꺾인 부분 개수를 구하는 문제.

입력:
M, N (2 <= M, N <= 100)

출력:
모든 칸이 채워질 때, 선이 꺾인 횟수 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
board = [[0] * M for _ in range(N)]
di = [0, 1, 0, -1]
dj = [1, 0, -1, 0]
board[0][0] = 1
result = 0
x = 0
y = 0

while True:
    nx = x + di[result%4]
    ny = y + dj[result%4]

    if 0 <= nx < N and 0 <= ny < M and board[nx][ny] == 0:
        board[nx][ny] = 1
        x, y = nx, ny
        temp = 0
        for k in range(4):
            check_x = x + di[k]
            check_y = y + dj[k]
            if 0 > check_x or check_x >= N or 0 > check_y or check_y >= M or board[check_x][check_y] == 1:
                temp += 1
        if temp == 4:
            break
    else:
        result += 1

print(result)