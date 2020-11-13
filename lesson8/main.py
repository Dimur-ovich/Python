# Проект содержит решение 7-го задания по курсу "Основы Python"
# Студент: Алексей Пискунов

# Вопросы преподавателю:
"""
1) правильно ли я понимаю, что статический метод в рамках класса не может обратиться к другому статическому методу этого же класса?
мне пришлось создать отдельную функцию leap_year_day для получения дополнительного дня високосного года,
которую использует метод валидации даты в задании 1. Было бы правильнее разместить эту функцию внутри описания
класса как статический метод, но как к ней в этом случае обратиться из другого статического метода этого же класса?

"""

# Пояснения к решению
"""
"""

task_min = 1
task_max = 7

class Task(object):
    def __init__(self):
        self.num = int(input("Введите номер задачи: "))

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        if num < task_min:
            self.__num = task_min
        elif num > task_max:
            self.__num = task_max
        elif num in (4, 5, 6) :
            self.__num = 4
        else: self.__num = num

    def get_task_num(self):
        return self.num

t = Task()
task = t.get_task_num()

print(f"Выполняется задача: {task}")

#---------------------------------------------------------------------------------
if task == 1:
    # создаем функцию, рассчитывающую значение дополнительного дня для високосного года

    def leap_year_day(num):
        if num % 4 == 0 and (num % 100 != 0 or num % 400 == 0):
            return 1
        else:
            return 0

    # создаем функцию, устраняющую любые символы кроме цифр и '-' из строки
    # Это был первый вариант реализации, но он может быть расценен пользователем как неправильный:
    # автоматическое удаление недопустимых символов в данной реализации является неявной логикой
    # обработки введенных данных. Пользователь может, например, опечататься, опечатка будет
    # автоматически устранена, но при этом дата может оказаться вовсе не той, которую хотел ввести пользователь.
    # Например, пользователь вводит 11-11-2020, опечатывается 11-1q-2020, и получает на выходе 11-01-2020
    def str_date_clear(date_str):
        date_str_list = list(date_str)
        result = ''
        for ch in date_str_list:
            if ch in ('0','1','2','3','4','5','6','7','8','9','-'):
                result += ch
        return result

    # поэтому лучше создим функцию, работающую по тому же принципу, но возвращающую результат сравнения
    # введенных и очищенных данных (а функцию str_date_clear используем как готовую основу)
    def str_date_check(date_str):
        return date_str == str_date_clear(date_str)

    # создаем класс "Дата"
    class Date(object):

        # метод конвертации даты в число (поскольку требований к ней нет, использовал свой любимый числовой формат для даты)
        @classmethod
        def date_to_num(cls, str_date):

            list_date = str_date_clear(str_date).split('-')
            if len(list_date) != 3:
                err_message = 'Некорректный формат даты'
                return err_message
            else:
                return int(list_date[0]) + int(list_date[1]) * 100 + int(list_date[2]) * 10000

        # метод валидации даты
        @staticmethod
        def date_valid(str_date):
            list_date = str_date_clear(str_date).split('-')
            err_message = ''
            if len(list_date) != 3:
                err_message += 'Некорректный формат даты'
                return err_message
            else:
                year = int(list_date[2])
                month = int(list_date[1])
                day = int(list_date[0])
                if list_date[2] == '':
                    err_message += 'Не указан год. '
                if month < 1 or month > 12:
                    err_message += 'Значение месяца вне диапазона 1-12. '
                if month in (1,3,5,7,8,10,12) and (day < 1 or day > 31):
                    err_message += 'Значение дня вне диапазона 1-31. '
                if month in (4,6,9,11) and (day < 1 or day > 30):
                    err_message += 'Значение дня вне диапазона 1-30. '
                if month == 2 and (day < 1 or day > (28 + leap_year_day(year))):
                    err_message += f'Значение дня вне диапазона 1-{28 + leap_year_day(year)}. '
                return 'OK' if err_message == '' else err_message

    d_str = input('Введите дату в формате "день-месяц-год": ')
    if str_date_check(d_str):
        ds = Date()
        print(f"Дата в форме числа: {ds.date_to_num(d_str)}")
        print(f"Результат валидации даты: {ds.date_valid(d_str)}")
    else:
        print("Введен хотя бы один некорректный символ, попробуйте еще раз")

#---------------------------------------------------------------------------------
if task == 2:
    class OwnError(Exception):
        def __init__(self, txt_error):
            self.txt = txt_error

    print("Вычисляем значение выражения (a + b) / c")
    print("Ведите значения переменных:")

    try:
        a = float(input("    a = "))
        b = float(input("    b = "))
        c = float(input("    c = "))
        if c == 0:
            raise OwnError("На ноль делить нельзя")
        result = (a + b) / c
    except ValueError:
        print("Вы ввели не число")
    except OwnError as Err:
        print(Err)
    else:
        print(f"Результат: {result}")

#---------------------------------------------------------------------------------
if task == 3:
    class OwnError(Exception):
        def __init__(self, txt):
            self.txt = txt

        @staticmethod
        def int_check(str):
            try:
                num = int(str)
            except ValueError:
                return False
            else:
                return True

        @staticmethod
        def float_check(str):
            try:
                num = float(str)
            except ValueError:
                return False
            else:
                return True

    print("Заполнение списка чисел (другие типы данных игнорируются)")
    print("Для выхода из цикла заполнения введите пустую строку (нажмите ENTER, ничего не вводя)")
    result_list = []
    while True:
        try:
            s = input("Введите элемент списка: ")
            if s == '':
                break
            e = OwnError("")
            if e.int_check(s):
                result_list.append(int(s))
            elif e.float_check(s):
                result_list.append(float(s))
            else:
                raise OwnError("Вы ввели не число")
        except OwnError as Err:
            print(Err)

    print(result_list)

#---------------------------------------------------------------------------------
if task in (4, 5, 6):
    print("Решения задач 4-6 объединены в одно, но к сожалению, 5 и 6 задачи решить не успел")
    #склад оргтехники
    class Stock(object):
        def __init__(self, name):
            self.name = name

        def __str__(self):
            return "\n Класс 'Склад'"


    # Оргтехника
    class Equipment(object):
        def __init__(self, name, price, brand, model, guarantee):
            self.name = name
            self.price = price
            self.brand = brand
            self.model = model
            self.guarantee = guarantee

        def __str__(self):
            return f"\n Класс 'Оргтехника'\n  Атрибуты:\n    наименование\n    цена\n    марка\n    модель\n    гарантия"

        #def income_to_stock(self, name, price, brand, model, guarantee, stock):


    #Принтеры
    class Printer(Equipment):
        def __init__(self, name, price, brand, model, guarantee, paper_format, paper_density, box_capacity, resolution, print_technology):
            super().__init__(name, price, brand, model, guarantee)
            # следующая группа параметров общая для принтеров, сканеров и копиров, но в общем случае
            # класс Оргтехника может включать устройства с принципиально иными параметрами,поэтому
            # я вынес их на уровень класса типа устройства
            self.paper_format = paper_format
            self.paper_density = paper_density
            self.box_capacity = box_capacity
            self.resolution = resolution
            # специфичные атрибуты класса принтеров
            self.print_technology = print_technology
            # допустимые значения
            self.print_technology_values = ('Лазерная','Светодиодная','Струйная')
            self.paper_format_values = ('A0','A1','A2','A3','A4','A6')

        def __str__(self):
            return f"\n Класс 'Принтеры'\n  Атрибуты:\n    наименование\n    цена\n    марка\n    модель\n" \
                   f"    гарантия\n    формат бумаги\n    плотность бумаги\n    емкость лотка\n" \
                   f"    разрешение\n    технология печати"

    # Сканеры
    class Scanner(Equipment):
        def __init__(self, name, price, brand, model, guarantee, paper_format, paper_density, box_capacity, resolution):
            super().__init__(name, price, brand, model, guarantee)
            # следующая группа параметров общая для принтеров, сканеров и копиров, но в общем случае
            # класс Оргтехника может включать устройства с принципиально иными параметрами,поэтому
            # я вынес их на уровень класса типа устройства
            self.paper_format = paper_format
            self.paper_density = paper_density
            self.box_capacity = box_capacity
            self.resolution = resolution
            # допустимые значения
            self.paper_format_values = ('A0', 'A1', 'A2', 'A3', 'A4', 'A6')

        def __str__(self):
            return f"\n Класс 'Сканеры'\n  Атрибуты:\n    наименование\n    цена\n    марка\n    модель\n" \
                   f"    гарантия\n    формат бумаги\n    плотность бумаги\n    емкость лотка\n    разрешение"

    # Копиры
    class Copier(Equipment):
        def __init__(self, name, price, brand, model, guarantee, paper_format, paper_density, box_capacity, resolution):
            super().__init__(name, price, brand, model, guarantee)
            # следующая группа параметров общая для принтеров, сканеров и копиров, но в общем случае
            # класс Оргтехника может включать устройства с принципиально иными параметрами,поэтому
            # я вынес их на уровень класса типа устройства
            self.paper_format = paper_format
            self.paper_density = paper_density
            self.box_capacity = box_capacity
            self.resolution = resolution
            # допустимые значения
            self.paper_format_values = ('A0', 'A1', 'A2', 'A3', 'A4', 'A6')

        def __str__(self):
            return f"\n Класс 'Ксероксы'\n  Атрибуты:\n    наименование\n    цена\n    марка\n    модель\n" \
                   f"    гарантия\n    формат бумаги\n    плотность бумаги\n    емкость лотка\n    разрешение"

    print(f"По задаче 4 созданы следующие классы:\n    {Stock('')}\n    {Equipment('','','','','')}\n    {Printer('','','','','','','','','','')}\n    {Scanner('','','','','','','','','')}\n    {Copier('','','','','','','','','')}")
#---------------------------------------------------------------------------------
if task == 7:

    class My_complex(object):
        def __init__(self, x, y):
            self.x = x
            self.y = y

        def __str__(self):
            return ("" if self.x > 0 else "-") + str(abs(self.x)) + (" + " if self.y >= 0 else " - ") + str(abs(self.y)) +"j"

        def __add__(self, other):
            return My_complex(self.x + other.x, self.y + other.y)

        def __sub__(self, other):
            return My_complex(self.x - other.x, self.y - other.y)

        def __mul__(self, other):
            return My_complex(self.x * other.x - self.y * other.y, self.y * other.x + self.x * other.y)


        def __truediv__(self, other):
            return My_complex((self.x * other.x + self.y * other.y) / (other.x ** 2 + other.y ** 2),
                              (self.y * other.x - self.x * other.y) / (other.x ** 2 + other.y ** 2))

    с_one = input("Введите действительную часть и мнимую часть комплексного числа (разделитель - пробел): ").split(" ")
    с_two = input("Введите действительную часть и мнимую часть комплексного числа (разделитель - пробел): ").split(" ")
    try:
        a = My_complex(float(с_one[0]), float(с_one[1]))
        b = My_complex(float(с_two[0]), float(с_two[1]))
    except ValueError:
        print("Где-то вы ввели не число. Попробуйте еще раз")
    else:
        print(f"комплексное число a: {a}")
        print(f"комплексное число b: {b}")
        print(f"Сумма (a + b) = {a + b}")
        print(f"Разность (a - b) = {a - b}")
        print(f"Произведение (a * b) = {a * b}")
        print(f"Частное (a / b) = {a / b}")

#=============================================================================================
# Сохраненный материал вебинара:
if task == 0:
    class Auto:
        COLOR = "red"
        def __init__(self):
            self.marka = "lada"

        @staticmethod
        def get_class_info(item):
            print("INFO", item)

        @classmethod
        def get_class_info_two(cls, item):
            print(cls.COLOR, item)

    #my_auto = Auto()
    #print(my_auto.marka)
    #print(my_auto.COLOR)
    #print(Auto.COLOR)
    Auto.get_class_info("!")
    Auto.get_class_info_two("!!!")

    # @staticmethod - эквивалент функции вне класса.
    # разницы нет
    # отнесение функций к классу - это всего лишь систематизация

    try:
        print(100/0)
    except ZeroDivisionError:
        print("На ноль не делим")
    except IndexError:
        print("Ошибка с индексом")

# создание класса для обработки собственного исключения
    class ErrorFirstCharter(Exception):
        def __init__(self, txt_error):
            self.txt = txt_error

    word = "ыва"

    try:
        if word[0] in ["ы", "ь", "ъ", "ё"]:
            raise ErrorFirstCharter("слово начинается не с той буквы")
    except ErrorFirstCharter as error_test_msg:
        print(error_test_msg)

# способ трассировки непонятных ошибок с помощью модуля traceback:
    import traceback
    try:
        res = 5 / 0
    except Exception as e:
        print('Ошибка:\n', e, '\n', traceback.format_exc())
