# Написать программу, которая будет ввыводить в консоль заданный текст (Python - один из самых популярных языков программирования в мире),
# затем принимать из консоли шаблон подстроки и удалять в заданом тексте все слова в которых присутствует введенный шаблон
# Пример:
# Python - один из самых популярных языков программирования в мире
# Введите подстроку: ам
# Python - один из популярных языков в мире

text_str = 'Python - один из самых популярных языков программирования в мире'
print(f'Исходный текст: {text_str}')

sub_text_str = input('Введите подстроку для удаления из исходного текста: ')

text_list = text_str.split(' ')
# print(text_list)

text_list_new = []

# В случае, если искомая подстрока для удаления слов состоит только из одной буквы
# for item in range(len(text_list)):
#     for char in text_list[item]:
#         if char == sub_text_str:
#             print(f'Строка {sub_text_str} присутствует в элементе {text_list[item]}')
#             break
#     else:
#         index = item
#         text_list_new.append(text_list[index])
# print(text_list_new)

# В случае, если искомая подстрока для удаления слов состоит из нескольких букв

sub_text_list = ''

for item in range(len(text_list)):
    sub_text_list = text_list[item]
    for char in range(len(sub_text_list)):
        if sub_text_list[char:char + len(sub_text_str)] == sub_text_str:
            print(f'Строка "{sub_text_str}" присутствует в элементе "{sub_text_list}"')
            break
    else:
        index = item
        text_list_new.append(text_list[index])
# print(text_list_new)

print(*text_list_new, sep=' ')

# Склейка элементов списка в строку через цикл
# text_new_str = ''
# for i in range(len(text_list_new)):
#     text_new_str += str(text_list_new[i]) + ' '
# print(f'Исходный текст с учетом исключения слов, в которых содержится подстрока "{sub_text_str}" - это "{text_new_str}"')

# Склейка элементов списка в строку через join
# text_new_str = ' '.join(text_list_new)
# print(f'Исходный текст с учетом исключения слов, в которых содержится подстрока "{sub_text_str}" - это "{text_new_str}"')
