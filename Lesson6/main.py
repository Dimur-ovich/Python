# Проект содержит решение 6-го задания по курсу "Основы Python"
# Студент: Алексей Пискунов

# Вопросы преподавателю:
# Возможно, что в первой задаче ожидалась другая реализация (типа ручного переключения),
# но мне показалось страным делать ручное там, где можно сразу сделать автомат.
# Если же я принципиально сделал в первой задаче что-то не то, прошу разъяснить, что именно требовалось :).

import time
import datetime

task = int(input('Введите номер задачи: '))

if task == 1:
    # В исходном задании совершенно не понял идею контроля последовательности переключений:
    # зачем это делать, если можно сразу реализовать правильную последовательность?
    # Поэтому в качестве дополнения сделал второй светофор с другим режимом переключений
    # И заодно немного познакомился с функциями дат и времени

    #создаем класс для эмуляции работы светофора в режиме, заданном в задании
    class TrafficLight(object):
        def __init__(self):
            self.__color = ""
            self.colors_regime = {"red": 7, "yellow": 2, "green": 5}   #режим работы светофора (оставляем публичным, чтобы иметь возможность переопределить)
            self.switches = 6         #количество переключений до запроса на прерывание (оставляем публичным)

        def running(self):
            i = 0
            while(True):
                if i // self.switches > 0 and i % self.switches == 0:
                    c = (input("Продолжить (да/нет)? - ")).upper()
                    while(c != "ДА" and c != "НЕТ"):
                        c = (input("Продолжить (да/нет)? - ")).upper()
                    if c == "НЕТ":
                        break

                colors = list(self.colors_regime.keys())
                self.__color = colors[i % 3]
                print(f'    {self.__color}, время включения: {datetime.datetime.today().strftime("%d.%m.%Y %H:%M:%S")}')
                time.sleep(float(self.colors_regime.get(self.__color)))
                i += 1

    # создадим класс с другим режимом работы светофора на основе класса TrafficLight
    class TrafficLightNew(TrafficLight):
        def __init__(self):
            self.colors_regime = {"red": 3, "yellow": 2, "green": 4}   #режим работы светофора
            self.switches = 9         #количество переключений до запроса на прерывание

    #Создаем объект класса TrafficLight и запускаем метод, эмулирующий переключения светофора в исходном режиме
    light = TrafficLight()
    print("Светофор 1:")
    light.running()

    #Создаем объект класса TrafficLightNew и запускаем метод, эмулирующий переключения светофора в новом режиме
    light_new = TrafficLightNew()
    print("Светофор 2:")
    light_new.running()

if task == 2:

    class Road(object):
        def __init__(self, length, width, thickness = 5):
            self._length = length
            self._width = width
            self.__outlay = 25              # кг/кв.м
            self.thickness = thickness      # толщина покрытия в см


        def get_mass(self):
            return self._length * self._width * self.__outlay * self.thickness / 1000
    l = float(input("Введите длину дороги: "))
    w = float(input("Введите ширину дороги: "))
    s_order = Road(l, w, 10)
    print(f"На строительство дороги нужно {s_order.get_mass()} тонн асфальта")

if task == 3:

    class Worker(object):
        def __init__(self, name, surname, position, wage, bonus):
            self.name = name
            self.surname = surname
            self.position = position
            self._income = {"wage": wage, "bonus": bonus}

    class Position(Worker):
        def __init__(self, name, surname, position, wage, bonus):
            super().__init__(name, surname, position, wage, bonus)

        def get_full_name(self):
            return self.name + ' ' + self.surname

        def get_total_income(self):
            return self._income.get("wage") + self._income.get("bonus")

    worker_one = Position("Иван", "Иванов", "Директор", 150000, 100000)
    print(worker_one.name)
    print(worker_one.surname)
    print(worker_one.position)
    print(worker_one._income)
    print(worker_one.get_full_name())
    print(worker_one.get_total_income())

if task == 4:

    class Car(object):
        def __init__(self, speed, color, name, is_police = False):
            self.speed = speed
            self.color = color
            self.name = name
            self.is_police = is_police

        def go(self):
            print(f"Автомобиль {self.color.title()} {self.name} поехал")

        def stop(self):
            print(f"Автомобиль {self.color.title()} {self.name} остановился")

        def turn(self, direction):
            print(f"Автомобиль {self.color.title()} {self.name} повернул {direction}")

        def show_speed(self):
            print(f"Автомобиль {self.color.title()} {self.name}. Скорость движения: {self.speed} км/ч")


    class TownCar(Car):
        def __init__(self, speed, color, name, is_police = False):
            super().__init__(speed, color, name, is_police = False)

        def show_speed(self):
            if self.speed > 60 :
                print(f"{self.color.title()} {self.name}, вы превысили скорость!!!")
            else:
                print(f"{self.color.title()} {self.name}, скорость движения: {self.speed} км/ч")

    class WorkCar(Car):
        def __init__(self, speed, color, name, is_police=False):
            super().__init__(speed, color, name, is_police=False)

        def show_speed(self):
            if self.speed > 40:
                print("Вы превысили ограничение скорости для рабочего автомобиля!")
            else:
                print(f"Скорость движения: {self.speed} км/ч")

    class SportCar(Car):
        def __init__(self, speed, color, name, is_police=False):
            super().__init__(speed, color, name, is_police=False)

    class PoliceCar(Car):
        def __init__(self, speed, color, name, is_police=True):
            super().__init__(speed, color, name, is_police)

    t_one = TownCar(60,"красный","Citroen")
    print(f"Автомобиль: {t_one.color}, {t_one.name}, {t_one.speed} км/ч, полиция = {t_one.is_police}")

    t_two = TownCar(80,"черный","Volvo")
    print(f"Автомобиль: {t_two.color}, {t_two.name}, {t_two.speed} км/ч, полиция = {t_two.is_police}")

    w = WorkCar(50,"оранжевый","КамАЗ")
    print(f"Автомобиль: {w.color}, {w.name}, {w.speed} км/ч, полиция = {w.is_police}")

    s = SportCar(250,"красно-желтый","Porche")
    print(f"Автомобиль: {s.color}, {s.name}, {s.speed} км/ч, полиция = {s.is_police}")

    p = PoliceCar(90,"бело-голубой","BMW")
    print(f"Автомобиль: {p.color}, {p.name}, {p.speed} км/ч, полиция = {p.is_police}")

    #Все тронулись
    t_one.go()
    t_two.go()
    w.go()
    s.go()
    p.go()

    #смотрим скорость
    t_one.show_speed()
    t_two.show_speed()
    w.show_speed()
    s.show_speed()
    p.show_speed()

    #кто-то поворачивает
    t_one.turn("направо")
    t_two.turn("налево")
    p.turn("налево")

    #полиция останавливает одного из нарушителей :)
    t_two.stop()
    p.stop()

if task == 5:

    class Stationary(object):
        def __init__(self, title):
            self.title = title

        def draw(self):
            print("Запуск отрисовки")

    class Pen(Stationary):
        def __init__(self):
            self.title = "Pen"

        def draw(self):
            print(f"Запуск отрисовки объекта {self.title}")


    class Pencil(Stationary):
        def __init__(self):
            self.title = "Pencil"

        def draw(self):
            print(f"Запуск отрисовки объекта {self.title}")

    class Handle(Stationary):
        def __init__(self):
            self.title = "Handle"

        def draw(self):
            print(f"Запуск отрисовки объекта {self.title}")

    s = Stationary("Степлер")
    pn = Pen()
    pl = Pencil()
    h = Handle()

    s.draw()
    pn.draw()
    pl.draw()
    h.draw()

if task < 1 or task > 5:
    print("Номер задачи должен быть от 1 до 5")