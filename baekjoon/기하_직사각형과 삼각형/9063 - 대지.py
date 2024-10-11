N = int(input())    #점 개수
x_point = []    #x좌표 모음
y_point = []    #y좌표 모음
land = 0    #대지의 넓이

for i in range(N):  #점개수만큼 입력 받기
    a, b = map(int, input().split())
    x_point.append(a)   #a는 x좌표 리스트에 추가
    y_point.append(b)   #b는 y좌표 리스트에 추가

#x좌표와 y좌표 각각 최대에서 최소값을 빼면 입력된 점을 모두 포함하는 사각형의 변 두 개를 구할 수 있다.
land = (max(x_point) - min(x_point)) * (max(y_point) - min(y_point))
print(land)