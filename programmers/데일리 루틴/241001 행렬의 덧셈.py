def solution(arr1, arr2):
    result = [[0 for i in range(len(arr1[0]))] for i in range(len(arr1))]
    #result는 arr1, 2의 덧셈을 저장할 것이기 때문에, arr1, 2와 똑같은 배열 형태를 가져야함.

    for i in range(len(arr1)):  #arr1 2차원 배열 길이만큼 반복.
        for j in range(len(arr1[i])):   #arr1의 1차원 배열 길이.
            result[i][j] = arr1[i][j] + arr2[i][j]  #각 같은 위치에 있는 원소들을 더해서 result배열에 저장.

    return result