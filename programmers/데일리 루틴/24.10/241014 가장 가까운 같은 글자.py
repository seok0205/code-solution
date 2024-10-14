#S 문자열에서 각 위치마다 자신보다 앞에 나왔으면서, 자신과 가장 가까운 곳에 있는 같은 글자가 어디 있는지 알려주는 문제.
# ex) foobar > [-1, -1, 1, -1, -1, -1]

s = 'banana'
answer = [] #변환한 숫자 배열
alphabet = {}   #알파벳: 인덱스 형태의 딕셔너리

for i in range(len(s)): #총 문자열 길이만큼 반복
    if s[i] not in alphabet:    #딕셔너리에 해당 알파벳이 없다면 처음 출현한 알파벳이므로 배열에 -1 추가(인덱스만 다른 형태면 새로운 인덱스로 저장.)
        answer.append(-1)
    else:   #만약 딕셔너리에 존재한다면, 
        answer.append(i-alphabet[s[i]]) #현재 인덱스에서 딕셔너리에 저장되어있는 인덱스를 빼서 차를 배열에 추가.
    alphabet[s[i]] = i  #한 자리 한 자리 딕셔너리에 모두 추가.

print(answer)