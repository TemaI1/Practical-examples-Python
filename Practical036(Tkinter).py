# Обучение Python GUI (уроки по Tkinter)

from tkinter import *

def clicked():
    lbl.configure(text="Я же просил...") # функция, которую нужно выполнить при нажатии кнопки

def clicked():
    res = "Привет {}".format(txt.get())
    lbl.configure(text=res)              # получить текст ввода, используя функцию

window = Tk()
window.title("PythonRu")
window.geometry('600x400') # установить размер окна

lbl = Label(window, text="Добрый день") # добавить текст
lbl = Label(window, text="Привет", font=("Arial Bold", 50)) # задать шрифт текста и размер
lbl.grid(column=0, row=0) # установим позицию в окне

txt = Entry(window, width=10) # получить пользовательский ввод
txt.focus() # дает возможность сразу написать текст (виджет ввода в фокусе)
# txt = Entry(window,width=10, state='disabled') # отключит виджет ввода
txt.grid(column=1, row=0) # установим позицию в окне


btn = Button(window, text="Не нажимать!") # кнопка создается и добавляется в окно
btn = Button(window, text="Не нажимать!", bg="black", fg="red") # поменять цвет текста fg, поменять цвет фона bg
btn = Button(window, text="Клик!", command=clicked) # подключим ​функцию с помощью кнопки
btn.grid(column=2, row=0) # установим позицию в окне

window.mainloop() # функция вызывает бесконечный цикл окна
