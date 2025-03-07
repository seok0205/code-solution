'''
D5 1242 암호코드 스캔

암호 규칙
1. 총 8개 숫자
2. 앞 7자리는 상품 고유 번호, 마지막 자리는 검증 코드
    - '(홀수 자리 합 x 3) + 짝수 자리 합 + 검증 코드'가 10의 배수여야함

코드를 인식하는 스캐너의 성능
1. 세로 2000, 가로 500 이하 직사각형 배열에 암호코드 정보 포함해 전달됨
2. 배열은 16진수, 이 배열을 2진수로 변환해 그 안에 포함된 암호코드 정보 확인
3. 배열에는 1개 이상 암호코드 존재(비정상 암호코드 포함 O)
4. 포함된 암호코드들의 고유 번호, 검증코드 확인해 정상여부 판별, 이 정상 암호코드들에 포함된 숫자의 합을 출력
5. 소요 시간 적을 수록 성능 좋은 것으로 간주

암호코드의 세부 규칙
1. 암호코드 하나는 8개 숫자(고유 7, 검증 1)
2. 각 숫자 하나가 차지하는 최소 칸수는 7, 최소 가로길이는 56
3. 가로 길이는 선 두께에 따라 달라짐. 선이 굵어지면 56배수의 길이 가짐
    - 예로 숫자 하나가 14칸 사용 시, 암호코드 하나 가로길이는 112.
    - 암호코드 하나에 포함된 암호코드 숫자들은 모두 동일한 크기 가짐
4. 암호코드 시작 구분선, 종료 구분선은 별도 존재 X
5. 암호코드 세로 길이는 5~100칸
6. 암호코드들이 붙어있는 경우 존재 X(각 암호코드의 둘레엔 최소 1칸 이상 빈 공간 존재)
'''

import sys
sys.stdin = open('tc.txt', 'r')


def find_code(z):
    lst = list()
    cnt = 1
    for i in range(len(z)):
        if i == len(z)-1:
            lst.append(cnt)
        elif z[i] == z[i+1]:
            cnt += 1
        else:
            lst.append(cnt)
            cnt = 1
    
    print(lst)
    a = min(lst)
    for i in range(4):
        lst[i] //= a
        
    return tuple(lst)
    

T = int(input())

for tc in range(1, T+1):
    N, M = map(int, input().split())
    raw_code = [input()[:M] for _ in range(N)]
    code_lst = list()
    
    binary_dic = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',
                  '5': '0101', '6': '0110', '7': '0111', '8': '1000',
                  '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
                  'D': '1101', 'E': '1110', 'F': '1111'}
    
    code_dic = {(3, 2, 1, 1): '0', (2, 2, 2, 1): '1', (2, 1, 2, 2): '2',
                (1, 4, 1, 1): '3', (1, 1, 3, 2): '4', (1, 2, 3, 1): '5',
                (1, 1, 1, 4): '6', (1, 3, 1, 2): '7', (1, 2, 1, 3): '8',
                (3, 1, 1, 2): '9'}
    
    for i in range(N):
        string = ''
        for j in range(M):
            if raw_code[i][j] in binary_dic.keys():
                string = string + binary_dic[raw_code[i][j]]
            else:
                if string and string not in code_lst:
                    code_lst.append(string)
                string = ''

    result = 0
    print(code_lst)
    
    if code_lst:
        for i in range(len(code_lst)):
            a = len(code_lst[i])
            num = ''
            for j in range(a):
                if int(code_lst[i][a-1-j]):
                    num += code_lst[i][:a-j]
                    break
                
            if len(num) < 56:
                for _ in range(56-len(num)):
                    num = '0' + num
            
            b = len(num) % 56
            num = num[b:]
            length = len(num)
            
            if length // 56:
                expand = -7 * (length // 56)
            else:
                expand = -7
            
            hol = 0
            zzak = 0
            
            for k in range(length-1, -1, expand):
                if k == length-1:
                    sub1 = num[k+(expand+1):k+1]
                    sub1 = find_code(sub1)
                    inspection = int(code_dic[sub1])
                elif k % 2:
                    sub2 = num[k+(expand+1):k+1]
                    sub2 = find_code(sub2)
                    zzak += int(code_dic[sub2])
                else:
                    sub3 = num[k+(expand+1):k+1]
                    sub3 = find_code(sub3)
                    hol += int(code_dic[sub3])
                
            sub_result = ((hol * 3) + zzak)

            if inspection == 10 - (sub_result % 10):
                result += (hol + zzak + inspection)
            
    print(f'#{tc} {result}')