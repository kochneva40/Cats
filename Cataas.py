from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO # Чтобы превратить картинку в нормальное изображение

window = Tk()
window.title("Cats!")
window.geometry("600x400")

Label = Label() # Создаем метку на которой будет выводиться
Label.pack()

url = "https://cataas.com/cat"
img = load_image() # функция загрузки изображения в который передаем url

if img:
    label.config(image=img)
    label.image = img # Чтобы сборщик мусора не выбросил нашу картинку

window.mainloop()
