arr1, arr2 = [], []

N, M= map(int, input().split()) #배열의 크기 정할 변수 입력.

for i in range(N):
    i = list(map(int, input().split()))
    arr1.append(i)  #행 개수 만큼 반복. list.append() 활용해서 arr1배열에 입력한 행 차례로 추가.

for i in range(N):
    i = list(map(int, input().split()))
    arr2.append(i)  #위와 같이 arr2배열에 입력.

for i in range(N):
    for j in range(M):
        print(arr1[i][j] + arr2[i][j], end=' ') #배열의 합은 같은 자리에 있는 수를 각각 더하면 됨. 출력값 사이간 공백 추가.