'''
G5 1074 Z

한수는 크기가 2**N x 2**N인 2차원 배열을 Z모양으로 탐색하려 함.
예로 왼쪽 위, 오른쪽 위, 왼쪽 아래, 오른쪽 아래 순서로 방문 시 Z모양임.

N이 1보다 클경우, 배열을 크기가 2**N-1 x 2**N-1으로 4등분하여 재귀적으로 순서 방문.

N이 주어질 때, r행 c열을 몇번 째로 방문하는지 구하는 문제
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline


def z_func(row, col, n, cnt):       # z 모양으로 읽는 칸의 순서 구하기
    n //= 2

    if row < n and col < n:     # 사분면마다의 조건(왼쪽 위)
        if n == 1:              # 나누지못할 정도로 분할했다면 출력후 함수 종료
            print(cnt)
            return
        z_func(row, col, n, cnt)
    
    elif row < n and col >= n:      # 오른쪽 위
        if n == 1:
            print(cnt + 1)
            return
        z_func(row, col - n, n, cnt + n**2)

    elif row >= n and col < n:      # 왼쪽 아래
        if n == 1:
            print(cnt + 2)
            return
        z_func(row - n, col, n, cnt + n**2 * 2)
    
    elif row >= n and col >= n:     # 오른쪽 아래
        if n == 1:
            print(cnt + 3)
            return
        z_func(row - n, col - n, n, cnt + n**2 * 3)


N, r, c = map(int, input().split())
length = 2**N       # 주어진 길이 무조건 2의 지수승

z_func(r, c, length, 0)