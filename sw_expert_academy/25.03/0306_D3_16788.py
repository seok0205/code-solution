'''
D3 16788 이진수2

0보다 크고 1미만인 십진수 N을 이진수로 바꾸려함. 예로 0.625를 이진수로 바꾸면 0.101이 됨

N을 소수점 아래 12자리 이내인 이진수로 표시할 수 있으면 0.을 제외한 나머지 숫자 출력,
13자리 이상이 필요한 경우 overflow를 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def change(a):
    x = float(a)    # 입력받은 인자를 float 자료로 지정
    string = ''     # 이진화한 결과 담기
    idx = -1        # 첫 idx(소수점 첫째 자리)
    num = 0         # 이진화 하면서 자리마다 늘어나는 수 담을 변수
    
    while True:
        if num >= x:    # 만약 구하려는 수보다 더해간 수가 같거나 넘어가는 순간 탈출
            break
        
        if x - num >= 2**(idx):     # 목표 수와 현재까지 더한 수의 차가 이번에 늘어날 수보다 크면
            num += 2**(idx)         # num에다가 더해줌
            string += '1'           # 이번 자리는 1
        else:                       # 만약 차가 이번에 더할 수 보다 작으면
            string += '0'           # 더하면 안됨. 이번 자리 0
            
        idx -= 1                    # 다음 소수점 자리를 위해 idx -1
        
    if len(string) > 13:            # 이진화 완료했는데 13자리 이상이면 overflow 반환
        return 'overflow'
        
    return string


T = int(input())

for tc in range(1, T+1):
    N = input()
    
    result = change(N)
    
    print(f'#{tc} {result}')