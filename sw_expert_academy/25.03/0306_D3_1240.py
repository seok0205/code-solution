'''
D3 1240 단순 2진 암호코드

암호코드에 규칙이 있음
1. 8개의 숫자로 이루어짐
2. 숫자 하나는 7개의 비트로 암호화되어 주어짐. 암호 코드 가로 길이는 56(무조건)
3. 올바른 암호 코드는 (홀수 자리 합 x 3) + (짝수 자리 합)이 10의 배수 되어야함

암호코드 1개가 포함된 직사각형 배열 읽음
직사각형 배열은 1, 0으로만 이루어져 있고, 암호코드 이외 부분은 전부 0
암호코드 정보가 포함된 2차원 배열을 입력으로 받아 올바른 암호코드인지 판별
'''

# import sys
# sys.stdin = open('tc.txt', 'r')

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    code = [input() for _ in range(N)]
    
    dic = {'0001101': '0', '0011001': '1', '0010011': '2', '0111101': '3',      # 딕셔너리에 번호 저장
           '0100011': '4', '0110001': '5', '0101111': '6', '0111011': '7',
           '0110111': '8', '0001011': '9'}
    
    changed_code = ''       # 암호
    result = 0              # 출력 값
    
    for i in range(N):
        for j in range(M-1, -1, -1):        # 행마다 열의 끝에서부터 탐색
            if code[i][j] == '1':           # 암호 이진수의 끝은 무조건 1임. 따라서 1 찾으면 끝의 7자리씩 탐색 시작
                for k in range(j, -1, -7):
                    string = code[i][k-6:k+1]
                    changed_code = dic.get(string, '') + changed_code       # 사전에 있으면 가져오고, 없으면 아무것도 추가하지 않음
            if len(changed_code) == 8:              # 8자리 채우면 열 탐색 종료
                break
        
    hol = 0     # 홀의자리 합
    zzak = 0    # 짝의자리 합
    
    for i in range(len(changed_code)):
        if i % 2:               # 인덱스를 나누기 때문에 2로 나눌때 나머지가 있으면 짝,
            zzak += int(changed_code[i])
        else:                   # 그렇지 않으면 홀.
            hol += int(changed_code[i])
        
    if ((hol * 3) + zzak) % 10 == 0:        # 조건에 맞춰 10으로 나눠떨어지지 않는다면 그냥 0 출력. 나눠 떨어지면 홀, 짝 더한 수 출력
        result = hol + zzak
    
    print(f'#{tc} {result}')