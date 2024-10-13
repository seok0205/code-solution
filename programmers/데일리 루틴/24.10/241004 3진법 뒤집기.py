def solution(n):
    answer = '' #답을 저장할 변수.

    while n >= 1:   #n이 0이 될때까지 반복.
        rest = n % 3    #3으로 나눈 나머지를 answer에 집어넣기 위해 따로 rest에 저장.
        n = n // 3  #3으로 나눈 몫은 n으로 재설정.
        answer += str(rest) #뒤집어서 10진화 해야하기 때문에 굳이 일의자리부터 넣지않아도 됨.
    return int(answer, 3)   #int에 기준진법을 통해서 10진법으로 변화시킬수 있다.

def solution(n):
    answer = ''

    while n >= 0:			
        n, rest = divmod(n,3)	#divmod()함수 통해 몫, 나머지를 구할 수 있다.
        answer += str(rest)
    return int(answer, 3)