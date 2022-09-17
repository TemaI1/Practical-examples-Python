# messagebox(окна с сообщением) Обучение Python GUI (уроки по Tkinter)

from tkinter import *
from tkinter import messagebox

def clicked():
    messagebox.showinfo('Заголовок', 'Текст') # показывает информационное сообщение
    messagebox.showwarning('Заголовок', 'Текст')  # показывает предупреждающее сообщение
    messagebox.showerror('Заголовок', 'Текст')  # показывает сообщение об ошибке

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('600x400') # установить размер окна

btn = Button(window, text="Клик!", command=clicked) # подключим ​функцию с помощью кнопки
btn.grid(column=0, row=0) # установим позицию в окне

res = messagebox.askquestion('Заголовок', 'Текст') # да, нет
res = messagebox.askyesno('Заголовок', 'Текст') # да, нет
res = messagebox.askyesnocancel('Заголовок', 'Текст') # да, нет, отмена 
res = messagebox.askokcancel('Заголовок', 'Текст') # ок, отмена
res = messagebox.askretrycancel('Заголовок', 'Текст') # повтор, отмена

window.mainloop()
