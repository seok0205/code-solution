'''
N개의 숫자로 구성된 숫자열 A, M개의 숫자로 구성된 숫자열 B.
A, B를 자유롭게 움직여서 숫자들이 서로 마주보는 위치를 변경할 수 있음.
단, 더 긴 쪽의 양끝을 벗어나서는 안됨.
서로 마주보는 숫자들을 곱한 뒤 모두 더할 때 최댓값을 구하라.

제한 사항:
N, M은 3 이상 20 이하.

입력:
첫 줄에 N, M
두번째 줄에 A
세번째 줄에 B

출력:
#t로 시작, 공백을 한 칸 두고 정답 출력.
'''
T = int(input())

for t_c in range(1, T + 1):
    N, M = map(int,input().split())
    A = list(map(int, input().split()))
    B = list(map(int, input().split()))

    num = 0

    if N > M:
        for i in range(N-M+1):
            total = 0
            for j in range(M):
                total += A[i+j] * B[j]
            if total > num:
                num = total
    else:
        for i in range(M-N+1):
            total = 0
            for j in range(N):
                total += A[j] * B[i+j]
            if total > num:
                num = total
    print('#%d %d' %(t_c, num))