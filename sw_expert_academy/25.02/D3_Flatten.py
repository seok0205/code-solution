def is_flatten(lst):    # 평탄화가 되었는지 확인하는 함수
    '''
    :param lst: 박스의 높이 담은 리스트
    :return: True, False
    '''
    check = [0] * 100   # 수의 등장 횟수 담을 리스트
    for i in range(len(lst)):   # 리스트 순회
        check[i] += 1   # 수 등장하면 해당 인덱스 1 증가
    if check.count(0) >= 98:    # 0의 개수가 98개 이상이면 리스트에 숫자가 2개밖에 없다는 것이므로 평탄화 완료
        return True
    else:
        return False


for tc in range(1, 11):
    dump = int(input())
    box_height = list(map(int, input().split()))

    for _ in range(1, dump+1):  # 덤프 횟수 만큼 반복
        max_index, max_height, min_index, min_height = [0, 0, 0, 100]   # min은 높이가 최대 100이므로 초기값 100을 설정 그래야 순회하며 서서히 줄어듬

        for i in range(len(box_height)):    # 각 최댓값, 최솟값의 인덱스와 높이를 구함
            if box_height[i] > max_height:
                max_index = i
                max_height = box_height[i]
            if box_height[i] < min_height:
                min_index = i
                min_height = box_height[i]

        box_height[max_index] -= 1  # 최대 높이의 박스 하나 빼고,
        box_height[min_index] += 1  # 최소 높이의 박스에 하나 더함

        if is_flatten(box_height):  # 평준화가 되있으면 즉시 반복문 탈출
            break

    max_box = 0
    min_box = 100

    for i in range(len(box_height)):    # 최댓값, 최솟값 구함
        if max_box < box_height[i]:
            max_box = box_height[i]
        if min_box > box_height[i]:
            min_box = box_height[i]

    result = max_box - min_box  # 차 출력
    print(f'#{tc} {result}')
