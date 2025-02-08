'''
D2 2001 파리 퇴치

NxN 배열 안의 MxM의 최대 합을 구하는 문제

제한 사항:
각 영역 숫자 30 이하

입력:
N = 배열의 가로 세로 값
M = 최대 합을 구할 가로 세로 값
'''

T = int(input())

for tc in range(1, T+1):
    N, M = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    
    for i in range(N-M+1):    # 배열 순회
        for j in range(N-M+1):
            num_sum = 0     # 구역의 합 저장
            for k in range(M):      # M개의 행마다 주어진 M만큼의 가로줄 합 누적
                num_sum += sum(matrix[i+k][j:j+M])
            if result < num_sum:    # 최댓값이면 result 교체
                result = num_sum
    
    print(f'#{tc} {result}')