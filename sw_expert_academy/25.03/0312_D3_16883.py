'''
D3 16883 최소 합

NxN 숫자가 적힌 판이 주어짐. 오른쪽이나 아래로만 이동 가능

맨 왼쪽 위에서 오른쪽 아래 까지 이동할 때, 지나진 칸에 써진 숫자의 합계가 최소가 되도록
움직였다면 이때의 합계가 얼마인지 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def go(s1, s2, num_sum):
    '''
    s1, s2 : 시작점 좌표
    num_sum : 이때까지 지나온 해당 좌표의 값들을 합친 값
    '''
    global min_sum
    
    num_sum += matrix[s1][s2]       # 함수 한번 실행 시마다 해당 인자로 받아온 좌표의 값을 num_sum에 합침
    
    if s1 == N-1 and s2 == N-1:     # 마지막 좌표일 경우 min_sum과 현재까지 더한 num_sum의 값을 비교 후 적은 값 대입
        if min_sum > num_sum:
            min_sum = num_sum
        return
    
    if 0 <= s1+1 < N and 0 <= s2 < N:       # 배열 범위 안이면 다음 칸으로 감
        go(s1+1, s2, num_sum)               # 재귀 호출
        
    if 0 <= s1 < N and 0 <= s2+1 < N:       # 배열 범위 안이면 다음 칸 이동
        go(s1, s2+1, num_sum)               # 재귀 호출

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    min_sum = float("inf")      # 최솟값
    
    go(0, 0, 0)     # 함수 실행
    
    print(f'#{tc} {min_sum}')