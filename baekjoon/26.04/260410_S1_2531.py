'''
S1 2531 회전 초밥

문제 설명:
초밥의 종류를 번호로 표현함.
회전 벨트 위에 같은 종류의 초밥이 있을 수 있음.
두 가지 방법으로 매상을 올리려 함.

1. 회전 초밥은 손님이 마음대로 초밥을 고르고, 먹은 초밥만큼 식대를 계산, 벨트의 임의의 한 위치부터 k개의 접시를 연속해서 먹을 경우 할인된 정액 가격으로 제공한다.
2. 각 고객에게 초밥의 종류 하나가 쓰인 쿠폰을 발행하고, 1번 행사에 참가할 경우 이 쿠폰에 적혀진 종류의 초밥 하나를 추가로 무료로 제공.
만약 이 번호에 적혀진 초밥이 현재 벨트위에 없을 경우, 요리사가 새로 만들어 제공.

회전 초밥 음식점의 벨트 상태, 메뉴에 있는 초밥 가짓수, 연속해서 먹는 접시의 개수, 쿠폰 번호가 주어졌을 때, 손님이 먹을 수 있는 초밥 가짓수의 최댓값을 구하는 프로그램 작성.

입력:
첫 번째 줄 - 회전초밥 벨트에 놓인 접시의 수 N, 초밥의 가짓수 d, 연속해서 먹는 접시의 수 k, 쿠폰 번호 c가 하나씩 공백두고 주어짐.
(2 <= N <= 30,000, 2 <= d <= 3,000, 2 <= k <= 3,000(k <= N), 1 <= c <= d)
두 번째 줄 - N개의 줄에 벨트의 한 위치부터 시작하여 회전 방향을 따라갈 때 초밥의 종류를 나타내는 1이상 d이하의 정수가 각 줄마다 하나씩 주어짐
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N, d, k, c = map(int, input().split())
sushies = []

for _ in range(N):
    sushi = int(input())
    sushies.append(sushi)

sushies.extend(sushies[:k-1])

ate = [0] * (d + 1)
ate[c] = 1
d_cnt = 1

for i in range(k):
    if ate[sushies[i]] == 0:
        d_cnt += 1
    ate[sushies[i]] += 1

result = d_cnt

for i in range(N-1):
    ate[sushies[i]] -= 1
    if ate[sushies[i]] == 0:
        d_cnt -= 1

    if ate[sushies[i + k]] == 0:
        d_cnt += 1 
    ate[sushies[i + k]] += 1

    result = max(result, d_cnt)

print(result)