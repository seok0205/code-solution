'''
S1 14940 쉬운 최단거리

지도가 주어질때 모든 지점에 대해서 목표지점까지의 거리를 구하는 문제
오직 가로와 세로로만 움직일 수 있음

입력:
n, m - 세로, 가로 크기
n개의 줄에 m개의 숫자 주어짐. 0은 갈 수 없는 땅, 1은 갈 수 있는 땅, 2는 목표지점, 2는 단 하나.

출력:
각 지점에서 목표지점까지의 거리를 출력. 원래 갈 수 없는 땅인 위치는 0 출력.
원래 갈 수 있는 땅인 부분 중에서 도달할 수 없는 위치는 -1 출력.
'''

import sys
from collections import deque
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

di = [0, 0, 1, -1]      # 4방향으로 이동 가능
dj = [1, -1, 0, 0]


def bfs(start):         # 너비 탐색(bfs)으로 특정 위치에서 각 위치 까지 거리 알아보기
    q = deque()
    visit = [[0] * m for _ in range(n)]
    visit[start[0]][start[1]] = 1
    q.append((start[0], start[1]))
    
    while q:
        x, y = q.popleft()      # 디큐
        
        for k in range(4):
            nx = x + di[k]
            ny = y + dj[k]

            if nx < 0 or nx >= n or ny < 0 or ny >= m:      # 범위 이탈 방지
                continue

            if visit[nx][ny] or fields[nx][ny] == 0:        # 방문 했거나, 못가는 위치면 다음 노드 탐색
                continue

            visit[nx][ny] = visit[x][y] + 1             # 이전 노드에서 다음 노드 이동하면 거리 1 증가
            q.append((nx, ny))      # 인큐

    for i in range(n):                      # visit에는 목표지점이 1로 되어있어서, 모든 노드들에서 1 빼야 값이 맞춰짐.
        for j in range(m):
            if fields[i][j] and visit[i][j] == 0:       # 단 방문할 수 있는데 방문 못한 곳은 -1로 변경
                visit[i][j] = -1
            elif visit[i][j] != 0:                      # 아니면 방문한 곳들이기에 1 줄여줌.
                visit[i][j] -= 1

    return visit        # 값을 담은 배열 반환


n, m = map(int, input().split())
fields = [list(map(int, input().split())) for _ in range(n)]

for i in range(n):
    for j in range(m):
        if fields[i][j] == 2:       # 목표점 찾기(2)
            s = (i, j)

results = bfs(s)        # 너비우선탐색 배열 반환받기

for result in results:
    print(' '.join(map(str, result)))       # 출력