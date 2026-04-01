'''
S3 21921 블로그

문제 설명:
블로그 시작한지 N일이 지남.
X일 동안 가장 많이 들어온 방문자 수와 그 기간을 알려고 함.
X일 동안 가장 많이 들어온 방문자 수와 기간이 몇 개 있는지 구하는 문제.

입력:
첫 줄 - 블로그 시작하고 지난 일수 N, X. (1 <= X <= N <= 250,000)
둘째 줄 - 블로그 시작 1일차부터 N일차까지 하루 방문자수가 공백으로 구분되어 주어짐(0 <= 방문자 수 <= 8000)

출력:
첫째 줄에 X일 동안 가장 많이 들어온 방문자 수 출력.
만약 최대 방문자 수가 0명이라면 SAD 출력.
만약 최대 방문자 수가 0명 아니면 둘째 줄에 기간이 몇 개있는지 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, X = map(int, input().split())
visit = list(map(int, input().split()))
records = [0] * N
records[0] = visit[0]

for i in range(1, X):
    records[i] = visit[i] + records[i-1]

for i in range(X, N):
    records[i] = visit[i] + records[i-1] - visit[i-X]

max_visit = max(records)

if max_visit == 0:
    print('SAD')
else:
    print(max_visit)
    print(records.count(max_visit))