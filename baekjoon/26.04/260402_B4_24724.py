'''
B4 24724 현대모비스와 함께하는 부품 관리

문제 설명:
부품을 여러 그룹으로 나눠서 관리.
각 그룹의 부품들의 크기의 합이 A가 넘지 않으면서 무게 합이 B가 안 넘어야 함.
그룹의 수를 최소화 하려고함.

그룹 분류 하려는 부품 크기와 무게가 주어질때, 그룹 분류를 하는 프로그램 작성.

입력:
부품 관리 횟수 - T (1 <= T <= 10)
각 부품 관리에 대한 입력
- 첫줄 부품 개수 N (1 <= N <= 10000)
- 두번째 줄 각 그룹 크기 제한, 무게 제한(1 <= A, B <= 10**9)
- 세번째 줄부터 N개의 줄에 걸쳐 각 부품 크기, 부품 정보인 u, v 주어짐. (1 <= u <= A, 1 <= v <= B)

출력:
첫 줄 - Material Management x 출력. x는 부품 관리 process의 번호 의미. 1부터 1씩 증가.
두번째 줄 - Classification ---- End! 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

T = int(input())

for tc in range(1, T+1):
    print(f'Material Management {tc}')

    N = int(input())
    a_limit, b_limit = map(int, input().split())

    for _ in range(N):
        u, v = map(int, input().split())

    print('Classification ---- End!')