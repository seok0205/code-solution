'''
D4 3143 가장 빠른 문자열 타이핑

문자를 타이핑하려고 함. 한 글자씩 타이핑 한다면 A의 길이만큼 키를 눌러야 함
문자열 B가 저장되어 있어 키를 한번 누른 것으로 B전체를 타이핑 할 수 있음
이미 타이핑 한 글자 지우는 건 안됨

A, B가 주어지면 A 전체 타이핑하기위해 키를 눌러야 하는 최솟값 구하는 문제
'''

T = int(input())

for tc in range(1, T+1):
    A, B = map(str, input().split())
    result = len(A)     # 겹치는 글자 없으면 길이가 타이핑 횟수
    used = list()       # 이미 참조한 인덱스

    for i in range(len(A)-len(B)+1):        # A의 글자를 순회하며
        if i not in used and A[i] == B[0]:      # 참조하지 않은 글자고 B의 첫글자와 같으면
            num = list()
            for j in range(len(B)):
                num.append(i+j)     # 현재 확인하고 있는 글자들을 num리스트에 추가
                if A[i+j] != B[j]:      # 다르면 반복문 탈출
                    break
            else:       # 만약 모두 확인하고 일치하는 문자열인게 확인되었으면
                used.extend(num)        # 참조한 인덱스 리스트에 추가
                result = result - len(B) + 1        # 그리고 B를 치면 B길이 -1만큼 타이핑 횟수 줄인다는 뜻

    print(f'#{tc} {result}')

'''
패턴 매칭 활용 풀이

T = int(input())

for tc in range(1, T + 1):
    A, B = input().split()
    i = 0
    N = len(A)
    M = len(B)
    pattern_count = N
    while i + M - 1 < N:
        if A[i] == B[0]:
            if A[i: i + M] == B:
                i = i + M
                pattern_count -= (M - 1)
            else :
                i += 1
        else:
            i += 1
    print(f"#{tc} {pattern_count}")
'''