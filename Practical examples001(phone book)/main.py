import controller as con

do = int(input('1 - Открыть книгу \n2 - Добавить контакт \n3 - Перезаписать книгу \nВведите, что вы хотите сделать 1-3: '))

if do == 1:
    con.open_all_contacts()
if do == 2:
    con.create_new_contact()
if do == 3:
    con.delete_book()
