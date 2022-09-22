import data

def open_all_contacts():
    book = open('phone book.txt', 'r')
    print(book.read())
    book.close()

def create_new_contact():
    with open('phone book.txt', 'a') as book:
        book.write(f'\nИмя: {data.name()} Возраст: {data.age()} Адрес: {data.placement()} Телефон: {data.telephone()}')

def delete_book():
    with open('phone book.txt', 'w') as book:
        book.write(f'Имя: {data.name()} Возраст: {data.age()} Адрес: {data.placement()} Телефон: {data.telephone()}')
