'''
S1 1522 문자열 교환

문제 설명:
a, b로만 이루어진 문자열이 주어질 때,
a를 모두 연속으로 만들기 위해서 필요한 교환의 횟수를 최소로 하는 프로그램 작성.
이 문자열은 원형, 처음과 끝은 서로 인접함.
예로, aabbaaabaaba가 주어질때, 2번의 교환이면 a를 모두 연속으로 만들 수 있음.

입력:
첫째 줄 - 문자열 (최대 1,000자)

출력:
교환 횟수의 최솟값.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

word = input().strip()
n = len(word)
a_cnt = word.count('a')

word = word + word[:a_cnt-1]
result = float('inf')

for i in range(n):
    window = word[i:i+a_cnt]
    swap = window.count('b')

    if swap < result:
        result = swap

print(result)