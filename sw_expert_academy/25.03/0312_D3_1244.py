'''
D3 1244 최대 상금

주어진 숫자판들 중에 두 개를 선택해서 정해진 횟수 만큼 서로의 자리를 위치 교환이 가능함

예로 32888 이 주어지고 교환 횟수가 2라고하면 32888 -> 82838 -> 88832로 바꿀 수 있음

숫자판의 오른쪽 끝이 1원이고 왼쪽으로 한칸씩 갈때마다 10의 배수로 커짐
동일한 위치의 교환이 중복되어도 됨. 반드시 횟수를 채워야 함

정해진 횟수만큼 숫자판 교환 시 받을 수 있는 가장 큰 금액 출력 
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def change_number(num, cnt):
    global max_money
    
    if cnt == int(change):              # 만약 횟수를 다채우면 최대 상금과 비교 후 더 높은 값으로 대체
        if int(num) > max_money:
            max_money = int(num)
        return
    
    num = list(num)                     # 받은 숫자 리스트화
    for i in range(len(num)):           # 모든 경우의 수 검색하면서
        for j in range(i+1, len(num)):
            num[i], num[j] = num[j], num[i]         # 자릿수 서로 바꿔줌
            if (''.join(num), cnt) not in num_used:     # 만약 해당 횟수에서 쓰지않은, 처음나온 숫자라면
                num_used.append((''.join(num), cnt))    # 사용한 리스트에 추가해주고,
                change_number(''.join(num), cnt + 1)    # 재귀 호출
            num[i], num[j] = num[j], num[i]             # 만약 쓴 숫자라면 어차피 재귀 호출해도 똑같은 값이 나와서 의미없는 탐색임.(특정 숫자를 함수에 넣으면 어차피 모든 경우의수를 탐색하기 때문)
        

T = int(input())

for tc in range(1, T+1):
    number, change = map(str, input().split())
    
    max_money = 0
    num_used = []
    
    change_number(number, 0)
    
    print(f'#{tc} {max_money}')