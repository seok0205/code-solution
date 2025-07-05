'''
S1 1629 곱셈

자연수 A를 B번 곱한 수를 알아보려 함.
단 구하려는 수가 매우 커질 수 있어서 이를 C로 나눈 나머지를 구하는 프로그램 작성.

입력:
A, B, C : 공백을 두고 순서대로 주어짐. 2,147,483,647 이하의 자연수들임

출력:
첫째 줄에 A를 B번 곱한 수를 C로 나눈 나머지 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

a, b, c = map(int, input().split())

def find_r(a, b):       # 파이썬 함수 pow()으로 대체 가능
    if b == 1:
        return a % c
    else:
        s = find_r(a, b//2)
        
        if b % 2 == 0:      # 분배법칙. B가 짝수면 똑같이 나누어서 나머지 구하고, 홀수면 A를 따로 곱해주고 나머지 구함
            return (s * s) % c
        else:
            return ((s * s) % c) * a % c
        
result = find_r(a, b)
print(result)