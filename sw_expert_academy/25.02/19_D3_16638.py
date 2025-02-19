'''
D3 16638 회전

N개의 숫자로 이루어진 수열이 존재.
맨 앞의 숫자를 맨 뒤로 보내는 작업을 M번했을 때, 수열의 맨 앞에 있는 숫자를 출력
'''

import sys
sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    # N : 숫자 개수
    # M : 맨 앞의 숫자를 맨뒤로 보내는 일을 M번 해야함, 작업횟수
    N, M = map(int, input().split())

    # 입력으로 들어온 한 줄 자체를 큐로 사용해버린다.
    Q = list(map(int, input().split())) + ([0] * M)

    front = -1
    rear = N - 1

    # 원소를 꺼내고 넣는 일을 M번 반복한다.
    for _ in range(M):
        # 원소를 꺼내고
        front += 1
        item = Q[front]
        # 원소를 넣고
        rear += 1
        Q[rear] = item

    # 맨 앞에 있는 원소는? dequeue 연산 한번 더 하면 된다.
    front += 1
    print(f"#{tc} {Q[front]}")
