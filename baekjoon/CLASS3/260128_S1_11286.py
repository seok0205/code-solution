'''
11286 S1 절댓값 힙

문제 설명:
절댓값 힙은 다음과 같은 연산을 지원하는 자료구조.

1. 배열에 정수 x를 (x != 0) 넣는다.
2. 배열에서 절댓값이 가장 작은 값을 출력하고, 그 값을 배열에서 제거한다.
절댓값이 가장 작은 값이 여러개일 때, 가장 작은 수를 출력하고, 그 값을 배열에서 제거.

프로그램은 처음에 비어있는 배열에서 시작

입력:
첫 줄 - 연산 개수 N (1~100,000)
N개의 줄 - 연산에 대한 정보 정수 x. 만약 x가 0이 아니라면 배열에  x를 추가하는 연산, 0이면 출력하고 제거하는 경우.
정수는 -2**31보다 크고, 2**31 보다 작다.

출력:
입력에서 0이 주어진 회수만큼 답을 출력.
만약 비어있는 경우인데 절댓값이 가장 작은 값을 출력하라고 한 경우에는 0을 출력하면 됨.
'''

import sys
import heapq
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())

hq = []

for _ in range(N):
    num = int(input())

    if num == 0:
        if hq:
            output(str(heapq.heappop(hq)[1]) + '\n')
        else:
            output('0' + '\n')

        continue

    heapq.heappush(hq, (abs(num), num))