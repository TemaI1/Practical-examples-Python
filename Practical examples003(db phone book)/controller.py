import data
import db

def open_all_contacts():
    for value in db.sql.execute("SELECT * FROM users"):
        print(f'name: {value[0]}, age: {value[1]}, placement: {value[2]}, telephone: {value[3]}')

def create_new_contact():
    db.sql.execute(f"INSERT INTO users VALUES (?, ?, ?, ?)", (data.name(), data.age(), data.placement(), data.telephone()))
    db.db.commit()
    print('Создали новую запись')

def go():
    do = int(input('1 - Открыть книгу \n2 - Добавить контакт \n3 - Выход из программы \nВведите, что вы хотите сделать 1-3: '))
    while do <= 3:
        if do == 1:
            open_all_contacts()
        if do == 2:
            create_new_contact()
        if do == 3:
            print('Goodbye!')
            break
        do = int(input('1 - Открыть книгу \n2 - Добавить контакт \n3 - Выход из программы \nВведите, что вы хотите сделать 1-3: '))