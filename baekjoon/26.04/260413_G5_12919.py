'''
12919 G5 A와 B 2

문제 설명:
A와 B로만 이루어진 영단어가 있음.
두 문자열 S, T가 주어질때, S를 T로 바꾸는 게임.
두 가지 연산 가능.

1. 문자열의 뒤에 A추가.
2. 문자열의 뒤에 B를 추가하고 문자열을 뒤집는다.

주어진 조건 이용해 S를 T로 만들 수 있는지 확인.

입력:
첫째 줄 - S (1 <= len(S) <= 49)
둘째 줄 - T (2 <= len(T) <= 50)
(len(S) < len(T))

출력:
바꿀 수 있으면 1, 없으면 0 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

S = input().strip()
T = input().strip()

def change(t):
    if len(t) == len(S):
        return 1 if t == S else 0

    if t[-1] == 'A':
        if change(t[:-1]) == 1:
            return 1
        
    if t[0] == 'B':
        if change(t[1:][::-1]) == 1:
            return 1
    
    return 0

print(change(T))