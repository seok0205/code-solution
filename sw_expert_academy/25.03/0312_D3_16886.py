'''
D3 16886 전자카트

사무실에서 출발해 각 구역을 한 번씩만 방문하고 사무실로 돌아올 때 최소 배터리 사용량 출력

각 구역 이동 시 배터리 사용량은 표로 제공, 1번은 사무실, 2번부터 N번은 관리구역 번호
두 구역 사이도 갈 때와 올때의 경사가 통행로가 다를 수 있어서 배터리 소비량 다를 수 있음
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def cleaning_route(idx, battery):
    global min_battery
    
    if False not in used:           # 열에 더이상 False가 없다면(모든 열과 행에 겹치지않게 경로를 구했다는 뜻)
        if min_battery > battery:   # 최소 배터리와 이번 경로 배터리를 비교한 후 적은 것을 대입
            min_battery = battery
    elif min_battery < battery:     # 이미 최소 배터리보다 현재 배터리가 클 때는 최솟값 불가.
        return
    
    for i in range(N):              # 재귀는 행으로, 열은 for문으로
        if used[i] or i == idx:     # 만약 행,열의 인덱스값이 같고(1,1 혹은 2,2) 이미 해당 값에 선택한 열이 있는 경우
            continue
        if i == 0 and False in used[1:]:        # 첫번째 행이고 그 뒤가 모두 False일때, (0,0)로 인한 오류 방지
            continue
        
        used[i] = True      # 해당 열은 사용했다는 의미
        cleaning_route(i, battery + section[idx][i])        # 다음 행으로 넘어가서 탐색
        used[i] = False     # 다음 행들 탐색 끝났다면 다시 False로 바꾸고 다음 열 내 인덱스로 넘어가서 위 과정 반복
        

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    section = [list(map(int, input().split())) for _ in range(N)]
    
    min_battery = float("inf")      # 최솟값
    used = [False] * N
    
    cleaning_route(0, 0)
    
    print(f'#{tc} {min_battery}')