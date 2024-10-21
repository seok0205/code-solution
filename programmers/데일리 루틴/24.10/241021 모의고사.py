#문제를 풀때 문항을 찍을려고한다. 일정한 규칙대로 찍으려고 하는 법을 구하는 문제.
#시험은 10000문제로 구성되어있고, 문제의 정답은 1번에서 5번 사이에 존재.
#가장 높은 점수 받은 사람이 여럿일 경우, return하는 값을 오름차순 정렬.

answers = [1, 3, 2, 4, 2]

def solution(answers):
    answer_1 = [1, 2, 3, 4, 5]  #각 학생의 답안 순서.
    answer_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    answer_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    score = [0 for i in range(3)]   #점수 담을 0이 3개인 배열 생성.
    result = [] #결과값
    for i in range(len(answers)):   #총 문제의 개수만큼 반복.
        if(answer_1[i%len(answer_1)] == answers[i]):    #답과 답안이 같으면 점수 1증가.(세 학생 모두 동일.)
            score[0] += 1
        if(answer_2[i%len(answer_2)] == answers[i]):
            score[1] += 1
        if(answer_3[i%len(answer_3)] == answers[i]):
            score[2] += 1
    for i in range(len(score)): #학생 3명의 최고 점수 알아내기.
        if(score[i] == max(score)): #score의 학생 점수가 배열 값중 최대와 같다면 배열에 추가.
            result.append(i+1)  #1번학생 2번학생 3번학생 차례로 인덱스는 0,1,2라서 1씩 더해야함.
    result.sort()   #정렬.
    return result

print(solution(answers))