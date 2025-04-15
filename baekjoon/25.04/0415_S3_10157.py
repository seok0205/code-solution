'''
S3 10157 자리배정

가로에 C개, 세로로 R개의 좌석이 격자형으로 배치. 좌석 번호는 (x, y)표시

맨왼쪽 아래 좌석이 (1,1). 줄을 선 사람들에게 번호표 부여.
(1, 1) 좌석부터 시작해 시계방향으로 돌아가며 순서대로 배정.

대기 순서가 K인 관객에게 배정될 좌석번호(x, y)를 찾는 문제.

입력:
C, R : 격자 크기(가로, 세로)
K : 관객 대기번호

출력:
K번 관객에게 부여될 좌석 번호 x, y를 공백 하나 두고 출력.
만약 좌석 배정 불가 시 0 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

C, R = map(int, input().split())
K = int(input())

di = [-1, 0, 1, 0]      # 델타 활용
dj = [0, 1, 0, -1]
direction = 0           # 방향 설정(상우하좌 방향은 항상 고정)
visit = [[0] * C for _ in range(R)]     # 자리 배정할 배열
x = R-1     # 첫 좌표
y = 0
num = 1     # 대기 번호

if K > C * R:       # 번호가 좌석 갯수를 초과한다면 0 출력
    print(0)
else:
    while True:
        if num == K:        # 목표 좌석 번호면 해당 좌표 출력
            print(y + 1, R - x)
            break
        
        visit[x][y] = num       # 좌석 배정
        
        nx = x + di[direction%4]        # 다음 좌표 확인
        ny = y + dj[direction%4]
        
        if nx < 0 or nx >= R or ny < 0 or ny >= C or visit[nx][ny]:
            direction += 1      # 좌석 끝에 도달하거나, 이미 좌석 배정 받은 자리에 도달하면, 다음 방향 돌리기
            
        x += di[direction%4]        # 본 좌표를 다음 좌표로 설정
        y += dj[direction%4]
        
        num += 1        # 번호 1 증가