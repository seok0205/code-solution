'''
G5 7576 토마토

토마토는 격자 모양 상자의 칸에 하나씩 넣어서 창고에 보관함.
보관 중인 토마토들 중 익은 것도 있고 안 익은 것들도 있을 수 있음.
보관 후 하루지나면 익은 토마토의 인접한 곳에 있는 익지 않은 토마토들은 익게 된다.
상하좌우방향의 토마토들이 해당됨.

대각선은 안되고, 혼자 저절로 익는 경우 없음. 며칠이 지나면 익게되는지 최소 일수 알고 싶음.
상자크기, 익은 토마토, 안익은 토마토들의 정보가 주어지면 모두 익는데에 걸리는 최소 일수를 구하는 프로그램 작성하는 문제.
상자의 일부 칸에는 토마토가 없을 수도 있음.

저장될 때부터 모든 토마토 익어있는 상태라면 0출력, 모두 익지 못하는 상황이면 -1 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque

di = [0, 0, 1, -1]                  # 델타 활용
dj = [1, -1, 0, 0]

M, N = map(int, input().split())
box = [list(map(int, input().split())) for _ in range(N)]
visit = [[0] * M for _ in range(N)]
result = 0
q = deque()                 # BFS 활용. 큐 생성

for i in range(N):
    for j in range(M):
        if box[i][j] == 1:              # 모든 박스 칸을 확인해서, 익은 토마토가 있는 좌표들을 모조리 인큐. 익은 토마토 있는 위치들에서 점점 퍼져나가다보면 결국 모두 채워짐.
            q.append((i, j))
            visit[i][j] = 1             # 중복 방문을 막기 위해 방문리스트 모두 미리 1로 설정
            
while q:                                # BFS 시작
    target = q.popleft()
    for k in range(4):                  # 4방향 확인
        x = target[0] + di[k]
        y = target[1] + dj[k]
        
        if x < 0 or x >= N or y < 0 or y >= M:      # 범위 이탈
            continue
        
        if box[x][y] == -1 or box[x][y] == 1:       # 토마토가 없거나, 이미 익은 토마토면 다음으로
            continue
        
        if visit[x][y]:             # 이미 방문한 곳이라면 다음으로
            continue
        
        visit[x][y] = visit[target[0]][target[1]] + 1       # 이전 토마토에서 이번 토마토가 익을 때까지는 하루가 걸림.
        q.append((x, y))                                    # 다음 익어야할 토마토들을 찾기 위해 이번 토마토 위치 인큐

for i in range(N):                                      # 박스가 다찼다면, 리스트의 숫자들 중 가장 큰 숫자가 토마토가 다익는데 걸린 최소 날짜임. 그 칸의 토마토가 마지막으로 익었단 소리.
    result = max(result, max(visit[i]))
    
for i in range(N):                                      # 만약 박스에 안익은 토마토가 존재하는데, 방문 리스트에는 0이라면, 익지 못할 위치에 토마토가 있었다는 뜻. 결과에서 1을 뺄것이라서 0을 설정.(모두 익지 못할 구조라면 결괏값 -1 출력해야함.)
    for j in range(M):
        if box[i][j] == 0 and visit[i][j] == 0:
            result = 0
    
print(result-1)