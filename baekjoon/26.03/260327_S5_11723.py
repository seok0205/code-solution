'''
S5 11723 집합 (복습)

문제 설명:
비어있는 공집합 S가 주어질 때, 연산 수행 프로그램 작성.
조건 : (1 <= x <= 20)
1. add x : S에 x 추가. S에 x가 이미 있으면 무시.
2. remove x : S에 x 제거. S에 x가 없는 경우에는 무시.
3. check x : S에 x가 있으면 1, 없으면 0출력.
4. toggle x : S에 x가 있으면 x 제거, 없으면 추가.
5. all : S를 {1, 2, ..., 20} 으로 바꿈.
6. empty : S를 공집합으로 바꿈.

입력:
첫째 줄에 수행해야하는 연산 수 M (1 <= M <= 3000000)
둘째 줄부터 M개의 줄에 수행해야하는 연산 주어짐.

출력:
check 연산 시에만 결과 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

M = int(input())
S = 0
for _ in range(M):
    data = list(map(str, input().strip().split()))

    if data[0] == 'all':
        S = (1 << 21) - 1
    elif data[0] == 'empty':
        S = 0
    else:
        command, num = data[0], int(data[1])

        if command == 'add':
            S |= (1 << num)
        elif command == 'remove':
            S &= ~(1 << num)
        elif command == 'check':
            if S & (1 << num):
                print(1)
            else:
                print(0)
        elif command == 'toggle':
            S ^= (1 << num)