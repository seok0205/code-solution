'''
S3 9461 파도반 수열

문제 설명:
삼각형이 나선 모양으로 놓여져 있음.
첫 삼각형은 정삼각형, 변은 1. 그 다음은 같은 과정으로 정삼각형 계속 추가.
나선에서 가장 긴 변의 길이를 k라할때, 그변에 길이가 k가 정삼각형을 추가.
P(N)은 나선에 있는 정삼각형의 변의 길이. P(1)부터 P(10)까지 첫 10개 숫자는
1, 1, 1, 2, 2, 3, 4, 5, 7, 9.
N이 주어질때, P(N)을 구하는 프로그램을 작성하시오.

입력:
첫째 줄에 T,
각 TC는 한줄이고, N이 주어짐(1~100)

출력:
각 TC 마다 P(N) 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
print = sys.stdout.write

T = int(input())
triangles = [1, 1, 1, 2, 2]

for _ in range(T):
    N = int(input())

    if len(triangles) < N:
        cnt = len(triangles) - 1
        while True:
            next_tri = triangles[cnt] + triangles[cnt-4]
            triangles.append(next_tri)
            cnt += 1
            if cnt == N:
                break
    
    print(str(triangles[N-1]) + '\n')
