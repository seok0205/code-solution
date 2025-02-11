'''
D2 16370 글자수

두 문자열이 주어지는데 첫번째 문자열에 포함된 글자들이 두번째 문자열에 몇 개씩 들어있는지 찾고,
그 중 가장 많은 글자의 개수를 출력

입력:
T : testcase
N : 첫번째 문자열
M : 두번째 문자열
'''

T = int(input())

for tc in range(1, T+1):
    N = list(input())
    M = list(input())

    string_dic = dict()     # 글자 출현횟수 집어넣을 딕셔너리 생성

    for i in N:     # 첫번째 문자열 글자마다
        dic = dict()        # 서브 딕셔너리 생성
        for j in M:         # 두번째 문자열에서 순회하면서
            if i == j and i not in dic:     # 같은 문자 딕셔너리에 횟수 증가
                dic[i] = 1
            elif i == j:
                dic[i] += 1
        string_dic.update(dic)      # 딕셔너리에 업데이트

    print(f'#{tc} {max(string_dic.values())}')      # 딕셔너리 밸류중 가장 큰값 출력
