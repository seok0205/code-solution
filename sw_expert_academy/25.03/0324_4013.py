'''
모의 SW 역량테스트 4013 특이한 자석

특이한 자석이 있는 판 존재
판에는 4개의 자석이 있고, 각 자석은 8개의 날을 가지고 있음
자석의 각 날마다 N 혹은 S극의 자성을 가짐

1번부터 4번까지 판에 일렬로 배치되어 있고, 빨간색 화살표 위치(맨 위) 날 하나가 오도록 배치되어 있음

규칙 :
임의의 자석을 1칸씩 K번 회전시키려고 해보니, 
하나의 자석이 1칸 회전될 때, 붙어 있는 자석은 서로 붙어 있는 날의 자성과 다를 경우에만 인력에 의해 반대 방향으로 1칸 회전됨
무작위로 자석을 돌릴 때, 모든 회전이 끝난 후, 아래와 같은 방법으로 점수 계산하려 함

- 1번 자석에서 빨간색 화살표 위치에 있는 날의 자석이 N극이면 0점, S극이면 1점 획득
- 2번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 2점 획득
- 3번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 4점 획득
- 4번 자석에서 빨간색 화살표 위치에 있는 날의 자성이 N극이면 0점, S극이면 8점 획득

4개의 자석의 자성정보와 자석을 1칸 씩 K번 회전시키려할때, K번 자석을 회전시킨 후 획득하는 점수의 총 합을 출력

제약 사항 :
자석 개수 4개, 각각 8개의 날을 가짐
K는 1이상 20이하 정수
하나의 자석이 1칸 회전 시, 붙어 있는 자석은 서로 붙어있는 날의 자성이 다를 경우만 반대 방향으로 1칸 회전
1은 시계방향, -1은 반시계 방향
N극이 0으로 S극이 1로 주어짐
자성정보는 빨간색 화살표 위치 날부터 시계방향 순서
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def turn(n, d):                 # 돌리는 함수 n이 톱니 4개를 벗어나면 함수 실행 안함
    if 1 > n or n > 4:
        return
    
    if possible_lst[n-1] == 0:      # 돌리면 안되는 톱니면 함수 실행 안함
        return
    
    if d == 1:                          # 돌릴 방향에 따라 wheels 값 변경
        a = wheels[n-1].pop()
        wheels[n-1].insert(0, a)
    elif d == -1:
        a = wheels[n-1].pop(0)
        wheels[n-1].append(a)


def search(n, lst):         # 돌려야하는 톱니인지 확인하는 함수
    idx = n - 1
    lst[idx] = 1
    
    for i in range(3):
        if 0 <= idx+i+1 < 4:
            if wheels[idx+i][2] != wheels[idx+i+1][6]:      # 맞닿는 부분 다르면 돌려야한다는 표시
                lst[idx+i+1] = 1
            else:
                break
        else:
            break
    
    for j in range(3):                                      # 맞닿는 곳이 다르면 돌려야한다는 표시, 톱니부터 퍼져나가는 식으로 확인
        if 0 <= idx-j-1 < 4:
            if wheels[idx-j][6] != wheels[idx-j-1][2]:
                lst[idx-j-1] = 1
            else:
                break
        else:
            break
        
    return lst


T = int(input())

for tc in range(1, T+1):
    K = int(input())
    wheels = [list(map(int, input().split())) for _ in range(4)]
    result = 0
    
    for _ in range(K):
        wheel_num, direction = map(int, input().split())
        
        possible = [0, 0, 0, 0]                     # 돌려야할 톱니인지 표시해놓을 리스트
        possible_lst = search(wheel_num, possible)  # 톱니 확인 함수 실행
        
        turn(wheel_num, direction)          # 처음 돌릴 톱니 돌리고,
        
        for i in range(1, 4):               # 퍼져나가는 식으로 톱니 확인. 바로 옆의 톱니는 방향 다르게 해야하므로 조건 추가.
            if i%2:
                turn(wheel_num+i, -direction)
                turn(wheel_num-i, -direction)
            else:
                turn(wheel_num+i, direction)
                turn(wheel_num-i, direction)
        
    for i in range(4):                      # 점수는 1번부터 4번까지 2의 0승부터 2의 3승까지 지수 단위로 증가(1, 2, 4, 8)
        if wheels[i][0]:
            result += 2**i
        
    print(f'#{tc} {result}')