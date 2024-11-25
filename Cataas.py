from tkinter import *
from PIL import Image, ImageTk
import requests
from io import BytesIO # Чтобы превратить картинку в нормальное изображение


def load_image(url): # Функция для картинки
    try: # Обработка исключений
        response = requests.get(url) # Запрос по адресу
        response.raise_for_status()
        image_data = BytesIO(response.content)
        img = Image.open(image_data)
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


window = Tk()
window.title("Cats!")
window.geometry("600x400")

Label = Label() # Создаем метку на которой будет выводиться
Label.pack()

url = "https://cataas.com/cat"
img = load_image(url) # Функция загрузки изображения в который передаем адрес картинки

if img:
    Label.config(image=img)
    Label.image = img # Чтобы сборщик мусора не выбросил нашу картинку

window.mainloop()
