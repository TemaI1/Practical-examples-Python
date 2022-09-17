# Загрузки файла GUI (уроки по Tkinter)

from tkinter import *
from tkinter import filedialog # добавления поля с файлом

window = Tk()
window.title("Добро пожаловать в приложение PythonRu")
window.geometry('600x400') # установить размер окна

file = filedialog.askopenfilename() # переменная файла будет содержать этот путь к файлу

file = filedialog.askopenfilename(filetypes = (("Text files","*.txt"),("all files","*.*"))) # указания типа файлов, важно указать расширение в tuples

dir = filedialog.askdirectory() # запросить каталог

from os import path
file = filedialog.askopenfilename(initialdir= path.dirname(__file__)) # указать начальную директорию для диалогового окна файла

window.mainloop()
