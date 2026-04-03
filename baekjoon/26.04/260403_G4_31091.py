'''
G4 31091 거짓말

문제 설명:
앞에 N명의 사람들이 있음.
각 사람은 자신을 포함해 몇 명이상이 거짓말을 하고 있다고 말하거나,
몇 명 이하의 사람이 거짓말 하고 있다고 말함.

사람들의 주장이 주어질때, 거짓말을 하는 사람의 수로 가능한 것을 모두 구하라.

입력:
첫 줄 - 사람 수 N (1 <= N <= 500,000)
둘째 줄 - N개의 정수. (-N <= k_i <= N (1 <= i <= N))
k_i가 양의 정수라면, i번째 사람이 k_i명 이상이 거짓말을 하고 있다고 말한다는 뜻.
k_i가 0이거나 음의 정수라면, i번째 사람이 -k_i명 이하가 거짓말을 하고 있다고
말했다는 뜻.

출력:
첫 줄 - 거짓말 하는 사람의 수로 가능한 수 개수 출력.
둘째 줄 - 가능한 수들을 공백 두고 오름차순으로 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
data = list(map(int, input().split()))

diff = [0] * (N+2)

for i in range(N):
    if data[i] > 0:
        diff[data[i]] += 1
        diff[N+1] -= 1
    else:
        target = abs(data[i])
        diff[0] += 1
        diff[target+1] -= 1

truth = 0
result = []

for i in range(N+1):
    truth += diff[i]

    if N - i == truth:
        result.append(i)

print(len(result))
print(*result)