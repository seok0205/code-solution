'''
G3 16236 아기 상어

NxN 크기의 공간에 물고리 M마리와 아기 상어 1마리 존재.
공간은 1x1 크기의 정사각형 칸으로 나뉘어져 있음. 한 칸에는 최대 물고기 1마리.

아기 상어, 물고기는 모두 크기를 가짐. 이 크기는 자연수.
가장 처음 아기 상어의 크기는 2. 아기 상어는 1초에 상하좌우로 인접한 한 칸씩 이동.

아기상어는 자신의 크기보다 큰 물고기가 있는 칸은 지나갈 수 없고, 나머지 칸은 모두 지나갈 수 있음.
아기 상어는 자신의 크기보다 작은 물고기만 먹을 수 있음.
따라서, 크기가 같은 물고기는 먹을 수 없지만, 그 물고기가 있는 칸은 지나갈 수 있음.

아기 상어의 이동 결정 방법:
1. 더 이상 먹을 수 있는 물고기가 공간에 없다면 아기 상어는 엄마 상어에게 도움 요청.
2. 먹을 수 있는 물고기가 한마리면, 그 물고기를 먹으러 감.
3. 먹을 수 있는 물고기가 한마리보다 많다면, 거리가 가장 가까운 물고기를 먹으러 감.
    - 거리는 아기 상어가 있는 칸에서 물고기가 있는 칸으로 이동할 때, 지나야하는 칸의 개수의 최솟값.
    - 거리가 가까운 물고기가 많다면, 가장 위에 있는 물고기, 그러한 물고기가 여러마리라면, 가장 왼쪽에 있는 물고기를 먹음.

아기 상어의 이동은 1초 걸림. 물고기를 먹는데 걸리는 시간은 없다고 가정.
즉, 물고기 있는 칸으로 이동 시, 이동과 동시에 물고기 섭취. 섭취 후 그 칸은 빈칸이 됨.

아기 상어는 자신의 크기와 같은 수의 물고기를 먹을 때마다 크기가 1증가.
예로, 크기 2인 아기 상어는 물고기 2마리 섭취 시 크기가 3이 됨.

공간의 상태가 주어질 때, 아기 상어가 몇 초동안 엄마 상어에게 도움을 요청하지 않고 물고기 잡아먹을 수 있는지 구하는 문제.

입력:
N - 공간의 크기
N줄 동안 공간의 상태 주어짐. 0, 1, 2, 3, 4, 5, 6, 9로 이루어짐.
0 : 빈 칸
1, 2, 3, 4, 5, 6 : 칸에 있는 물고기의 크기
9 : 아기 상어의 위치(한 마리)

출력:
도움 요청하지 않고 물고기 잡아먹을 수 있는 시간 출력.
'''

import sys
from collections import deque
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

di = [-1, 0, 1, 0]
dj = [0, -1, 0, 1]


def bfs(start):      # 상어가 1회 이동하는 로직
    q = deque()
    q.append((start[0], start[1]))
    visit = [[0] * N for _ in range(N)]
    visit[start[0]][start[1]] = 1
    fish = []                       # 먹을수 있는 물고기 저장 리스트

    while q:
        x, y = q.popleft()      # 디큐
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]

            if nx < 0 or nx >= N or ny < 0 or ny >= N:      # 범위 이탈 방지
                continue

            if visit[nx][ny]:       # 방문을 이미 했을 때 다음 노드 확인
                continue
                
            if space[nx][ny] != 9 and space[nx][ny] > baby_shark:    # 아기상어가 아니고, 자신의 크기보다 크면 못감.
                continue

            visit[nx][ny] = visit[x][y] + 1     # 방문하면 이전 거리에 1 증가 시킨 값으로 대체
            q.append((nx, ny))      # 인큐

            if space[nx][ny] != 0 and space[nx][ny] != 9 and space[nx][ny] < baby_shark:       # 만약 공간의 물고기보다 아기상어가 더 크면 먹음.
                fish.append((visit[nx][ny] - 1, nx, ny))            # (거리, 위치1, 위치2) 형태로 넣기

    fish.sort(key=lambda x: (x[0], x[1], x[2]))         # 람다식 활용하여 거리, 위쪽에 있는 것과 그중 가장 왼쪽의 것을 얻어야함.
    return fish


N = int(input())
space = [list(map(int, input().split())) for _ in range(N)]
seconds = 0     # 아기 상어가 공간에서 버틴 시간
baby_shark = 2  # 상어 처음 크기 2로 시작
cnt = 0     # 상어가 먹은 물고기 수 크기 만큼 먹으면 초기화 후 상어크기 1증가

for i in range(N):
    for j in range(N):
        if space[i][j] == 9:
            start = (i, j)

while True:
    fish = bfs(start)

    if not fish:                # 먹을 물고기 없으면 누적 시간 출력.
        print(seconds)
        break

    time, x, y = fish[0]
    cnt += 1                    # 물고기 섭취

    if cnt == baby_shark:       # 상어 크기 증가 조건
        baby_shark += 1
        cnt = 0

    space[x][y] = 0             # 물고기 먹었으니 해당 자리 물고기 삭제
    start = (x, y)              # 상어출발 자리도 바꿔주기(다음 물고기 찾아야 함)
    seconds += time             # 시간 누적