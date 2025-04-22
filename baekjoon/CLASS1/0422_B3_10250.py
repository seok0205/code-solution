'''
B3 10250 ACM 호텔

설문조사 결과대로 호텔 정문으로부터 걷는 거리가 가장 짧도록 방을 배정하는 프로그램을 작성.
호텔은 직사각형, 각 층에 W개의 방이 있는 H층의 건물.
엘리베이터는 가장 왼쪽에 존재. 호텔 정문은 일층 엘리베이터 바로 앞에 있음. 정문에서 엘리베이터 까지 거리는 무시.
모든 인접한 두 방사이의 거리는 같은 거리(1), 호텔 정면 쪽에만 방이있다고 가정.
방번호는 YXX, YYXX 형태. YY는 층수, XX는 엘리베이터에서부터 세었을 때 번호.

N번째로 도착한 손님에게 배정될 방 번호 계산.
첫손님은 101호, 두번째 손님은 201호.
H = 6 이므로 10번째 손님은 402호 배정.

입력:
T개의 테스트 데이터
H, W, N : 호텔의 층 수, 각 층의 방 수, 몇번째 손님인지.

출력:
N번째 손님에게 배정되어야 하는 방 번호 출력
'''

import sys
sys.stdin = open('tc.txt', 'r')

T = int(input())

for _ in range(T):
    H, W, N = map(int, input().split())

    cnt = 0
    result = 0

    for i in range(1, W):
        for j in range(H, 0, -1):
            cnt += 1
            if cnt == N:
                if i < 10:
                    result = str(H-j+1) + '0' + str(i)
                else:
                    result = str(H-j+1) + str(i)
                break
        if result:
            break

    print(result)