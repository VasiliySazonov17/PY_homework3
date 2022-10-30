# Задача 1 Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на нечётной позиции.

# *Пример:*

# - [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randrange


def genarate_rand_num(number_quantity):

    array_rand_num = []

    for i in range(1, number_quantity+1):

        rand_num = randrange(1, 10)
        array_rand_num.append(rand_num)

    return(array_rand_num)

def create_array_odd(array_full):

    array_odd = []
    count = 0

    for i in array_full:
        if (count % 2 != 0):
            array_odd.append(i)
            count += 1
        else:
            count +=1
            continue

    return array_odd

def sum_array(array):

    sum_array = 0

    for i in array:
        sum_array += i
    
    return sum_array


number_quantity = int(input('input quantity numbers: '))
array = genarate_rand_num(number_quantity)
print(array)
array_odd = create_array_odd(array)
sum_odd_num = sum_array(array_odd)
print(f'на нечетных позициях {array_odd}, ответ: {sum_odd_num} ')