#문자를 입력하고 나서 입력된 문자가 연속해서 나타나는 경우만이 그룹단어.
#똑같은 문자가 연속적이지 않고 비연속적으로 후에 한번 더 입력된다면 그것은 그룹단어가 아니다.

num = int(input())
gw = num

for i in range(num):
    word = input()

    for j in range(0, len(word)-1):
        if word[j] == word[j+1]:
            pass
        elif word[j] in word[j+1:]:
            gw -= 1
            break

print(gw)