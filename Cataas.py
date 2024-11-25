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
        img.thumbnail((600,480), Image.Resampling.LANCZOS) #Подгоняем изображения под окно
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def set_image():
    img = load_image(url)  # Функция загрузки изображения в который передаем адрес картинки

    if img:
        label.config(image=img)
        label.image = img  # Чтобы сборщик мусора не выбросил нашу картинку


window = Tk()
window.title("Cats!")
window.geometry("600x520")

label = Label() # Создаем метку на которой будет выводиться
label.pack()

update_button = Button(text="Обновить", command=set_image) # Кнопка обновления изображения
update_button.pack()

url = "https://cataas.com/cat"

set_image() # Вызываем функцию отображения картинки при первом запуске проекта

window.mainloop()
