'''
S4 2164 카드2(재풀이)

문제 설명:
N장의 카드가 있음.
각각 1부터 N까지의 번호가 붙어있고, 1번 카드가 제일 위에, N번 카드가 제일 아래인 상태로 순서대로 카드가 놓여 있음.
카드 한장 남을 때까지 같은 동작을 반복함.
1. 제일 위에 있는 카드를 바닥에 버린다.
2. 제일 위에 있는 카드를 제일 아래에 있는 카드 밑으로 옮긴다.

예로, N=4라면 1234 순서로 놓여있고, 1을버리면 234, 2를 밑으로 옮기면 342.
3버리면 42, 4를밑으로 옮기면 24. 마지막 2를 버리면 남는 카드는 4.

N이 주어질 때 마지막에 남는 카드를 구하는 문제.

입력:
N (1 <= N <= 500000)
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

from collections import deque

N = int(input())

cards = deque([i for i in range(1, N+1)])

if N == 1:
    print(1)
else:
    while True:
        cards.popleft()

        if len(cards) == 1:
            break

        a = cards.popleft()
        cards.append(a)
    
    print(cards[0])