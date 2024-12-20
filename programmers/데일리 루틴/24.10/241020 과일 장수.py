#m개의 사과를 담을 수 있는 박스를 판매하려고한다.
#사과의 가격은 1부터 k까지 배정된다.
#각 사과의 가격은 score배열에 담겨 있고, score에 있는 가격의 개수가 판매하려는 사과의 총 개수이다.
#사과 박스의 가격 책정은 같은 상자에 담긴 사과중 가장 낮은 사과의 가격을 기준으로 계산한다.
#최대 이익을 구하는 문제이다. 단, 상자 하나를 m개로 채우지 못하면 그 사과들은 팔 수 없다.
k = 4
m = 3
score = [4, 1, 2, 2, 4, 4, 4, 4, 1, 2, 4, 2]

cost = 0    #총 이익
score.sort(reverse=True)    #가격을 낮은 순서대로 정렬한다. 가장 가격이 낮은 사과 기준이므로 최대한 비슷한 가격 끼리 구성하는게 최적의 방법이다.

for i in range(0, len(score), m):   #i가 m씩 증가 하므로, i부터 i+m까지 score에서 슬라이싱하면 한박스를 구성가능하다.
    box = score[i:i+m]
    if len(box) == m:   #슬라이싱이 제대로 되었다면 한 박스가 구성되었다는 것이므로, 총 가격에 더한다.
        cost += min(box)*m

print(cost)