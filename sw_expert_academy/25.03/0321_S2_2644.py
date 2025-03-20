'''
S2 2644 촌수계산

부모 자식 사이 1촌.
나, 할아버지는 2촌, 아버지 형제와 할아버지는 1촌, 나, 아버지 형제들과는 3촌.
여러 사람들에 대한 부모 자식간 관계가 주어지면 두 사람 촌수를 계산하는 프로그램 작성
'''

import sys
sys.stdin = open('tc.txt', 'r')

N = int(input())
a, b = map(int, input().split())
M = int(input())
relationship = [[] for _ in range(N)]

for _ in range(M):
    r1, r2 = map(int, input().split())