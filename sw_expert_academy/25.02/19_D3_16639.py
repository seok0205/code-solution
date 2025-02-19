'''
D3 16639 피자굽기

N개의 피자를 동시에 구울 수 있는 화덕. 1번부터 M번까지 M개의 피자를 순서대로 화덕에 넣을 때,
꺼내지는 순서는 다를 수 있음. 가장 마지막까지 남아있는 피자 번호 알아내는 문제

1. 피자는 1번위치에서 넣거나 뺌
2. 내부받침은 천천히 회전해서 1번에서 잠시 꺼내 치즈 확인후 다시 같은자리 넣을수 있음
3. M개의 피자에 처음 뿌려진 치즈의 양이 주어지고, 화덕을 한 바퀴 돌때 녹지않은 치즈의 양은 반으로 줄어듦
이전 치즈의 양을 C라고 하면 다시 꺼낼 때 C//2로 줄어듦
4. 치즈가 모두 녹아 0이 되면 화덕에서 꺼내고, 바로 그 자리에 남은 피자 순서대로 넣음
'''

import sys
sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    cheese = list(map(int, input().split()))

    qsize = N + 1   # 화덕 크기(1번부터 N번까지, front위한 빈칸 1개)
    fire = [0] * qsize      # 화덕 생성
    front = rear = 0        # 큐 생성 위함

    for i in range(N):      # 첫 오븐에 피자를 넣음
        rear = (rear + 1) % qsize
        fire[rear] = i

    next_p = N              # 다음 들어갈 피자 번호

    while front != rear:    # 화덕이 비어있지 않으면 계속
        front = (front + 1) % qsize
        now_p = fire[front]     # 피자 꺼냄

        cheese[now_p] //= 2     # 남은 치즈

        if cheese[now_p] > 0:       # 치즈가 다 안녹으면
            rear = (rear + 1) % qsize
            fire[rear] = now_p      # 다시 넣음
        else:           # 다녹았으면
            if next_p < M:     # 다음 넣을 피자 남아있으면
                rear = (rear + 1) % qsize   # 다음 피자 넣음
                fire[rear] = next_p
                next_p += 1     # 다음피자 번호

    print(f'#{tc} {now_p + 1}')
