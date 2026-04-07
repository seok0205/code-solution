'''
S2 1138 한 줄로 서기

문제 설명:
N명의 사람들은 매일 아침 한 줄로 섬.
자리를 마음대로 서지 못하고 오민식의 지시대로 섬.

오민식은 사람들이 줄 서는 위치를 기록해 놓음.
아침에 자기가 기록해 놓은 것과 사람들이 줄을 선 위치가 맞는지 확인.

사람들은 자기보다 큰 사람이 왼쪽에 몇 명 있었는지만을 기억.
N명의 사람이 있고, 사람들의 키는 1부터 N까지 모두 다름.

각 사람들이 기억하는 정보가 주어질 때, 줄을 어떻게 서야 하는지 출력하는 프로그램 작성.

입력:
첫 줄 - 사람수 N. 10보다 작거나 같은 자연수.
둘째 줄 - 키가 1인 사람부터 차례로 자기보다 키가 큰 사람이 왼쪽에 몇명 있었는지 주어짐.
i번째 수는 0보다 크거나같고, N-i보다 작거나 같음. i는 0부터 시작.

출력:
줄을 선 순서대로 키를 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
info = list(map(int, input().split()))
result = [0] * N

for i in range(N):
    cnt = info[i]
    for j in range(N):
        if cnt == 0 and result[j] == 0:
            result[j] = i + 1
            break
        elif result[j] == 0:
            cnt -= 1

print(' '.join(map(str, result)))