'''
S4 10828 스택

스택을 구현. push, pop, size, empty, top.

push : 정수 X를 스택에 넣는 연산
pop : 가장 위의 정수 빼고 그 수 출력. 스택에 든 정수 없으면 -1 출력
size : 스택에 든 정수 개수 출력
empty : 스택에 비어있으면 1, 아니면 0
top : 스택의 가장 위에든 정수 출력. 만약 스택에 들어있는 정수가 없는 경우 -1 출력.
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def push(num):          # 스택에 push(숫자 넣기)
    stack.append(num)


def pop():              # pop : 가장 위 정수 빼고, 출력. 스택이 비어있다면 -1 출력
    if stack:
        print(stack.pop())
    else:
        print(-1)


def size():             # size : 스택에 든 정수 개수 출력
    print(len(stack))


def empty():            # empty : 스택에 비어있으면 1, 아니면 0
    if stack:
        print(0)
    else:
        print(1)


def top():              # top : 스택의 가장 위에든 정수 출력. 만약 스택에 들어있는 정수가 없는 경우 -1 출력.
    if stack:
        print(stack[-1])
    else:
        print(-1)


N = int(input())
stack = list()          # 명령에 따라 활용할 스택 생성

for _ in range(N):
    command = input()       # 명령 입력 받기

    if command[:4] == 'push':       # push면 뒤에 숫자를 알아야함
        com, num = map(str, command.split())        # 공백 단위로 둘로 나누고 num을 int화시킴
        num = int(num)
        push(num)                   # 정수화시킨 num을 푸시
    elif command == 'top':
        top()
    elif command == 'size':
        size()
    elif command == 'pop':
        pop()
    elif command == 'empty':
        empty()