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

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]


def bfs(x, y):
    global result
    
    direction = 0           # 방향 저장할 변수
    q = deque()             # 큐 생성
    q.append((x, y, 0, direction))
    INF = float('inf')      # 최단 거리 측정. 높은 값 정하기
    visit = [[[INF] * (K+1) for _ in range(N)] for _ in range(N)]       # visit로 방문 기록
    visit[x][y][0] = 1      # 첫 시작은 1
    
    while q:
        x, y, t_cnt, direction = q.popleft()    # 디큐해서 정보 저장. x: x좌표, y: y좌표, t_cnt: 나무 벤 횟수, direction: 방향 저장 변수
        
        for i in range(4):    
            if i == 3:
                a = -1      # 왼쪽으로 가는건 방향을 3번도는것보다 -1로 한번도는게 더 최단
            else:
                a = i
                
            nx = x + di[(direction+a)%4]        # 다음 좌표
            ny = y + dj[(direction+a)%4]
            
            if nx < 0 or nx >= N or ny < 0 or ny >= N:      # 범위 벗어나면 다음 탐색
                continue
            
            new = visit[x][y][t_cnt] + abs(a) + 1       # 다음 노드로 갈때의 누적 횟수
            
            if field[nx][ny] == 'Y':            # 목표만나면 최솟값 비교
                result = min(new - 1, result)
                continue
            
            elif t_cnt < K and visit[nx][ny][t_cnt+1] > new and field[nx][ny] == 'T':       # 다음 누젓 횟수가 이미 저장된 횟수보다 작은데, 나무면, 나무벤 횟수 1증가 후 값 대체
                visit[nx][ny][t_cnt+1] = new
                q.append((nx, ny, t_cnt+1, direction+a))        # 인큐
                
            elif visit[nx][ny][t_cnt] > new and field[nx][ny] == 'G':       # 누적 횟수가 이미 저장된 횟수보다 작은데, 땅이면 비교 후 대체
                visit[nx][ny][t_cnt] = new
                q.append((nx, ny, t_cnt, direction+a))          # 인큐
                

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    field = [list(input()) for _ in range(N)]
    result = float('inf')
    
    car = None              # 차 처음 위치 구하기
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':
                car = (i, j)
                break
        if car:
            break
    
    bfs(car[0], car[1])     # 최단 거리 구하기
    
    if result == float('inf'):      # 못가는 상황이어서 최솟값 갱신이 안되었다면 -1 출력
        result = -1
    
    print(f'#{tc} {result}')