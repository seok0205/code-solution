'''
D4 1210 Ladder1

사다리 타기와 같이 0과 1이 존재하는 2차원 배열에서 1을 통해서 목표점인 2에 도달하는 출발점을 구하는 문제
배열은 100x100, 출발점에서 오른편에 1이나오면 무조건 좌나 우로 가야함

제한사항:
한 막대에서 출발한 가로선이 다른 막대를 가로질러서 연속해 이어지는 경우는 없음

입력:
10개의 테스트 케이스

출력:
# 부호, 테스트케이스 번호, 출발점 x좌표
'''

for tc in range(1, 11):
    T = int(input())
    matrix = [list(map(int, input().split())) for _ in range(100)]
    result = 0
    
    dj = [1, -1]    # 좌우만 확인하면 됨. i는 변환 값이 좌우 이동 시 0, 0이므로 델타 필요 X
    
    dir = 'down'    # 방향
    
    for start in range(100):    # 첫 줄의 100칸이 모두 출발점이 될 수 있음
        i = 0
        j = start       # 시작점
        if matrix[0][start]:    # 값이 1이면 시작
            while True: 
                if i == 99:     # 맨 마지막까지 내려간 상태면 2를 못 찾은 것이라서 while문 종료
                    break
                
                elif dir == 'down':     # 방향은 down부터 시작
                    i += 1      # 한칸 전진
                    for num in range(2):    # 좌우 살펴봄
                        x1, y1 = i, j + dj[num]     # 옆 칸 임시 좌표
                        if 0 <= y1 <= 99 and matrix[x1][y1] == 1 and num == 0:  # 배열 안쪽이고, 오른쪽 칸 1이면 방향 right로 변경(num == 0 or 1 조건은 오른쪽, 왼쪽임을 구별하기 위함)
                            dir = 'right'
                            break
                        elif 0 <= y1 <= 99 and matrix[x1][y1] == 1 and num == 1:    # 왼쪽 칸 1이면 방향 left로 변경
                            dir = 'left'
                            break
                        
                elif dir == 'right':    # 방향이 오른쪽이면
                    j += dj[0]        # j가 1 증가. 오른쪽으로 전진
                    x2, y2 = i + 1, j    # 밑 칸 임시좌표
                    if matrix[x2][y2]:      # 밑의 칸이 1이라면 방향 down으로 변경
                        dir = 'down'
                        
                elif dir == 'left':     # 왼쪽이면
                    j += dj[1]        # j가 -1 감소. 왼쪽 전진
                    x3, y3 = i + 1, j    # 밑 칸 임시좌표
                    if matrix[x3][y3]:      # 오른쪽일 때와 조건 같음
                        dir = 'down'
                        
                if matrix[i][j] == 2:   # 다다른 곳이 2라면 해당 출발점 result에 대입 후 while문 종료
                    result = start
                    break
                
        if result != 0:     # result가 디폴트 값 0이 아니면 더이상 찾을 필요 X. 전체 종료
            break
    print(f'#{tc} {result}')