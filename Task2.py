# Задача 2. Напишите программу, которая найдёт произведение пар чисел списка. Парой считаем первый и последний элемент, второй и предпоследний и т.д.

# *Пример:*

# - [2, 3, 4, 5, 6] => [12, 15, 16];
# - [2, 3, 5, 6] => [12, 15]

from random import randrange

def genarate_rand_num(number_quantity):

    array_rand_num = []

    for i in range(1, number_quantity+1):

        rand_num = randrange(1, 10)
        array_rand_num.append(rand_num)

    return(array_rand_num)


def multiplic_pair (array):

    multiplic_pair = 0
    multiplic_array = []

    for i in range(0, int(len(array)/2+1)):

        multiplic_pair = array[i] * array[-1 - i]
        multiplic_array.append(multiplic_pair)

        
    return multiplic_array

    

num = int(input("input Q = "))
array = genarate_rand_num(num)
array_pair = multiplic_pair (array)
print(f'Массив {array} - произведение пар чисел массива: {array_pair} ')