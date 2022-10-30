# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randrange


def genarate_rand_num(number_quantity):

    array_rand_num = []

    for i in number_quantity:

        rand_num = randrange(1, 10)
        array_rand_num.append(rand_num)

    print(array_rand_num)


    number_quantity = input('input: ')
    genarate_rand_num(number_quantity)