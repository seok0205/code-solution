'''
S5 7568 덩치(재풀이)

문제 설명:
어떤 사람 키, 몸무게를 (x, y) 형태로 표현.

만약 (x1, y1), (x2, y2)가 있따면 키, 몸무게 모두 상대방 보다 커야 덩치가 크다고 할 수 있음.

한가지만 작아도 덩치가 누가 더 크다고 할 수 없음.

N명의 집단에서 덩치 등수는 자신보다 더 큰 덩치의 사람 수로만 주어짐.

학생 N 명의 몸무게, 키가 담긴 입력을 받아 각 사람의 등수를 계산해 출력.

입력:
첫 줄 - N(2 <= N <= 50)
N개의 줄 - 각 사람의 몸무게, 키를 나타내는 정수 x, y 공백을 두고 입력.

출력:
입력에 나열된 사람의 덩치 등수를 구해서 첫줄에 출력. 각 덩치 등수는 공백문자로 분리.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

N = int(input().strip())
records = []
result = [0] * N
for i in range(N):
    weight, height = map(int, input().split())
    records.append((weight, height))

for i in range(N):
    temp = 0
    for j in range(N):
        if i == j:
            continue

        if records[i][0] < records[j][0] and records[i][1] < records[j][1]:
            temp += 1

    result[i] = temp + 1

print(' '.join(map(str, result)))