# SpinBox Обучение Python GUI (уроки по Tkinter)

from tkinter import *

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('600x400') # установить размер окна

spin = Spinbox(window, from_=-100, to=100, width=5) # создания спинбокса, from и to диапазон номеров, width ширина
spin.grid(column=0, row=0) # установим позицию в окне

spin = Spinbox(window, values=(3, 8, 11), width=5) # покажет только эти числа: 3, 8 и 11
spin.grid(column=1, row=0) # установим позицию в окне

var = IntVar()
var.set(36) # задать значение по умолчанию
spin = Spinbox(window, from_=0, to=100, width=5, textvariable=var)
spin.grid(column=2, row=0) # установим позицию в окне

window.mainloop()
