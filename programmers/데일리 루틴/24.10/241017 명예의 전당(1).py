#가수들이 정해진 기간 동안 하루에 한명씩 노래를 부른다. 상위 k명은 명예의전당에 기록된다. 따라서 k일 이후부터는 명예의 전당의 점수 목록이 뒤바뀐다.
#하루마다 갱신되는 명예의 전당에서 각 날마다의 최저점수를 담은 배열을 구하는 문제.

k = 3
score = [10, 100, 20, 150, 1, 100, 200]

halloffame = [] #명예의 전당
result = [] #각 날마다 명예의 전당에서의 최저 점수

for i in score: #점수 개수가 곧 가수의 인원 및 진행 기간.
    halloffame.append(i)    #그 날의 점수 명예의 전당에 기입.
    if len(halloffame) > k: #만약 명예의 전당 기록 한도에 도달한 경우
        halloffame.remove(min(halloffame))  #명예의전당에서 최저점수를 삭제.
    result.append(min(halloffame))  #일간 꼴찌 점수를 배열에 저장. 

print(result)