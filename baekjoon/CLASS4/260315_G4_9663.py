'''
G4 9663 N Queen

문제 설명:
N-Queen 문제는 크기가 N x N인 체스판 위에 퀸 N개를 서로 공격할 수 없게 놓는 문제이다.

N이 주어졌을 때, 퀸을 놓는 방법의 수를 구하는 프로그램을 작성하시오.

입력:
첫째 줄 N (1 <= N <= 15)
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
board = [[0] * N for _ in range(N)]
answer = 0

visit_one = [0] * N
visit_two = [0] * (2 * N - 1)
visit_three = [0] * (2 * N - 1)


def dfs(n):
    global answer

    if n == N:
        answer += 1
        return
    
    for i in range(N):
        if not visit_one[i] and not visit_two[n+i] and not visit_three[n-i+(N-1)]:
            visit_one[i] = visit_two[n+i] = visit_three[n-i+(N-1)] = 1
            dfs(n+1)
            visit_one[i] = visit_two[n+i] = visit_three[n-i+(N-1)] = 0


dfs(0)
output(str(answer))