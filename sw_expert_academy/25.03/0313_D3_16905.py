'''
D3 16905 베이비진 게임

0부터 9까지인 숫자 카드 4세트를 섞은 후 6개의 카드를 골랐을 때, 연속인 숫자가
3개 이상이면 run, 같은 숫자가 3개이상이면 triplet이라 함

게임 시작 시 player 1, player 2가 교대로 한 장씩 카드를 가져가며,
6장을 채우기 전전이라도 먼저 run이나 triplet이 되는 사람이 승자

두사람이 가져가게 되는 순서대로 12장의 카드에 대한 정보가 주어졌을 때 승자를
알아내는 문제

만약 무승부면 0출력

입력은 0에서 9사이인 숫자 12개가 주어짐
'''

import sys
sys.stdin = open('tc.txt', 'r')


def find_winner(turn, arr1, arr2):
    arr1.sort()
    arr2.sort()
    sarr1 = list(set(arr1))
    sarr2 = list(set(arr2))
    
    for i in range(turn-1):     # 같은 숫자 3개라면 1
        if arr1[i] == arr1[i+1] == arr1[i+2]:
            return 1
    
    for i in range(len(sarr1)-2):       # 연속된 숫자가 존재한다면 1, 예로 1, 2, 2, 3을 가지고 있다면 위에서는 run을 인지하지 못함. 따라서 set로 겹치는 숫자를 없애 줘야함
        if sarr1[i]+2 == sarr1[i+1]+1 == sarr1[i+2]:
            return 1
        
    for i in range(turn-1):     # 위 2개의 for문과 같은 구조
        if arr2[i] == arr2[i+1] == arr2[i+2]:
            return 2
        
    for i in range(len(sarr2)-2):
        if sarr2[i]+2 == sarr2[i+1]+1 == sarr2[i+2]:
            return 2


def game(turn, winner):     # 턴 횟수와, 승자 번호(아직 승부 판정 안난 경우는 0)
    global result
    
    if winner == 1:     # winner 값이 1, 2중 하나라면 해당 숫자가 결과. 함수 종료.
        result = 1
        return
    
    if winner == 2:
        result = 2
        return

    if turn == 6:
        return
    
    p1.append(card[turn*2])     # 차례가 지날때마다 플레이어 1, 2는 카드를 나눠 가짐
    p2.append(card[turn*2+1])

    if turn >= 2:               # 카드가 3개씩 가지고 있을 때부터 카드에 연속된 숫자나 같은 숫자 3장씩 있는지 확인
        winner = find_winner(turn, p1, p2)
    
    game(turn + 1, winner)      # 다음 턴 진행


T = int(input())

for tc in range(1, T+1):
    card = list(map(int, input().split()))
    
    p1 = []
    p2 = []
    result = 0
    game(0, 0)
    
    print(f'#{tc} {result}')