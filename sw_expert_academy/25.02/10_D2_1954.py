"""
D2 1954 달팽이 숫자

1부터 NxN까지 숫자가 시계방향으로 이루어져 있음
정수 N을 입력받아 N크기의 숫자열 출력

N이 3이면
[[1, 2, 3],
[4, 5, 6],
[7, 8, 9]]

입력:
T = 테스트 케이스
N = 정수
"""

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [[0 for _ in range(N)] for _ in range(N)]
    distance = [N-1]

    for i in range(N-1, 0, -1):     # 앞으로 가는 방향 리스트에 순서대로 추가
        distance.append(i)          # 달팽이 매트릭스의 규칙은 첫 시작은 N만큼 직진
        distance.append(i)          # 그 이후는 i번째마다 N-i만큼 2회 직진한다. 이를 이용

    # 우 -> 하 -> 좌 -> 상 -> 우 ...
    d = 0

    di = [0, 1, 0, -1]      # 상하좌우 방향을 순서대로 표현
    dj = [1, 0, -1, 0]

    # 직접 행, 열번호 관리
    # i = 행번호, j = 열번호
    i, j = 0, 0

    matrix[i][j] = 1    # 첫 칸은 1
    num = 2             # 두 번째 칸부터는 2부터 대입

    for a in distance:      # 리스트에 있는 방향 순서대로 N-i만큼 직진
        for _ in range(a):
            i += di[d % 4]
            j += dj[d % 4]

            matrix[i][j] = num      # 숫자 대입
            num += 1    # 다음 칸을 위해 1 증가
        d += 1

    print(f'#{tc}')
    for i in range(N):
        print(f"{' '.join(map(str, matrix[i]))}")
