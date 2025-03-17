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

# import sys
# sys.stdin = open('tc.txt', 'r')


def binary_search(left, right, target):
    global x
    
    if left > right:    # 왼쪽 끝이 오른쪽 끝 역전하면 종료
        return
    
    mid = n_lst[(left+right)//2]        # 중간값
    
    if mid == target:       # 찾던 값과 같으면 x 에 대입
        x = mid
        return
    
    if target < mid:        # 만약 찾던 값보다 중간값이 크면 왼쪽, 아니면 오른쪽 탐색
        search.append(1)
        binary_search(left, (left+right)//2-1, target)
    else:
        search.append(0)
        binary_search((left+right)//2+1, right, target)


T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    n_lst = list(map(int, input().split()))
    m_lst = list(map(int, input().split()))
    n_lst.sort()
    
    result = 0
    
    
    for i in m_lst:
        search = []     # 번갈아서 탐색하는지 확인
        x = 0
        
        binary_search(0, N-1, i)
        
        if x == i:      # 탐색해서 값을 찾았다면 번갈아서 탐색했는지 확인
            for i in range(len(search)-1):      # 0아니면 1이라서 다음 값과 같으면 break
                if search[i] == search[i+1]:
                    break
            else:       # for문 break없이 수행했다면 조건 만족, result 1 증가
                result += 1
    
    print(f'#{tc} {result}')