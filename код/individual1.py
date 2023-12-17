def buy_karandash(n):
    if n == 1:
        print(f"Я купил {n} карандаш")
    elif 2 <= n <= 4:
        print(f"Я купил {n} карандаша")
    else:
        print(f"Я купил {n} карандашей")

# ввод от пользователя
N = int(input("Введите количество карандашей (N ≤ 10): "))

# функция buy_karandash с введенным значением
buy_karandash(N)
