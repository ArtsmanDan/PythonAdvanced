min_num = 2
max_num = 100
num = 0
STAR = '*'
SPACE = ' '
while True:
    text = input(f"Введите сколько рядов должно быть у ёлки, число должно быть \n"
                 f"от {min_num} до {max_num} или наберите exit для выхода: >>> ")
    if text == 'exit': exit()
    if text.isdigit():
        num = int(text)
        if min_num <= num <= max_num: break
        else: print(f'число не в диапазоне {min_num} до {max_num}')
    else: print('Введено не число')

spaces = num - 1
stars = 1
for i in range(num):
    print((SPACE * spaces) + (STAR * stars) + (SPACE * spaces))
    # sp = ''
    # st = ''
    # for j in range(spaces):
    #     sp += SPACE
    # for j in range(stars):
    #     st += STAR
    # print(sp + st + sp)
    spaces -= 1
    stars += 2
# # ___***___
# # __*****__
# # _*******_
# # *********

# # _____*_____
# # ____***____
# # ___*****___
# # __*******__
# # _*********_
# # ***********




