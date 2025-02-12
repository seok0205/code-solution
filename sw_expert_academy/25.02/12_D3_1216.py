'''
D3 1216 회문 2

거꾸로 읽거나 똑바로 읽어도 같은 문장 혹은 단어를 회문이라 함
100x100 글자배열에서 가장 긴 회문을 구하는 문제
'''

import sys
sys.stdin = open('tc.txt', 'r')


def length_func(arr):
    for M in range(100, 0, -1):
        for i in range(100):
            for j in range(100-M+1):
                row_string = matrix[i][j:j+M]       # 열 확인
                row_length = len(row_string)
                
                if row_string[0] == row_string[-1]:     # 양 끝값이 같을때만 비교 시작
                    for l in range(row_length//2):
                        if row_string[l] != row_string[row_length-l-1]:
                            break
                    else:
                        return M
                        
                col_string = list()     # 행 확인
                for k in range(M):
                    col_string.append(matrix[j+k][i])
                col_length = len(col_string)
                
                if col_string[0] == col_string[-1]:     # 양 끝값이 같을때만 비교 시작
                    for m in range(col_length//2):
                        if col_string[m] != col_string[col_length-m-1]:
                            break
                    else:
                        return M        # 가장 높은 값 도출이므로 최대 길이 100에서 내려오기 때문에 도출시 바로 함수 종료


for tc in range(1, 11):
    T = int(input())
    matrix = [input() for _ in range(100)]
    
    result = length_func(matrix)
    
    print(f'#{tc} {result}')