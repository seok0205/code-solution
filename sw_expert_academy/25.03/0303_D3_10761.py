'''
D3 10761 신뢰

두 사람이 존재. 서로 다른 복도에 존재.

한 복도에 1 이상 100 이하의 정수로 구분되는 100개의 버튼 존재
버튼 K는 복도의 시작점에서 K미터 떨어져 있음. 두 로봇은 버튼 1에서 시작
매 1초마다, 복도의 양 방향 중 하나로 1미터 걷거나, 자기 위치에 있는 버튼을 누르거나, 아무것도 안함

한 테스트는 여러개의 버튼 수열로 표시, 로봇들이 수열에 표시된 순서대로 버튼을 눌러야 함
버튼은 O x, B x 같은 형태로 주어짐. O x는 첫번째 사람이 눌러야하고, B x는 두번째 사람이 눌러야함
순서대로 버튼을 눌러야 해서, 두 로봇이 동시에 버튼을 누를 순 없다.

모든 수열에 표시된 버튼 누르기를 끝내는 가장 빠른 시간을 출력

입력:
T : 테스트 케이스 개수
첫 번째 정수는 테스트에서 눌러야하는 버튼의 개수 N
이후 버튼 N개가 공백 기준으로 한 줄에 주어짐.

출력:
각 테스트 케이스마다 최소 시간 출력
'''

T = int(input())

for tc in range(1, T+1):
    string = list(map(str, input().split()))
    N = int(string[0])
    rare_command = string[1:]
    
    orange_command = list()     # 오렌지의 명령
    blue_command = list()       # 블루의 명령
    
    for i in range(0, len(rare_command), 2):        # 명령 분배
        if rare_command[i] == 'O':
            orange_command.append([int(rare_command[i+1]), i//2+1])
        else:
            blue_command.append([int(rare_command[i+1]), i//2+1])

    time = 0        # 최소 시간 담을 변수
    orange = 1      # 오렌지 위치
    blue = 1        # 블루 위치
    orange_idx = 0  # 오렌지 명령 인덱스
    blue_idx = 0    # 블루 명령 인덱스
    orange_button = 0   # 버튼 누를 수 있는 위치인지 판별
    blue_button = 0
    
    while True:
        if blue_idx >= len(blue_command) and orange_idx >= len(orange_command): # 명령 인덱스가 모두 양측 길이 이상이면 모든 명령 완료, 반복문 탈출
            break
        
        if orange_idx < len(orange_command):        # 인덱스가 명령 리스트의 범위 안이면 진행
            if orange_command[orange_idx][0]:       # 버튼의 위치까지 이동
                if orange_command[orange_idx][0] > orange:
                    orange += 1
                elif orange_command[orange_idx][0] < orange:
                    orange -= 1
                else:
                    orange_button = 1           # 버튼에 도착했으면 버튼 누를 수 있음. 동시에 버튼을 못눌러도 다음 턴에도 1 유지.
        
        if blue_idx < len(blue_command):
            if blue_command[blue_idx][0]:
                if blue_command[blue_idx][0] > blue:
                    blue += 1
                elif blue_command[blue_idx][0] < blue:
                    blue -= 1
                else:
                    blue_button = 1
                
        if blue_button and orange_button and blue_button == orange_button:      # 만약 둘 다 버튼을 누를 수 있는 상태라면
            if orange_command[orange_idx][1] > blue_command[blue_idx][1]:       # 우선 순위에 따라 둘 중 누가 먼저 누를지 결정
                blue_button = 0
                blue_idx += 1
            else:
                orange_button = 0
                orange_idx += 1
        elif orange_button and blue_idx == len(blue_command):       # 오렌지가 누를 수 있는 상태인데 만약 블루는 명령을 모두 이행한 상태라면
            orange_button = 0
            orange_idx += 1
        elif blue_button and orange_idx == len(orange_command):     # 위 elif문의 반대 상황. 블루가 누를 수 있는 상태지만 오렌지는 모두 이행 완료 상태
            blue_button = 0
            blue_idx += 1
        else:                       # 둘다 명령 수행중에 있으면, 우선순위가 중요하므로 고려 후 선택
            if blue_button and orange_command[orange_idx][1] > blue_command[blue_idx][1]:
                blue_button = 0
                blue_idx += 1
            elif orange_button and orange_command[orange_idx][1] < blue_command[blue_idx][1]:
                orange_button = 0
                orange_idx += 1
        
        time += 1       # 한번 동작함. 턴 증가
        
    print(f'#{tc} {time}')