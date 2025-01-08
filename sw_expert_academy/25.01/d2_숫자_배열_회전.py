'''
NxN 행렬이 주어질 때, 시계 방향으로 90도, 180도, 270도 회전한 모양을 출력하라.

제한 사항 : 3 <= N <= 7
'''
T = int(input())

for test_case in range(1, T + 1):
    N = int(input())
    num = [[] for i in range(N)]

    for i in range(N):
        num[i] = list(map(int, input().split()))

    result = [[0 for i in range(3)] for i in range(N)]

    for i in range(N):
        result[i][0] = ''.join([str(num[j][i]) for j in range(N)])[::-1]
        result[i][1] = ''.join([str(num[N-i-1][N-j-1]) for j in range(N)])
        result[i][2] = ''.join([str(num[j][N-i-1]) for j in range(N)])

    print(f"#{test_case}")
    for i in range(N):
        print(''.join(str(result[i][j])+" " for j in range(3)))