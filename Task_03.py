# Задание №3
# ✔ Напишите программу, которая получает целое число и возвращает
# его двоичное, восьмеричное строковое представление.
# ✔ Функции bin и oct используйте для проверки своего
# результата, а не для решения.
# Дополнительно:
# ✔ Попробуйте избежать дублирования кода в преобразовании к разным степеням счисления
# Избегайте магических чисел


base = [2, 8]


n = int(input("Введите число: "))
for i in range(len(base)):
    res = ''
    res1 = ''
    sys_select = base[i]
    n1 = n
    while n1>0:
        res = str(n1%sys_select) + res
        n1 = n1 // sys_select
    if base[i] == 2:
        res1 = bin(n)
    elif base[i] == 8:
        res1 = oct(n)
    # else:
    #     res1 = str(n)
    print(f"Результат = {res}\tПроверка {res1[2:]}")
