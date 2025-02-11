'''
D2 9489 고대 유적

N x M 사진이 주어지고 구조물이 있는 곳은 1, 빈 땅은 0으로 표시
무조건 직선이고 폭 1, 길이 2 이상
가장 긴 구조물의 길이를 구하는 문제
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    max_length = 1
    
    for i in range(N):      # 행 마다 연속된 1 최대 길이 구함
        length = 1
        for j in range(M-1):
            if matrix[i][j] and matrix[i][j+1]:     # 해당자리와 다음 인덱스 1일때 1 증가.
                length += 1
                if max_length < length:     # 현재 최대 길이, 구한 길이 비교 후 판단
                    max_length = length
            else:       # 0나오면 1로 초기화
                length = 1
    
    for j in range(M):      # 열 마다 연속된 1 최대 길이 구함
        length = 1
        for i in range(N-1):
            if matrix[i][j] and matrix[i+1][j]:     # 이하 동문
                length += 1
                if max_length < length:
                    max_length = length
            else:
                length = 1
                
    print(f'#{tc} {max_length}')