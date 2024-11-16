'''
수확한 귤 k개를 골라 상자 하나에 담아 판매혀려고 함.
예로 수확한 귤 8개 크기가 [1, 3, 2, 5, 4, 5, 2, 3] 일 때, 6개를 판매하고 싶다면 크기가 1, 4인 귤을 제외한 여섯 개의 귤을 상자에 담으면 2, 3, 5로 총 3가지가 된다. 이 때가 서로 다른 종류가 최소일 때.
귤 개수 k와 크기를 담은 배열 tangerine이 매개변수.
k일 때, 크기가 서로 다른 종류의 수를 최솟값으로 return 하도록 작성.

제한 사항 :
1 <= k <= len(tangerine) <= 100,000
1 <= tangerine[i] <= 10,000,000

접근 :
1. 먼저 요소별로 공통 요소 개수 센 num리스트에 추가.
2. 공통 개수 추출 한 것 중 큰 것 부터 k에서 뺌. 뺀 요소는 num에서 제거.
3. k가 0이 될 때까지 반복한 횟수 출력.
'''

'''
오답 코드 : 시간 초과

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
num = []
t = set(tangerine)

for i in t:
    a = tangerine.count(i)
    num.append(a)

num.sort(reverse=True)

for i in range(len(num)):
    k -= num[i]
    if k <= 0:
        result = i + 1
        break
'''

k = 6
tangerine = [1, 3, 2, 5, 4, 5, 2, 3]
result = 0
t = {}

for i in tangerine: # 리스트에 등장 할 때마다 t딕셔너리의 키값 1 상승.
    if i in t:  # 존재하면 1 증가.
        t[i] += 1
    else:   # 새로 등장한 수면 키값 1로 등록.
        t[i] = 1

'''
핵심. t에 저장된 내용을 기존 t의 value의 값들을 기준으로 내림차순으로 정렬.(높은 수를 먼저 k값에서 빼야하므로)

lambda식을 활용한 딕셔너리 정렬 :
sorted(t.keys(). key=lambda x: x) # key 출력(list).
sorted(t.values(), key=lambda x: x) # value 출력(list).
sorted(t, key=lambda x: t[x]) # 딕셔너리 t의 key를 x에 넣어 t[x], value로 정렬해서 key 출력(list).
sorted(t.items(), key=lambda x: x[0]) # 딕셔너리 key, value 쌍을 x에 넣어 정렬해서 출력 x[0]은 key, x[1]은 value(tuple in list).
'''
t = dict(sorted(t.items(), key=lambda x: x[1], reverse=True))   # 참고 부분!

for i in t: # 정렬된 딕셔너리 순서대로
    if k <= 0:  # k가 0보다 작거나 같을 때까지
        break
    k -= t[i]   # k가 0보다 아직 크면 차례로 t의 value값(귤의 개수)을 뺌.
    result += 1 # 반복 횟수 누적(즉, 상자에 포함된 크기별 종류가 1 증가.)

print(result)   # result값 출력.