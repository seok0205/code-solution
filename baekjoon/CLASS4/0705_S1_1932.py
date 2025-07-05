'''
S1 1932 정수 삼각형

크기가 5인 정수 삼각형의 한 모습
맨 위층 7부터 시작해 아래에 있는 수 중 하나를 선택해 아래로 내려올 때, 이제까지 선택된 수의 합이 최대가 되는 경로를 구하는 문제
아래 층에 있는 수는 현재 층에서 선택된 수의 대각선 왼쪽 또는 대각선 오른쪽에 있는 것 중에서만 선택 가능

삼각형 크기는 1이상 500 이하. 삼각형을 이루고 있는 각 수는 모두 정수. 0이상 9999이하.

입력:
n : 삼각형 크기(1이상 500 이하)
두번째줄 ~ n+1번째줄 : 정수 삼각형 구성
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline

n = int(input())
num = list(map(int, input().split()))

for i in range(1, n):       # 삼각형의 한줄 마다 확인
    nums = list(map(int, input().split()))
    
    for j in range(i+1):        # 양 옆의 끝 요소들은 윗줄의 하나의 요소만 더할 수 있음.
        if j == 0:
            nums[0] += num[0]
        elif j == i:
            nums[j] += num[j-1]
        else:                   # 양 끝 요소 제외한 나머지는 윗줄의 같은 인덱스, 1을 뺀 인덱스와 더할 선택이 주어짐. 둘중에 큰것을 선택.
            nums[j] = max(nums[j] + num[j], nums[j] + num[j-1])
    
    num = nums      # 다음 줄 계산을 위해 num 주기적으로 교체해줌. num은 맨 윗줄부터 차례로 저장된 값이 바뀜
    
print(max(num))     # 마지막줄의 최댓값이 답.