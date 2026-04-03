'''
S1 26091 현대모비스 소프트웨어 아카데미

문제 설명:
견학생 모집하려고 함.
팀 단위로 진행되며, 두 조건을 만족하는 팀만 견학 가능함.

1. 팀원이 두 명.
2. 팀의 능력치가 M이상.(모든 팀원 능력치를 합한 수치)

학회원 N명이 견학을 희망함. N명으로 최대한 많은 팀을 만들어 견학 보내려고 함.
최대 몇 팀이나 견학 보낼 수 있을 지 구하기.

입력:
첫 줄 - 견학 희망 학회원 수 N, 최소 능력치 M가 공백 두고 주어짐. (1 <= N <= 100,000, 1 <= M <= 10**9)
둘째 줄 - 학회원 N명의 능력치 N개 정수(a_i)가 공백을 두고 주어짐. (1 <= a_i <= 10**9)

출력:
최대로 보낼 수 있는 팀 수
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, M = map(int, input().split())
members = list(map(int, input().split()))
members.sort()
result = 0
left = 0
right = N-1

while left < right:
    cost = members[left] + members[right]

    if cost >= M:
        result += 1
        left += 1
        right -= 1
        continue

    if cost < M:
        left += 1

print(result)