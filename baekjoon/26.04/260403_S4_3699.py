'''
S4 3699 주차 빌딩

문제 설명:
주차 빌딩의 원리.
차를 엘리베이터에 주차시키고 차에서 내림.
엘리베이터와 컨베이어 벨트는 빈 주차 공간을 찾아 그곳으로 이동시킴.
차를 찾으러 오기 전까지는 계속 그자리에 있음.
차찾으러 오면, 엘리베이터와 컨베이어 벨트는 해당 차를 찾아 다시 입구로 가져옴.

주차 빌딩은 중앙 엘리베이터가 있고, 이를 이용해 층 사이 이동 가능함.
각 층에는 거대한 원형 컨베이어 벨트가 있고, 이 컨베이어 벨트 위에 차가 있음.
벨트는 시계, 반시계방향 움직임.
엘리베이터가 어떤 층 도착하면, 컨베이어 벨트의 일부가 되며, 차는 엘리베이터를 통과해서 이동 가능.

하루 일과 끝날때 쯤, 사람들은 온 순서대로 차를 찾을수 있음.
엘리베이터는 차가 있는 곳으로 이동하고, 컨베이어 벨트는 차를 엘리베이터에 싣고, 다시 아래로 내려가 고객에게 차를 줌.
모든 고객이 차를 찾는 데 걸리는 시간을 구하는 프로그램 작성.

엘리베이터가 층을 이동하는 데 걸리는 시간은 10초, 컨베이어 벨트가 차 한 대 만큼 시계방향 또는 반시계방향으로 이동하는 데 걸리는 시간은 5초.

입력:
첫줄 - TC 개수 최대 100개.
각 TC의 첫줄에는 빌딩 높이 h, 벨트 길이 I가 주어짐.(1 <= h <= 50, 2 <= I <= 50).
다음 h개 줄에 I개의 정수가 주어짐. 빌딩의 차 정보.
i번째 줄의 j 번째 숫자는 i번 층의 j번 위치에 있는 차 정보 나타냄.
정수가 -1이면 비어있고, 다른 값인 r인 경우, r번째 손님이 찾아갈 차라는 뜻.
손님은 차를 1층에서 찾아가고, 엘리베이터는 첫 번째 위치에있음.
엘리베이터는 처음에 항상 비어있음. 주차 빌딩에 차가 항상 존재하는 경우만 입력으로 주어짐.
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    h, I = map(int, input().split())
    building = [list(map(int, input().split())) for _ in range(h)]
    result = 0
    person = 1

    def turn_left(x, cnt):
        for _ in range(cnt):
            new = building[x].pop(0)
            building[x].append(new)

    def turn_right(x, cnt):
        for _ in range(cnt):
            new = building[x].pop()
            building[x].insert(0, new)
    

    while True:
        for i in range(h):
            for j in range(I):
                if building[i][j] == person:
                    if j < I - j:
                        turn_left(i, j)
                        result += (20 * i) + (5 * j)
                    else:
                        turn_right(i, I - j)
                        result += (20 * i) + (5 * (I - j))

                    building[i][0] = -1
                    person += 1
            
        check = 0
        for floor in building:
            check += sum(floor)
        
        if check == -(h*I):
            break

    print(result)