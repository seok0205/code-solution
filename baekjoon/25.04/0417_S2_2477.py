'''
S2 2477 참외밭

밭에서 자라는 참외가 몇 개가 되는지 구하려고 함.
1m**2의 넓이의 자리에 자라는 참외의 개수는 세었고, 참외밭 넓이만 구하면 됨.

참외밭은 ㄱ자보양이거나 ㄱ자를 90, 180, 270도 회전한 모양의 육각형임. 다행히 밭의 경계는
모두 동서 방향이거나 남북방향임.
밭의 한 모퉁이에서 출발해 밭의 둘레를 돌면서 밭경계 길이를 모두 측정함.

1m**2의 넓이에 자라는 참외의 개수와, 참외밭을 이루는 육각형의 임의의 한 꼭짓점에서 출발하여 반시계 방향으로
둘레를 돌면서 지나는 변의 방향과 길이가 순서대로 주어짐. 이 참외밭에서 자라는 참외의 수를 구하는 문제
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

K = int(input())

borderline = []     # 방향과 변의 길이를 담을 리스트

for _ in range(6):
    direction, length = map(int, input().split())

    borderline.append((direction, length))      # 방향, 길이를 튜플 형태로 모든 요소 삽입

# 3 1 3 1 : 왼쪽 아래 사각형
# 1 4 1 4 : 오른쪽 아래 사각형
# 4 2 4 2 : 오른쪽 위 사각형
# 2 3 2 3 : 왼쪽 위 사각형
# 이 4개의 경우의 수밖에 존재하지 않기 때문에 리스트를 돌려서 위와 동일한 경우 찾기

for i in range(5):      # 육각형을 만드는 거라 무조건 6개의 입력값이 주어짐. 5번만 돌리면 순서 모두 찾을 수 있음
    if borderline[0][0] == borderline[2][0] and borderline[1][0] == borderline[3][0]:
        break

    a = borderline.pop(0)       # 앞의 것을 빼서
    borderline.append(a)        # 뒤에 붙이기

large_field = borderline[4][1] * borderline[5][1]   # 이런 상황에서는 큰 사각형의 넓이는 작은 사각형 만드는 4개의 요소 제외한 나머지 두개의 요소의 길이 곱하면 됨
small_field = borderline[1][1] * borderline[2][1]   # 중간 두개의 요소의 변을 곱하면 작은 사각형의 넓이를 구할 수 있음

result = (large_field - small_field) * K        # 큰 사각형에서 작은 사각형 빼고, K 곱해줌. 참외 개수 구하기 완료

print(result)