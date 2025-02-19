'''
D3 16585 토너먼트 카드게임

1번부터 N번까지 N명의 학생이 N장의 카드 나눠가짐
전체를 두 그룹으로 나누고, 그룹의 승자끼리 카드 비교 후 이긴 사람이 최종 승자
승자 그룹에서 또 두 그룹으로 나누어 i부터 j 번까지 속한 그룹은
i부터 (i+j)//2까지와 (i+j)//2+1부터 j까지 나눔
두 그룹이 각각 1명이 되면 양쪽 카드 비교해 승자를 가림
1은 가위, 2는 바위, 3은 보, 같은 카드인 경우 편의상 번호가 작은 사람이 승자. 카드 변경 X.
N명의 학생들이 카드를 골랐을 때 1등 찾는 문제
'''


def find_winner(a, b):
    if a == b:      # 그룹이 1명이 되면, a번째의 학생 반환
        return a
    else:
        left = find_winner(a, (a+b)//2)     # 1명이 될때까지 두 그룹으로 계속 나눔.
        right = find_winner((a+b)//2+1, b)

        if cards[left] == cards[right]:     # 왼쪽 학생의 카드와 오른쪽 학생의 조건 따라 승리 갈림
            return left
        elif cards[left] == 1 and cards[right] == 3:
            return left
        elif cards[left] == 2 and cards[right] == 1:
            return left
        elif cards[left] == 3 and cards[right] == 2:
            return left
        else:
            return right


T = int(input())
for tc in range(1, T+1):
    N = int(input())
    cards = list(map(int, input().split()))

    result = find_winner(0, N-1) + 1    # 결과는 인덱스 형태이므로 1을 더해야 학생 진짜 번호

    print(f'#{tc} {result}')
