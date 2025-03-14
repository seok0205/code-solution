'''
D4 1486 장훈이의 높은 선반

높이가 B인 선반이 하나 있는데 장훈이는 키가 큼, 선반 위 물건 자유롭게 사용 가능
서점에 있는 N명의 점원들이 선반 위에 있는 물건을 사용해야 하는 일이 생김

각 점원의 키는 H, 점원들은 탑을 쌓아 선반 위 물건 사용하기로 함
점원들이 쌓는 탑은 점원 1명 이상으로 이루어짐

탐의 높이는 점원이 한명일 경우 그 점원의 키와 같고, 2명 이상이면 탑 만든 모든 점원 키의 합과 같음
탑 높이 B 이상인 경우 선반위 물건 사용할 수 있는데 탑의 높이가 높을수록 더 위험하므로 높이가
B 이상인 탑 중에서 높이가 가장 낮은 탑을 알아내려고 함
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def top(cnt, h):
    global result

    if h >= B:                          # 함수 실행 시마다 입력 받은 키의 합과 선반 높이 차 비교
        if result > h - B:
            result = h - B
        return
    
    if cnt == N:                        # 점원 모두 키의 합 탐색하면 재귀 종료
        return
    
    top(cnt + 1, h + height[cnt])       # 재귀로 해당 점원의 키를 포함하거나, 안하거나
    top(cnt + 1, h)
    

T = int(input())

for tc in range(1, T+1):
    N, B = map(int, input().split())
    height = list(map(int, input().split()))
    
    result = float("inf")
    
    top(0, 0)
    
    print(f'#{tc} {result}')