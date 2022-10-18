#from random import randint


print('Введите кол-во мигрантов')
n = int(input())
if n > 20: 
    n = 20
elif n < 3:
    n = 3
def errors(instring: str):
    k = 0
    import random
    for i in range(len(instring)):
        if k == len(instring)/2:
            break
        if random.randrange(10) < 3:
            instring = instring[:i] + '?' + instring[i + 1:]
            k = k + 1
    return instring
def input_m(n: int, m: list):
    for i in range(n):
        print('Введите имя',i + 1,'мигранта')
        f_n = input()
        f_n = errors(f_n.capitalize())
        print('Введите фамилию',i + 1,'мигранта')
        l_n = input().capitalize()
        l_n = errors(l_n)
        print('Введите возраст',i + 1,'мигранта')
        age = int(input())
        print('Выберете пол',i + 1,'мигранта (м/ж)')
        sex = input()
        m.append([f_n, l_n, age, sex])
    return m
migrators = []
migrators = input_m(n, migrators)
print(migrators[1][3])
for i in range(len(migrators)):
    if (migrators[i][2] <= 35) and (migrators[i][2] >= 18):
        print(migrators[i])
