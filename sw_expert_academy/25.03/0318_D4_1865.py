'''
D4 1865 동철이의 일 분배

N명의 직원이 있음
해야할 일 N개가 생김
직원들에게 하나씩 배분하려 함

직원들 번호가 1부터 N까지 매겨져 있고, 해야할 일에도 번호가 1부터 N까지 매겨져 있을 때, i번 직원이 j번 일을 하면
성공할 확률이 P(i,j)임

직원들에게 해야 할 일 하나씩 배분하는 방법은 여러 가지
여러 방법 중 주어진 일이 모두 성공할 확률의 최댓값을 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def work(row, p):
    global result
    
    if p < result:          # 구한 최댓값보다 p가 작아지기 시작하면 중단. 확률 곱이라 한번 작아지면 1이상 수를 곱하지 않으면 커질 가망이 없음
        return
    
    if row == N:            # 길이가 끝까지가면 확률 비교 후 최댓값 결정
        if p > result:
            result = p
        return
    
    for col in range(N):
        if distribute[col]:     # 사용한 열 인덱스라면 다음 열 인덱스로 넘어감
            continue
        
        if percent[row][col] == 0:      # 해당 직원의 일 확률이 0 이면 그냥 넘어감
            continue
        
        distribute[col] = 1             # 부분 곱을 위함
        memory = p                      # 이전 확률 기억함
        p *= (percent[row][col]/100)        # 확률로 만들어서 곱해줌
        work(row+1, p)
        distribute[col] = 0
        p = memory                      # 기억했떤 확률 되돌리기


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    percent = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0
    distribute = [0] * N
    work(0, 1)
    
    print(f'#{tc}', '{:6f}'.format(result*100))