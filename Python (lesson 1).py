task = int(input('Введите номер задачи: '))

if task == 1:
    a = 1
    b = 'test'
    c = input('введите числовую переменную с:')
    s = input('введите строку s:')
    print(f'переменная a: {a}')
    print(f'переменная b: {b}')
    print(f'переменная c: {c}')
    print(f'переменная s: {s}')
elif task == 2:
    base = 60
    c = int(input('Введите время в секундах: '))
    seconds = str(c % base)
    all_minutes = c // base
    hours = str(all_minutes // base)
    minutes = str(all_minutes % base)
    if len(seconds) == 1:
        seconds = '0' + seconds
    if len(minutes) == 1:
        minutes = '0' + minutes
    if len(hours) == 1:
        hours = '0' + hours
    print(f"Вы ввели время {hours}:{minutes}:{seconds}")
elif task == 3:
    n = input('Введите целое число: ')
    nn = n + n
    nnn = nn + n
    result = int(n) + int (nn) + int (nnn)
    print(f'Ваш результат: {result}')
elif task == 4:
    n = abs(int(input('Введите целое число, можно даже отрицательное ;) : ')))
    max_digit = 0
    while(n // 10 > 0):
        m = n % 10
        if m > max_digit:
            max_digit = m
        n = n // 10
    if n > max_digit:
        max_digit = n
    print(f'Максимальная цифра во введенном числе: {max_digit}')
elif task == 5:
    income = int(input('Введите вашу выручку за месяц (округлите до 1 рубля): '))
    cost = int(input('Введите ваши затраты за месяц (округлите до 1 рубля): '))
    benefit = income - cost
    if benefit == 0:
        print('Удивительная точность: сколько заработали, столько и потратили :). Ждите налоговую инспекцию с проверкой ;)')
    elif benefit < 0:
        print(f'Увы, этот месяц вы отработали в убыток, потери составили {abs(benefit)} рублей')
    else:
        print(f'Поздравляю! Этот месяц вы отработали с прибылью, заработано {benefit} рублей')
        print(f'Рентабельность за месяц составила {round(benefit/income*100,2)} процентов')
        staff = int(input('Какое количество сотрудников у вас работает? : '))
        print(f'Прибыль в расчете на одного сотрудника составила {round(benefit/staff,2)} рублей')
elif task == 6:
    a = int(input('С какой дистанции спортсмен начинает тренировки? (округлите до километра): '))
    b = int(input('На какую дистанцию он должен выйти, прибавляя по 10% в день? (округлите до километра): '))
    i = 1
    if b < a:
        print('Целевая дистанция меньше начальной')
    else:
        while a < b:
            a += 0.1 * a
            i += 1
            print(f'{i}-й день: {round(a,2)} километров')
        print(f'На {i} день спортсмен достигнет результата - не менее {b} километров')
elif task < 1:
    print('Нумерация задач начинается с 1')
else:
    print('Но-но-но! Не увлекайтесь. Задач было всего 6')

