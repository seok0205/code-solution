# keymap이라는 자판이 있다. 이 자판은 키 하나에 여러 숫자가 포함되어 있는데, 1번 누를때마다 바뀐다.(중복 숫자도 포함 가능)
# targets를 치기위해서 키를 몇번 눌러야 하는지 단어마다 최소값을 찾아서 구하는 문제.
# 문자열을 타이핑하지 못할땐 -1을 출력한다.

keymap = ['ABACD', 'BCEFD']
targets = ['ABCD', 'AABB']
result = []
dict = {}

for i in range(len(keymap)):    # 키맵에 있는 모든 글자를 딕셔너리에 집어넣는다.
    for j in range(len(keymap[i])):
        word = keymap[i][j]
        if word not in dict:    # 문자가 딕셔너리에 처음들어간다면 해당 인덱스를 넣고,
            dict[word] = (j + 1)
        else:   # 이미 같은 문자, 키값이 존재한다면 작은 밸류을 딕셔너리에 넣는다.
            dict[word] = min(dict[word],(j + 1))

for i in targets:   # 타이핑 횟수를 구하기 위한 for문.
    cnt = 0 # 단어 하나의 타이핑 수
    for j in i: # 단어 하나의 문자 하나하나 탐색.
        if j in dict:   # 사전에 있다면 
            cnt += dict[j]  # 해당 밸류를 타이핑 횟수에 더함.
        else:   # 사전에 없다면
            cnt = -1    # 만들 수 없는 단어이므로 -1 출력.
            break   # 즉시 for문에서 빠져나옴.
    result.append(cnt)  # 도출된 합을 result에 추가.

print(result)

# 딕셔너리를 쓰는 이유 :
# 키와 밸류만 저장해서 리스트보다 적은 메모리를 사용한다. 내부적으로 해시 테이블을 사용해서 검색 속도도 빠름.
# 따라서 데이터 검색이 많으면 딕셔너리가 효율적이고 유용하다.