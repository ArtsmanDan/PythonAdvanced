text = input('Ведите текст или число: >>> ')
if text.isdigit():
    text = int(text)
    text1 = oct(text)
    text2 = hex(text)
    print(text, text1, text2)
    # print(text.int(), text.oct(), text.hex())

if str:
    print('Да это "ASCII"')