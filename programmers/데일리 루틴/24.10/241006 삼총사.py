#학생들이 보유한 고유 정수의 배열이 주어짐. 학생들끼리의 합이 0이라면 삼총사. 주어진 배열에서 삼총사의 경우의 수를 구하는 문제.

def solution(number):
    answer = 0  #삼총사의 경우의 수.
    for i in range(len(number)): #경우의 수를 구하기 위해 중복 for문 사용. i는 첫번째 학생.
        for j in range(i+1, len(number)):   #첫번째 학생을 제외한 나머지 학생중 두번째 학생 선택.
            for k in range(j+1, len(number)):   #이전 선택한 학생들과 겹치지않게 세번째 학생 선택.
                if number[i] + number[j] + number[k] == 0:  #모든 학생들이 보유한 정수의 합이 0이라면 삼총사 경우의수 1증가.
                    answer += 1
    return answer

number = [-2, 3, 0, 2, -5]
print(solution(number))