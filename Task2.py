# Задайте список из n чисел последовательности (1 + 1/n)^n. Вывести в консоль сам список и сумму его элементов.

number = int(input('Введите количество чисел N: '))

list = []
sum = 0

for i in range(1, number + 1):
    list.append(round((1 + 1 / i) ** i, 2))
print(f'Список из последовательности количества {number} чисел по формуле (1 + 1/n)^n - это {list}')

for item in range(len(list)):
    sum += list[item]

print(f'Сумма элементов списка равна {sum}')
