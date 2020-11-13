# Проект содержит решение 5-го задания по курсу "Основы Python"
# Студент: Алексей Пискунов

# Вопросы преподавателю:
# 1) Возможно, где-то пропустил материал, но при решении 7-й задачи вынужденно оставил наименования компаний на латинице
# Правильно ли я понимаю, что в заголовках атрибутов JSON использование кириллицы должно быть исключено?
# Или есть способ вывести UTF-8 в файл так, чтобы русский текст при открытии читался нормально?
# 2) Правильно ли я понимаю, что учебные задания следует выполнять "буквально"?
# Например, меня как аналитика немного удивило условие задачи "добавлять фирму со значением убытков в словарь",
# никак не выделяя, что это убыток. Был бы я разработчиком, по такой задаче непременно бы задал вопрос ее постановщику.
# Но в рамках обучения, как я понимаю, важнее при реализации требований задания точно следовать
# требованиям в условии задачи, правильно?
# А то прям-таки подмывало в 7-й задаче поставить отрицательное значение прибыли в словарь :)

task = int(input('Введите номер задачи: '))

if task == 1:
    out_f = open("file_from_task_1.txt", "w", encoding="utf-8")

    while True:
        new_string = input("Введите строку для записи в файл (окончание ввода - пустая строка): ")

        if new_string == "":
            break
        else:
            out_f.write(new_string + "\n")

    out_f.close()

if task == 2:
    source_file_name = "file_for_task_2.txt"

    with open(source_file_name, "r", encoding="utf-8") as source_f:
        content = source_f.read()

    content_list = content.split("\n")
    str_count = len(content_list)
    print(f"Количество строк в файле {source_file_name}: {str_count}")
    print("Количество слов в строках:")
    i = 1
    for el in content_list:
        el_str = el.split(" ")
        print(f"    строка {i}: {len(el_str)}")
        i += 1

if task == 3:
    source_file_name = "file_for_task_3.txt"

    with open(source_file_name, "r", encoding="utf-8") as source_f:
        content = source_f.read()

    content_list = content.split("\n")
    str_count = len(content_list)
    total_salary = 0

    print("Фамилии сотрудников с окладом менее 20000:")
    for el in content_list:
        el_str = el.split(" ")
        total_salary += float(el_str[1])
        if(float(el_str[1]) < 20000):
            print(f"    {el_str[0]}   (оклад: {el_str[1]})")

    print(f"Средняя величина оклада сотрудников в файле {source_file_name}: {round(total_salary/str_count,2)}")

if task == 4:

    source_f = open("file_for_task_4.txt", "r", encoding="utf-8")
    target_f = open("file_from_task_4.txt", "w", encoding="utf-8")

    for line in source_f:
        if (line.find('One') >= 0):
            line = line.replace('One','Один')
        if (line.find('Two') >= 0):
            line = line.replace('Two','Два')
        if (line.find('Three') >= 0):
            line = line.replace('Three','Три')
        if (line.find('Four') >= 0):
            line = line.replace('Four','Четыре')
        target_f.write(line)
    source_f.close()
    target_f.close()

if task == 5:

    file_name = "file_for_task_5.txt"

    with open(file_name, "w") as sample_f:
        num_str = input("Введите строку чисел, разделенных пробелами (разделитель десятичых разрядов - '.'): ")
        sample_f.write(num_str)

    with open(file_name, "r") as source_f:
        first_string = source_f.readline()
        nums = first_string.split(" ")
        sum = 0
        for el in nums:
            sum += float(el)

    print(f"Сумма чисел в файле {file_name} равна {sum}")

if task == 6:
    file_name = "file_for_task_6.txt"
    res_dict = {}
    with open(file_name, "r", encoding="utf-8") as source_f:
        for line in source_f:
            if (line.find(':') > 0):          #используем символ ':' как признак наличия названия предмета в начале строки
                subject = line.split(':')
                raw_hours_str = subject[1].split(' ')  #разделим подстроки с часами
                hours = 0
                for el in raw_hours_str:
                    i = 0
                    h = ''
                    while i < len(el):
                        if el[i] >= '0' and el[i] <= '9':       #обрезаем все символы кроме цифр
                            h += el[i]
                        i += 1
                    if h != '':
                        hours += int(h)             #собираем все часы по одному предмету

                step_dict = {subject[0] : hours}    #сохраняем полученные очищенные значения в словарь
                res_dict.update(step_dict)          #дополняем результирующий словарь

        print(res_dict)

if task == 7:

    import json

    file_source = "file_for_task_7.txt"
    file_target = "file_from_task_7.json"

    res_dict = {}
    profit_dict = {}
    pl = 0
    profit = 0
    with open(file_source, "r", encoding="utf-8") as source_f:
        for line in source_f:
            if line.replace(' ','') != '':
                res = line.split(' ')
                name = res[0]
                income = float(res[2])
                cost = float(res[3])
                profit_one = income - cost
                if profit_one >= 0:
                    profit += profit_one
                    pl += 1
                step_dict = {name : abs(profit_one)}
                res_dict.update(step_dict)
        if pl > 0:
            profit_dict = {"average_profit": profit/pl}
        else:
            profit_dict = {"average_profit": "отсутствует"}
        result = [res_dict, profit_dict]
        print(f"Результат выведен в файл {file_target}")
        with open(file_target, "w", encoding="utf-8") as target_f:
            json.dump(result, target_f)

else:
    print('Номера задач лежат в диапазоне от 1 до 7')


