'''
D3 5356 의석이의 세로로 말해요

문자열들이 주어지면 세로로 읽으려고 함
하지만 글자가 없다면 뛰어넘어서 읽어야함. 세로로 읽은 순서대로 글자를 출력하는 문제

입력:
T : 테스트 케이스 수
테스트 케이스 입력

출력:
#T 출력 후 공백을 두고 세로로 읽은 순서대로 글자 출력
'''

T = int(input())

for tc in range(1, T+1):
    string = [list(input()) for _ in range(5)]
    idx = 0
    result = list()     # 결과 문자열 넣을 리스트
    
    while idx < 15:     # 단어 최대 길이 15. 인덱스 14까지 존재하므로 idx가 15되는 순간 중단
        for i in range(5):      # 5줄 순회하면서
            if idx < len(string[i]):        # 조건은 인덱스가 문자열의 길이보다 길면 빼올 문자열이 없어서 추가했음
                result.append(string[i][idx])       # 차례대로 결과 리스트에 추가
        idx += 1    # 인덱스 1 증가
    
    print(f"#{tc} {''.join(result)}")