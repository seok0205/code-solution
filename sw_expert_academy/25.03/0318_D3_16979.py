'''
D3 16979 최소 생산 비용

A사는 여러 곳에 공장을 보유. N종의 제품을 N곳의 공장에서 한 곳당 한가지씩 생산하려 함
각 제품의 공장별 생산비용이 주어질 때 전체 제품의 최소 생산 비용을 계산하는 프로그램 만드는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def product(row, sub):
    global result
    
    if sub > result:        # 합이 이미 구한 최솟값을 넘어가면 종료(더이상 탐색 필요 없음)
        return
    
    if row == N:            # 끝 행까지 탐색을 끝내면 최솟값과 sub를 비교하여 더 적은값을 result에 대입
        if result > sub:
            result = sub
        return
    
    for col in range(N):    # 만약 col이 이미 1, 합에 사용한 열위치라면 넘어감
        if visit[col]:
            continue
        
        visit[col] = 1      # 해당 열을 사용했다는 방문 기록지에 표시
        sub += cost[row][col]       # 합에 더함
        product(row+1, sub)         # 다음 합할 열의 원소 찾으러 감
        visit[col] = 0              # 합하지 않은 경우의 수를 위해 0으로 바꾸어줌
        sub -= cost[row][col]       # 합에서도 빼줌


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cost = [list(map(int, input().split())) for _ in range(N)]
    
    result = float("inf")
    visit = [0] * N
    
    product(0, 0)
    
    print(f'#{tc} {result}')