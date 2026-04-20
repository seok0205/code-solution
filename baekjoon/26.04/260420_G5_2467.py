'''
G5 2467 용액

문제 설명:
산성, 알칼리성 용액 보유중.
각 용액에는 그 용액의 특성을 나타내는 하나의 정수가 주어짐.
산성은 1부터 1,000,000,000 양의정수.
알칼리성은 -1부터 -1,000,000,000 음의 정수.

같은 양의 두용액을 혼합한 용액의 특성값은 각 용액의 합으로 정의.
특성값이 0에 가까운 용액 만들려고 함.

예로 [-99, -2, -1, 4, 98]인 경우, 특성값이 -99인 용액이랑 98인 용액 혼합하면 특성값 -1인 용액. 이것이 특성값이 0에 가장 가까운 용액.
참고로 두 종류의 알칼리성이나 산성용액만으로도 0에 가까운 용액 만들 수 있음.

특성값이 정렬된 순서로 주어질 때, 이 중 두개의 서로 다른 용액을 혼합하여 특성값이 0에 가까운 용액을 만들어내는 두 용액을 찾는 프로그램 작성.

입력:
첫째 줄 - 전체 용액 수 N (2 이상 100,000 이하 정수)
둘째 줄 - 용액의 특성값을 나타내는 N개의 정수가 오름차순으로 입력.
(모두 -1,000,000,000 이상 1,000,000,000 이하)
N개의 용액들의 특성값은 모두 서로 다름, 산성 용액만이나 알칼리성으로만 주어진 입력도 존재.

출력:
0에 가장 가까운 용액을 만들어내는 두 용액의 특성값 출력.
오름차순으로 출력.
조합이 두 개 이상이면 아무거나 한 조합 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
liquid = list(map(int, input().split()))

left = 0
right = N-1
min_cost = float('inf')
ans_l = 0
ans_r = N-1

while left < right:
    cost = liquid[left] + liquid[right]

    if abs(cost) < min_cost:
        min_cost = abs(cost)
        ans_l = left
        ans_r = right
    
    if cost == 0:
        break
    elif cost > 0:
        right -= 1
    else:
        left += 1

print(liquid[ans_l], liquid[ans_r])