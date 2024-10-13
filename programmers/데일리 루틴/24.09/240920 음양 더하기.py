#absolutes에 절대값, signs에 True와 False로 부호를 저장.
#True면 총합에 절대값을 더하고 False면 절대값을 뺀다.

def solution(absolutes, signs):
    answer = 0  #결과 저장할 변수
    for i in range(len(absolutes)): #절댓값 담은 리스트 길이만큼 반복.
        if signs[i] == True:    #signs의 인덱스와 같은 absolutes 인덱스의 절대값을 더함.
            answer += absolutes[i]
        else:   #signs의 인덱스와 같은 absolutes 인덱스의 절대값을 뺌.
            answer -= absolutes[i]
    return answer