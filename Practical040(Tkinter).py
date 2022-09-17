# ScrolledText Обучение Python GUI (уроки по Tkinter)

from tkinter import *
from tkinter import scrolledtext

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('600x400') # установить размер окна

txt = scrolledtext.ScrolledText(window, width=40, height=10) # класс ScrolledText, ширина и высота
txt.insert(INSERT, 'Текстовое поле') # настроить содержимое
txt.delete(1.0, END) # очистить содержимое, с координатами очистки
txt.grid(column=0, row=0) # установим позицию в окне

window.mainloop()
