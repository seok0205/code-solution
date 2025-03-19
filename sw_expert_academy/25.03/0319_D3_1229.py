'''
D3 1229 암호문2

0 ~ 999999 사이의 수를 나열해 만든 암호문이 있음. 급히 수정해야함
이 암호문은 특수 제작된 처리기로만 수정 가능. 2개의 기능이 존재

1. I x,y,s : 앞에서부터 x의 위치 바로 다음에 y개의 숫자 삽입. s는 덧붙일 숫자들.
2. D x,y : 앞에서부터 x의 위치 바로 다음부터 y개의 숫자를 삭제.

입력:
첫줄 - 원본 암호문의 길이 N(100 <= N <= 200 정수)
두줄 - 원본 암호문
세줄 - 명령어의 개수(10 <= N <= 20 정수)
네줄 - 명령어
'''

import sys
sys.stdin = open('tc.txt', 'r')

for tc in range(1, 11):
    N = int(input())
    code = list(map(int, input().split()))
    c_num = int(input())
    command = list(map(str, input().split()))
    
    for i in range(len(command)-2):
        if command[i] == 'I':
            pass
        elif command[i] == 'D':
            pass