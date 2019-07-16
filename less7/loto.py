#!/usr/bin/python3

"""
== Лото ==

Правила игры в лото.

Игра ведется с помощью специальных карточек, на которых отмечены числа, 
и фишек (бочонков) с цифрами.

Количество бочонков — 90 штук (с цифрами от 1 до 90).

Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр, 
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:

--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86 
--------------------------

В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается 
случайная карточка. 

Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.

Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
	Если цифра есть на карточке - она зачеркивается и игра продолжается.
	Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
	Если цифра есть на карточке - игрок проигрывает и игра завершается.
	Если цифры на карточке нет - игра продолжается.
	
Побеждает тот, кто первый закроет все числа на своей карточке.

Пример одного хода:

Новый бочонок: 70 (осталось 76)
------ Ваша карточка -----
 6  7          49    57 58
   14 26     -    78    85
23 33    38    48    71   
--------------------------
-- Карточка компьютера ---
 7 11     - 14    87      
      16 49    55 77    88    
   15 20     -       76  -
--------------------------
Зачеркнуть цифру? (y/n)

Подсказка: каждый следующий случайный бочонок из мешка удобно получать 
с помощью функции-генератора.

Подсказка: для работы с псевдослучайными числами удобно использовать 
модуль random: http://docs.python.org/3/library/random.html

"""

import random

answer = []


def get_tick():
    '''
       ф. набирает в ticket 15 случ. неповторяющихся цифр от 1 до 15
    :return:  этот список
    '''
    all_num_ticket = [x for x in range(1, 91)]  # массив цифр (1-90)
    i = len(all_num_ticket)  # кол-во цифр
    num_ticket = 0  # текущая цифра
    ticket = []
    itm = 0
    while itm < 15:  # ф. набирает в ticket 15 случ. неповторяющихся цифр
        num_ticket = all_num_ticket.pop(
            random.randint(0, (i - 1)))  # берём из списка цифр (от 1 до iго), удаляя его из списка
        i = len(all_num_ticket)  # вычисляется оставшееся кол-во цифр
        ticket.append(num_ticket)
        itm += 1
    return ticket


def print_tick(u1):
    itm = 0
    z = 0
    while itm < 3:  # ф. три раза печатает строку билета
        line1 = u1[(0 + z):(5 + z)]
        line1.sort()
        z += 5

        itm2 = 0
        while itm2 < 5:  # добавляем случайным образом  пять ' ' в строку билета
            line1.insert(random.randint(0, len(line1)), ' ')
            itm2 += 1
        print(*line1)  # * - вывод без '', []
        itm += 1
    #u1.clear()


def user_answer():
    #global a
    a = 0
    us_an = input('Введите ответ, если нет такой цифры то, [-]:')
    for i2 in user:
        if str(i2) == str(us_an) and str(i2) == str(barrel):
            a = 1
            itm = user.index(i2)
            user.remove(i2)
            user.insert(itm, 'X')
            break
        elif str(i2) != us_an and us_an == '-':
            a = 2
        else:
            a = 3
    return a


user = get_tick()
user2 = get_tick()

all_barrel = [x for x in range(1, 91)]  # массим всех бочонков
i = len(all_barrel)  # кол-во бочонков
barrel = 0  # текущий бочонок
while i > 0:
    barrel = all_barrel.pop(random.randint(0, (i - 1)))  # берём из списка бочонков (от 1 до iго), удаляя его из списка
    i = len(all_barrel)  # вычисляется оставшееся кол-во бочонков
    answer = f'Новый бочонок: {barrel} (осталось {i})'

    print(answer)
    print('------ Ваша карточка -----')
    print_tick(user)
    print('--------------------------')
    print('-- Карточка компьютера ---')
    print_tick(user2)
    print('--------------------------')
    print(' ')
    if user_answer() < 3:
        print('Верно')
    else:
        print('Неправильно')
        break
