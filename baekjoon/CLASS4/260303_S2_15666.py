'''
S2 15666 N과 M(12)

문제 설명:
N개의 자연수와 자연수 M이 주어질 때, 아래 조건을 만족하는 길이가 M인 수열을 모두 구하는 프로그램을 작성.

- N개의 자연수 중에서 M개를 고른 수열
- 같은 수를 여러 번 골라도 된다
- 고른 수열은 비내림차순이어야 함
    - 길이가 K인 수열 A가 A1 <= A2 <= ... <= AK를 만족하면, 비내림차순

입력:
첫 줄 N, M (1 <= M <= N <= 8)
둘째 줄 N개의 수. 각각 10,000보다 작거나 같은 자연수
'''

import sys

# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N, M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
visit = [0] * N
results = []

def solution(idx, cnt):
    if cnt == M:
        temp = []

        for k in range(N):
            for _ in range(visit[k]):
                temp.append(nums[k])

        if temp not in results:
            results.append(temp)
        return
    
    for i in range(idx, N):
        visit[i] += 1
        solution(i, cnt + 1)
        visit[i] -= 1

solution(0, 0)

for result in results:
    output(' '.join(map(str, result)) + '\n')