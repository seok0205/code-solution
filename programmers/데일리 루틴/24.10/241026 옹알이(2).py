babbling = ["aya", "yee", "u", "maa"]

def solution(babbling):
    answer = 0
    word = ['aya', 'ye', 'woo', 'ma']

    for i in babbling:  # babblingg�� �ܾ� �ϳ��� Ȯ��.
        for j in word:
            if j * 2 not in i:  # �������� �� ���´ٸ� �������� ��ȯ.
                i = i.replace(j, ' ')
        if i.isspace(): # �������θ� �̷���� ������ answer 1 ����.
            answer += 1

    return answer

print(solution(babbling))