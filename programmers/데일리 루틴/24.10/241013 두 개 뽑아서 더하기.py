def solution(numbers):
    answer = [] #두 수의 합을 저장할 배열.
    for i in range(len(numbers)):   #원소들을 하나씩 비교하기 위해 입력한 numbers 배열의 길이만큼 반복.
        for j in range(len(numbers)):   
            if i == j:  #같은 인덱스 끼리는 합을 구하지 않는다. 건너뜀.
                continue
            if numbers[i] + numbers[j] not in answer:   #만약 합을 저장한 공간에 똑같은 수가 존재한다면 추가하지 않음. 새로운 값만 저장함.
                answer.append(numbers[i]+numbers[j])
    answer.sort()   #크기순으로 정렬.
    return answer

numbers = [2, 1, 3, 4, 1]
print(solution(numbers))