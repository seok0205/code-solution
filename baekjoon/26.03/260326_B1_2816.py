'''
B1 2816 디지털 티비

문제 설명:
채널 리스트의 순서를 바꾸려고 함.
버튼 4개가 존재.

1. 화살표를 한 칸 아래로 내림. (i -> i+1)
2. 화살표를 위로 한칸 올림. (i -> i-1)
3. 현재 선택한 채널을 한 칸 아래로 내림 (i와 i+1의 위치 바꿈, 화살표는 i+1을 가리키고 있음)
4. 현재 선택한 채널을 위로 한칸 올림 (i와 i-1의 위치 바꿈, 화살표는 i-1 가리키고 있음)

채널리스트 범위를 화살표가 넘어가면 그 명령 무시
채널 리스트 순서 주어질 때, KBS1을 첫번째, KBS2를 두번째로 순서를 바꾸는 방법을 구하는 문제.
방법의 길이는 500보다 작아야 하고, 두 채널 제외한 다른 채널의 순서는 상관 없음.

입력:
채널 수 N (2 <= N <= 100)
다음 N개 줄에는 채널의 이름이 한 줄에 하나씩 주어짐. 채널 이름은 최대 10글자, 알파벳 대문자, 숫자로 이루어짐.
이미 KBS1, KBS2가 가야하는 자리에 존재하는 경우는 안주어짐.

출력:
눌러야 하는 버튼을 순서대로 공백없이 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
for i in range(N):
    channel = input().strip()
    if channel == 'KBS1':
        k1 = i
    elif channel == 'KBS2':
        k2 = i

result = []
idx = 0
while k1 != 0:
    if k1 > idx:
        result.append(1)
        idx += 1
    elif idx == k1:
        if idx-1 == k2:
            k2 += 1
        result.append(4)
        idx -= 1
        k1 -= 1

while k2 != 1:
    if k2 > idx:
        result.append(1)
        idx += 1
    elif idx == k2:
        result.append(4)
        idx -= 1
        k2 -= 1

print(''.join(map(str, result)))