'''
D2 12712 파리 퇴치 3

NxN 배열에서 가장 합이 높은 구역을 출력하는 문제
구역의 정중앙부터 M-1만큼 '+' 혹은 'x'모형으로 모든 방향으로 뻗어나가는 형태

제약 사항:
5 <= N <= 15
2 <= M <= N
각 영역의 숫자는 30이하

입력:
N = 배열 가로세로 길이
M = 합을 구할 구역 방향당 길이 (원점 포함)
'''

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    num_sum = 0
    result = 0
    
    di = [-1, 1, 0, 0]      # 상하좌우 모양 
    dj = [0, 0, -1, 1]
    
    xi = [-1, 1, -1, 1]     # X자 모양
    xj = [-1, 1, 1, -1]
    
    for i in range(N):
        for j in range(N):
            area_plus = matrix[i][j]    # 해당 인덱스에다가 주변 값들을 더할 예정
            area_x = matrix[i][j]
            for k in range(4):      # 4방향
                for l in range(1, M):       # 범위 M 만큼
                    a = i + di[k] * l       # (a, b), (c, d)는 (x, y)형태 좌표를 의미. l은 M이 커지면 반복횟수 커지며 범위가 확장
                    b = j + dj[k] * l
                    c = i + xi[k] * l
                    d = j + xj[k] * l
                    
                    if -1 < a < N and -1 < b < N:   # 만약 a, b 좌표가 배열 안이라면
                        area_plus += matrix[a][b]   # 합에 추가
                        
                    if -1 < c < N and -1 < d < N:
                        area_x += matrix[c][d]
                
            num_sum = max(area_plus, area_x)    # +, x 중 더 큰 값 설정
            if result < num_sum:    # 최댓값 비교 후 교체
                result = num_sum
                    
    print(f'#{tc} {result}')