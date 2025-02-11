'''
D2 16811 당근 포장하기

N개 당근 주문 시 대, 중, 소로 구분해 포장

조건:
같은 크기 당근은 같은 상자에 있어야 함
비어 있는 상자 있으면 안됨
N/2를 초과하는(N이 홀수면 소수점 버림) 것도 안됨

각 상자에 든 당근의 개수 차이가 최소가 되도록 포장해야 함
개수 차이를 서류에 표시

입력:
T : 수확 횟수
N : 당근 개수
C : 당근 크기

출력:
포장 할 수 없으면 -1, 포장할 수 있다면 상자에 든 당근의 개수 차이가 최소 일대 차이값 출력
'''

import sys
sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    C = list(map(int, input().split()))
    C.sort()
    
    cnt = [0 for _ in range(N+1)]
    
    for i in C:
        cnt[i] += 1
        
    print(cnt)
    
    