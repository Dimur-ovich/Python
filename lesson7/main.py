# Проект содержит решение 7-го задания по курсу "Основы Python"
# Студент: Алексей Пискунов

# Вопросы преподавателю:
"""
1)  не совсем понял смысл условия "реализовать метод, принимающий экземпляр класса" (возможно, перемудрил).
Если я правильно понял, в Python мы имеем дело с 3-мя типами методов: instancemethod (методы экземпляра класса),
classmethod (методы класса, привязанные к самому классу, а не к его экземпляру), и staticmethod (методы, которые
"не знают, к какому классу относятся", т.е. не связанные ни с классом, ни с его экземплярами).
И "реализовать метод, принимающий экземпляр класса" означает "реализовать метод экземпляра класса" т.е. instancemethod.
Правильно?
"""

# Пояснения к решению
"""
В этом задании я использовал тот же принцип выбора номера задачи, что и во всех предыдущих, 
но реализовал его с помощью класса и декоратора @Property.
Код, конечно, получился более громоздким, но это чисто для практики :)  
"""

task_min = 1
task_max = 3

class Task(object):
    def __init__(self):
        self.num = int(input("Введите номер задачи: "))

    @property
    def num(self):
        return self.__num

    @num.setter
    def num(self, num):
        if num < 1:
            self.__num = 1
        elif num > 3:
            self.__num = 3
        else: self.__num = num

    def get_task_num(self):
        return self.num

t = Task()
task = t.get_task_num()

print(f"Номер задачи: {task}")

#--------------------------------------------------------------------------------------
if task == 1:
    # Создаем простую функцию для ввода двумерного "списка списков"
    def get_list_of_list():
        res_list = []
        tmp_list = []
        i = 1
        print("Введите построчно двумерную целочисленную матрицу (количество чисел в каждой строке должно быть одинаковым)")
        print("Для завершения ввода введите пустую строку")
        while(True):
            s = input(f"   {i}-я строка: ").split(',')
            if s == ['']:
                break
            else:
                res_list.append(s)
                i += 1
        return res_list

    # создаем класс Matrix
    class Matrix(object):
        def __init__(self, list_of_list):
            self.matrix = list_of_list

        def __str__(self):
            return '\n'.join('\t'.join(map(str, row)) for row in self.matrix)

        def size(self):
            matrix_size = (len(self.matrix), len(self.matrix[0]))
            return matrix_size

        def __add__(self, other):
            result = []
            for i in range(len(self.matrix)):
                tmp_res = []
                for j in range(len(self.matrix[0])):
                    summa = int(other.matrix[i][j]) + int(self.matrix[i][j])
                    tmp_res.append(summa)
                result.append(tmp_res)
            return Matrix(result)

    obj_one = Matrix(get_list_of_list())
    obj_two = Matrix(get_list_of_list())
    print(f"Матрица 1:\n{obj_one}")
    print(f"Матрица 2:\n{obj_two}")
    if obj_one.size() != obj_two.size():
        print("Матрицы имеют разный размер, сложение невозможно")
    else:
        print(f"Сумма матриц:\n{obj_one + obj_two}")

if task == 2:

    class Garments(object):
        def __init__(self, name):
            self.name = name

    class Coat(object):
        def __init__(self, name, size):
            self.name = name
            self.size = size

        @property
        def cloth_outlay(self):
            self.__cloth_outlay = self.size / 6.5 + 0.5
            return round(self.__cloth_outlay, 2)

        def get_cloth_outlay(self):
            return f"Расход ткани на пошив одного изделия '{self.name}' составит {self.cloth_outlay} (кв.метров?)"

    class Suit(object):
        def __init__(self, name, height):
            self.name = name
            self.size = height

        @property
        def cloth_outlay(self):
            self.__cloth_outlay = self.size * 2 + 0.3
            return round(self.__cloth_outlay, 2)

        def get_cloth_outlay(self):
            return f"Расход ткани на пошив одного изделия '{self.name}' составит {self.cloth_outlay} (кв.метров?)"

    v = float(input("Введите свой размер пальто (например, 48): "))
    h = float(input("Введите свой рост в сантиметрах: ")) / 100         #переводим рост в метры

    cl = Coat("Пальто шерстяное", v)
    st = Suit("Костюм", h)

    print(cl.get_cloth_outlay())
    print(st.get_cloth_outlay())

    #print("Замечание разработчика: в условиях задачи нужно уточнить единицы измерения расхода и, возможно, формулы расчета :)")

if task == 3:
    pass

    class Cell(object):
        def __init__(self, number):
            self.number = number

        def __add__(self, other):
            new_sell = Cell(self.number + other.number)
            return new_sell

        def __sub__(self, other):
            if self.number - other.number > 0:
                return self.number - other.number
            else:
                return "Для клеток вычитание невозможно (результат меньше либо равен нулю)"

        def __mul__(self, other):
            new_sell = Cell(self.number * other.number)
            return new_sell

        def __truediv__(self, other):
            quot = round(self.number / other.number, 0)
            if quot > 0:
                new_sell = Cell(quot)
                return new_sell
            else:
                return "Для указанных клеток деление невозможно (не остается клеток для построения новой)"

        def make_order(self, set_size):
            result = ''
            i = 0
            while(i < self.number // set_size):
                result += '*' * set_size + '\n'
                i += 1
            return result + '*' * (self.number % set_size)

    n_one = int(input("Введите количество ячеек в первой клетке: "))
    n_two = int(input("Введите количество ячеек во второй клетке: "))

    c_one = Cell(n_one)
    c_two = Cell(n_two)

    print(f"Количество ячеек в первой клетке: {c_one.number}")
    print(f"Количество ячеек во второй клетке: {c_one.number}")
    print(f"Количество ячеек в объединенной клетке: {(c_one + c_two).number}")
    print(f"Разность ячеек в двух клетках: {(c_one - c_two)}")
    print(f"Количество ячеек в объединенной клетке (умножение): {(c_one * c_two).number}")
    print(f"Количество ячеек в объединенной клетке (деление): {(c_one / c_two).number}")

    n_three = int(input("Введите количество ячеек в клетке: "))
    draw_size = int(input("Введите количество ячеек в ряду для отрисовки: "))
    c_three = Cell(n_three)
    print(c_three.make_order(draw_size))

# сохраненный материал урока
if task == 0:
    class MyInt(object):
        def __init__(self, item):
            self.number = item

        def __add__(self, other):
            return self.number + other.number

    one_num = MyInt(4)
    two_num = MyInt(3)

    print(one_num + two_num)

    class Iterator(object):
        def __init__(self, start, stop):
            self.stop = stop
            self.start = start

        def __iter__(self):
            return self

        def __next__(self):
            if self.start != self.stop:
                self.start += 1
                return self.start
            else:
                raise StopIteration

    my_iterator = Iterator(1, 100)
    for i in my_iterator:
        print(i)

