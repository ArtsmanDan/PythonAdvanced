a = 0
min_num = 1
max_num = 9999
while True:
    text = input(f"Введите число от {min_num} до {max_num} или наберите exit для выхода: >>> ")
    if text == 'exit': exit()
    if text.isdigit():
        a = int(text)
        if min_num <= a <= max_num: break
        else: print(f'число не в диапазоне {min_num} до {max_num}')
    else: print('Введено не число')


if 1 <= a < 10:
    a1 = a * a
    print(f' Вы ввели число: {a}, квадрат равен {a1}')
if 10 <= a < 100:
    b = a // 10
    c = a % 10
    d = b * c
    print(f' Вы ввели число: {a}, произведение равно {d}')

if 100 <= a < 1000:
    c = a % 100
    b1 = a // 100
    b2 = c // 10
    b3 = c % 10
    print(f' Вы ввели число: {a}, а мы его вывернули на изнанку  {b3}{b2}{b1}')

