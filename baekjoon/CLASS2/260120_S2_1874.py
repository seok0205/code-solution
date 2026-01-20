'''
S3 1874 스택 수열

문제 설명:
스택은 자료를 넣는 입구, 뽑는 입구가 같아 LIFO 특성 가짐. (후입 선출)
1부터 n까지의 수를 스택에 넣었다가 뽑아 늘어놓음으로써, 하나의 수열 만들 수 있음.
이때 스택에 push하는 순서는 반드시 오름차순을 지키도록 한다고 할 때,
임의의 수열이 주어질 때, 스택을 이용해 그 수열을 만들 수 있는지, 있으면 어떤 순서로 push, pop연산을 수행하는지 알수 있음.
이를 계산하는 프로그램 작성

입력:
첫 줄에 n이 주어짐 (1 <= n <= 100,000)
둘째 줄부터 n개의 줄에는 수열을 이루는 1이상 n이하의 정수가 하나씩 순서대로 주어짐.
같은 정수 두 번 나오는 일 없음

출력:
입력된 수열을 만들기 위해 필요한 연산 한줄에 하나씩, push는 +, pop은 -로 표현.
불가능한 경우 NO 출력
'''

import sys
# sys.stdin = open('tc.txt', 'r')
input = sys.stdin.readline
print = sys.stdout.write

n = int(input())
nums = []

for _ in range(n):
    num = int(input())
    nums.append(num)

targets = sorted(nums)
stack = []
nums_idx = 0
result = []

for i in range(n):
    target = targets[i]
    stack.append(target)
    result.append('+')

    while True:
        if stack and nums[nums_idx] == stack[-1]:
            stack.pop()
            result.append('-')
            nums_idx += 1
        else:
            break

if stack:
    print('NO')
else:
    for j in result:
        print(j + '\n')