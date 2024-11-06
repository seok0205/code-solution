'''
공원의 산책로가 직사각형 격자 모양이다. 주어진 방향대로 산책했을 때 도착점을 구하는 문제.
걸어다닐 수 있는 길은 'O', 장애물이 있으면 'X', 시작점은 'S'로 표시.
주어진 방향은 동서남북"EWSN"과 1부터 9사이의 거리로 이루어져 있고 routes 리스트로 주어진다.
직사각형 격자 모양 공원 밖으로 나가거나 routes에 주어진 한 방향의 이동 경로중 장애물이 있다면 명령은 무시한다.
'''

park = ["OSO","OOO","OXO","OOO"]
routes = ["E 2","S 3","W 1"]

for i in range(len(park)):  # S, 시작 위치 찾기
    for j in range(len(park[i])):
        if park[i][j] == 'S':
            S = [i, j]
            break

for i in range(len(routes)):    # 이동 명령 수행.
    direction, distance = routes[i].split() # 방향과 거리.
    x, y = S[1], S[0]   # 위치 초기화
    for n in range(int(distance)):  # 장애물 위치 확인을 해야하기 때문에 1씩 가야하는 거리만큼 진행.
        if direction == 'E' and x != len(park[0])-1 and park[y][x+1] != 'X':    # 오른쪽에 공간이 없거나 장애물이 있다면 동쪽 이동 불가능.
            x += 1  # 1칸 이동.
            if n == int(distance)-1:    # for문 반복 끝날 때 line 19 초기화 위해서 S[1] 재설정.
                S[1] = x
        elif direction == 'W' and x != 0 and park[y][x-1] != 'X':   # 왼쪽에 공간 없거나 장애물 있으면 서쪽 이동 불가.
            x -= 1
            if n == int(distance)-1:
                S[1] = x
        elif direction == 'S' and y != len(park)-1 and park[y+1][x] != 'X': # 아래 칸에 더이상 공간 없거나 장애물 있으면 남쪽 이동 불가.
            y += 1
            if n == int(distance)-1:
                S[0] = y
        elif direction == 'N' and y != 0 and park[y-1][x] != 'X':   # 위 칸에 공간 없거나 장애물 있으면 북쪽 이동 불가.
            y -= 1
            if n == int(distance)-1:
                S[0] = y

print(S)