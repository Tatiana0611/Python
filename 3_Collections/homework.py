# Дан список повторяющихся элементов.
# Вернуть список с дублирующимися элементами.
# В результирующем списке не должно быть дубликатов.

my_list = [1, 2, 3, 4, 1, 1, 2, 5]
new_list = []

for elem in my_list:
    if my_list.count(elem) > 1 and elem not in new_list:
        new_list.append(elem)

print(new_list)



# В большой текстовой строке подсчитать количество встречаемых
# слов и вернуть 10 самых частых. Не учитывать знаки препинания
# и регистр символов. За основу возьмите любую статью
# из википедии или из документации к языку.

import wikipedia
import string

text = wikipedia.page('Python (programming language)').content[:9676]

# Удаление знаков препинания
table = str.maketrans('', '', string.punctuation)
translated_text = text.translate(table)
# print(translated_text)

words = translated_text.lower().split()
set_words = set(words)
dict_words = {}

# Ключ - слово, значение - сколько раз слово встречается в тексте
for word in set_words:
    dict_words[word] = words.count(word)

# Сортировка словаря по значению и вывод 10 самых часто встречаемых слов
print(sorted(dict_words.items(), key=lambda x: x[1], reverse=True)[:10])



# Создайте словарь со списком вещей для похода в качестве
# ключа и их массой в качестве значения. Определите какие
# вещи влезут в рюкзак передав его максимальную
# грузоподъёмность. Достаточно вернуть один допустимый вариант.

objects = {'phone': 40, 'map': 50, 'dishes': 200, 'meal': 80, 'water': 100, 'lighter': 70}
chosen_objects = {}
max_weight = 470
sum = 0

for key, value in objects.items():
    sum += value
    if sum <= max_weight:
        chosen_objects[key] = value

print(chosen_objects)