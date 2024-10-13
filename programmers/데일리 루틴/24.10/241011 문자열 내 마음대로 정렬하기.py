def solution(strings, n):
    result = []
    for i in strings:   #입력받은 문자열 길이만큼 반복
        result.append(i[n] + i) #기준이되는 n번째 인덱스를 제일 앞자리로 추가해서 리스트 재생성
    result.sort()   #앞자리에 기준 알파벳이 있기에, 재생성한 리스트를 정렬한다.
    result = [i[1:] for i in result]    #앞자리를 빼고 슬라이싱한 원소를 다시 result에 저장.
    return result

def othersolution(strings, n):
    return sorted(strings, key=lambda x: x[n])
#strings의 문자열들을 n번째 글자를 기준으로 정렬해서 반환.