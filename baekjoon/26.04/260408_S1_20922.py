'''
S1 20922 겹치는 건 싫어

문제 설명:
수열에서 같은 원소가 여러 개 들어 있는 수열을  싫어함.
같은 원소가 K개 이하 들어있는 최장 연속 부분 수열의 길이를 구하려함.
100,000 이하의 양의 정수로 이루어진 길이가 N인 수열이 주어짐.
이 수열에서 같은 정수를 K개 이하로 포함한 최장 연속 부분 수열의 길이를 구하는 프로그램 작성.

입력:
첫째 줄 - N, K (1 <= N <= 200,000, 1 <= K <= 100)
둘째 줄 - a_1 ~ a_n이 주어짐 (1 <= a_i <= 100,000)

출력:
조건 만족하는 최장 연속 부분 수열의 길이 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, K = map(int, input().split())
nums = list(map(int, input().split()))

result = 1
visit = [0] * 100001
left = 0
visit[nums[left]] += 1
right = 0

while right < N:
    if right < N-1:
        right += 1
    else:
        break

    visit[nums[right]] += 1

    if visit[nums[right]] > K:
        while visit[nums[right]] > K:
            visit[nums[left]] -= 1
            left += 1
    else:
        result = max(result, right - left+1)

print(result)