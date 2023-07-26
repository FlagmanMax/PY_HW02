# Task_07b
# Напишите программу, которая принимает две строки
# вида “a/b” — дробь с числителем и знаменателем.
# Программа должна возвращать сумму
# и *произведение дробей. Для проверки своего
# кода используйте модуль fractions.
import fractions
import math

(a1, b1) = map(int, input("Введите первую дробь в формате 'a/b': ").split('/'))
(a2, b2) = map(int, input("Введите вторую дробь в формате 'a/b': ").split('/'))


#summ
numerator_01 = int(a1*b2 + a2*b1)
denominator_01 = int(b1*b2)
gcd_01 = math.gcd(numerator_01, denominator_01)

numerator_01 = int(numerator_01/gcd_01)
denominator_01 = int(denominator_01/gcd_01)
if denominator_01 == 1:
    denominator_01 = ""
else:
    denominator_01 = "/" + str(denominator_01)

print(">>>")
print(f"Результат сложения дробей = {numerator_01}{denominator_01}")
print(f"Результат проверки сложения дробей = {fractions.Fraction(a1,b1) + fractions.Fraction(a2,b2)}")


#prod
numerator_02 = a1*a2
denominator_02 = b1*b2
gcd_02 = math.gcd(numerator_02, denominator_02)

numerator_02 = int(numerator_02/gcd_02)
denominator_02 = int(denominator_02/gcd_02)
if denominator_02 == 1:
    denominator_02 = ""
else:
    denominator_02 = "/" + str(denominator_02)

print(">>>")
print(f"Результат умножения дробей = {numerator_02}{denominator_02}")
print(f"Результат проверки умножения дробей = {fractions.Fraction(a1,b1) * fractions.Fraction(a2,b2)}")
