'''
옷을 매일 다른 조합으로 입으려고 한다.
가진 옷들을 담은 2차원 배열이 주어질 때, 서로 다른 옷의 조합의 수를 return 하는 문제.

조건 :
각 종류별로 최대 1가지 의상만 착용 가능.
착용 의상 일부가 겹쳐도, 다른 의상이 겹치지 않거나, 혹은 의상을 추가로 더 착용한 경우에 서로 다른 방법으로 옷을 착용한 것으로 계산.
하루에 최소 하나의 의상은 착용.

제한 사항 :
배열의 각 행은 [의상이름, 의상종류].
의상 수는 1개 이상 30개 이하.
같은 이름 존재 X.
모든 원소는 문자열.
문자열 길이는 1 이상 20 이하 자연수, 알파벳 소문자 혹은 언더바로 이루어짐.
'''

clothes = [["yellow_hat", "headgear"], ["blue_sunglasses", "eyewear"], ["green_turban", "headgear"]]

result_1 = 0
result_2 = 1
species = {}    # 의상 종류 구분 위한 딕셔너리 생성.
species_list = []   # 의상 가짓수 리스트.

for i in range(len(clothes)):   # 딕셔너리에 의상 종류당 개수 저장.
    if clothes[i][1] not in species:
        species[clothes[i][1]] = 1
    elif clothes[i][1] in species:
        species[clothes[i][1]] += 1

print(species)

for i in species.keys():    # key 값 당 value에 1을 더해서 의상 가짓수 리스트에 추가.(더한 1은 아예 안입는 경우)
    species_list.append(species[i] + 1)
    
for i in species_list:  # species_list에 저장된 값들을 전체 경우의 수 구하기 위해 곱함.
    result_2 *= i

print(result_2 - 1) # 모두 안입는 경우가 포함되어 있어서 1을 빼줘야함. 최소 하나는 입어야하기 때문.

'''
해시 활용한 풀이.

# 옷 종류별로 구분
hash_map = {}
for clothe, type in clothes:
    hash_map[type] = hash_map.get(type, 0) + 1

# 입지 않은 경우 추가해 모든 조합 계산
result = 1
for type in hash_map:
    result *= (hash_map[type] + 1)

# 아무 옷도 입지 않는 경우 제외(기본 조건)
return result - 1
'''