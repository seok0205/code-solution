'''
S3 15652 N과 M (4)

문제 설명:
자연수 N과 M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램 작성.

1. 1부터 N까지 자연수 중에서 M개를 고른 수열
2. 같은 수를 여러 번 골라도 됨.
3. 고른 수열은 비내림 차순이어야 함.
    - 길이가 K인 수열 A가 A1 <= A2 <= .. <= Ak-1 <= Ak를 만족하면, 비내림차순이라 함

입력:
첫째 줄 - 자연수 N, M (1 <= M <= N <= 8)

출력:
한 줄에 하나씩 문제의 조건을 만족하는 수열 출력.
중복되는 수열을 여러번 출력하면 안됨. 각 수열은 공백으로 구분해서 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().strip().split())
nums = [i for i in range(1, N+1)]
permutation = []


def backtracking(idx):
    if len(permutation) == M:
        output(' '.join(map(str, permutation)) + '\n')
        return
    
    for i in range(idx, N+1):
        permutation.append(i)
        backtracking(i)
        permutation.pop()


backtracking(1)