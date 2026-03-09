'''
G5 2096 내려가기

문제 설명:
N줄에 0 이상 9 이하의 숫자가 세 개씩 적혀 있다. 내려가기 게임을 하고 있는데, 이 게임은 첫 줄에서 시작해서 마지막 줄에서 끝나게 되는 놀이이다.

먼저 처음에 적혀 있는 세 개의 숫자 중에서 하나를 골라서 시작하게 된다. 그리고 다음 줄로 내려가는데, 다음 줄로 내려갈 때에는 다음과 같은 제약 조건이 있다. 바로 아래의 수로 넘어가거나, 아니면 바로 아래의 수와 붙어 있는 수로만 이동할 수 있다는 것이다.

숫자표가 주어져 있을 때, 얻을 수 있는 최대 점수, 최소 점수를 구하는 프로그램을 작성하시오. 점수는 원룡이가 위치한 곳의 수의 합.

입력:
첫째 줄 - N (1 <= N <= 100,000)
다음 N개의 줄에는 숫자가 세 개씩 주어짐. (0, 1, 2, 3, 4, 5, 6, 7, 8, 9 중 하나)
'''

import sys
sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

N = int(input())

max_chart = [0, 0, 0]

for i in range(N):
    a, b, c = map(int, input().split())

    max_chart[0], max_chart[1], max_chart[2] = max(max_chart[0] + a, max_chart[1] + a), max(max_chart[0] + b, max_chart[1] + b, max_chart[2] + b), max(max_chart[1] + c, max_chart[2] + c)

    if i == 0:
        min_chart = [a, b, c]
    else:
        min_chart[0], min_chart[1], min_chart[2] = min(min_chart[0] + a, min_chart[1] + a), min(min_chart[0] + b, min_chart[1] + b, min_chart[2] + b), min(min_chart[1] + c, min_chart[2] + c)

output(str(max(max_chart)) + ' ' + str(min(min_chart)))