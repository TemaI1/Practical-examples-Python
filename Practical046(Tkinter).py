# Notebook(управление вкладкой) Обучение Python GUI (уроки по Tkinter)

from tkinter import *
from tkinter import ttk

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('600x400') # установить размер окна

tab_control = ttk.Notebook(window) # создается элемент управления вкладкой

tab1 = ttk.Frame(tab_control) # создаст вкладку, используя класс Frame
tab2 = ttk.Frame(tab_control) # создаст вкладку, используя класс Frame

tab_control.add(tab1, text='Первая') # добавит tab1(вкладку) в элемент управления вкладками
tab_control.add(tab2, text='Вторая') # добавит tab1(вкладку) в элемент управления вкладками

lbl1 = Label(tab1, text='Вкладка 1') # добавить текст
lbl1 = Label(tab1, text= 'Вкладка 1', padx=10, pady=10) # padx и pady отступы для элементов 
lbl1.grid(column=0, row=0) # установим позицию в окне

lbl2 = Label(tab2, text='Вкладка 2') # добавить текст
lbl2.grid(column=0, row=0) # установим позицию в окне

tab_control.pack(expand=1, fill='both') # запакует tab_control, чтобы он стал видимым в окне

window.mainloop()
