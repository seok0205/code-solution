'''
1244 S4 스위치 켜고 끄기(재풀이)

문제 설명:
1부터 연속적으로 번호가 있는 스위치가 있음.
켜져 있거나 꺼져있는 상태. 1이 켜진거 0이 꺼진거
학생들이 스위치를 받음. 자신의 성별과 받은 수에 따라 스위치조작.

남학생은 스위치 번호가 자기가 받은 수의 배수면, 스위치 상태 바꿈.
즉, 스위치 켜져있으면 끄고, 켜져있으면 끔.

여학생은 자기가 받은 수와 같은 번호가 붙은 스위치를 중심으로 좌우가 대칭이면서 가장 많은 스위치를 포함하는 구간 찾아서, 그 구간의 스위치 모두 바꿈.
이때 구간에 속한 스위치 개수는 항상 홀수.

입력으로 스위치의 처음상태 주어지고, 각 학생의 성별, 받은 수가 주어짐.
학생들은 입력되는 순서대로 자신의 성별과 받은 수에 따라 스위치 상태 바꿈.
마지막 상태를 구하는 문제.

입력:
첫 줄 - 스위치 개수 (100이하 양의 정수)
둘째 줄 - 스위치 상태(공백 두고 1 혹은 0)
셋째 줄 - 학생 수 (100이하 양의 정수)
넷째줄 부터 마지막 줄 - 성별, 받은 수(1 남, 2 여, 스위치 개수 이하의 양의 정수, 세 개의 수가 공백 두고 입력)

출력:
1번에서 시작해서 마지막 스위치까지 한줄에 20개 출력.
만약 21번이 있으면 이건 둘째 줄부터 표시. 공백 두고 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
switches = [0] + list(map(int, input().split()))
M = int(input())

for _ in range(M):
    sex, num = map(int, input().split())

    if sex == 1:
        for i in range(1, N+1):
            if i % num == 0:
                switches[i] = 0 if switches[i] else 1
    elif sex == 2:
        switches[num] = 0 if switches[num] else 1
        idx = 1
        while True:
            if num - idx < 1 or num + idx > N:
                break
            if switches[num-idx] == switches[num+idx]:
                switches[num-idx] = 0 if switches[num-idx] else 1
                switches[num+idx] = 0 if switches[num+idx] else 1
            else:
                break
            
            idx += 1

for i in range(1, N+1, 20):
    print(' '.join(map(str, switches[i:i+20])))