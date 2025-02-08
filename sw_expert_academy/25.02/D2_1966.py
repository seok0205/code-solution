'''
D2 1966 숫자를 정렬하자

주어진 N길이 숫자열을 오름차순으로 정렬

제한 사항:
5 <= N <= 50

입력:
N = 숫자 개수
N_lst = 정렬할 숫자
'''

def bubblesort(lst):        # 버블 정렬
    for _ in range(len(lst)-1):     # 맨앞에 있는 원소를 다음 원소와 비교해 값이 큰 것을 오른쪽으로 옮김
        for i in range(len(lst)-1):     # 이 과정을 정렬할 리스트의 길이만큼 반복하면 결국 정렬된 리스트 반환
            if lst[i] > lst[i+1]:
                lst[i], lst[i+1] = lst[i+1], lst[i]
    
    return lst

def countingsort(lst):      # 카운팅 정렬
    temp = [0 for _ in range(len(lst))]
    cnt = [0 for _ in range(max(lst)+1)]
    
    for i in range(len(lst)):       # lst에 담긴 값과 같은 cnt의 인덱스에 1 증가. cnt의 인덱스가 lst의 값이 됨
        cnt[lst[i]] += 1
    
    for i in range(1, len(cnt)):        # cnt에 담긴 원소들중 이전 원소와 현재 원소의 차가 현재 인덱스와 같은 lst의 값의 갯수
        cnt[i] = cnt[i-1] + cnt[i]
    
    for i in range(len(temp)-1, -1, -1):    # 정렬한 수를 담은 temp의 끝에서부터 일정 숫자 하나가 담길때마다 해당 숫자와 같은 cnt 인덱스의 값이 1씩 줄어듬.
        cnt[lst[i]] -= 1
        temp[cnt[lst[i]]] = lst[i]
    
    return temp

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_lst = list(map(int, input().split()))
    
    result = N_lst
    result.sort()   # 정렬
    
    # result = bubblesort(N_lst)
    # result = countingsort(N_lst)
    
    for i in range(N):      # 출력문
        if i == 0:
            print(f'#{tc} {result[i]}', end=' ')
        elif i == N-1:
            print(f'{result[i]}')
        else:
            print(f'{result[i]}', end=' ')