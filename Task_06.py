# Задание №6
# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег


total = 0
counter = 0
while True:
    print(f"Сумма на счете: {total}")

    operation = int(input("Введите операцию: 1 - пополнить; 2 - снять; 3 - выйти: "))

    if total > 5_000_000:
        total *= 0.9
        print (f"Налог на богатство: -10%! Сумма на счете {total} ")

    if operation > 3 or operation < 1:
        continue

    match operation:
        case 1:
            value = int(input("Введите сумму пополнения кратную 50 y.e "))

            if value%50 != 0:
                print("Ошибка ввода!")
                continue

            total += value
            counter += 1

        case 2:
            value = float(input("Введите сумму снятия кратную 50 y.e. Внимание: оплата -1,5% от суммы "))

            if value % 50 != 0:
                print("Ошибка ввода!")
                continue

            interest = 1.015*value
            if interest < 30:
                interest = 30
            elif interest > 600:
                interest = 600

            if total - (value + interest) < 0:
                print("Недостаточно средств на счете!")
                continue

            counter += 1

        case 3:
            print("До свидания!")
            exit(1)

    if counter >= 3:
        total *= 1.03
        counter = 0
        print("3% - бонус за 3 снятия/пополнения!")
