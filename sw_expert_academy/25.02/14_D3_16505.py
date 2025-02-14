'''
D3 16505 종이붙이기

10x20, 20x20 종이가 여러장 있음
바닥에 이 종이들로 빈틈없이 붙일 방법 찾음

10의 배수인 N이 주어질때, 종이를 붙이는 모든 경우 찾으려면 테이프로 만든 표시영역을 몇 개 만들어야 하는지 계산
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input()) // 10
    result_lst = [0] * (N + 1)
    result_lst[1] = 1
    result_lst[2] = 3
    for i in range(3, N + 1):
        result_lst[i] = (result_lst[i-2] * 2) + result_lst[i-1]

    print(f'#{tc} {result_lst[-1]}')
