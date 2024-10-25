#로또의 번호가 훼손되었을 수도 있는 경우에 당첨 최고, 최저 순위 예측.
# 번호가 지워져서 확인이 쉽지 않은 경우는 0으로 표현.
# 예를 들어, lottos의 번호가 3개가 맞고, 0이 1개 존재하는 경우, 최저 순위는 4등, 최고 순위는 3등이다.

lottos = [44, 1, 0, 0, 31, 25]
win_nums = [31, 10, 45, 1, 6, 19]

def solution(lottos, win_nums):
    result = [0, 0]
    same_num = 0
    zero_num = 0
    for i in lottos:    # 로또 번호 하나씩.
        if i in win_nums:   # 정답 번호에 i가 존재하면 same_num 1증가.
            same_num += 1
        elif i == 0:    # lottos 번호가 0이면 zero_num 1증가.
            zero_num += 1
    for i in range(7):  # 등수는 맞춘 개수가 0,1이면 6등, 2면 5등... 6개 1등.
        if same_num == 0:
            result[1] = 6
        elif i == same_num:
            result[1] = 7 - i
    if same_num == 0 and zero_num == 6: # 맞춘 숫자가 0이면서 0의 개수가 6개면 최고 등수가 0등이 나오는 경우 방지.
        result[0] = 1
    else:
        result[0] = result[1] - zero_num
    return result
    
print(solution(lottos, win_nums))

# 다른 풀이의 경우. 등수의 범위가 6등으로 좁다보니,
# 랭킹의 배열을 일치하는 로또 번호 개수를 인덱스로 하여 선언해놓은 방식이 있었다.
# [6, 6, 5, 4, 3, 2, 1] 이런식으로.