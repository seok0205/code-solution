'''
B3 5073 삼각형과 세 변

문제 설명:
삼각형의 세 변의 길이가 주어질 때 변의 길이에 따라 다음과 같이 정의.

1. Equilateral : 세 변의 길이가 모두 같은 경우
2. Isosceles : 두 변의 길이만 같은 경우
3. Scalene : 세 변의 길이가 모두 다른 경우

단 삼각형 조건을 만족 못하면 "Invalid" 출력.
예로 6, 3, 2는 가장 긴 변의 길이보다 두 변의 길이의 합이 길지 않아서 삼각형 조건을 만족하지 못한다. 세 변의 길이가 주어질 때, 위 정의에 따른 결과 출력.

입력:
각 줄에는 1,000을 넘지 않는 양의 정수 3개가 입력.
마지막 줄은 0 0 0 이며 계산하지 않는다.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

while True:
    a, b, c = map(int, input().split())

    if a == 0 and b == 0 and c == 0:
        break

    max_length = max(a, b, c)

    if max_length >= a + b + c - max_length:
        print('Invalid')
    else:
        if a == b and b == c:
            print('Equilateral')
        elif a == b or b == c or a == c:
            print('Isosceles')
        else:
            print('Scalene')

