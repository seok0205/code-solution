'''
D4 1861 정사각형 방

N**2개 방이 NxN 배열 형태로 늘어서 있음
위에서 i번째 줄의 왼쪽에서 j번째 방에는 1이상 N**2 이하의 수 A가 적혀 있으며,
이 숫자는 모든 방에 대해 서로 다름
니가 어떤 방에 있다면, 상하좌우에 있는 다른 방으로 이동 가능
물론 이동하려는 방이 존재해야 하고, 이동하려는 방에 적힌 숫자가 현재 방에 적힌 숫자보다 정확히 1 더 커야함
처음 어떤 수가 적힌 방에서 있어야 가장 많은 개수의 방을 이동할 수 있는지 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

# from collections import deque

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    rooms = [list(map(int, input().split())) for _ in range(N)]
    
    visited = [0] * (N * N + 1)         # 방번호는 1부터 차례대로 N*N번 까지 있음
    
    di = [0, 0, 1, -1]
    dj = [1, -1, 0, 0]
    
    for i in range(N):                  # 모든 방위치에서 시작해봄
        for j in range(N):
            for k in range(4):          # 델타로 4방향 방을 확인
                x = i + di[k]
                y = j + dj[k]
                if 0 <= x < N and 0 <= y < N and rooms[x][y] == rooms[i][j] + 1:        # 현재 방보다 1 크면 그방의 인덱스에 해당되는 visited 값을 1로 변경
                    visited[rooms[i][j]] = 1
                    break
    
    room_num = 0            # 방번호
    can_move = 0            # 센 횟수
    can_move_max = 0        # 최대 횟수
    
    for i in range(1, N * N + 1):       # visited를 보면서
        if visited[i] == 1:             # 만약 방문한 방이라면
            can_move += 1               # 이동 횟수 1증가
        else:
            if can_move_max < can_move:     # 이동 횟수와 최대 횟수 비교
                can_move_max = can_move     # 현재 횟수가 더 크다면
                room_num = i - can_move     # 방번호도 같이 바꿈(방번호는 횟수 빼면 방 번호)
            can_move = 0                    # 방 연속 방문 끊기므로 0 초기화
    
    # room_num = 0        # 방 시작 번호
    # can_move_max = 0    # 최대 이동 횟수
    # di = [0, 0, 1, -1]      # 델타
    # dj = [1, -1, 0, 0]
    
    # q = deque()         # 큐 활용
    
    # for i in range(N):      # 모든 좌표 탐색
    #     for j in range(N):
    #         visit = [[0] * N for _ in range(N)]
    #         max_num = 0     # 해당 좌표에서의 횟수 기록
    #         q.append((i, j))    # 시작 좌표 인큐
    #         visit[i][j] = 1     # 첫 좌표는 첫 번째 들어간 방
            
    #         while q:
    #             target = q.popleft()    # 디큐
                
    #             for k in range(4):
    #                 x = target[0] + di[k]
    #                 y = target[1] + dj[k]
    #                 if 0 <= x < N and 0 <= y < N and rooms[x][y] == rooms[target[0]][target[1]] + 1:        # 방번호가 이전 방의 +1이어야 함
    #                     q.append((x, y))        # 다음 방 인큐
    #                     visit[x][y] = visit[target[0]][target[1]] + 1       # 횟수 1증가
    #                     max_num = visit[x][y]  # 횟수 저장
            
    #         if can_move_max == max_num:     # 한번 탐색 끝나면 최대횟수와 방 번호 대체 해줌
    #             if room_num > rooms[i][j]:
    #                 room_num = rooms[i][j]            
    #         elif can_move_max < max_num:
    #             room_num = rooms[i][j]
    #             can_move_max = max_num
    
    print(f'#{tc} {room_num} {can_move_max}')