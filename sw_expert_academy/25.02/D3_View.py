'''
10
0 0 254 185 76 227 84 175 0 0
'''

N = int(input())
height = list(map(int, input().split()))

result = 0

for i in range(2, N - 2):   # 맨 왼편의 2칸, 맨 오른편 2칸은 건물이 없어서 순회할 건물이 있을곳만 범위로 설정
    leftside = max(height[i - 1], height[i - 2])    # 왼편의 건물들의 높이 중 더 높은 건물
    rightside = max(height[i + 1], height[i + 2])   # 오른편의 건물들의 높이 중 더 높은 건물
    if leftside < height[i] and rightside < height[i]:  # 만약 왼, 오른편의 건물이 모두 본 건물보다 낮다면? 조망권이 확보되는 층이 있다는 의미
        result += height[i] - max(leftside, rightside)  # 결괏값인 조망권이 확보되는 층수 값에 본 건물과 가장 높은 건물과의 차이 더함.

print(result)

'''
어떤 아파트는 양쪽 모두 2 이상의 거리의 공간이 확보될 때 조망권이 확보된다.
아파트들의 높이가 주어질 때, 조망권을 확보한 층수의 총합을 구하는 문제

제약 사항:
가로 길이 1000이하, 맨 왼, 오른쪽 두칸은 아파트 없음. ex) [0,0,10,15,0,0]
건물 최대 높이 255

접근 방법:
건물의 조망권을 얻으려면 주변 건물이 모두 본건물보다 낮아야함. 그러면 양옆 합쳐서 4칸의 건물이 본 건물보다 낮아야하고,
그 4개의 건물중 가장 높은 건물과의 차이가 본 건물의 조망권이 확보되는 층수!
'''

for tc in range(1, 11):
    N = int(input())
    height = list(map(int, input().split()))

    result = 0

    def Bubblesort(arr, N):
        for i in range(N-1, 0, -1):
            for j in range(i):
                if arr[j] > arr[j+1]:
                    arr[j], arr[j+1] = arr[j+1], arr[j]

    for i in range(2, N-2):
        hei_lst = list()
        for j in range(i-2, i+3):
            if height[j] < height[i]:
                hei_lst.append(height[i] - height[j])
            elif  i == j:
                hei_lst.append(height[i])
            else:
                break

        if len(hei_lst) == 5:
            Bubblesort(hei_lst, len(hei_lst))
            result += hei_lst[0]

    print(f'#{tc} {result}')
    
'''
버블 정렬을 활용한 풀이

'''