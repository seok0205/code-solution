'''
D3 6190 정곤이의 단조 증가하는 수

어떤 규칙을 만족하는 수를 찾는 중
규칙은 단조 증가하는 수. 각 숫자의 자릿수가 단순하게 증가하는 수를 말함

k자리수 X=d1d2dk가 d1<=d2<=dk를 만족하면 단조 증가하는 수
예로, 111566, 2333359는 단조 증가하는 수, 12343, 999888은 단조 증가하는 수가 아님

양의 정수 N개가 주어짐
두 i, j에 대해 단조증가하는 수 인 것들을 구하고 그 중 최댓값을 출력
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    nums = list(map(str, input().split()))
    
    satisfied = list()      # 단조 증가하는 수 담을 리스트
    
    for i in range(N-1):    # 모든 수 곱하는 경우의 수 탐색
        for j in range(i+1, N):
            target = int(nums[i]) * int(nums[j])    # 곱을 target으로 삼고,
            str_target = str(target)                # 자릿수끼리 비교 위해 문자열 형태로 변형
            
            if len(str_target) == 1:                # 만약 한자리면 그냥 단조 증가하는 수에 포함
                    satisfied.append(target)
            else:                                   # 자릿수가 여러개라면 비교 진행
                for k in range(1, len(str_target)):
                    if str_target[k] < str_target[k-1]:     # 만약 자릿수가 증가할때마다 수도 증가하지 않고 오히려 작다면
                        break                               # break
                else:
                    satisfied.append(target)        # 만약 break되지않고 for문을 전부 진행했다면, 단조 증가하는 수.
            
    if len(satisfied) == 0:     # 만약 만족하는 수 없다면 -1출력
        print(f'#{tc} -1')
    else:
        print(f'#{tc} {max(satisfied)}')        # 만족하는 수중 최댓값 출력