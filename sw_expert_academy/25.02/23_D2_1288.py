'''
D2 1288 새로운 불면증 치료법

양 세기를 진행. 첫번째는 N번 양, 그 뒤로 2N양, k번째는 kN번 양을 셈
몇번을 세야 0~9 모든 숫자를 볼 수 있는지 구하는 문제
모든 자릿수에 상관없이 구할 수 있음
'''

T = int(input())

for tc in range(1, T+1):
    N = int(input())
    N_str = str(N)          # 자릿수 탐색 위한 문자열 변경
    
    num_lst = list()        # 나타나는 수 담을 리스트
    time = 1                # 세는 횟수
    
    while True:             # 조건 충족되면 멈춰야하므로
        for num in N_str:               # 문자열 자릿수마다 탐색
            if num not in num_lst:      # 새 숫자 출현시 리스트에 추가
                num_lst.append(num)
         
        if len(num_lst) == 10:          # 0부터 9까지 찾으면 되는 것. 길이 10채우면 반복문 탈출
            break
        
        time += 1       # 다 못찾았으면 다음 횟수 준비
        
        N_int = N * time        # kN번째 수 구한 뒤
        N_str = str(N_int)      # 탐색 위해 문자열로 변형
        
    print(f'#{tc} {N_int}')     # 마지막으로 설정된 N_int 출력