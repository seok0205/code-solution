'''
모의 SW 역량테스트 5658 보물상자 비밀번호

각 변에 16진수 숫자(0~F)가 적힌 보물상자 존재
보물 상자 뚜껑은 시계방향으로 돌릴 수 있고, 한 번 돌릴 때마다 숫자가 시계방향으로 한 칸씩 회전

각 변에는 동일한 개수의 숫자가 있고 ,시계방향 순으로 높은 자리 숫자에 해당하며 하나의 수 나타냄
보물상자에는 자물쇠가 걸려있는데, 이 자물쇠의 비밀번호는 보물 상자에 적힌 숫자로 만들 수 있는 모든 수 중, K번째로 큰 수를
10진수로 만든 수다.

N개의 숫자가 입력으로 주어질 때, 보물상자의 비밀 번호를 출력하는 프로그램 만들기
(서로 다른 회전 횟수에서 동이한 수가 중복으로 생성될 수 있음. 크기 순서를 셀 때 같은 순를 중복으로 세지 않도록 주의)
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, K = map(int, input().split())
    numbers = list(input())
    num_list = []
    
    for i in range(N//4):           # 변에 있는 숫자 개수만큼 회전하면 원상태의 변들과 같은상태로 돌아감
        for k in range(0, N, N//4):         # 그 상태의 변들을 10진수로 만들어 리스트에 중복되지않게 추가
            num = ''
            for a in range(N//4):
                num += numbers[(k+i+a)%N]
            if int(num, 16) not in num_list:
                num_list.append(int(num, 16))
    
    num_list.sort(reverse=True)     # 큰 수부터 나열
    
    print(f'#{tc} {num_list[K-1]}')     # K번째 큰수 출력