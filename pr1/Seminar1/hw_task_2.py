# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

num = 4551


if 0 < num <= 100000:
    i = 2
    while i < num:
        if num % i == 0:
            print('составное')
            print(i)
            exit()
        i += 1
    print('простое')
else: print('Это число не подходит')

def is_simple(num):
    if num % 2 == 0:
        return num == 2
    i = 3
    while i * i <= num and num % i != 0:
        i += 2
    return i * i > num



# Напишите код, который запрашивает число и сообщает является ли оно простым или составным.
# Используйте правило для проверки: «Число является простым, если делится нацело только на единицу
# и на себя». Сделайте ограничение на ввод отрицательных чисел и чисел больше 100 тысяч.

def is_simple(num):
    if num % 2 == 0:
        return num == 2
    i = 3
    while i * i <= num and num % i != 0:
        i += 2
    return i * i > num


def advanced_input(min, max):
    while True:
        text = input(f'введите число от {min} до {max} или exit для выхода >>> ')
        if text == 'exit': exit()
        if text.isdigit():
            num = int(text)
            if min <= num <= max:
                return num
            else:
                print(f'Число не входит в диапазон от {min} до {max}')
        else:
            print("Введено не число")


min = 1
max = 100000
num = advanced_input(min, max)
if is_simple(num):
    print("Число является простым")
else:
    print('Число является составным')
