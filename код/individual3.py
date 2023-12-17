def kolichectvo_bikov_korov_telyat(total_money, total_heads):
    # переменные для количества быков, коров и телят
    Bulls = 0
    cows = 0
    calves = 0

    # перебор возможных комбинаций количества быков, коров и телят
    for num_bulls in range(total_heads + 1):
        for num_cows in range(total_heads + 1 - num_bulls):
            num_calves = total_heads - num_bulls - num_cows
            # Проверяем, хватит ли денег
            if (num_bulls*10 + num_cows*5 + num_calves*0.5) == total_money:
                bulls, cows, calves = num_bulls, num_cows, num_calves
                break

    return bulls, cows, calves

# параметры
total_money = 100
total_heads = 100

# Вызываем функцию для расчета количества быков, коров и телят
num_bulls, num_cows, num_calves = kolichectvo_bikov_korov_telyat (total_money, total_heads)

# Выводим результат
print(f"Количество быков: {num_bulls}, коров: {num_cows}, телят: {num_calves}")
