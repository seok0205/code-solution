'''
S2 11053 가장 긴 증가하는 부분 수열

수열 A가 주어졌을 때, 가장 긴 증가하는 부분 수열을 구하는 문제.
예로, A = [10, 20, 10, 30, 20, 50]일 때,
가장 긴 증가하는 부분 수열은 A = [10, 20, 30, 50]이고 길이는 4.

가장 긴 증가하는 부분 수열의 길이 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))
sequence = [0] * N          # 끝날 위치에서의 최대 수열 길이 담기

for i in range(N):          # A의 모든 칸에서 끝날 때 탐색해보기
    for j in range(i):      # 이전 값들과 비교
        if A[i] > A[j] and sequence[i] < sequence[j]:       # 이전값이 더 작아야 하고, sequence에 저장된 마지막 값보다는 커야함.
            sequence[i] = sequence[j]               # 이전값의 값을 넣어주고,
    sequence[i] += 1                # 최대 길이 1 증가

print(max(sequence))        # sequence의 최댓값 구하기