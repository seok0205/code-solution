'''
S2 20006 랭킹전 대기열

문제 설명:
운영하던 게임에 랭킹전 기능 추가하려 함.
플레이어 간의 실력차가 있을 수 있기 때문에 입장을 신청하면 비슷한 레벨의 플레이어들을 매칭해 게임 시작하려 함.
시스템의 규칙은 아래와 같음

1. 플레이어가 입장을 신청하였을 때 매칭이 가능한 방이 없다면 새로운 방을 생성하고 입장시킨다. 이때 해당 방에는 처음 입장한 플레이어의 레벨을 기준으로 -10부터 +10까지 입장 가능하다.
2. 입장 가능한 방이 있다면 입장시킨 후 방의 정원이 모두 찰 때까지 대기시킨다.
    - 이때 입장이 가능한 방이 여러개라면 먼저 생성된 방에 입장한다.
3. 방의 정원이 모두 차면 게임을 시작시킨다.

플레이어의 수 p, 플레이어 닉네임 n, 플레이어 레벨 I, 방 한개의 정원 m이 주어질 때, 위와 같은 방법으로 매칭해주고 최종적으로 만들어진 방의 상태와 입장 플레이어들을 출력하는 프로그램 작성.

입력:
첫 째 줄에는 플레이어의 수 p(1 <= p <= 300), 방의 정원 m(1 <= m <= 300) 주어짐.
두번 째 줄부터 p개의 줄에는 플레이어의 레벨 I (1 <= I <= 500)과 닉네임 n이 공백을 두고 주어짐.
입력된 순서대로 게임을 시작함.
닉네임은 중복되지 않으며 공백을 포함하지 않는 알파벳 소문자로 되어있으며 닉넴 길이는 16을 넘지 않는다.

출력:
모두 생성된 방에 대해서 게임의 시작 유무와 방에 들어있는 플레이어들의 레벨과 아이디를 출력.
시작 유무와 플레이어의 정보들은 줄 바꿈으로 구분. 레벨, 아이디는 한줄에서 공백으로 구분.
방은 생성된 순서대로 출력.
방의 플레이어들은 닉네임이 사전순으로 앞서는 플레이어부터 출력.
방이 시작되었으면 Started!를 대기 중이면 Waiting!을 출력.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

p, m = map(int, input().split())
rooms = []

for _ in range(p):
    data = list(map(str, input().split()))
    l, n = int(data[0]), data[1]
    
    if rooms:
        for room in rooms:
            if len(room) == m:
                continue

            if room[0][0] - 10 <= l <= room[0][0] + 10:
                room.append((l, n))
                break
        else:
            rooms.append([(l, n)])
    else:
        rooms.append([(l, n)])

for room in rooms:
    if len(room) == m:
        print('Started!')
    else:
        print('Waiting!')

    room.sort(key=lambda x: x[1])
    
    for player in room:
        print(player[0], player[1])