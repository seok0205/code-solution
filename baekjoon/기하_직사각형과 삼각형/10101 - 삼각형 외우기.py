angle = []

for i in range(3):  #angle에 세 각 입력.
    N = int(input())
    angle.append(N)

if sum(angle) == 180:   #삼각형이 되는 조건은 각의 합이 180.
    if angle[0] == 60 and angle[1] == 60 and angle[2] == 60:    #세각이 모두 같으면 'Equilateral'
        print('Equilateral')
    elif angle[0] == angle[1] or angle[1] == angle[2] or angle[0] == angle[2]:  #두각만 같으면 'Isosceles'
        print('Isosceles')
    elif angle[0] != angle[1] and angle[1] != angle[2]: #세각이 모두 다르다면 'Scalene'
        print('Scalene')
else:   #각의 합이 180이 아니라면 삼각형이 아니라서 'Error' 출력.
    print('Error')