'''
D2 22654 차윤이의 RC카

RC카를 필드위에서 조종하려고 함

맵 정보:
G : RC카가 이동 가능한 땅
T : RC카가 이동이 불가능한 나무
X : 현재 RC카의 위치
Y : RC카를 이동시키고자 하는 위치

RC카의 조종 동작:
A : 앞으로 이동 - 나무가 있거나 필드 벗어나는 경우 아무일도 일어나지 않음
L : 현재 바라본 방향에서 왼쪽으로 90도 회전
R : 현재 바라본 방향에서 오른쪽으로 90도 회전

항상 RC카를 위를 바라보는 방향으로부터 조종 시작
커맨드 주어질 때, 목적지에 도달할 수 있는지 구하는 문제.
커맨드 종료시, 목적지에 위치해 있어야 함.

입력:
T : 테스트 케이스 개수
N : 필드 크기
N줄에 걸쳐 필드의 정보 주어짐.
Q : 조종할 횟수
Q줄 동안 커맨드 길이 C와 커맨드가 공백으로 주어짐

출력:
커맨드마다 목적지에 도달할 수 있으면 1, 아니면 0을 공백으로 구분하여 출력.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

di = [-1, 0, 1, 0]  # rc 카는 처음에 위를 바라보고 시작. R, L등장시마다 인덱스에 +, - 1씩 해주면 알맞은 방향을 찾음
dj = [0, 1, 0, -1]

for tc in range(1, T+1):
    N = int(input())
    field = [list(input()) for _ in range(N)]
    Q = int(input())
    result = []
    
    for i in range(N):
        for j in range(N):
            if field[i][j] == 'X':      # 첫 RC카의 위치 찾기
                car_x = i
                car_y = j
                break
    
    for a in range(Q):      # 주어지는 명령 세트
        C, command = map(str, input().split())
        direction = 0       # 처음은 위를 바라보고 시작
        x, y = car_x, car_y

        for i in range(int(C)):
            if command[i] == 'R':   # 오른쪽 회전
                direction += 1
            elif command[i] == 'L':     # 왼쪽 회전
                direction -= 1
            else:                   # A 등장시 앞으로 전진.
                nx = x + di[direction%4]
                ny = y + dj[direction%4]
                
                # 단, 앞에 나무가 있거나, 맵밖으로 가라는 명령이면 다음 명령 수행하러 감
                if field[nx][ny] == 'T' or nx < 0 or nx >= N or ny < 0 or ny >= N:
                    continue
                
                x = nx      # 위 조건에 안걸리면 다음 칸으로 전진한 위치 반환
                y = ny
                
        if field[x][y] == 'Y':      # 마지막 위치가 Y라면 결과 리스트에 1추가, 아니면 0추가
            result.append('1')
        else:
            result.append('0')
    
    print(f'#{tc} {" ".join(result)}')      # 결과 출력