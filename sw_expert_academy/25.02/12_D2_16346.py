'''
D2 16346 문자열 비교

두 개의 문자열 주어짐. 두번째 문자열 안에 첫번째 문자열과 일치하는 부분이 있는지 찾는 문제
존재하면 1, 존재하지 않으면 0 출력
'''

T = int(input())

for tc in range(1, T+1):
    str1 = input()
    str2 = input()

    result = 0

    for i in range(len(str2)-len(str1)+1):  # str2를 순회하면서 str1의 첫글자와 같은 부분 시작점
        if str1[0] == str2[i]:
            length = 0
            for j in range(len(str1)):      # str1가 str2에 있는지 확인하기 위함
                if str1[j] == str2[i+j]:    # 있으면 길이 1 추가
                    length += 1
            if length == len(str1):     # str1과 길이가 같으면 결과 1 도출
                result = 1
                break

    print(f'#{tc} {result}')
