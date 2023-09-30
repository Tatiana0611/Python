# Напишите функцию группового переименования файлов. Она должна:
# ✔ принимать параметр желаемое конечное имя файлов.
# При переименовании в конце имени добавляется порядковый номер.
# ✔ принимать параметр количество цифр в порядковом номере.
# ✔ принимать параметр расширение исходного файла.
# Переименование должно работать только для этих файлов внутри каталога.
# ✔ принимать параметр расширение конечного файла.
# ✔ принимать диапазон сохраняемого оригинального имени. Например для диапазона
# [3, 6] берутся буквы с 3 по 6 из исходного имени файла. К ним прибавляется
# желаемое конечное имя, если оно передано. Далее счётчик файлов и расширение.


import os


def rename_file(final_name: str, sequence_num: int, old_extension: str, new_extension: str, range_new_name: list):
    os.chdir('..')
    count = 1
    for i in os.listdir():
        if i.split('.')[-1] == old_extension:
            new_original_name = i[range_new_name[0]-1: range_new_name[1]]
            # print(new_original_name)
            os.rename(i, new_original_name+final_name+str(count).zfill(sequence_num)+'.'+new_extension)
            count += 1


if __name__ == '__main__':
    rename_file('_file', 3, 'doc', 'txt', [1, 2])

