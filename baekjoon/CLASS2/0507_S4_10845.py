'''
S4 10845 큐

큐를 구현하는 문제.

명령 6가지
1. push X: 정수 X를 인큐
2. pop: 큐의 가장 앞의 정수를 빼고, 그 수를 출력. 큐가 비어있다면 -1 출력
3. size: 큐에 들어있는 정수의 개수 출력
4. empty: 큐가 비어있으면 1, 아니면 0 출력
5. front: 큐가 가장 앞에 있는 정수를 출력. 만약 큐에 들어있는 정수 없으면 -1 출력
6. back: 큐가 가장 뒤에 있는 정수를 출력. 만약 큐에 들어있는 정수 없으면 -1 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

from collections import deque


def push(num):          # push X: 정수 X를 인큐
    q.append(num)


def pop():              # pop: 큐의 가장 앞의 정수를 빼고, 그 수를 출력. 큐가 비어있다면 -1 출력
    if q:
        print(q.popleft())
    else:
        print(-1)


def size():             # size: 큐에 들어있는 정수의 개수 출력
    print(len(q))


def empty():            # empty: 큐가 비어있으면 1, 아니면 0 출력
    if q:
        print(0)
    else:
        print(1)


def front():            # front: 큐가 가장 앞에 있는 정수를 출력. 만약 큐에 들어있는 정수 없으면 -1 출력
    if q:
        print(q[0])
    else:
        print(-1)


def back():             # back: 큐가 가장 뒤에 있는 정수를 출력. 만약 큐에 들어있는 정수 없으면 -1 출력
    if q:
        print(q[-1])
    else:
        print(-1)


N = int(input())
q = deque()

for _ in range(N):
    command = input()

    if command[:4] == 'push':               # 명령에 따른 함수 실행
        com, num = map(str, command.split())
        num = int(num)
        push(num)
    elif command == 'pop':
        pop()
    elif command == 'size':
        size()
    elif command == 'empty':
        empty()
    elif command == 'front':
        front()
    elif command == 'back':
        back()