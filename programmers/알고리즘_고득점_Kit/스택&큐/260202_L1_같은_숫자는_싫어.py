'''
L2 같은 숫자는 싫어

배열 arr이 주어짐. 배열 arr의 각 원소는 숫자 0부터 9까지로 이루어짐.
배열 arr에서 연속적으로 나타나는 숫자는 하나만 남기고 전부 제거하려고 함. 단, 제거된 후 남은 수들을 반환할 때는 배열 arr의 원소들의 순서를 유지해야함.

예로,
arr = [1, 1, 3, 3, 0, 1, 1] 이면 [1, 3, 0, 1]을 return.
arr = [4, 4, 4, 3, 3] 이면 [4, 3]을 return

배열 arr에서 연속적으로 나타나는 숫자는 제거하고 남은 수들을 return 하는 solution 함수를 완성하시오.

제약:
배열 arr의 크기 : 1,000,000이하 자연수
배열 arr의 원소의 크기 : 0보다 크거나 같고 9보다 작거나 같은 정수
'''

def solution(arr):
    stack = [arr[0]]
    
    top = 0
    for i in arr:
        if stack[top] == i:
            continue

        stack.append(i)
        top += 1
    return stack