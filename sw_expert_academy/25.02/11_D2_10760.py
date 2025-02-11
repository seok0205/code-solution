'''
D2 10760 우주선 착륙 2

착륙 지점 중심으로 주변 8개 구역을 대상으로 착륙 지점보다 높이가 낮은 구역의 사진을 찍을 수 있음
비상 상황 대비 예비 후보지를 정하려 하는데, 8개의 방향 중 사진을 찍을 수 있는 방향이 4방향 이상인 지점으로 정하려 함
예비 후보지 수를 알아내는 문제
주변에 높이 정보가 없는 영역이 포함되어 있어도 알려진 영역의 높이만 조건을 만족 시 후보지 포함
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0

    di = [0, 1, 1, 1, 0, -1, -1, -1]    # 델타 사용
    dj = [1, 1, 0, -1, -1, -1, 0, 1]

    for i in range(N):
        for j in range(M):
            area_con = 0
            for k in range(8):  # 8방향 탐색
                a = i + di[k]
                b = j + dj[k]
                if 0 <= a <= N-1 and 0 <= b <= M-1:     # 좌표가 배열 안에 존재했을 때,
                    if matrix[a][b] < matrix[i][j]:     # 만약 가운데 높이보다 탐색한 높이가 낮으면
                        area_con += 1                   # 예비후보지 가능 구역 1증가
            if area_con >= 4:       # 8방향 탐색후 예비후보지 가능지가 4군데 이상이면
                result += 1         # 총 결과 1 증가
    
    print(f'#{tc} {result}')
