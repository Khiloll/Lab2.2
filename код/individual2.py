#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import cmath

def solve_quadratic(a, b, c):
    # Вычисляем дискриминант
    discriminant = (b ** 2) - (4 * a * c)

    # Вычисляем корни уравнения
    root1 = (-b + cmath.sqrt(discriminant)) / (2 * a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2 * a)

    return root1, root2

# Ввод коэффициентов квадратного уравнения
a = float(input("Введите коэффициент a: "))
b = float(input("Введите коэффициент b: "))
c = float(input("Введите коэффициент c: "))

# Решение квадратного уравнения
solution1, solution2 = solve_quadratic(a, b, c)

print(f"Корень 1: {solution1}")
print(f"Корень 2: {solution2}")
