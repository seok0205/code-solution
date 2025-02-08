import sys
sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = list(map(int, input().split()))
    matrix = [list(map(int, input().split())) for _ in range(N)]
    result = 0
    
    for i in range(N):
        matrix[i].append(0)
    matrix.append(list(0 for _ in range(N+1)))
    
    for i in range(N):
        max_length_row = 0
        max_length_col = 0
        for j in range(N):   
            if matrix[i][j] and matrix[i][j+1] or matrix[i][j]:
                max_length_row += 1
            else:
                max_length_row = 0
                
            if matrix[j][i] and matrix[j+1][i] or matrix[j][i]:
                max_length_col += 1
            else:
                max_length_col = 0
                
            if matrix[i][j+1] == 0 and max_length_row == K:
                result += 1
                
            if matrix[j+1][i] == 0 and max_length_col == K:
                result += 1
    
    print(f'#{tc} {result}')