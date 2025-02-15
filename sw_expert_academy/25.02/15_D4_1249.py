'''
D4 1249 보급로

출발지(S)에서 도착지(G)까지 가기 위한 도로 복구 작업을 빠른 시간 내에 수행하려 함
도로가 파여진 깊이에 비례해 복구 시간 증가
출발지에서 도착지까지 가는 경로 중 복구 시간이 가장 짧은 경로에 대한 총 복구 시간을 구하는 문제
깊이가 1이면 복구에 드는 시간은 1이라 가정
이동 경로는 상하좌우 방향, 1칸씩 이동 가능
지도 정보엔 각 칸마다 파여진 도로의 깊이 주어짐
도로 복구 후에만 다른 곳 이동 가능

접근:
도로로 가는 합이 가장 작을때를 찾는 것이 핵심
BFS 활용하여 최소값을 찾을 것
'''

from collections import deque


def bfs(s, v):      # 너비 우선 탐색
    queue = deque()             # 큐 생성
    queue.append([s, v])        # 첫 좌표 엔큐
    bfs_matrix[s][v] = 0        # 탐색 결과 그래프의 첫 좌표 0
    
    di = [0, 1, -1, 0]
    dj = [1, 0, 0, -1]
    
    while queue:        # 큐에 탐색할 노드가 존재할 때
        x, y = queue.popleft()      # 엔큐한 첫 좌표 반환
        for i in range(4):      # 4방향 모두 비교
            mx = x + di[i]
            my = y + dj[i]
            if 0 <= mx < N and 0 <= my < N:     # 배열 내에 있을 때만
                if bfs_matrix[mx][my] > matrix[mx][my] + bfs_matrix[x][y]:      # 해당 방향의 다음 노드에 해당되는 탐색 결과 그래프 내 값이 현재 탐색 결과 그래프 내 값과 주어진 배열에서 다음 노드에 해당하는 값의 합보다 크면
                    bfs_matrix[mx][my] = matrix[mx][my] + bfs_matrix[x][y]      # 최소 시간 값이 바뀌는 것
                    queue.append([mx, my])      # 그 방향의 다음 방향들도 탐색해야 하니 비교 끝나면 다음 노드를 큐에 추가


C = int(input())

for tc in range(1, C+1):
    N = int(input())
    matrix = [list(map(int, list(input()))) for _ in range(N)]
    
    INF = float("inf")      # 첫 합이 무조건 작아야 탐색 결과 그래프에 들어가야하므로 디폴트값이 어느 값보다 커야 함
    bfs_matrix = [[INF for _ in range(N)] for _ in range(N)]
    
    bfs(0, 0)       # 시작점을 bfs함수에 대입
    
    print(f'#{tc} {bfs_matrix[-1][-1]}')        # G는 무조건 오른쪽 구석이므로 탐색 결과 그래프의 오른쪽 구석 출력 시 최소 시간 얻을 수 있음
