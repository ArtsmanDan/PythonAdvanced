n = int(input(" Введите первое число n: "))
e = int(input(" Введите первое число e: "))
a = 2
sum = 0
ZERO = 0
if n > ZERO and e > ZERO:
    while a <= n:
        if a % e != 0:
            sum = sum + a
            # print(a)
        a += 2
print(sum)