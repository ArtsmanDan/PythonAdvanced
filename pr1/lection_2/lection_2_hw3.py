# Напишите программу, которая принимает две строки вида “a/b” - дробь с числителем и знаменателем.
# Программа должна возвращать сумму и произведение* дробей. Для проверки своего кода используйте модуль fractions.

from fractions import Fraction
import math

fraction1 = '1/2'
fraction2 = '1/2'


def simplify_fraction(numerator, denominator):
    if math.gcd(numerator, denominator) == denominator:
        return int(numerator / denominator)
    elif math.gcd(numerator, denominator) == 1:
        return str(numerator) + "/" + str(denominator)
    else:
        top = int(numerator / math.gcd(numerator, denominator))
        bottom = int(denominator / math.gcd(numerator, denominator))
        return str(top) + "/" + str(bottom)


def split_fraction(fraction1: str, fraction2: str):
    try:
        num1_1 = int(fraction1.split('/')[0])
        num1_2 = int(fraction1.split('/')[1])
        num2_1 = int(fraction2.split('/')[0])
        num2_2 = int(fraction2.split('/')[1])
    except ValueError:
        return None
    return num1_1, num1_2, num2_1, num2_2


def multiplying_fractions(fraction1, fraction2):
    num1_1, num1_2, num2_1, num2_2 = split_fraction(fraction1, fraction2)
    multi_fract1 = num1_1 * num2_1
    multi_fract2 = num1_2 * num2_2
    fraction = simplify_fraction(multi_fract1, multi_fract2)
    print(f'Произведение "{fraction1}" и  "{fraction2}" равна "{multi_fract1}/{multi_fract2}"')
    print(f'Произведение "{fraction1}" и  "{fraction2}" равна "{fraction}"')
    print(f'Проверка: Произведение "{fraction1}" и  "{fraction2}" равна "{Fraction(fraction1) * Fraction(fraction2)}"')


def sum_fractions(fraction1, fraction2):
    num1_1, num1_2, num2_1, num2_2 = split_fraction(fraction1, fraction2)
    sum_fract1 = num1_1 * num2_2 + num2_1 * num1_2
    sum_fract2 = num1_2 * num2_2
    fraction = simplify_fraction(sum_fract1, sum_fract2)
    print(f'Сумма "{fraction1}" и  "{fraction2}" равна "{sum_fract1}/{sum_fract2}"')
    print(f'Сумма "{fraction1}" и  "{fraction2}" равна "{fraction}"')
    print(f'Проверка: Сумма "{fraction1}" и  "{fraction2}" равна "{Fraction(fraction1) + Fraction(fraction2)}"')


multiplying_fractions(fraction1, fraction2)
sum_fractions(fraction1, fraction2)