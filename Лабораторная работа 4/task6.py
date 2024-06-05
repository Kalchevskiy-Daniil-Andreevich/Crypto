def analyze_correction_ability(Xn, Yn):
    # Инициализация счетчика ошибок
    error_count = 0

    # Сравнение каждого бита в Xn и Yn
    for i in range(len(Xn)):
        if Xn[i] != Yn[i]:
            error_count += 1

    # Возвращение количества ошибок
    return error_count


# Определение кодовых слов
Xn = "00111010010101001011111010101010110101"
Yn = "01111010010101001011111010101010110101"

# Вызов функции для анализа корректирующей способности и вывод результатов
print(f"The number of errors in code words is {
      analyze_correction_ability(Xn, Yn)}.")
