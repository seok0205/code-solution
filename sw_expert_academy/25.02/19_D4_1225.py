'''
D4 1225 암호생성기

8개 숫자를 입력받고
첫번째 숫자를 1감소한뒤 맨뒤에 모냄
다음 첫번째 수는 2 감소한 뒤 맨 뒤로, 그 다음 첫번째 수는 3을 감소하고 맨 뒤로, 그 다음 수는 4, 그 다음수는 5를 감소
숫자가 감소할 때 0보다 작아지는 경우 0으로 유지, 프로그램 종료
입력받고 암호가 된 상태를 구하는 문제
'''

import sys
sys.stdin = open('tc.txt', 'r')

from collections import deque   # 덱 사용

T = 10

for tc in range(1, T+1):
    tc_num = int(input())
    data = list(map(int, input().split()))

    q = deque()     # 큐 생성

    for i in range(8):  # 먼저 데이터들을 넣음 8개의 숫자 모두
        q.append(data[i])

    while True:
        for i in range(1, 6):   # 1에서 5까지 한사이클
            a = q.popleft()
            a -= i      # 디큐한 수에서 i뺌 (1~5사이)

            if a > 0:       # 뺀 결과가 0보다 크면 다시 인큐
                q.append(a)
            else:           # 0이나 0보다 작으면 0으로 들고 인큐
                a = 0
                q.append(a)
                break    
        if q[-1] == 0:      # 인큐된 숫자가 0이면 while문 중단
            break

    print(f'#{tc_num} {" ".join(list(map(str, q)))}')