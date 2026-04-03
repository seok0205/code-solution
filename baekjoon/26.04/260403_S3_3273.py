'''
S3 3273 두 수의 합

문제 설명:
n개의 서로 다른 양의 정수로 이루어진 수열이 있음.
a_i의 값은 1보다 크거나 같고, 1000000보다 작거나 같은 수.
자연수 x가 주어질 때, a_i + a_j = x(1 <= i <= j <= n)을 만족하는 (a_i, a_j) 쌍의 수를 구하는 문제.

입력:
첫 줄 - 수열 크기 n (1 <= n <= 100000)
두번째 줄 - 수열에 포함되는 수들
셋째 줄 - x (1 <= x <= 2000000)

출력:
조건 만족하는 쌍의 개수
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

n = int(input())
nums = list(map(int, input().split()))
x = int(input())
nums.sort()

result = 0
left = 0
right = n-1

while left < right:
    cost = nums[left] + nums[right]
    if cost == x:
        result += 1
        left += 1
        right -= 1
        continue

    if cost > x:
        right -= 1
    elif cost < x:
        left += 1

print(result)