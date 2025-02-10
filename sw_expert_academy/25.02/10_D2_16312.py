"""
D2 16312 이진 탐색

A, B 두 명 중 누가 이진 탐색을 더 적게 했는가 구하는 문제

입력:
1 <= T <= 50
P = 탐색할 수 범위
Pa, Pb = A, B가 찾아야 할 각각 숫자
"""

def binary_search(num, key_num):
    """
    이진 탐색 함수

    num : 이진 탐색할 범위 끝 값.(이 문제는 시작점이 1로 고정)
    key_num : 찾으려는 목표값
    """
    turn = 0
    start = 1
    end = num
    while True:
        mid = (end + start) // 2    # 중간 값 구하고
        if mid == key_num:      # 목표값과 같으면
            turn += 1       # 탐색 횟수 1증가 후 종료
            break
        elif mid < key_num:     # 목표값보다 작으면
            turn += 1
            start = mid     # 시작점을 중간값과 똑같이 만들어 왼쪽 부분 재탐색
        else:       # 목표값보다 크면
            turn += 1
            end = mid       # 끝점을 중간값과 똑같이 만들어 오른쪽 부분 재탐색
    return turn     # 탐색 횟수 반환


T = int(input())

for tc in range(1, T+1):
    P, aP, bP = list(map(int, input().split()))

    A = binary_search(P, aP)
    B = binary_search(P, bP)

    if A < B:       # 탐색 횟수가 B가 더 크면 A가 승리
        print(f'#{tc} A')
    elif B < A:     # 탐색 횟수 A가 더 크면 B가 승리
        print(f'#{tc} B')
    else:           # 같으면 0 출력
        print(f'#{tc} 0')

