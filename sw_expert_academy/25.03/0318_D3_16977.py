'''
D3 16977 전기버스2

충전지를 교환하는 방식의 전기버스 운행하려 함
정류장에는 교체용 충전지가 있는 교환기가 있고, 충전지마다 최대로 운행할 수 있는 정류장 수 정해져 있음

충전지 방전 전에 교체하며 운행해야 하는데 교체 시간을 줄이려면 최소한의 교체횟수로 목적지에 도착해야 함
정류장, 충전지에 대한 정보가 주어질 때, 목적지에 도착하는데 필요한 최소한의 교환횟수를 출력하는
프로그램 만드는 문제. 출발지에서의 배터리 장착은 교환횟수에서 제외
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def charge(station, cnt):
    global result
    
    if cnt > result:        # 횟수가 현재 최소 횟수보다 커지면 더이상 탐색할 필요가 없으므로 중단
        return
    
    if station >= N-1:      # 위치가 마지막 정류장와 같거나 이상이면 횟수 비교하고 중단
        if cnt - 1 < result:
            result = cnt - 1
        return
    
    for i in range(line[station], 0, -1):       # 한번 충전해서 갈수 있는 곳마다 다음 충전을 시도(재귀 호출)
        charge(station + i, cnt + 1)


T = int(input())

for tc in range(1, T+1):
    info = list(map(int, input().split()))
    N = info[0]
    line = info[1:] + [0]
    result = float("inf")
    
    charge(0, 0)
    print(f'#{tc} {result}')