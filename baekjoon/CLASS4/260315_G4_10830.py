'''
G4 10830 행렬 제곱

문제 설명:
NxN 행렬 A가 주어짐.
이때, A의 B제곱을 구하는 프로그램을 구하시오.
수가 매우 커질 수 있어 ,A^B의 각 원소를 1,000으로 나눈 나머지를 출력.

입력:
첫 줄 - N, B (2 <= N <= 5, 1 <= B <= 100,000,000,000)
둘째 줄부터 N개의 줄에 행렬의 각 원소주어짐.
행렬의 각 원소는 1,000보다 작거나 같은 자연수 혹은 0.

출력:
첫째 줄부터 N개의 줄에 걸쳐 행렬 A에 B제곱한 결과 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N, B = map(int, input().split())
matrix = [list(map(int,input().split())) for _ in range(N)]


def multiply(matrix_1, matrix_2):
    result = [[0] * N for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += matrix_1[i][k] * matrix_2[k][j]
            result[i][j] %= 1000
    return result


def divide(matrix, b):
    if b == 1:
        for i in range(N):
            for j in range(N):
                matrix[i][j] %= 1000
        return matrix
    
    temp = divide(matrix, b // 2)

    if b % 2 == 0:
        return multiply(temp, temp)
    else:
        return multiply(multiply(temp, temp), matrix)


answer = divide(matrix, B)

for i in answer:
    output(' '.join(map(str, i)) + '\n')