year = int(input('Напишиет год в формате: хххх '))
if year % 4 == 0:
    if year % 100 != 0:
        print("Этот год Високосный")
    elif year % 400 == 0:
        print("Этот год Високосный")
    else:
        print("простой год")
else:
    print("простой год")