#카드 뭉치 두 개로 goal의 문장을 만들 수 있는지 확인하는 문제
#단 카드 뭉치의 단어들은 인덱스 순서대로만 쓸수 있다. 하지만 각각의 뭉치는 번갈아가면서 사용이 가능하다.
#카드는 반드시 사용을 하고 다른 카드 뭉치로 넘어가야한다.
#한 번 사용한 카드는 재사용이 불가능하다.

cards1 = ["i", "water", "drink"]
cards2 = ["want", "to"]
goal = ["i", "want", "to", "drink", "water"]

def solution(cards1, cards2, goal):
    cards1_count = 0    #각 카드 뭉치의 인덱스 담당 변수
    cards2_count = 0

    for i in range(len(goal)):  #목적 단어의 단어 개수만큼 반복
        if cards1_count < len(cards1) and goal[i] == cards1[cards1_count]:  #카드 뭉치의 허용 인덱스 내에서, 목적의 단어와 카드 뭉치의 단어가 일치.
            cards1_count += 1   #재사용 불가, 뭉치의 다음 단어로 넘어가기 위함.
        elif cards2_count < len(cards2) and goal[i] == cards2[cards2_count]:
            cards2_count += 1
    return 'Yes' if cards2_count + cards1_count == len(goal) else 'No'  #목적의 단어 갯수와 각 카드 뭉치의 사용 횟수가 같으면 문장을 성공적으로 만들 수 있다는 증거. 조건 만족 시 Yes, 그렇지 않으면 No 출력.

print(solution(cards1, cards2, goal))