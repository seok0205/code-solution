def solution(array, commands):  #array와 i,j,k가 순서대로 입력되어있는 commands 입력받음.
    answer = [] #array에서 i번째부터 j번째까지 슬라이싱한 리스트중 정렬한 상태에서의 리스트의 k번째 수를 저장.
    for i in range(len(commands)):  #commands의 길이가 곧 테스트 케이스 개수.
        result = array[commands[i][0]-1:commands[i][1]] #array의 i번째부터 j번째 인덱스까지 슬라이싱
        result.sort()   #정렬.
        answer.append(result[commands[i][2]-1]) #k번째 수 answer에 저장.
    return answer