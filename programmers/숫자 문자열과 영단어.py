def solution(s):
    number_eng = ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
    number = s
    i = 0

    for j in number_eng:
        number = number.replace(j, str(i))
        i += 1

    return number

s = input()
print(solution(s))