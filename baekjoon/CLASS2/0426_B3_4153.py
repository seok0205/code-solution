'''
B3 4153 직각삼각형

과거 이집트인들은 각 변들의 길이가 3, 4, 5인 삼각형이 직각 삼각형인것을 알아냈음. 주어진 세변의 길이로
삼각형이 직각인지 아닌지 구분하는 문제

맞으면 right, 틀리면 wrong 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

while True:         # 0, 0, 0 입력 받을 때까지는 계속 진행
    edge = list(map(int, input().split()))

    if sum(edge) == 0:      # 세 숫자 모두 0이면 (모두 양수라서 sum활용 가능) 종료
        break
    else:
        edge.sort()     # 적은 변부터 리스트에 정렬
        
        if edge[0]**2 + edge[1]**2 == edge[2]**2:       # 피타고라스 만족하면 right 출력
            print('right')
        else:
            print('wrong')