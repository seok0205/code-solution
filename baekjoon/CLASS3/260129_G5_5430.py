'''
G5 5430 AC

문제 설명:
새로운 언어 AC 만듦.
AC는 정수 배열에 연산을 하기 위해 만든 언어.
이 언어에는 함수 R(뒤집기), D(버리기)가 있음.
함수 R은 배열에 있는 수의 순서를 뒤집는 함수. D는 첫번째 수를 버리는 함수.
배열이 있는데 D를 사용하면 에러 발생.
함수는 조합해서 한 번에 사용 가능. 예로, AB는 A를 수행한 다음 바로 이어서 B를 수행하는 함수.
예로, RDD는 배열을 뒤집은 다음 처음 두수를 버리는 함수.
배열 초기값과 수행할 함수가 주어질때, 최종 결과를 구하는 프로그램 작성

입력:
첫 줄 - T (최대 100)
TC의 첫 줄 - 수행할 함수 p (길이는 1~100,000)
다음 줄에 배열에 들어있는 수의 개수 n (0~100,000)
다음 줄에 [x1, x2 ... xn] 형태로 배열에 들어있는 정수 주어짐 (1~100)
전체 TC에 주어지는 p의 길이의 합과 n의 합은 70만을 넘지 않음

출력:
각 TC에 대해, 입력으로 주어진 정수 배열에 함수를 수행한 결과를 출력함.
만약, 에러가 발생한 경우에는 error를 출력.
'''

import sys
from collections import deque
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

T = int(input())

for _ in range(T):
    func = input().strip()
    n = int(input().strip())
    raw_nums = input().strip()
    nums = deque()
    if n > 0:
        nums = deque(raw_nums[1:-1].split(','))

    reverse = False
    error = False
    
    for command in func:
        if command == 'R':
            reverse = not reverse
        elif command == 'D':
            if len(nums) == 0:
                output('error' + '\n')
                error = True
                break

            if reverse:
                nums.pop()
            else:
                nums.popleft()
    
    if not error:
        if reverse:
            nums.reverse()

        output('[' + ','.join(nums) + ']\n')