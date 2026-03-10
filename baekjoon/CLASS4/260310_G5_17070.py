'''
G5 17070 파이프 옮기기 1

문제 설명:
집 크기는 NxN 격자판. 1x1 크기의 정사각형 칸으로 나뉨.
각 칸은 (r, c)로 표현. r은 행의 번호, c는 열의 번호. 1부터 시작함.
각각의 칸은 빈 칸이거나 벽이다.
파이프는 2x1크기의 격자에 들어가는 크기. 회전시킬 수 있고, 3가지 방향이 가능함.
각각 -,/,1자 형태이다.
파이프는 항상 빈칸만 차지해야하고, 가로 파이프는 가로 파이프와 대각선 파이프와 연결 가능함.
세로파이프는 세로파이프와 대각선, 대각선은 3가지 모두 연결 가능. 대각선은 2x2 모두 빈칸이여야 설치 가능.
파이프의 한쪽 끝을 (N, N)으로 이동시키는 방법 개수를 구하는 문제.

입력:
첫째 줄 집 크기 N (3 <= N <= 16)
둘째 줄부터 N개의 줄에는 집의 상태 주어짐. 빈칸은 0, 벽은 1
(1,1), (1,2)는 항상 빈칸.

이동못한다면 0 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
home = [list(map(int, input().split())) for _ in range(N)]
visit = [[[0] * N for _ in range(N)] for _ in range(3)]
visit[0][0][0] = 1
visit[0][0][1] = 1

for i in range(N):
    for j in range(1, N):
        if home[i][j] == 1:
            continue

        if j + 1 < N and home[i][j+1] == 0:
            visit[0][i][j+1] += visit[0][i][j] + visit[2][i][j]

        if i + 1 < N and home[i+1][j] == 0:
            visit[1][i+1][j] += visit[1][i][j] + visit[2][i][j]

        if i + 1 < N and j + 1 < N:
            if home[i+1][j+1] == 0 and home[i+1][j] == 0 and home[i][j+1] == 0:
                visit[2][i+1][j+1] += visit[0][i][j] + visit[1][i][j] + visit[2][i][j]
        
answer = visit[0][N-1][N-1] + visit[1][N-1][N-1] + visit[2][N-1][N-1]
output(str(answer))