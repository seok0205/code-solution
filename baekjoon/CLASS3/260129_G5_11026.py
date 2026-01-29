'''
G5 11026 적록색약

문제 설명:
NxN 그리드의 각 칸안에 R, G, B 중 하나를 색칠한 그림이 있음.
몇 개의 구역으로 나뉘는데, 구역은 같은 색으로 이루어져 있음.
같은 색상이 상하좌우로 인접해 있는 경우에 두 글자는 같은 구역에 속함(색상 차이 못느껴도 같은 색상이라 함)

예를 들어,
RRRBB
GGBBB
BBBRR
BBRRR
RRRRR
같은 경우, 적록색약이 아닌 사람이 보면 구역의 수는 총 4개. 하지만, 적록색약인 사람은 3가지만 볼 수 있음.(빨-초 2, 파 1)

그림이 입력으로 주어질 때, 적록색약인 사람이 봤을 때, 아닌 사람이 봤을 때 구역의 수를 구하는 프로그램 작성

입력:
첫 줄 - N (1~100)
둘째 줄부터 N개의 줄 - 그림 상태

출력:
적록색약아닌 사람, 적록색약인 사람이 봤을 때의 구역 수를 공백으로 구분해 출력.
'''

import sys
from collections import deque
sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input().strip())
picture = []

for _ in range(N):
    area_row = input().strip()
    picture.append(area_row)

xi = [0, 0, 1, -1]
xj = [1, -1, 0, 0]


def jeoknok():
    q = deque()
    visit = [[0 for _ in range(N)] for _ in range(N)]
    area = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                if picture[i][j] == 'B':
                    color = 'B'
                else:
                    color = 'RG'
                area += 1
                q.append((i, j))
                visit[i][j] = area

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + xi[k]
                        ny = y + xj[k]

                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue

                        if visit[nx][ny]:
                            continue

                        if picture[nx][ny] not in color:
                            continue

                        visit[nx][ny] = visit[x][y]
                        q.append((nx, ny))
    output(str(area))
    return


def not_jeoknok():
    q = deque()
    visit = [[0 for _ in range(N)] for _ in range(N)]
    area = 0
    for i in range(N):
        for j in range(N):
            if not visit[i][j]:
                area += 1
                q.append((i, j))
                visit[i][j] = area

                while q:
                    x, y = q.popleft()

                    for k in range(4):
                        nx = x + xi[k]
                        ny = y + xj[k]

                        if nx < 0 or nx >= N or ny < 0 or ny >= N:
                            continue

                        if visit[nx][ny]:
                            continue

                        if picture[x][y] != picture[nx][ny]:
                            continue

                        visit[nx][ny] = visit[x][y]
                        q.append((nx, ny))
    output(str(area) + ' ')
    return

not_jeoknok()
jeoknok()