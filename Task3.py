# Реализуйте алгоритм перемешивания списка. Встроенный алгоритм SHUFFLE не использовать! Реализовать свой метод

from random import randint as rnd
import random

size = int(input('Введите длину основного списка: '))

list_original = []

for i in range(size):
    list_original.append(rnd(1, 100))
print(f'Исходный список - это {list_original}.')

list_shuffle = list_original

for item in range(len(list_shuffle)):
    index = rnd(0, len(list_shuffle) - 1)
    temp = list_shuffle[item]
    list_shuffle[item] = list_shuffle[index]
    list_shuffle[index] = temp
print(f'Перемешанный список - это {list_shuffle}.')
