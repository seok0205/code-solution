'''
모의 SW 역량 테스트 1953 탈주범 검거

탈주범은 시간당 1의 거리 움직일 수 있음
지하터널은 총 7종류의 터널 구조물로 되어있음
좌표는 (2, 1)이면 세로 기준 2번째 칸, 가로 기준 1번째 칸 의미

구조물 타입:
1 - 상하좌우 연결
2 - 상하 연결
3 - 좌우 연결
4 - 상우 연결
5 - 하우 연결
6 - 하좌 연결
7 - 상좌 연결

탈주범이 탈출 한 시간 뒤 도달할 수 있는 지점은 한 곳
1시간마다 한 칸을 갈 수 있음

지하 터널 지도, 맨홀 뚜껑 위치, 경과된 시간이 주어질 때 탈주범이 위치할 수 있는 장소 개수 계산 문제

제약 사항:
5 <= N, M(세로, 가로 크기) <= 50
0 <= R(맨홀 뚜껑 세로 위치) <= N-1, 0 <= C(가로 위치) <= M-1
1 <= L(탈출 후 소요된 시간) <= 20
터널 지도엔 반드시 1개 이상의 터널 존재
맨홀 뚜껑은 항상 터널이 있는 위치에 존재

입력:
1~7은 구조물 타입, 0은 터널이 없는 장소
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque

T = int(input())

pipe = {1: ((1, 0), (-1, 0), (0, 1), (0, -1)), 2: ((-1, 0), (1, 0)),        # 파이프 번호에 따른 이어진 방향
        3: ((0, -1), (0, 1)), 4: ((-1, 0), (0, 1)), 5: ((1, 0), (0, 1)),
        6: ((1, 0), (0, -1)), 7: ((-1, 0), (0, -1))}

for tc in range(1, T+1):
    N, M, R, C, L = map(int, input().split())
    turnel = [list(map(int, input().split())) for _ in range(N)]
    visit = [[0] * M for _ in range(N)]
    
    q = deque()
    q.append((R, C))    # 첫 맨홀 뚜껑 좌표 넣고 시작
    visit[R][C] = 1     # 맨홀 뚜껑이 첫 한 시간이 지나고 위치한 곳
    
    while q:
        target = q.popleft()
        directions = pipe[turnel[target[0]][target[1]]]     # 파이프 번호에 따른 가능한 이동 방향
        
        for dir in directions:      # 이동 경로 탐색
            x = target[0] + dir[0]
            y = target[1] + dir[1]
            if 0 <= x < N and 0 <= y < M and turnel[x][y] and visit[x][y] == 0:     # 만약 지도 안에 있고, 파이프가 있는 곳이며, 방문하지 않은 곳이라면
                if (-dir[0], -dir[1]) in pipe[turnel[x][y]]:            # 다음 좌표가 현재 위치와 연결이 되어있따면
                    q.append((x, y))                                    # 갈 수 있는 곳
                    visit[x][y] = visit[target[0]][target[1]] + 1       # 한칸이동하면 1시간 걸림
    
    result = 0
    for i in visit:     # vist에 L보다 같거나 작으면 그곳이 주어진 제한 시간동안 위치할 수 있는 곳
        for j in i:
            if j != 0 and j <= L:
                result += 1
        
    print(f'#{tc} {result}')