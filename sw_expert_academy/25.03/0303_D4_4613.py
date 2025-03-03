'''
D4 4613 러시아 국기 같은 깃발

깃발은 N행 M열로 나뉘어 있고, 각 칸은 흰색, 빨간색, 파란색 중 하나로 칠해져 있음

몇 개의 칸에 있는 색을 다시 칠해 깃발을 러시아 국기처럼 만들려고 함.
1. 위에서 한 줄 이상은 모두 흰색으로 칠해져 있어야함
2. 다음 몇 줄(한 줄 이상)은 모두 파란색이어야함
3. 그 다음 몇 줄(한 줄 이상)은 모두 빨간색이어야 함

새로 칠해야 하는 칸의 개수의 최솟값을 구하는 문제

입력:
T : 테스트케이스 개수
N, M : 두 정수
다음 N개의 줄에 M개의 문자로 이루어진 문자열 주어짐(i번째 줄의 j번째 문자는 깃발에서 i번째 행 j번째 열인 칸의 색 의미)
W는 흰색, B는 파란색, R은 빨간색 의미. 다른 문자는 입력 X
'''

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    flag = [list(input()) for _ in range(N)]
    color = ['W', 'B', 'R']     # 색깔 순서(위에서부터 하얀색, 파란색, 빨간색이 와야하므로)
    
    min_change = N * M      # 바꿔야할 최악의 수로 먼저 설정(최솟값이기 때문에)
    
    all_case = list()
    for i in range(1, N-1):     # 국기의 색이 각각 몇 줄인지 경우의 수
        for j in range(1, N-i):
            all_case.append([i, j, N-j-i])
            
    for i in all_case:          # 구한 경우의 수의 합을 모두 비교
        sub_min = 0
        idx = 0
        for j in range(3):      # 3가지 색을 구별해야함
            for k in range(idx, idx+i[j]):      # 경우의 수에 따른 줄만큼 탐색
                sub_min += (M - flag[k].count(color[j]))        # 그 줄에서 바꿔야할 칸(해당 줄에서 이뤄야할 색이 아닌 칸)만큼 sub_min에 더해줌
            idx += i[j]         # 다음 시작 열 인덱스
        if sub_min < min_change:        # 횟수 비교
            min_change = sub_min
            
    print(f'#{tc} {min_change}')