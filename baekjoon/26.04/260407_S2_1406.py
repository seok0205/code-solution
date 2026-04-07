'''
S2 1406 에디터

문제 설명:
간단한 에디터 구현하려 함.
영엇 소문자만 기록할 수 있는 편집기. 최대 600,000자까지 입력가능.

이 편집기엔 '커서'라는 것이 있음.
커서는 문장의 맨 앞(첫 번째 문자의 왼쪽), 문장의 맨 뒤(마지막 문자의 오른쪽), 또는 문장 중간 임의의 곳(모든 연속된 두 문자 사이)에 위치 가능.

길이가 L인 문자열이 현재 편집기에 입력되어 있으면, 커서가 위치할 수 있는 곳은 L+1가지 경우가 있음.

L - 커서를 왼쪽으로 한 칸 옮김(커서가 문장의 맨 앞이면 무시)
D - 커서를 오른쪽으로 한칸 옮김(커서가 맨뒤면 무시)
B - 커서 왼쪽 문자 삭제(커서 문장 맨 앞이면 무시). 삭제로 인해 커서는 한칸 왼쪽 이동한 것처럼 나타나지만 실제로 커서의 오른쪽에 있던 문자는 그대로.
P $ - $라는 문자를 왼쪽에 추가.

모든 명령어 실행하고 편집기에 입력된 남은 문자열 출력.
단, 명령어 수행되기 전에 커서는 문장의 맨 뒤에 위치.

입력:
첫째 줄 - 문자열 주어짐. 길이가 N, 영어 소문자로만 되어있음. 길이는 100,000을 넘지 않음.
둘째 줄 - 입력할 명령어의 개수를 나타내는 정수 M(1 <= M <= 500,000)이 주어짐.
셋째 줄부터 M개의 줄에 걸쳐 입력할 명령어가 순서대로 주어짐.
명령어는 위 네 가지 중 하나의 형태로만 주어짐.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

from collections import deque

left = list(input().strip())
right = deque()
M = int(input())

for _ in range(M):
    data = input().strip().split()
    command = data[0]

    if len(data) > 1:
        spell = data[1]
    
    if command == 'L' and left:
        a = left.pop()
        right.appendleft(a)
    elif command == 'D' and right:
        a = right.popleft()
        left.append(a)
    elif command == 'B' and left:
        left.pop()
    elif command == 'P':
        left.append(spell)

print(''.join(map(str, left + list(right))))