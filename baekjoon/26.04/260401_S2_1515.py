'''
S2 1515 수 이어 쓰기

문제 설명:
세준이는 1부터 N까지 모든 수를 차례대로 공백없이 한줄에 다 씀.
세준이가 저녁 먹으러 간 사이에 다솜이는 세준이가 쓴 수에서 마음에 든 몇 개 숫자를 지웠음.
세준이는 수를 방금 전과 똑같이 쓰기로 함.
N이 기억이 안남.
남은 수를 이어 붙인 수가 주어질 때, N의 최솟값을 구하는 문제.
아무것도 지우지 않을 수도 있음.

입력:
첫째 줄에 남은 수를 이어 붙인 수가 주어짐. 최대 3000자리.

출력:
가능한 N중에 최솟값 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

from collections import deque
nums = deque(list(input().strip()))

result = 0
while nums:
    result += 1

    result_str = list(str(result))

    for i in result_str:
        if nums and i == nums[0]:
            nums.popleft()

print(result)