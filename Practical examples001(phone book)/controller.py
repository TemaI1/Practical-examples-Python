import data

def open_all_contacts():
    book = open('phone book.txt', 'r')
    print(book.read())
    book.close()

def create_new_contact():
    with open('phone book.txt', 'a') as book:
        book.write(f'\nname: {data.name()} age: {data.age()} placement: {data.placement()} telephone: {data.telephone()}')

def delete_book():
    with open('phone book.txt', 'w') as book:
        book.write(f'name: {data.name()} age: {data.age()} placement: {data.placement()} telephone: {data.telephone()}')

def go():
    do = int(input('1 - Открыть книгу \n2 - Добавить контакт \n3 - Перезаписать книгу \n4 - Выход из программы \nВведите, что вы хотите сделать 1-4: '))
    while do <= 4:
        if do == 1:
            open_all_contacts()
        if do == 2:
            create_new_contact()
        if do == 3:
            delete_book()
        if do == 4:
            print('Goodbye!')
            break
        do = int(input('1 - Открыть книгу \n2 - Добавить контакт \n3 - Перезаписать книгу \n4 - Выход из программы \nВведите, что вы хотите сделать 1-4: '))
        