'''
D3 10580 전봇대

두 전봇대가 있는데, N개의 팽팽한 전선으로 연결되어 있음.
두 전선이 끝점이 같은 경우는 없고, 교차하는 경우는 존재함.
세 개 이상의 전선이 하나의 점에서 만나지 않는다고 가정. 이 전봇대의 교차점을 구하는 문제

입력:
TC - 테스트 케이스
N - 전선의 개수
두 양수 A, B를 N줄 동안 입력

A, B는 i번째 전선이 첫번째 전봇대의 Acm 고도에 걸려있고, 두번 째 전봇대의 Bcm고도에 걸려있음을 뜻함
모든 A, B는 각각 서로 다르다. 두 전선의 끝점이 같은경우가 없기 때문 세 전선이 한 점에서 만나지 않게 입력 주어짐
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    cable = [list(map(int, input().split())) for _ in range(N)]
    
    result = 0      # 교차점 횟수
    
    for i in range(len(cable)):     # 하나의 전선과 하나의 전선을 비교.
        for j in range(i+1, len(cable)):        # 하지만 중복된 전선을 비교하지 않고, 비교했던 것도 비교하지 않기 위해, j는 i다음 인덱스부터 탐색
            if cable[i][0] < cable[j][0] and cable[i][1] > cable[j][1]:     # 끝점의 조건으로 교차점이 생기는 지 알 수 있음. 대각선형태로 전선이 연결되어 있을때, 교차점이 생기려면 무조건 중간을 지나가야하기 때문에
                result += 1                                                 # 양쪽의 끝점이 각각 더 크고, 더 작으며 대각선이 반대 방향이라면 끝점의 위치가 더 작고, 더 커야한다.
            elif cable[i][0] > cable[j][0] and cable[i][1] < cable[j][1]:
                result += 1
    
    print(f'#{tc} {result}')