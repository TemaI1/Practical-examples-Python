# Панель меню Обучение Python GUI (уроки по Tkinter)

from tkinter import *
from tkinter import Menu

def clicked():
    lbl.configure(text="Спасибо что нажал") # функция, которую нужно выполнить при нажатии кнопки "Нажми на меня"

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('600x400') # установить размер окна

menu = Menu(window) #создаем меню

new_item = Menu(menu) #создаем меню
menu.add_cascade(label='Файл', menu=new_item) # добавить пункты меню
new_item.add_command(label='Создать') # добавляем пункт подменю
new_item.add_command(label='Изменить') # добавляем пункт подменю
new_item.add_command(label='Нажми на меня', command=clicked) # подключим ​функцию с помощью меню "Нажми на меня"

new_item2 = Menu(menu, tearoff=0) # создаем меню и заменяем(отключаем) пунктирную линию
menu.add_cascade(label='Текст', menu=new_item2) # добавить пункты меню
new_item2.add_command(label='Стиль') # добавляем пункт подменю
new_item2.add_separator() # разделитель меню
new_item2.add_command(label='Размер') # добавляем пункт подменю

lbl = Label(window) # добавить текст
lbl.grid(column=0, row=0) # установим позицию в окне

window.config(menu=menu)

window.mainloop()
