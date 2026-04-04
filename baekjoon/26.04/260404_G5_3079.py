'''
G5 3079 입국심사

문제설명:
사람이 N명. 입국심사대는 N개.
입국심사관이 심사를 하는데 걸리는 시간은 모두 다름.
k번 심사대에 앉은 심사관의 시간은 T_k.
한 심사대에 한 명씩, 비어있는 심사대가 보이면 거기로 가서 심사 받음.
항상 이동해야하는 것은 아님.
더 빠른 심사대의 심사가 끝나길 기다린 다음 거기 가도 됨.
심사 받는 데 걸리는 시간의 최솟값 구하는 문제.

입력:
N, M (1 <= N <= 100,000, 1 <= M <= 1,000,000,000)
다음 N개의 줄에 각 심사가 걸리는 시간 T_k (1 <= T_k <= 10**9)
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
times = []

for _ in range(N):
    time = int(input())
    times.append(time)

min_time = 0
low_t = 0
high_t = max(times) * M

while low_t <= high_t:
    mid_t = (low_t + high_t) // 2

    total = 0
    for time in times:
        total += (mid_t // time)

        if total >= M:
            break

    if total >= M:
        min_time = mid_t
        high_t = mid_t - 1
    else:
        low_t = mid_t + 1 

print(min_time)