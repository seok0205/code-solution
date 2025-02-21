'''
D3 1289 원재의 메모리 복구하기

비트중 한자리 골라 0, 1인지 결정하면 메모리 끝까지 덮어씌움
예로 0100에서 3번째 비트 골라 1로 설정하면 0111이 됨
원래 상태가 주어질때 초기화 상태에서 원래 상태로 돌아가는데 최소 몇번을 고쳐야하는 지 계산
'''

import sys
sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    target = list(map(int, input()))
    bit = [0] * len(target)
    
    for i in range(len(bit)):
        if bit[i] != target[i]:
            for j in range(i, len(bit)):
                bit[i] = int(not bit[i])

    print(bit)