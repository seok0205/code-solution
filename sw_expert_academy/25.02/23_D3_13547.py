'''
D3 13547 팔씨름

소정, 세정이 15번 팔씨름하여 과반횟수 이상 이기는 사람이 승리
k번의 팔씨름 진행중, 길이가 k인 o,x로만 이루어진 문자열 주어짐
S[i]가 o면 소정이가 승, x면 패배
15번째 경기까지 했을 때 승리할 가능성을 구하는 문제
승리할 수 있으면 'YES', 아니면 'NO'출력
'''

T = int(input())

for tc in range(1, T+1):
    records = input()
    
    lose = 0
    
    for record in records:      # 전적 중 패배 횟수 확인
        if record == 'x':
            lose += 1
            
    if lose < 8:        # 이때까지 전적중 패배가 8번만 넘지 않으면 승리할 가능성은 무조건 존재
        result = "YES"
    else:
        result = "NO"
        
    print(f'#{tc} {result}')