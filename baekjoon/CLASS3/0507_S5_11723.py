'''
S5 11723 집합

비어있는 공집합 S가 주어질 때, 아래 명령 수행하는 프로그램 작성.

1. add x: S에 x 추가. 이미 있으면 연산 무시
2. remove x: S에서 x 제거. 이미 없으면 무시
3. check x: S에 x 있으면 1, 없으면 0 출력
4. toggle x: S에 x 있으면 x 제거, 없으면 x 추가
5. all: S를 {1, 2, ... 20}으로 바꿈
6. empty: S를 공집합으로 바꿈
'''

import sys
# sys.stdin = open('tc.txt', 'r')

M = int(sys.stdin.readline())       # fast I/O 활용
S = set()

for _ in range(M):
    command = sys.stdin.readline().split()

    if 'all' in command:                    # all: S를 {1, 2, ... 20}으로 바꿈
        S = set([i for i in range(1, 21)])
    elif 'empty' in command:                # empty: S를 공집합으로 바꿈
        S = set()
    else:
        com, x = command[0], int(command[1])
        if com == 'add':                        # add x: S에 x 추가. 이미 있으면 연산 무시
            S.add(x)
        elif com == 'remove':                   # remove x: S에서 x 제거. 이미 없으면 무시
            S.discard(x)
        elif com == 'check':                    # check x: S에 x 있으면 1, 없으면 0 출력
            if x in S:
                sys.stdout.write('1\n')
            else:
                sys.stdout.write('0\n')
        elif com == 'toggle':                   # toggle x: S에 x 있으면 x 제거, 없으면 x 추가
            if x in S:
                S.discard(x)
            else:
                S.add(x)