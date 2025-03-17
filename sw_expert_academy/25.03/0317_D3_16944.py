'''
D3 16944 병합 정렬

병합 정렬 이용해 오름차순으로 정렬
N개의 정렬 대상을 가진 리스트 L을 분할 할때 L[0:N//2], L[N//2:N]으로 분할
병합 과정에서 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 큰 경우의 수를 출력
정렬이 끝난 리스트 L에서 L[N//2] 원소 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def merge_sort(s, e):       # 병합 정렬 함수
    if s == e - 1:          # 더이상 쪼갤 수 없으면 끝
        return s, e         # 길이 1일때 시작, 끝 반환
    
    mid = (s + e) // 2      # 절반 나누기
    
    left_s, left_e = merge_sort(s, mid)     # 왼쪽 정렬
    right_s, right_e = merge_sort(mid, e)   # 오른쪽 정렬
    
    merge(left_s, left_e, right_s, right_e)
    
    return s, e


def merge(ls, le, rs, re):
    global cnt
    
    l, r = ls, rs       # 왼쪽 배열 제일 작은 원소 인덱스 : l, 오른쪽 배열 제일 작은 원소 : r
    
    if n_lst[le-1] > n_lst[re-1]:       # 왼쪽 마지막 원소가 오른쪽 마지막 원소보다 크면 개수 + 1
        cnt += 1
        
    length = re - ls        # 합치면 만들어지는 배열 길이
    
    result = [0] * length   # 정렬 결과 담을 리스트
    
    idx = 0     # 정렬 결과 배열에 놓을 원소 인덱스 위치
    
    while l < le and r < re:        # 왼쪽 끝과 오른쪽 끝에 도달하기 전까지(다 쓰기 전까지)
        if n_lst[l] < n_lst[r]:     # 왼쪽 원소, 오른쪽 원소 비교 후 오른쪽이 더 크면 왼쪽 원소를 result에 먼저 넣음
            result[idx] = n_lst[l]
            l += 1                  # 왼쪽 원소 사용, 왼쪽의 다음 인덱스
            idx += 1                # result의 다음 인덱스
        else:                       # 왼쪽이 더 크면 반대로
            result[idx] = n_lst[r]
            r += 1                  # 원소하나 쓰고 인덱스 증가
            idx += 1                # result의 다음 인덱스 채우러 ㄱㄱ
            
    while r < re:                   # 왼쪽 or 오른쪽에 원소가 없고, 한쪽에만 남아있는 경우
        result[idx] = n_lst[r]
        r += 1
        idx += 1
        
    while l < le:
        result[idx] = n_lst[l]
        l += 1
        idx += 1
        
    for i in range(length):         # 정렬 결과를 원래 배열에다가 넣어줌
        n_lst[ls + i] = result[i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    n_lst = list(map(int, input().split()))
    
    cnt = 0
    
    merge_sort(0, N)
    
    print(f'#{tc} {n_lst[N//2]} {cnt}')