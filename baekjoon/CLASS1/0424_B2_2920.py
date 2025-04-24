'''
B2 2920 음계

다장조는 c d e f g a b C, 총 8개 음으로 이루어져 있음.
이 문제에서 8개 음은 다음과 같이 숫자롤 바꾸어 표현.
c는 1, d는 2, ..., C는 8로 바꿈.

1부터 8까지 차례로 연주한다면 ascending, 8부터 1은 descending 둘다 아니라면 mixed임.
연주 순서가 주어질 때, 이것이 ascending인지 descending인지, mixed인지 판별하는 문제

입력:
첫째 줄 8개 숫자. 한번씩 등장(1~8)
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

nums = list(map(int, input().split()))

for i in range(7):      # 7번 확인해야함
    if i == 0:              # 첫 자리가 8이거나 1이 아니면 mixed임
        if nums[i] == 8:
            numtype = 1
        elif nums[i] == 1:
            numtype = 2
        else:
            print('mixed')
            break
    
    if numtype == 1:        # 첫자리에서 8이 뜨면 descending의 경우를 확인해야함
        if nums[i] == nums[i+1] + 1:
            continue
        else:               # 조건 만족 못하면 mixed 판정내리고 break
            print('mixed')
            break
    elif numtype == 2:      # 첫자리에서 1이 뜨면 ascending의 경우 확인
        if nums[i] == nums[i+1] - 1:
            continue
        else:               # 위 else문과 동일한 로직
            print('mixed')
            break
else:                       # break없이 for문 수행하면 조건 모두 만족하는 것.
    if numtype == 1:        # type에 맞는 결과문 출력.
        print('descending')
    elif numtype == 2:
        print('ascending')