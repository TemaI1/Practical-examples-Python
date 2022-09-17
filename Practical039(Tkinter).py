# Radiobutton Обучение Python GUI (уроки по Tkinter)

from tkinter import *
from tkinter.ttk import Radiobutton

def clicked():  
    lbl.configure(text=selected.get()) # получит элемент, использовав функцию get

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('600x400') # установить размер окна

selected = IntVar()

rad1 = Radiobutton(window, text='Первый', value=1, variable=selected) # установим value каждой кнопки с уникальным значением
rad2 = Radiobutton(window, text='Второй', value=2, variable=selected) # установим value каждой кнопки с уникальным значением
rad3 = Radiobutton(window, text='Третий', value=3, variable=selected) # установим value каждой кнопки с уникальным значением
rad1.grid(column=0, row=0) # установим позицию в окне
rad2.grid(column=1, row=0) # установим позицию в окне
rad3.grid(column=2, row=0) # установим позицию в окне

btn = Button(window, text="Клик", command=clicked) # подключим ​функцию с помощью кнопки
btn.grid(column=3, row=0) # установим позицию в окне

lbl = Label(window)
lbl.grid(column=0, row=1) # установим позицию в окне

window.mainloop()
