# Создайте программу для игры в ""Крестики-нолики"".

def table():
    print(list[0], list[1], list[2])
    print(list[3], list[4], list[5])
    print(list[6], list[7], list[8])

def completion_x(figure):
    if figure == 1:
        list[0] = 'x'
    if figure == 2:
        list[1] = 'x'
    if figure == 3:
        list[2] = 'x'
    if figure == 4:
        list[3] = 'x'
    if figure == 5:
        list[4] = 'x'
    if figure == 6:
        list[5] = 'x'
    if figure == 7:
        list[6] = 'x'
    if figure == 8:
        list[7] = 'x'
    if figure == 9:
        list[8] = 'x'  

def completion_o(figure):
    if figure == 1:
        list[0] = 'o'
    if figure == 2:
        list[1] = 'o'
    if figure == 3:
        list[2] = 'o'
    if figure == 4:
        list[3] = 'o'
    if figure == 5:
        list[4] = 'o'
    if figure == 6:
        list[5] = 'o'
    if figure == 7:
        list[6] = 'o'
    if figure == 8:
        list[7] = 'o'
    if figure == 9:
        list[8] = 'o'  


    list[0] == 1 or list[1] == 2 or list[2] == 3 or list[3] == 4 or list[4] == 5 or list[5] == 6 or list[6] == 7 or list[7] == 8 or list[8] == 9

def combination_x():
    if list[0] == 'x' and list[1] == 'x' and list[2] == 'x':
        print('Первый игрок победил')
    if list[3] == 'x' and list[4] == 'x' and list[5] == 'x':
        print('Первый игрок победил')
    if list[6] == 'x' and list[7] == 'x' and list[8] == 'x':
        print('Первый игрок победил')
    if list[0] == 'x' and list[3] == 'x' and list[6] == 'x':
        print('Первый игрок победил')
    if list[1] == 'x' and list[4] == 'x' and list[7] == 'x':
        print('Первый игрок победил')
    if list[2] == 'x' and list[5] == 'x' and list[8] == 'x':
        print('Первый игрок победил')
    if list[0] == 'x' and list[4] == 'x' and list[8] == 'x':
        print('Первый игрок победил')
    if list[2] == 'x' and list[4] == 'x' and list[6] == 'x':
        print('Первый игрок победил')

def combination_o():
    if list[0] == 'o' and list[1] == 'o' and list[2] == 'o':
        print('Второй игрок победил')
    if list[3] == 'o' and list[4] == 'o' and list[5] == 'o':
        print('Второй игрок победил')
    if list[6] == 'o' and list[7] == 'o' and list[8] == 'o':
        print('Второй игрок победил')
    if list[0] == 'o' and list[3] == 'o' and list[6] == 'o':
        print('Второй игрок победил')
    if list[1] == 'o' and list[4] == 'o' and list[7] == 'o':
        print('Второй игрок победил')
    if list[2] == 'o' and list[5] == 'o' and list[8] == 'o':
        print('Второй игрок победил')
    if list[0] == 'o' and list[4] == 'o' and list[8] == 'o':
        print('Второй игрок победил')
    if list[2] == 'o' and list[4] == 'o' and list[6] == 'o':
        print('Второй игрок победил')

list = [1, 2, 3, 4, 5, 6, 7, 8, 9]
table()

while list[0] == 1 or list[1] == 2 or list[2] == 3 or list[3] == 4 or list[4] == 5 or list[5] == 6 or list[6] == 7 or list[7] == 8 or list[8] == 9:
    first_play = int(input('Введите на кокой позиции list (1-9) вы хотите поставить x: '))
    completion_x(first_play)
    table()
    second_play = int(input('Введите на кокой позиции list (1-9) вы хотите поставить o: '))
    completion_o(second_play)
    table()
    combination_x()
    combination_o()
