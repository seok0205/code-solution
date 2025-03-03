'''
D3 1860 진기의 최고급 붕어빵

N명의 사람이 붕어빵을 맛볼려고 함
0초부터 붕어빵을 만들기 시작하고, M초의 시간을 들이면 K개의 붕어빵을 만들 수 있음
붕어빵이 완성되면 시간 지연 없이 다음 붕어빵 만들기 시작 가능
0초 이후에 손님들이 언제 도착하는지 주어지면, 모든 손님들에게 기다리는 시간없이 붕어빵을 제공할 수 있는지 판별하는 문제

입력:
T : 테스트 케이스의 수
N, M, K: 사람 수, K개의 붕어빵을 만드는 시간 M
N개의 정수가 주어짐(사람이 언제 도착하는 지, 0이상 11,111이하)

출력:
기다리는 시간 없이 제공가능하면 Possible, 아니면 Impossible 출력
'''

T = int(input())

for tc in range(1, T+1):
    N, M, K = map(int, input().split())
    arrive = list(map(int, input().split()))
    
    arrive.sort()       # 들어오는 시간순으로 정렬
    boong = 0           # 붕어빵 개수
    time = 0            # 흐른 시간
    result = 'Possible' # 중간에 특정 조건들만 만족한다면 그대로출력
    
    while arrive:       # 도착할 사람들이 남았을 때는 계속 반복
        arrived_people = list()     # 도착할 사람들(첫 붕어빵 만들 시간 필요하므로 처음 오는 사람들이 있다면 대기 불가피)
        
        for i in range(len(arrive)):        # 붕어빵 추가될 한 타임 동안의 도착할 사람들
            if arrive[i] >= time + M:       # 다음 시간이 되기 전에 오는 사람들을 arrived_people에 추가
                arrived_people.extend(arrive[:i])       # i번째 인덱스까지만 하면 조건 만족한 인덱스 전까지만 들어가게 됨
                arrive = arrive[i:]         # arrive는 추가된 사람들 제외한 리스트로 다시 설정해줌
                break                       # 이후 인덱스들은 탐색할 필요 X
        else:
            arrived_people = arrive.copy()          # 만약 찾지못하고 for문을 모두 반복했다면 리스트에 존재하는 인원 모두 도착할 사람이라는 뜻이므로 arrive_people에 통째로 넣어주고,
            arrive.clear()                          # while문 반복할 이유가 없으므로, arrive를 빈 리스트로 만들어 while 조건문을 0(False)로 만들어 줌
        
        boong -= len(arrived_people)                # 붕어빵에서 도착할 사람들 리스트의 길이(인원)만큼 빼줌
        
        if boong < 0:                               # 만약 0보다 작으면 붕어빵 부족하다는 뜻. 대기 불가피이므로 Impossible 설정해주고 while문 종료
            result = 'Impossible'
            break
        
        boong += K                                  # 다음 시간 턴의 손님들을 위해 붕어빵 생성 및 다음 시간 설정
        time += M
                
    print(f'#{tc} {result}')