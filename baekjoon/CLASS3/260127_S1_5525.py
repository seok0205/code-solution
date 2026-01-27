'''
S1 5525 IOIOI

문제 설명:
N+1개의 I와 N개의 O로 이루어져 있으면, I와 O이 교대로 나오는 문자열을 PN이라고 함
ex) IOI - P1, IOIOI - P2, IOIOIOI - P3

I와 O로만 이루어진 문자열 S와 정수 N이 주어졌을 때, S안에 PN이 몇 군데 포함되어 있는지 구하는 프로그램 작성

입력:
첫째 줄에 N. 1~1,000,000
둘째 줄에 S의 길이 M. 2N+1 ~ 1,000,000
셋째 줄에 S.

출력:
S에 PN이 몇 군데 포함되어 있는지 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
M = int(input())
S = input().strip()

result = 0
cnt = 0
idx = 0

while idx < M - 1:
    if S[idx:idx+3] == 'IOI':
        cnt += 1

        if cnt == N:
            result += 1
            cnt -= 1

        idx += 2

    else:
        cnt = 0
        idx += 1

output(str(result))