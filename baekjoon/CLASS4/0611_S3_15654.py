'''
S3 15654 N과 M (5)

N개의 자연수와 자연수 M이 주어졌을 때, 아래 조건 만족하는 길이 M인 수열 구하는 문제
N개의 자연수는 모두 다른 수.
1. N개의 자연수 중에서 M개를 고른 수열
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline


def find_func(cnt):
    if cnt == M:        # M개 만족하면 호출 중단 및 출력
        print(' '.join(map(str, result)))
        return
    
    for i in range(N):
        if num_list[i] not in result:       # 같은 숫자 중복 출력 방지 조건
            result.append(num_list[i])
            find_func(cnt + 1)
            result.pop()


N, M = map(int, input().split())
num_list = list(map(int, input().split()))
num_list.sort()                             # 사전 순으로 출력하기 위해

result = []

find_func(0)        # 수열 찾기