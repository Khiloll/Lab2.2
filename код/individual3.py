#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def sum_of_multiples(n, k):
    total_sum = 0
    for i in range(10**(n-1), 10**n):  # Генерируем все n-значные числа
        if i % k == 0:  # Проверяем, кратно ли число k
            total_sum += i
    return total_sum

# Ввод значений n и k
n = int(input("Введите значение n (от 1 до 4): "))
k = int(input("Введите значение k: "))

# Вычисление суммы всех n-значных чисел, кратных k
result = sum_of_multiples(n, k)
print(f"Сумма всех {n}-значных чисел, кратных {k}: {result}")