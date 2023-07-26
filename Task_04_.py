# Задание №4
# ✔ Напишите программу, которая вычисляет площадь
# круга и длину окружности по введённому диаметру.
# ✔ Диаметр не превышает 1000 у.е
# Точность не менее 42 знаков после запятой
import decimal
import math

decimal.getcontext().prec = 42

d = float(input("Input diameter "))

s = decimal.Decimal(math.pi*((d/2)**2))
l = decimal.Decimal(2*math.pi*(d/2))

print(f"s = {s},\r\nl = {l} ")