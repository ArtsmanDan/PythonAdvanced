# Напишите программу банкомат.
# ✔ Начальная сумма равна нулю
# ✔ Допустимые действия: пополнить, снять, выйти
# ✔ Сумма пополнения и снятия кратны 50 у.е.
# ✔ Процент за снятие — 1.5% от суммы снятия, но не менее 30 и не более 600 у.е.
# ✔ После каждой третей операции пополнения или снятия начисляются проценты - 3%
# ✔ Нельзя снять больше, чем на счёте
# ✔ При превышении суммы в 5 млн, вычитать налог на богатство 10% перед каждой
# операцией, даже ошибочной
# ✔ Любое действие выводит сумму денег
import sys

balance = 0
banknot = 50
take_off_min = 30
take_off_max = 600
take_off_percent = 0.015
percent_debit = 0.03
count_period = 3
tax = 0.1
limit = 5_000_000
count_operation = 0


def show_balance():
    print(f'На вашем счету: {balance}')


def tax_pay():
    global balance
    if balance > limit:
        tax1 = tax * balance
        print(f'С вас снят налог в размере {tax1}')
        balance -= tax1


def add_percent():
    global balance
    global count_operation
    count_operation += 1
    if count_operation % count_period == 0:
        sum_percent = balance * percent_debit
        balance += sum_percent
        print(f'Начислен процент  {sum_percent}')

def is_multiplicity(sum):
    if sum % banknot == 0:
        return True
    else:
        return False


# Внесение денег
def replenishment(sum):
    global balance
    if is_multiplicity(sum):
        balance += sum
        add_percent()
    else:
        print('Сумма не кратна')
    show_balance()


def take_off(sum):
    global balance
    if balance >= sum:
        if is_multiplicity(sum):
            if sum * take_off_percent < take_off_min:
                sum_take_off_percent = take_off_min
            elif sum * take_off_percent > take_off_max:
                sum_take_off_percent = take_off_max
            else:
                sum_take_off_percent = take_off_percent * balance
            if balance > sum + sum_take_off_percent:
                balance = balance - sum - sum_take_off_percent
                print(f'Cписан процент за снятие в размере: {sum_take_off_percent} ')
                add_percent()
            else: print('Отсутствует нужная сумма на балансе')
        else:
            print(f'Сумма не кратна {banknot} ')
    else:
        print('Недостаточно денег на счете')
    show_balance()


def advanced_input(min=1, max=3):
    while True:
        tax_pay()
        text = input(
            f'Какую операцию вы желаете произвести:\n 1. Снять наличные \n 2. Пополнить баланс \n 3. Выход >>> ')
        if text == '3': exit()
        try:
            num = int(text)
        except ValueError:
            print("Введено не число")
            continue
        if min <= num <= max:
            return num
        else:
            print(f'Число не входит в диапазон от {min} до {max}')


def advanced_input_sum(min=banknot, max=sys.maxsize):
    while True:
        show_balance()
        text = input(f'Введите сумму в диапазон от {min} до {max}, или exit для завершения >>> ')
        if text == 'exit': exit()
        try:
            num = int(text)
        except ValueError:
            print("Введено не число")
            continue
        if min <= num <= max:
            return num
        else:
            print(f'Число не входит в диапазон от {min} до {max}')


while True:
    num = advanced_input(1, 3)
    if num == 1:
        sum = advanced_input_sum()
        take_off(sum)
    if num == 2:
        sum = advanced_input_sum()
        replenishment(sum)
    if num == 3:
        pass
