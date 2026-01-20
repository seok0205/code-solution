'''
S2 2108 통계학

문제 설명:
N개의 수를 대표하는 기본 통계값들. 단 N은 홀수

1. 산술평균 : N개의 수들의 합을 N으로 나눈 값
2. 중앙값 : N개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치한 값
3. 최빈값 : N개의 수들 중 가장 많이 나타나는 값
4. 범위 : N개의 수들 중 최댓값과 최솟값의 차이

N개의 수가 주어질 때, 네 가지 기본 통계값을 구하는 프로그램 작성

입력:
첫째 줄에 수의 개수 N이 주어짐 (1 <= N <= 500,000). N은 홀수
N개의 줄에는 정수들이 주어짐. 입력된 정수의 절댓값은 4,000을 넘지 않음

출력:
산술평균 출력 - 소수점 이하 첫째 자리에서 반올림한 값 출력
중앙값 출력
최빈값 출력 - 여러 개 있을 땐 최빈값 중 두 번째로 작은 값 출력
범위 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
print = sys.stdout.write

N = int(input())
nums = []

for _ in range(N):
    num = int(input())
    nums.append(num)

def avg_func(nums):
    a = round((sum(nums) / N) + 0.00000001)
    print(str(a) + '\n')

def central_func(nums):
    new_nums = sorted(nums)
    print(str(new_nums[N//2]) + '\n')

def mode_func(nums):
    num_cnt = [0 for _ in range(8002)]
    for i in nums:
        num_cnt[i] += 1

    max_cnt = max(num_cnt)
    mode_cnt = num_cnt.count(max_cnt)
    cnt = 0

    if mode_cnt > 1:
        for j in range(-4000, 4001):
            if num_cnt[j] == max_cnt:
                cnt += 1
                if cnt == 2:
                    print(str(j) + '\n')
                    break
    else:
        for j in range(-4000, 4001):
            if num_cnt[j] == max_cnt:
                print(str(j) + '\n')
                break
    
def range_func(nums):
    min_num = min(nums)
    max_num = max(nums)
    print(str(max_num - min_num) + '\n')

avg_func(nums)
central_func(nums)
mode_func(nums)
range_func(nums)