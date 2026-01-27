'''
S1 2178 미로 탐색

문제 설명:
NxM 배열의 미로가 있음.
미로에서 1은 이동 가능, 0은 이동 못하는 칸.
(1,1)에서 출발해서 (N, M)으로 이동할 때 지나야 하는 최소 칸 개수를 구하는 프로그램 작성
인접한 칸만으로만 이동 가능.
칸 셀 때 시작, 도착 위치 포함.

입력:
첫 줄 - N(2~), M(~100)
N개의 줄마다 M개씩의 정수로 미로 주어짐. 붙어서 입력으로 주어짐

출력:
최소 칸 수 출력. 항상 도착 위치로 이동 가능한 경우만 입력 주어짐
'''

import sys
from collections import deque
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().strip().split())
maze = [list(map(int, input().strip())) for _ in range(N)]

xi = [0, 0, 1, -1]
xj = [1, -1, 0, 0]

q = deque([(0, 0)])
visit = [[0] * M for _ in range(N)]
visit[0][0] = 1

while q:
    x, y = q.popleft()

    for k in range(4):
        nx = x + xi[k]
        ny = y + xj[k]

        if nx < 0 or nx >= N or ny < 0 or ny >= M:
            continue

        if visit[nx][ny] or maze[nx][ny] == 0:
            continue
        
        q.append((nx, ny))
        visit[nx][ny] = visit[x][y] + 1

output(str(visit[N-1][M-1]))