'''
D3 16586 배열 최소 합

NxN 배열에의 한 줄에서 하나씩 N개의 숫자를 골라 합이 최소가 되도록 하려 함.
세로로 같은 줄의 2개 이상 숫자 고를 수 없음
최소 합을 출력하는 문제
'''


def f(i, N):    # 크기가 N이고 순열을 저장한 p배열에서 p[i]를 결정하는 함수
    global min_v
    if i == N:  #
        s = 0
        for j in range(N):
            s += matrix[j][p[j]]
        if min_v > s :
            min_v = s
    else:
        for j in range(i, N):
            p[i], p[j] = p[j], p[i]
            f(i+1, N)   # i+1자리 결정
            p[i], p[j] = p[j], p[i]

          
# def f(i, N, s):
#     global min_v
#     if i == N:
#         if min_v > s :
#             min_v = s
#         elif min_v < s:
#             return
#     else:
#         for j in range(i, N):
#             p[i], p[j] = p[j], p[i]
#             f(i+1, N, s + matrix[j][p[j]])   # i+1자리 결정
#             p[i], p[j] = p[j], p[i]


T = int(input())

for tc in range(1, T+1):
    N = int(input())
    matrix = [list(map(int, input().split())) for _ in range(N)]
    
    # P[i] : i에서 고른 열 번호
    p = [i for i in range(N)]
    min_v = 10000
    f(0, N)
    print(f"#{tc} {min_v}")