# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

task = int(input('Введите номер задачи: '))

if task == 1:
    def my_div(val_one, val_two):
        if val_two == 0:
            print('Функция my_div. Ошибка деления на ноль')
            return 'ZeroDivisionError: division by zero'
        else:
            return val_one/val_two
    num = float(input('Ведите числитель: '))
    den = float(input('Ведите знаменатель: '))
    print(my_div(num, den))
elif task == 2:
    def user_info(name, last_name, year, place, email, phone):
        return (name + ' ' + last_name + ', ' + year + ', ' +
                place + ', ' + email + ', ' + phone)

    print(user_info(name = 'Алексей', last_name = 'Пискунов', year = '1966',
                    place = 'Самара', email = 'info@piskunov.ru', phone = '+79998886655' ))

elif task == 3:
    def my_func(val_one, val_two, val_three):
        val_min = min(val_one, val_two, val_three)
        return (val_one + val_two + val_three - val_min)

    first = float(input('Ведите первое число: '))
    second = float(input('Ведите второе число: '))
    third = float(input('Ведите третье число: '))
    print(f' Сумма двух наибольших чисел равна: {my_func(first, second, third)}')

elif task == 4:
    def my_func(x,y):
        err = ''
        res_one = None
        res_two = None
        if type(x) != type(1.0) or type(y) != type(1):
            err = 'Неверный тип хотя бы одного входящего значения'
        elif type(y) == type(1) and y >= 0:
            err = 'Второй атрибут функции должен быть меньше нуля'
        else:
            res_one = x ** y
            res_two = 1
            i = 0
            while i < abs(y):
                res_two *= 1 / x
                i += 1
        return err, res_one, res_two
    # проверяем работу функции
    xxx = float(input('Введите число: '))
    yyy = int(input('Введите отрицательную степень числа: '))
    res = my_func(xxx, yyy)
    if res[0] == '':
        print(f'Результат первого метода возведения в степень: {res[1]}, результат второго: {res[2]}')
    else:
        print(f'Ошибка: {res[0]}')
    #print(f'тест на возврат ошибки с типом: {my_func("", "")[0]}')
elif task == 5:
    def sly_func(calc_string, start_sum = 0):
        end_flag = 0
        res_sum = start_sum
        string_set = calc_string.split(' ')
        for el in string_set:
            if el == '#':
                end_flag = 1
            elif end_flag == 0:
                res_sum += float(el)
        return end_flag, res_sum
    # организуем выполнение задачи
    ef = 0
    result = 0
    while ef == 0:
        input_string = input('Введите последовательность чисел через пробел(для завершения работы программы введите # вместо числа: ')
        sf_out = sly_func(input_string, result)
        result = sf_out[1]
        ef = sf_out[0]
    print(f'Сумма введенных чисел: {result}')
    #result = 0

elif task == 6:
    def int_func(word):
        # поскольку никаких ограничений на реализацию функции в задании не наложено,
        # а времени как всегда не хватает, идем к цели кратчайшим путем :)
        return word.title() # самый простой способ, его можно использовать и для всей фразы, но нужна функция :)
        # в процессе тестирования обнаружил, что любые символы, кроме букв, title определяет как разделители слов
        # но, рассудив, что иное решение без title займет непонятное пока время, оставил как есть
    # выполняем задание с помощью функции int_func
    string_in = input('Введите строку из слов, разделенных пробелами, в нижнем регистре: ')
    string_split = string_in.split(' ')
    string_out = ''
    for el in string_split:
        string_out += int_func(el) + ' '
    print(string_out[0 : len(string_out) - 1])   ## выводим итоговую строку, убирая последний пробел
elif task == 0:
    # правильное решение 6-й задачи (с идей разбора)
    def int_func(text):
        result = ''
        for word in text.split(' '):
            result += word[0].upper() + word[1:].lower() + ' '
        return result

    t = input('введите текст: ')
    print(int_func(t))
elif task == 7:
    my_list = [2, 3, 7, 42, 37]
    new_list = [el for el in my_list if el % 2 == 1]
    print(new_list)

    my_dict = {el: el * 2 for el in range(10, 20)}
    print(my_dict)

    from functools import reduce


    def my_func(prev_el, el):
        # prev_el - предыдущий элемент
        # el - текущий элемент
        return prev_el + el

    print(reduce(my_func, [10, 20, 30, 40]))

    print(reduce(lambda x, y: x + y, [2, 3, 4, 5, 6, 7]))
    print(list(map(lambda x: x + 10, [2, 3, 4, 5, 6, 7])))

    def my_func(one,two):
        return one + two
    from functools import partial
    new_func = partial(my_func, 2)

    print(new_func(3))
    print(new_func(5))
    print(new_func(7))

else:
    print('Номер задачи должен находится в диапазоне от 1 до 6')
