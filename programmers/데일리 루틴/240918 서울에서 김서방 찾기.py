def solution(seoul):
    for i in range(len(seoul)): #입력받은 리스트 길이만큼 kim과 비교. 인덱스와 함께 문장출력
        if seoul[i] == 'Kim':
            return f'김서방은 {i}에 있다'