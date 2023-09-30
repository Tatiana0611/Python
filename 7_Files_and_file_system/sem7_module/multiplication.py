# Напишите функцию, которая открывает на чтение созданные в прошлых задачах файлы с числами и именами.
# ✔ Перемножьте пары чисел. В новый файл сохраните имя и произведение:
# ✔ если результат умножения отрицательный, сохраните имя записанное строчными буквами и произведение по модулю
# ✔ если результат умножения положительный, сохраните имя прописными буквами и произведение округлённое до целого.
# ✔ В результирующем файле должно быть столько же строк, сколько в более длинном файле.
# ✔ При достижении конца более короткого файла, возвращайтесь в его начало.


def mult_name_file():
    with (
        open('../file_1.txt', 'r', encoding='utf-8') as f_1,
        open('../file_2.txt', 'r', encoding='utf-8') as f_2,
        open('../file_3.txt', 'a', encoding='utf-8') as f_3,
    ):

        names = [line[:-1] for line in f_2]
        mult_nums = []

        for line in f_1:
            num_1, num_2 = line[:-1].split('|')
            mult_nums.append(round((int(num_1) * float(num_2)), 2))
        # print(mult_nums)
        # print(names)

        max_length = max(len(mult_nums), len(names))
        # print(max_length)

        i = 0
        j = 0

        for k in range(max_length):

            if mult_nums[i] < 0:
                print(f'{names[j].lower()} {abs(mult_nums[i])}', file=f_3)
            else:
                print(f'{names[j].upper()} {mult_nums[i]:.0f}', file=f_3)

            i = (i + 1) % len(mult_nums)
            j = (j + 1) % len(names)


if __name__ == '__main__':
    mult_name_file()