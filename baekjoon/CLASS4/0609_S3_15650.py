'''
S3 15650 N과 M (2)

자연수 N, M이 주어졌을 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 문제
1. 1부터 N까지 자연수 중에서 중복 없이 M개를 고른 수열
2. 고른 수열은 오름차순이어야함

입력:
N, M

출력:
한 줄에 하나씩 문제 조건 만족하는 수열 출력. 중복된 수열을 여러번 출력하면 안됨.
각 수열은 공백으로 구분해서 출력해야 함.
'''

import sys
sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline


def find_num(idx, cnt):
    if cnt == M:
        print(' '.join(map(str, result)))
        return
    
    for i in range(idx+1, N+1):
        result.append(i)
        find_num(i, cnt + 1)
        result.pop()


N, M = map(int, input().split())
result = []

find_num(0, 0)