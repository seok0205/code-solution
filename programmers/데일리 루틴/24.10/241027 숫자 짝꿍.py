# X와 Y에서 존재하는 공통된 짝꿍의 수(100과 102에서 1과 0은 각각 짝꿍.)
# 짝꿍으로 이루어진 최대 수를 출력하는 문제. ex. 짝꿍의 수가 5,6,1,2일 때, 최대수는 6521.
# 단 0만으로 짝꿍 수가 이루어져 있으면 0출력. 같은 수가 하나도 없으면 -1 출력.

X = '100'
Y = '203045'

def solution(X, Y):
    answer = '' #최대 수 집어넣을 변수

    for i in range(9, -1, -1):  #9부터 0까지 탐색.
        answer += (str(i) * min(X.count(str(i)), Y.count(str(i))))  
        #어차피 큰 수는 짝꿍수를 정렬한 수이므로, 큰수가 여러개 겹친다면 큰수가 먼저나오게 되어있다.
    if answer == '':    #같은 수가 없다면 -1출력.
        return '-1'
    elif len(answer) == answer.count('0'):  #0만으로 이루어져있다면, 0출력.
        return '0'
    else:
        return answer
    
print(solution(X,Y))