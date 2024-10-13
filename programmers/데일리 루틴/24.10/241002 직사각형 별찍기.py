a, b = map(int, input().strip().split(' ')) #두 변 입력받음.

for i in range(b):  #b는 세로변. 따라서 반복문으로 표현.
    print('*' * a)  #밑변 길이만큼 '*' 출력.