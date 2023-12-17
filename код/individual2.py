def naibolshee_chislo(a, b, c):
    return max(a, b, c)

num1 = float(input("Введите первое число: "))
num2 = float(input("Введите второе число: "))
num3 = float(input("Введите третье число: "))

maximum = naibolshee_chislo(num1, num2, num3)
print(f"Наибольшее из введенных чисел: {maximum}")
