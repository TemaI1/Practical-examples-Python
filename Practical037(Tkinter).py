# Combobox Обучение Python GUI (уроки по Tkinter)

from tkinter import *
from tkinter.ttk import Combobox # добавит виджет поля с выпадающем списком

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('600x400') # установить размер окна

combo = Combobox(window)
combo['values'] = (1, 2, 3, 4, 5, "Текст") # добавит значения в поле со списком
combo.current(2)  # установит вариант индекса combo['values'] по умолчанию
combo.grid(column=0, row=0) # установим позицию в окне

window.mainloop()
