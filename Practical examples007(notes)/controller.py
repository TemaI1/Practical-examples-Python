import data

def open_all():
    book = open('book of notes.json', 'r')
    print(book.read())
    book.close()

def create_new():
    with open('book of notes.json', 'a') as book:
        book.write(f'\nheading: {data.heading()}; date of note change: {data.dateChange()}; note number: {data.noteID()}; information: {data.info()}')

def delete_book_note():
    with open('book of notes.json', 'w') as book:
        book.write(f'heading: {data.heading()}; date of note change: {data.dateChange()}; note number: {data.noteID()}; information: {data.info()}')

def go():
    do = int(input('1 - Открыть книгу заметок \n2 - Добавить заметку \n3 - Перезаписать книгу, добавить новую заметку \n4 - Выход из программы \nВведите, что вы хотите сделать 1-4: '))
    while do <= 4:
        if do == 1:
            open_all()
        if do == 2:
            create_new()
        if do == 3:
            delete_book_note()
        if do == 4:
            print('Goodbye!')
            break
        do = int(input('1 - Открыть книгу заметок \n2 - Добавить заметку \n3 - Перезаписать книгу, добавить новую заметку \n4 - Выход из программы \nВведите, что вы хотите сделать 1-4: '))
        