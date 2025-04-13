'''
D3 22683 나무 베기

출발지에서 목적지까지 최소의 조작으로 이동시킬 수 있음.
(최단 거리X, 최소 리모컨 조작 횟수O)

나무에 가로막혀 RC카를 목적지까지 이동시킬 수 없음.

NxN크기의 필드 정보, 벨 수 있는 최대 나무의 수가 주어졌을 때,
RC카를 목적지까지 이동시키기 위한 최소 조작횟수를 구하는 문제
항상 위를 바라본 상태로 RC카 조작.

맵 정보:
G : 이동 가능 땅
T : 나무
X : RC카 위치
Y : 이동시키고자 하는 위치

RC카 이동 못시키면 -1 출력

입력:
T : 테스트케이스 개수
N, K : 필드 크기, 나무 벨 수 있는 횟수
N개의 줄에 걸쳐 필드 정보 주어짐
'''

import sys
sys.stdin = open('tc.txt', 'r')

from collections import deque


def bfs(x, y):
    global result
    
    direction = 0
    q = deque()
    q.append((x, y, 0, direction))
    visit = [[[0] * (K+1) for _ in range(N)] for _ in range(N)]
    visit[x][y][0] = 1
    
    while q:
        x, y, t_cnt, direction = q.popleft()
        
        for i in range(4):    
            if i == 3:
                a = -1
            else:
                a = i
                
            nx = x + di[(direction+a)%4]
            ny = y + dj[(direction+a)%4]
            
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:
                continue
            
            if field[nx][ny] == 'Y':
                result = min(visit[x][y][t_cnt] + abs(a), result)
                continue
            
            elif t_cnt < K and visit[nx][ny][t_cnt+1] == 0 and field[nx][ny] == 'T':
                visit[nx][ny][t_cnt+1] = visit[x][y][t_cnt] + abs(a) + 1
                q.append((nx, ny, t_cnt+1, direction+a))
                
            elif visit[nx][ny][t_cnt] == 0 and field[nx][ny] == 'G':
                visit[nx][ny][t_cnt] = visit[x][y][t_cnt] + abs(a) + 1
                q.append((nx, ny, t_cnt, direction+a))


T = int(input())

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]

for tc in range(1, T+1):
    N, K = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    result = float('inf')
    
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                car_x = i
                car_y = j
                break
    
    bfs(car_x, car_y)
    
    print(f'#{tc} {result}')