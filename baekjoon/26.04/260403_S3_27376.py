'''
S3 27376 참살이길

문제 설명:
참살이길에서 사고율 0퍼센트의 자율주행차를 시운전하려 함.
길이가 n미터이고, 그 위에 k개의 신호등 존재.
참살이길의 시작점에서 끝점까지 도달하는 데 얼마나 시간이 걸리는지 알고 싶음.

시작점 좌표 0, 끝점 좌표가 n인 수직선으로 가정 가능.
신호등은 오직 정수 좌표점에서만 존재 가능.
신호등은 빨, 초 두 가지 상태를 가지며, i번째 신호등안 빨, 초가 각각 t_i초동안 번갈아가면서 켜짐.
주행 시작 지점에서 s_i초 이후에 이 신호등은 처음으로 빨에서 초가 됨.
빨일 때, 차는 신호등 위치에서 반드시 정지, 초일 때는 문제 없이 지나감.

참살이길에선 과속하면 안됨. 1m/s의 속도로 이동.
가속, 감속 없이 항상 이속도로 이동 혹은 정지.
시작점, 끝점에는 신호등 존재하지 않고, 한 정수 좌표점에 두 개 이상 신호등 존재 불가능.
신호등이 초에서 빨로 바뀌는 시점에 해당 신호등 위치에 있는 차는 출발 못함.

각 신호등 좌표, 주기가 주어질 때, 가장 빠르게 완주하는 데 걸리는 시간 구하기.

입력:
길이와 신호등 개수 n, k (1 <= n <= 10**9, 0 <= k <= min(10**5, n-1))
다음 k개의 줄 중 i번째 줄에 i번째 신호등의 좌표의 주기, 신호등이 처음 초록불 될때까지 걸린 시간 x_i, t_i, s_i가 주어짐.
(1 <= i <= k, 1 <= x <= n-1, 1 <= t <= 10**9, 0 <= s <= t-1)
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

n, k = map(int, input().split())
sign = []

for _ in range(k):
    x, t, s = map(int, input().split())
    sign.append((x, t, s))

sign.sort(key=lambda x: x[0])

last_location = 0
now_t = 0
for location, change_time, first_change in sign:
    now_t += (location - last_location)
    last_location = location

    temp = (now_t - first_change) // change_time
    next_cnt = change_time - ((now_t - first_change) % change_time)
    is_red = temp % 2

    if is_red:
        now_t += next_cnt

now_t += (n - last_location)
print(now_t)