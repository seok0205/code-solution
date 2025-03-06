'''
D3 16786 이진수

16진수 1자리는 2진수 4자리로 표시
N자리 16진수가 주어지면 각 자리 수를 4자리 2진수로 표시하는 문제

단, 2진수의 앞자리 0도 반드시 출력
'''

# import sys
# sys.stdin = open('tc.txt', 'r')


def change(a):
    string = '0123456789ABCDEF'     # 16진수 변환 스트링
    binary = ''     # 이진수 저장
    
    for i in range(len(string)):    # 16진수 변환 스트링에서 a의 문자열과 같은 부분의 인덱스 지정
        if string[i] == a:
            x = i
            break
    
    while x > 0:        # 해당 인덱스를 이진수로 변환해야함
        if x % 2:
            binary = '1' + binary
        else:
            binary = '0' + binary
        x //= 2
        

    while len(binary) < 4:      # 만약 x가 작아서 4비트를 못채운면 앞자리에 0을 채워줌
        binary = '0' + binary
    
    return binary       # 만들어진 이진수 변환


T = int(input())

for tc in range(1, T+1):
    N, N_HEX = map(str, input().split())
    result = ''
    
    for i in range(int(N)):
        result += change(N_HEX[i])
        
    print(f'#{tc} {result}')