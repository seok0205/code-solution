def solution(s):
    return (''.join(reversed(sorted(s))))

def A_solution(s):
    return (''.join(sorted(s)[::-1]))

def B_solution(s):
    return ''.join(sorted(s, reverse=True))
#join은 리스트나 문자열을 연결. join의 뒤에 나온 구조는 정렬하여 거꾸로 뒤집어 주는 방법.

def C_solution(s):
    answer = ''
    s = sorted(s, reverse=True)
    for i in s:
        answer += i
    return answer