# Проект содержит решение 4-го задания по курсу "Основы Python"
# Студент: Алексей Пискунов

# Вопросы преподавателю:
# 1. Алексей, даже не вопрос, а просьба: укажите, пожалуйста, на конкретные примеры нарушения PEP-8.
# Дело в том, что я его просмотрел, и был уверен, что мой код соответствует его требованиям.
# Первое замечание я списал на некоторые реальные отклонения от PEP-8 в задании 1 из-за невнимательности
# (в некоторых местах не было пробелов, где они нужны, и были там, где не нужны).
# Но за этим стал следить, и эти отклонения не должны быть слишком частыми, хотя не исключаю,
# что при проверке замечаю не все.
# Второе и третье замечание я получил одновременно, но опять в общем виде, без конкретики.
# Я понимаю, что если погрузиться в скурпулезное чтение рекомендаций, я смогу и сам раскопать все свои ошибки
# Но буду очень признателен, если вы конкретизируете это замечание примерами моих ошибок в стиле
# (к сожалению, я пока не очень справляюсь с рабочей и учебной нагрузкой одновременно, и конкретные
# замечания помогут сэкономить мне время на исправление своих ошибок).
# Заранее благодарен.

task = int(input('Введите номер задачи: '))

if task == 1:

    print('Выполните в терминале команду (вместо параметров в <> подставьте числовые значения): ')
    print('python salary.py <hours> <cost> <bonus>')

if task == 2:
    my_list_inp = input('Введите произвольный список целых чисел через пробел: ')
    my_list = [int(el) for el in my_list_inp.split(' ')]

    res_list = [my_list[i] for i in range(len(my_list)) if i > 0 and my_list[i] > my_list[i - 1]]
    # А строка с кодом ниже была ошибкой.
    # Забыл, что my_list.index(el) возвращает первое вхождение элемента в список.
    # Хорошо, что при  контрольной проверке решения повторяющиеся значения в список ввел.
    # Оставил на память :).
    #res_list = [el for el in my_list if my_list.index(el) > 0 and el > my_list[my_list.index(el) - 1]]

    print(my_list)
    print(res_list)

if task == 3:

    print([el for el in range(20,241) if el % 20 == 0 or el % 21 == 0])     # включая границы заданного диапазона

if task == 4:

    my_list_inp = input('Введите список целых чисел через пробел: ')
    my_list = [int(el) for el in my_list_inp.split(' ')]

    res_list = [el for el in my_list if my_list.count(el) == 1]

    print(my_list)
    print(res_list)

if task == 5:

    from functools import reduce

    def my_func(prev_el,el):
        return prev_el * el

    my_list = [el for el in range(100,1001) if el % 2 == 0]

    print(f'{my_list[0:5]} ... {my_list[-5:]}')
    print(reduce(my_func, my_list))

if task == 6:

    print('Запустите в терминале генератор целых чисел (в параметрах в <> задайте диапазон):')
    print('python gen_int.py <start> <end>')

    print('Запустите в терминале повторитель элементов списка, заданного в скрипте (<count> замените на количество повторений):')
    print('python repeat_list.py <count>')

if task == 7:

    from itertools import count
    from math import factorial

    # Это было первое некрасивое решение. Жуть, но работает :)
    def fact_old(n):
        res = 1
        res_list = []
        i = 1
        while(i <= n):
            res *= i
            res_list.append(res)
            i += 1
        for el in res_list:
            yield el

    # А вот за это уже не стыдно :)
    def fact(n):
        res_list = [factorial(i + 1) for i in range(n)]
        for el in res_list:
            yield el

    num = int(input('Введите целое число: '))

    print(fact(num))

    for el in fact(num):
        print(el)



