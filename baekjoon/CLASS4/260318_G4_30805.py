'''
G4 30805 사전 순 최대 공통 부분 수열

문제 설명:
어떤 수열이 다른 수열의 부분 수열이란 것
- 해당 수열의 원소들이 다른 수열 내에서 순서대로 등장.

또한 어떤 수열이 다른 수열보다 사전 순으로 나중이라는 것
- 두 수열 중 첫 번째 수가 큰 쪽은 사전 순으로 나중.
- 두 수열의 첫 번째 수가 같다면, 첫 번째 수를 빼고 두 수열을 다시 비교했을 때 사전 순으로 나중인 쪽이 사전 순으로 나중.
- 길이가 0인 수열과 다른 수열을 비교하면 다른 수열이 사전순으로 나중.

양의 정수로 이루어진 길이가 N인 수열이 주어짐.
마찬가지로 양의 정수로 이루어진 길이가 M인 수열이 주어짐.
수열 A, B가 공통으로 갖는 부분 수열 중 사전 순으로 가장 나중인 것을 구하는 문제.

입력:
첫 줄 - 수열 A의 길이 N (1 <= N <= 100)
둘째 줄 - N개의 양의 정수
셋째 줄 - 수열 B의 길이 M (1 <= M <= 100)
넷째 줄 - M개의 양의 정수

출력:
A와 B의 공통 부분 수열 중 사전 순으로 가장 나중인 수열의 크기 K 출력
K != 0이면, 다음 줄에 K개의 수를 공백으로 구분해 출력.
i번째 수는 A, B의 공통 부분 수열중 사전 순으로 가장 나중인 수열의 i번째 수.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())
A = list(map(int, input().split()))
M = int(input())
B = list(map(int, input().split()))

nums = []
a_idx = 0
b_idx = 0

while True:
    common = set(A[a_idx:]) & set(B[b_idx:])

    if not common:
        break

    max_num = max(common)
    nums.append(max_num)

    a_idx = A.index(max_num, a_idx) + 1
    b_idx = B.index(max_num, b_idx) + 1

output(str(len(nums)) + '\n')
if nums:
    output(' '.join(map(str, nums)))