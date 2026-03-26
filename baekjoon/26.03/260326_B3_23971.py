'''
B3 23971 ZOAC 4

문제 설명:
강의실을 예약하려함.
강의실에서 대회를 치르려면 거리두기 수칙 지켜야함.
한 명씩 앉을 수 있는 테이블이 행마다 W개씩 H행에 걸쳐 있을 때, 모든 참가자는 세로로 N칸 혹은 가로로 M칸 이상 비우고 앉아야 함.
즉, 다른 모든 참가자와 세로줄 번호의 차가 N보다 크거나 M보다 큰 곳에만 앉을 수 있다.
거리두기 수칙을 지키면서 최대 몇 명을 수용할 수 있는지 구하는 문제.

입력:
H, W, N, M이 공백으로 구분되어 주어짐.
(0 < H, W, N, M <= 50000)
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

H, W, N, M = map(int, input().split())

a = H // (N+1)
b = W // (M+1)

if H % (N+1) >= 1:
    a += 1

if W % (M+1) >= 1:
    b += 1

result = a * b
print(result)