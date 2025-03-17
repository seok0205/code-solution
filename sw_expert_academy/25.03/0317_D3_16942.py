'''
D3 16942 퀵 정렬

퀵 정렬을 구현해 N개의 정수를 정렬해 리스트 A에 넣고, A[N//2]에 저장된 값을 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def partition(left, right):         # pivot 정하고, 퀵 정렬 과정 중 1회 진행 하는 함수
    mid = (left + right) // 2
    pivot = lst[mid]                # 중간값을 pivot 값으로 지정
    lst[left], lst[mid] = lst[mid], lst[left]       # pivot을 첫 자리와 교환시켜줌
    i = left + 1                    # 비교할 값은 lst[0](pivot 자리) 이후부터
    j = right
    
    while i <= j:           # i와 j가 교차하기 전까지
        while i <= j and lst[i] <= pivot:   # 만약 pivot보다 왼쪽값들이 작으면 계속 인덱스 증가하다가 큰 값이 나오면 그 인덱스에서 멈춤.
            i += 1
        while i <= j and lst[j] >= pivot:   # 오른쪽 값들도 pivot과 비교후, 작은 값이 나오면 그 인덱스에서 정지
            j -= 1
        if i < j:                           # 멈춘 인덱스들은 조건이 상반되므로 자리를 교환해주면 맞는 조건을 가지게 됨
            lst[i], lst[j] = lst[j], lst[i]
    
    lst[left], lst[j] = lst[j], lst[left]       # j는 처음 mid의 값일 것이고, lst[left]는 맨 처음 값(현재 pivot자리) 이므로 pivot값을 원래 있던 위치인 중간으로 맞바꾸어줌
    return j


def quick_sort(left, right):        # 퀵 정렬 함수
    if left < right:
        pivot = partition(left, right)
        
        quick_sort(left, pivot - 1)
        quick_sort(pivot + 1, right)


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    lst = list(map(int, input().split()))
    
    quick_sort(0, len(lst)-1)
    result = lst[N//2]              # 원하는 출력 값은 정렬한 상태의 N//2 인덱스에 위치한 값
    
    print(f'#{tc} {result}')