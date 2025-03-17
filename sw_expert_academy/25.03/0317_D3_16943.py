'''
D3 16943 이진 탐색

서로 다른 정수 N개가 주어지면 정렬한 상태로 리스트 A에 저장
다음 리스트 B에 저장된 M개의 정수에 대해 A에 들어있는 수인지 이진 탐색으로 알려고함 

전체 탐색 구간의 시작과 끝 인덱스를 l, r이라 하면, 중심 원소의 인덱스 m=(l+r)//2 이고,
이진 탐색의 왼쪽 구간은 l부터 m-1, 오른쪽 구간은 m+1 부터 r

이때 B에 속한 어떤 수가 A에 들어있으면서, 동시에 탐색 과정에서 양쪽구간을 번갈아 선택하게 되는
숫자의 개수를 알아보려 함

m에 찾는 원소가 있는 경우 방향 따지지 않음. M개의 정수 중 조건을 만족하는 정수의 개수를 알아내는 문제
'''

import sys
sys.stdin = open('tc.txt', 'r')


def binary_search(left, right):
    global result
    
    mid = n_lst[(left+right)//2]
    
    if mid in m_lst:
        m_lst.remove(mid)
        result += 1
    
    if left >= right:
        return
    
    binary_search(left, (left+right)//2-1)
    binary_search((left+right)//2+1, right)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    n_lst = list(map(int, input().split()))
    m_lst = list(map(int, input().split()))
    
    result = 0
    
    binary_search(0, N-1)
    
    print(f'#{tc} {result}')