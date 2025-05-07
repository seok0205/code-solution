'''
S4 10828 스택

스택을 구현. push, pop, size, empty, top.

push : 정수 X를 스택에 넣는 연산
pop : 가장 위의 정수 빼고 그 수 출력. 스택에 든 정수 없으면 -1 출력
size : 스택에 든 정수 개수 출력
empty : 스택에 비어있으면 1, 아니면 0
top : 스택의 가장 위에든 정수 출력. 만약 스택에 들어있는 정수가 없는 경우 -1 출력.
'''

import sys
sys.stdin = open('tc.txt', 'r')


def push(num):
    pass


def pop():
    pass


def size():
    pass


def empty():
    pass


def top():
    pass


N = int(input())
stack = list()

for _ in range(N):
    command = input()

    if command[:4] == 'push':
        com, num = map(input().split())
        num = int(num)
        push(num)
    elif command == 'top':
        top()
    elif command == 'size':
        size()
    elif command == 'pop':
        pop()
    elif command == 'empty':
        empty()