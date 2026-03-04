'''
S1 9465 스티커

문제 설명:
스티커 2n개 구매. 스티커는 2행 n열로 배치된 상태.
스티커 한 장을 떼면, 그 스티커와 변을 공유하는 스티커는 찢어져 사용못함.
즉, 뗀 스티커의 왼쪽, 오른쪽, 위, 아래 스티커는 사용을 못함.

각 스티커에 점수를 매기고, 점수의 합이 최대가 되게 스티커를 떼어내려 함.
뗄 수 있는 스티커의 최댓값을 구하는 프로그램 작성.

입력:
첫 줄 - T(테스트 케이스 개수)
테스트 케이스의 첫 줄 - n (1 <= n <= 100,000)
다음 두 줄에 n개의 정수, 각 정수는 그위치에 해당하는 스티커 점수.
연속하는 두 정수 사이에는 공백 하나. 점수는 0보다 크거나 같고, 100보다 작거나 같은 정수.
'''

import sys

# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
output = sys.stdout.write

T = int(input())

for _ in range(T):
    n = int(input())
    sticker = []
    
    for _ in range(2):
        line = list(map(int, input().split()))
        sticker.append(line)
    
    visit = [[0] * n for _ in range(2)]

    for i in range(n):
        if i == 0:
            visit[0][0], visit[1][0] = sticker[0][0], sticker[1][0]
        elif i == 1:
            visit[0][1] = sticker[1][0] + sticker[0][1]
            visit[1][1] = sticker[0][0] + sticker[1][1]
        else:
            visit[0][i] = max(sticker[0][i] + visit[1][i-1], sticker[0][i] + visit[1][i-2])
            visit[1][i] = max(sticker[1][i] + visit[0][i-1], sticker[1][i] + visit[0][i-2])
        
    answer = max(visit[0][-1], visit[1][-1])
    output(str(answer) + '\n')