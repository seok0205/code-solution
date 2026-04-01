'''
S2 2512 예산

문제 설명:
국가 역할 중 하나는 여러 지방의 예산요청 심사 후 국가 예산의 분배이다.
예산 총액은 미리 정해져 있어. 모두 배정하기 어려울 수 있다.
그래서 정해진 총액 이하에서 가능한 한 최대의 총 예산을 다음 방법으로 배정.

1. 모든 요청이 배정될 수 있는 경우는 요청한 금액을 그대로 배정.
2. 모든 요청이 배정될 수 없는 경우에는 특정한 정수 상한액을 계산하여 그 이상인 예산 요청에는 모두 상한액을 배정. 상한액 이하의 예산 요청에 대해서는 요청한 금액을 그대로 배정.

예로, 전체 예산이 485이고, 4개 지방 요청이 120, 110, 140, 150일때,
상한액을 127로 잡으면, 위 요청에 대해 120, 110, 127, 127을 배정하고 그합이 484로 가능한 최대가 됨.

여러 지방의 예산 요청과 국가예산의 총액이 주어질 때, 위의 조건을 모두 만족하도록 예산을 배정하는 프로그램을 작성.

입력:
첫째 줄 - 지방 수 N(3 <= N <= 10000)
두번째 줄 - 각 지방의 예산요청 N개 정수가 공백두고 입력. 모두 1이상 100,000이하
세번째 줄 - 총 예산 M (N <= M <= 1,000,000,000)

출력:
첫째 줄에 배정된 예산들 중 최댓값인 정수 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
req = list(map(int, input().split()))
M = int(input())

left = 0
right = max(req)
result = 0


def check(limit, m, req):
    cost = 0
    for i in req:
        if i < limit:
            cost += i
        else:
            cost += limit

    if cost > m:
        return False
    else:
        return True


while left <= right:
    mid = (left + right) // 2
    can = check(mid, M, req)

    if can:
        left = mid + 1
        result = mid
    else:
        right = mid - 1

print(result)