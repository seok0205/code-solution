# s가 입력되었을 때, 문자열을 분해하고 분해된 문자열의 개수를 구하는 문제.
# 첫 글자가 x일 때, 첫 글자부터 문자열을 읽어 나가면서, 첫 문자를 포함한 x와 같은 문자가 나온 횟수, 다른 문자가 나온 횟수가 같아진다면 즉시 문자열 분리.
# 그리고 다시 x를 설정하여 같은 과정을 문자열이 끝날 때까지 반복한다. 마지막 남은 문자열까지 합친 총 문자열의 개수를 구하는 문제.

s = 'banana'

def solution(s):
    answer = 0  # 분리된 문자열 총 개수.
    x_count = 0 # x가 나온 횟수.
    no_x_count = 0  # x가 아닌 글자가 나온 횟수.

    for i in s: # 문자열의 글자 하나씩 반복.
        if x_count == no_x_count:   # 횟수가 같으면 문자열 분리 기준이므로, 횟수 1증가 및 해당 문자열을 x로 지정.
                                    # 어차피 횟수가 똑같을 때가 분리 기준이라서 count를 0으로 초기화할 필요가 없다.
            answer += 1
            x = i
        if x == i:  # x와 같으면 x_count 증가
            x_count += 1
        else:   # 다른 문자라면 no_x_count 증가
            no_x_count += 1

    return answer

print(solution(s))