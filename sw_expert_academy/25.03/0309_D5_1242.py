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

# import sys
# sys.stdin = open('tc.txt', 'r')


def find_code(z):                   # 코드 8자리의 1과 0의 비율을 반환하는 함수
    all_code_rate = list()
    
    while True:                     # 같은 열에 두개 이상의 코드가 있을 수 있으므로 while
        rate = [0] * 32             # 0부터 31의 인덱스는 코드 한자리당 4자리씩, 총 8자리의 코드
        expand = 0                  # 이때까지 센 개수 기억
        
        for i in range(31, -1, -1):    # rate의 32자리에 해당 숫자의 비율을 넣어야함
            for j in range(len(z)-1-expand, -1, -1):        # 세었던 자리부터 인덱스 0 까지 탐색
                if i == 0:                                  # 만약 rate의 i번째 인덱스에 넣으려는데 마지막 자리이다? 그때 세는 건 0, 하지만 0은 코드가 아닌 부분과도 연결되있음.
                    zero_cut = 56 - (expand % 56)           # 그래서 코드는 항상 56의 배수이므로 56에서 56에 이때까지 센 expand를 나눈 나머지를 빼면 마지막 0의 개수를 알 수 있음.
                    rate[i] = zero_cut
                    break                                   # 어차피 마지막 0을 센것이라서 그대로 for문 종료
                elif i % 2:                                 # 코드의 0과 1은 차례로 번갈아가면서 나옴, 따라서 0을 세다가 1이나오면 인덱스를 바꾸고 1을 세다가 0이 나오면 인덱스를 바꾸는 형식으로 리스트에 넣으면 됨
                    if z[j] == '1':                         # 1이 계속 나와야 다음 자리도 확인
                        rate[i] += 1
                    else:                                   # 0이나오면 다음 rate의 인덱스로 이동(0이나올 차례이기 때문)
                        break
                else:                                       # 0나와야할 차례
                    if z[j] == '0':                         # 0이 나와야 다음 자리도 확인
                        rate[i] += 1
                    else:                                   # 1나오면 다음 rate의 인덱스로 이동(1이 나와야할 차례)
                        break
            expand += rate[i]                               # 세었던 자리를 기억.
    
        all_code_rate.append(rate)                          # 8자리 코드를 알아낼 수 있는 비율을 저장
        
        z = z[:-expand]                                     # 만약 한줄에 다른 코드도 있을 수 있기 때문에 마지막에 세었던 자리인 expand까지 슬라이싱.
        
        if z.count('1') == 0:                               # 만약 잘라낸 코드에 1이 없으면, 남은 코드 없으므로 while문 종료
            break
        else:                                               # 만약 있으면 오른쪽 0모두 잘라내고 다시 코드 비율 탐색 시작
            z = z.rstrip('0')
            
    return all_code_rate                                    # 찾아낸 코드들의 비율을 반환
    

T = int(input())

binary_dic = {'0': '0000', '1': '0001', '2': '0010', '3': '0011', '4': '0100',      # 16진수를 2진수로 변환하기 위한 딕셔너리
                  '5': '0101', '6': '0110', '7': '0111', '8': '1000',
                  '9': '1001', 'A': '1010', 'B': '1011', 'C': '1100',
                  'D': '1101', 'E': '1110', 'F': '1111'}
    
code_dic = {(3, 2, 1, 1): 0, (2, 2, 2, 1): 1, (2, 1, 2, 2): 2,          # 2진수중 0과 1의 비율이 뜻하는 숫자들을 나타낸 딕셔너리
            (1, 4, 1, 1): 3, (1, 1, 3, 2): 4, (1, 2, 3, 1): 5,
            (1, 1, 1, 4): 6, (1, 3, 1, 2): 7, (1, 2, 1, 3): 8,
            (3, 1, 1, 2): 9}

for tc in range(1, T+1):
    N, M = map(int, input().split())
    raw_code = [input()[:M] for _ in range(N)]
    raw_code_2 = list(set(raw_code))            # 받은 입력값들 중 중복된 줄 삭제
    code_lst = list()
    
    for i in range(len(raw_code_2)):
        string = ''
        for j in range(len(raw_code_2[i])):
            string = string + binary_dic[raw_code_2[i][j]]      # 16진수 모두 딕셔너리 통해 2진수로 변환
        if string and string.count('1'):                        # 만약 string에 담긴 문자가 있고, 1의 개수가 하나라도 있따면 오른쪽 0 모두 잘라내고 code_lst에 저장
            code_lst.append(string.rstrip('0'))

    result = 0          # 결과(홀 자리, 짝 자리 합)
    dup_code = []       # 중복 코드
    
    for i in code_lst:      # code_lst에 코드가 몇개 담긴지 모르는 한 줄이 주어짐.
        code_rate = find_code(i)            # find_code 함수 실행하면 code_rate에 코드의 비율이 담긴 리스트가 반환됨
        
        for j in code_rate:     # 반환된 리스트에 담긴 비율들을 탐색
            if j not in dup_code:       # 만약 중복코드에 이 비율이 없다면(비율이 곧 해석된 코드이기 때문에 비율만 모두 같아도 똑같은 값이 나오는 코드임)
                dup_code.append(j)      # 중복된 코드 리스트에 넣음
                
                hol = 0     # 홀, 짝 넣을 변수
                zzak = 0
                idx2 = 0    # 홀 짝 자리 나타낼 인덱스 변수
                
                for k in range(0, 32, 4):
                    idx2 += 1                   # 자릿수 1부터 8까지
                    sub = j[k:k+4]              # 4자리씩 끊어서 확인
                    min_rate = min(j[k:k+4])    # 가장 작은 수를 구해서
                    
                    for m in range(4):          # 4자리 모두 비율 최솟값을 나누면
                        sub[m] //= min_rate
                        
                    sub2 = tuple(sub)           # 최종 비율 완성
                    
                    if k == 28:                 # 마지막 8번째 자리는 inspection
                        inspection = code_dic[sub2]
                        break
                    elif idx2 % 2:              # 홀수 자릿수
                        hol += code_dic[sub2]
                    else:                       # 짝수 자릿수
                        zzak += code_dic[sub2]
                    
                sub_result = ((hol * 3) + zzak)     # 올바른 코드인지 확인하는 공식

                if inspection == (10 - (sub_result % 10)) % 10:     # inspection이 sub_result의 합을 이룰때 10의 배수가 될 수 있는 수라면 그 코드는 올바른 코드
                    result += (hol + zzak + inspection)             # 최종 결과에 모든 자릿수를 더한 값을 더해줌
            
    print(f'#{tc} {result}')