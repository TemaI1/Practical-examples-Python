# Progressbar Обучение Python GUI (уроки по Tkinter)

from tkinter import *
from tkinter.ttk import Progressbar
from tkinter import ttk

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('600x400') # установить размер окна

style = ttk.Style()
style.theme_use('default')
style.configure("red.Horizontal.TProgressbar", background='red')
bar2 = Progressbar(window, length=200, style='red.Horizontal.TProgressbar') # созданный стиль
bar2['value'] = 70 # заполненный на 70, значение progressbar
bar2.grid(column=0, row=0) # установим позицию в окне

bar1 = Progressbar(window, length=100) # созданный стиль
bar1['value'] = 30 # заполненный на 30, значение progressbar
bar1.grid(column=0, row=1) # установим позицию в окне

window.mainloop()
