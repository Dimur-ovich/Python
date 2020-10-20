
# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

task = int(input('Введите номер задачи: '))

if task == 1:
    my_list = [7, True,'Строка', 46.8, None]
    print(f'Типы элементов списка (элемент - тип):')
    for el in my_list:
        print(f'    {el} - {type(el)}')

elif task == 2:
    my_list = input('Введите список элементов через запятую: ').split(',')
    print(f'Исходный список после ввода:    {my_list}')
    # конвертируем строковые значения списка в bool, int и float, если это возможно
    # (это небольшое дополнительное упражнение по личной инициативе)
    i = 0
    while(i < len(my_list)):
        tmp = my_list[i]
        if tmp == 'True': my_list[i] = True
        elif tmp == 'False': my_list[i] = False
        else:
            # Проверяем возможность конвертации в int или float
            dot_count = tmp.count('.')
            if(dot_count == 1):
                float_flag = True
            else:
                float_flag = False
            if(dot_count == 0):
                int_flag = True
            else:
                int_flag = False

            #Сбрасываем флаги, если анализ символов в элементе указывает на невозможность конвертациив int или float
            for el in tmp:
                if float_flag == True:
                    if ord(el) < ord('0') and ord(el) != ord('.') or ord(el) > ord('9'):
                        float_flag = False
                if int_flag == True:
                    if ord(el) < ord('0') or ord(el) > ord('9'):
                        int_flag = False
            # конвертируем элемент списка в int или float
            if int_flag == True:
                my_list[i] = int(tmp)
            elif float_flag == True:
                my_list[i] = float(tmp)
        i += 1
    print(f'Список до преобразования:    {my_list}')
    i = 0
    while(i < (len(my_list) // 2) * 2):
        tmp = my_list[i]
        my_list[i] = my_list[i + 1]
        my_list[i + 1] = tmp
        i += 2
    print(f'Список после преобразования: {my_list}')

elif task == 3:
    seasons = dict(winter = (1,2,12), spring = (3,4,5), summer = (6,7,8), autumn = (9,10,12))
    m_seasons_list = ['Зима','Зима',
                      'Весна','Весна','Весна',
                      'Лето','Лето','Лето',
                      'Осень','Осень','Осень',
                      'Зима']
    m_seasons_dict = {1: 'Зима', 2: 'Зима',
                      3: 'Весна', 4: 'Весна', 5: 'Весна',
                      6: 'Лето', 7: 'Лето', 8: 'Лето',
                      9: 'Осень', 10: 'Осень', 11: 'Осень',
                      12: 'Зима'}
    month = int(input('Введите порядковый номер месяца (от 1 до 12): '))
    method = input('Введите метод определения сезона (l - через список, d - через словарь): ')
    success_flag = False
    if method == 'l':
        method_name = 'через список'
        season = m_seasons_list[month-1]
        success_flag = True
    elif method == 'd':
        method_name = 'через словарь'
        season = m_seasons_dict.get(month)
        success_flag = True
    else:
        print('Неизвестный метод. Проверьте раскладку клавиатуры и регистр, и попробуйте еще раз')
    if success_flag == True:
        print(f'Месяц {month} относится к сезону {season} (метод определения - {method_name})')

elif task == 4:
    my_list = input('Введите строку из нескольких слов: ').replace(',','').split(' ')
    i = 0
    for el in my_list:
        if len(el) > 10:
            el = el[:10]
        print(f'{i}: {el}')
        i += 1

elif task == 5:
    my_rating = [120,100,75,40,25,12,9,8,7,5,4,2,1]
    print(f'Стартовый рейтинг: {my_rating}')

    number = int(input('Введите целое положительное число (для выхода из цикла введите отрицательное): '))
    insert_flag = False
    while(number > 0):
        for el in my_rating:
            if insert_flag == False:
                if number > el:
                    my_rating.insert(my_rating.index(el), number)
                    insert_flag = True
        print(f'Текущий рейтинг: {my_rating}')
        insert_flag = False
        number = int(input('Введите целое положительное число (для выхода из цикла введите отрицательное): '))

elif task == 6:
    choice = input('Если хотите ввести товар, введите "Да": ')
    good_structure = []
    i = 0
    # Создаем и заполняем структуру данными о товарах
    while(choice == 'Да'):
        name = input('Название товара: ')
        cost = int(input('Цена: '))
        count = int(input('Количество: '))
        mesure = input('Ед.измерения: ')
        i += 1
        if i == 1:
            good_structure = [(i, {"название": name, "цена": cost, "количество": count, "ед": mesure})]
            #print(good_structure)
        else:
            good_structure.append((i, {"название": name, "цена": cost, "количество": count, "ед": mesure}))
            #print(good_structure)
        choice = input('Если хотите ввести новый товар, введите "Да": ')
    print(good_structure)
    # создаем пустые списки для формирования аналитики
    name_list = []
    cost_list = []
    count_list = []
    mesure_list = []
    # Заполняем списки для аналитики
    for el in good_structure:
        #print(el[1])
        #
        name_list.append(el[1].get("название"))
        cost_list.append(el[1].get("цена"))
        count_list.append(el[1].get("количество"))
        mesure_list.append(el[1].get("ед"))
    # Формируем итоговый словарь
    analytic_dict = {"название": list(set(name_list)),
                     "цена": list(set(cost_list)),
                     "количество": list(set(count_list)),
                     "ед": list(set(mesure_list))
                    }
    print(analytic_dict)
else:
    print('Номер задачи должен находится в диапазоне от 1 до 6')

