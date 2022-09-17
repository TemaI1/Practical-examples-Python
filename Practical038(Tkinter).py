# Checkbutton Обучение Python GUI (уроки по Tkinter)

from tkinter import *
from tkinter.ttk import Checkbutton

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('600x400') # установить размер окна

chk1_state = IntVar() # создаем переменную типа IntVar
chk1_state.set(0) # False или chk_state.set(1) # True (проверка состояния чекбокса)
chk1 = Checkbutton(window, text='Выбрать', var=chk1_state) # передаем IntVar классу Checkbutton
chk1.grid(column=1, row=0) # установим позицию в окне

chk2_state = BooleanVar() # создаем переменную типа BooleanVar
chk2_state.set(True)  # задайте проверку состояния чекбокса
chk2 = Checkbutton(window, text='Выбрать', var=chk2_state) # передаем BooleanVar классу Checkbutton
chk2.grid(column=0, row=0) # установим позицию в окне

window.mainloop()
