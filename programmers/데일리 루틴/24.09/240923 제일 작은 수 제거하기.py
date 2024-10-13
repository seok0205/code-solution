def solution(arr):
    if len(arr) == 1:   #arr의 길이가 1일 때는 최솟값 제거가 아니라 -1을 출력해야함.
        arr[0] = int(-1)
    else:   #길이가 1이 아니라면 최솟값을 제거한 나머지 원소들만 리스트에 출력.
        arr.remove(min(arr))
    return arr