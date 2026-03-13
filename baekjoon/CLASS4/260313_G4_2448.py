'''
G4 2448 별 찍기 - 11

문제 설명:
예제를 보고 규칙을 유추한 뒤 별을 찍는 문제.

입력:
첫째 줄에 N이 주어짐. N은 항상 3 * 2**k 수임.
'''

import sys
sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
star = [[' ' for _ in range(2 * N - 1)] for _ in range(N)]


def solution(n, x, y):
    if n == 3:
        star[x][y] = '*'
        star[x+1][y-1] = '*'
        star[x+1][y+1] = '*'

        for i in range(-2, 3):
            star[x + 2][y + i] = '*'
        return
    
    nn = n // 2

    solution(nn, x, y)
    solution(nn, x + nn, y - nn)
    solution(nn, x + nn, y + nn)


solution(N, 0, N-1)

for s in star:
    output(''.join(s) + '\n')