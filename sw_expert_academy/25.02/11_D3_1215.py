'''
D3 1215 회문 1

똑바로 읽거나 거꾸로 읽어도 똑같은 단어 및 문장을 회문이라 함
8x8 평변 글자 배열에서 제시된 길이를 가진 회문 개수를 구하는 문제

제약 사항:
칸의 글자는 A, B, C 중 하나
가로 혹은 세로로 이어진 회문의 개수만 셈
ABA, A, ABBA도 회문
직선이 아니면 인정 X

입력:
10개 테스트 케이스
M : 찾아야하는 회문의 길이
8x8글자판
'''

import sys
sys.stdin = open('seok.txt', 'r')

for tc in range(1, 11):
    M = int(input())
    matrix = [list(input()) for _ in range(8)]
    result = 0

    for i in range(8):
        for j in range(8-M+1):
            row_str = matrix[i][j:j+M]
            for k in range(M//2):
                if row_str[k] != row_str[M-k-1]:
                    break
            else:
                result += 1

    for i in range(8):
        for j in range(8-M+1):
            col_str = list()
            for k in range(M):
                col_str.append(matrix[j+k][i])
            for l in range(M//2):
                if col_str[l] != col_str[M-l-1]:
                    break
            else:
                result += 1

    print(f'#{tc} {result}')
