#숫자로 이루어진 문자열 t, p가 주어질 때, t에서 p와 길이가 같은 부분문자열 중에서 ex) 1003 = t, 4 = p일 때, t의 부분 문자열은 한 자리.
#p가 나타내는 수보다 작거나 같을 때의 t 부분 문자열 개수를 구하여라

def solution(t, p):
    count = 0   #p보다 작거나 같은 t의 부분 문자열 개수.
    for i in range(len(t) - len(p) + 1):    #길이는 부분 문자열의 경우의 수만큼만 반복.
        if int(t[i:i+len(p)]) <= int(p):    #p와 t부분 문자열은 자릿수가 같음. 따라서 슬라이싱을 다음과 같이 진행.
            count += 1 #조건 만족시 count +1.
    return count