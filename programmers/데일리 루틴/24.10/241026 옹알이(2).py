babbling = ["aya", "yee", "u", "maa"]

def solution(babbling):
    answer = 0
    word = ['aya', 'ye', 'woo', 'ma']

    for i in babbling:  # babblingg의 단어 하나씩 확인.
        for j in word:
            if j * 2 not in i:  # 연속으로 안 나온다면 공백으로 변환.
                i = i.replace(j, ' ')
        if i.isspace(): # 공백으로만 이루어져 있으면 answer 1 증가.
            answer += 1

    return answer

print(solution(babbling))