'''
D3 17029 최소 비용

출발에서 최종 도착지까지 경유하는 지역의 높이 차이에 따라 연료 소비량이 달라짐
최적의 경로로 이동하면 최소한의 연료로 이동 가능

각 지역의 높이를 기록한 표가 있음. 항상 출발은 맨 왼쪽 위, 도착지는 가장 오른쪽 아래.
각 칸에서는 상하좌우칸이 나타내는 인접 지역으로만 이동 가능
(대각선 이동 불가)

인접 지역으로 이동시 기본적으로 연료 1만큼 들고, 더 높은곳으로 가는 경우 차이만큼 추가로 연료 소비
이동 가능한 지역의 높이 정보에 따라 최소 연료 소비량을 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

import heapq


def dijkstra(s):        # 다익스트라(최단경로) 알고리즘 활용
    global result
    
    hq = [(0, s[0], s[1])]
    visit = [[0] * N for _ in range(N)]
    
    di = [0, 0, 1, -1]      # 델타 활용
    dj = [1, -1, 0, 0]
    
    while hq:
        d, x, y = heapq.heappop(hq)     # 연료, 배열의 위치. 최소힙을 사용하면 가장 최단 연료값으로 갈 수 있는 위치들이 힙큐의 최상단으로 올라옴
        
        if visit[x][y]:     # 이미 방문한 곳이면 다음 데이터
            continue
        
        if x == N-1 and y == N-1:   # 만약 도달하려는 곳이면 도달하는데 써야하는 최소 연료인 d를 출력
            result = d
            return
        
        visit[x][y] = 1     # 방문 표시
        
        for k in range(4):          # 4방향 탐색
            next_x = x + di[k]
            next_y = y + dj[k]
            
            if next_x < 0 or next_x >= N or next_y < 0 or next_y >= N:      # 배열 밖이면
                continue
                
            if visit[next_x][next_y]:       # 이미 도달한 곳이면 탈출
                continue
            
            if area[next_x][next_y] - area[x][y] > 0:           # 올라가야하는 곳이면 이전 위치까지 사용한 연료값에 이번 행선지와 다음 행선지의 높이 차에 기본 연료값(1)을 더해줌
                next_d = d + (area[next_x][next_y] - area[x][y]) + 1
                heapq.heappush(hq, (next_d, next_x, next_y))        # 그리고 힙큐에 푸쉬해줌
            else:                               # 높이가 같거나 내려가야하는 곳이면 그냥 기본 1만 더해줌
                next_d = d + 1
                heapq.heappush(hq, (next_d, next_x, next_y))


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    area = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    
    dijkstra((0, 0))
    
    print(f'#{tc} {result}')