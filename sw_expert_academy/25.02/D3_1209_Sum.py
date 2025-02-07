import sys

sys.stdin = open('seok.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    matrix = [list(map(int, input().split())) for _ in range(100)]

    sum_list = list()

    for i in range(100):    # 행의 합
        row_sum = 0
        for j in range(100):
            row_sum += matrix[i][j]
        sum_list.append(row_sum)

    for i in range(100):    # 열의 합
        col_sum = 0
        for j in range(100):
            col_sum += matrix[j][i]
        sum_list.append(col_sum)

    dia_sum = 0     # 대각선 합
    dia_sum_2 = 0
    for i in range(100):
        dia_sum += matrix[i][i]
        dia_sum_2 += matrix[i][99-i]
    sum_list.append(dia_sum)
    sum_list.append(dia_sum_2)

    result = sum_list[0]    # 모은 합들 중 최댓값 도출
    for i in sum_list:
        if result < i:
            result = i

    print(f'#{tc} {result}')
