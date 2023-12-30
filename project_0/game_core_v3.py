"""Игра угадай число
Компьютер сам загадывает и сам угадывает число
"""

import numpy as np


def random_predict(number: int = 1) -> int:
    """Рандомно угадываем число

    Args:
        number (int, optional): Загаданное число. Defaults to 1.

    Returns:
        int: Число попыток
    """
    x = 1 # нижняя граница диапазона
    y = 100 # верхняя граница диапазона
    predict_number=np.random.randint(x,y) # загаданное число
    count=0 # начальное количество попыток угадать равно нулю
        
    while predict_number != number:# цикл длится пока загаданное число predict_number не равно предложенному в качестве ответа числу number    
        if number > predict_number: # если предложенное в качестве ответа число больше загаданного числа 
            x = predict_number # нижняя граница диапазона принимается за загаданное число (уменьшается возможный диапазон)
            predict_number = np.random.randint(x, y) # выбирается случайное число из уменьшенного диапазона
            count += 1 # количество попыток отгадать увеличается на единицу
        elif number < predict_number: # если предложенное в качестве ответа число меньше загаданного числа
            y = predict_number # верхняя граница диапазона принимается за загаданное число (уменьшается возможный диапазон)
            predict_number = np.random.randint(x, y) # выбирается случайное число из уменьшенного диапазона
            count += 1 # количество попыток отгадать увеличается на единицу
        else:
            number == predict_number #загаданное число predict_number равно предложенному в качестве ответа числу number
            break #выход из цикла, т.к. угадали
    return count # возвращаем количество попыток


def score_game(random_predict) -> int:
    """За какое количство попыток в среднем за 1000 подходов угадывает наш алгоритм

    Args:
        random_predict ([type]): функция угадывания

    Returns:
        int: среднее количество попыток
    """
    x = 1 # нижняя граница диапазона
    y = 100 # верхняя граница диапазона
    count_ls = []
    np.random.seed(1)  # фиксируем сид для воспроизводимости
    random_array = np.random.randint(x, y, size=(1000))  # загадали список чисел

    for number in random_array:
        count_ls.append(random_predict(number))

    score = int(np.mean(count_ls))
    print(f"Ваш алгоритм угадывает число в среднем за:{score} попыток")
    return score


if __name__ == "__main__":
    # запуск
    score_game(random_predict)