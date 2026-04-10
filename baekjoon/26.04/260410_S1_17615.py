'''
S1 17615 볼 모으기

문제 설명:
빨간색 볼과 파란색 볼이 일직선상에 놓여있음.
볼을 옮겨서 같은 색 볼끼리 인접하게 놓이도록 하려고 함.

1. 바로 옆에 다른 색깔의 볼이 있으면 그 볼을 모두 뛰어 넘어 옮길수 있음.
즉, 빨간색 볼은 옆에 있는 파란색볼 무더기를 한번에 뛰어 넘어 옮길 수 있음.
유사하게, 파란색 볼은 빨간색 볼 무더기를 한번에 뛰어 넘을 수 있음.

2. 옮길 수 있는 볼의 색깔은 한 가지. 즉, 처음에 빨간색 옮겼으면 빨간색만 옮길 수 있음.
파란색을 처음에 옮기면 그 뒤로 파란색만 옮길 수 있음.

일직선상에 놓인 볼들에 관한 정보가 주어질 때, 규칙에 따라 볼을 이동하여 같은 색끼리 모으되 최소 이동횟수를 찾는 문제.

입력:
첫째 줄 - 볼 개수 N (1 <= N <= 500,000)
다음 줄 - 볼의 색깔 R, B로 이루어진 문자열. 만약 한가지 문자로만 구성되어 있으면 0출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input())
balls = input().strip()

is_red = balls.count('R')
is_blue = balls.count('B')

if is_red == 0 or is_blue == 0:
    print(0)
else:
    result = []

    is_red_left = balls.lstrip('R')
    result.append(is_red_left.count('R'))

    is_red_right = balls.rstrip('R')
    result.append(is_red_right.count('R'))

    is_blue_left = balls.lstrip('B')
    result.append(is_blue_left.count('B'))

    is_blue_right = balls.rstrip('B')
    result.append(is_blue_right.count('B'))

    print(min(result))