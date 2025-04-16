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

import sys
sys.stdin = open('tc.txt', 'r')

K = int(input())

borderline_x = []
borderline_y = []

for _ in range(6):
    direction, length = map(int, input().split())
    if direction in [1, 2]:
        borderline_x.append(length)
    else:
        borderline_y.append(length)

large_field = max(borderline_x) * max(borderline_y)
small_field = 1200

result = (large_field - small_field) * K

print(result)
