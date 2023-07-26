# Task_07a
# Напишите программу, которая получает целое
# число и возвращает его шестнадцатеричное
# строковое представление. Функцию hex
# используйте для проверки своего результата.

base = [16]

n = int(input("Введите число: "))
for i in range(len(base)):
    res = ''
    res1 = ''
    sys_select = base[i]
    n1 = n
    while n1 > 0:
        remainder = n1 % sys_select
        if remainder == 10:
            remainder_s = "a"
        elif remainder == 11:
            remainder_s = "b"
        elif remainder == 12:
            remainder_s = "c"
        elif remainder == 13:
            remainder_s = "d"
        elif remainder == 14:
            remainder_s = "e"
        elif remainder == 15:
            remainder_s = "f"
        else:
            remainder_s = str(remainder)

        res = remainder_s + res
        n1 = n1 // sys_select
    if base[i] == 2:
        res1 = bin(n)
    elif base[i] == 8:
        res1 = oct(n)
    elif base[i] == 16:
        res1 = hex(n)
    # else:
    #     res1 = str(n)

    print(f"\tРезультат преобразования в шестнадцатиричную систему: {res}")
    print(f"\tПроверка: {res1[2:]}")
    # print(f"{if(iseqres1.)}")

    print(f"\t{res == res1[2:]}")