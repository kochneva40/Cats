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
        img.thumbnail((600,480), Image.Resampling.LANCZOS) #Подгоняем изображения под окно не теряя качества
        return ImageTk.PhotoImage(img)
    except Exception as e:
        print(f"Произошла ошибка: {e}")
        return None


def open_new_window(): # Открыть картинку в новом окне
    img = load_image(url)  # Функция загрузки изображения в который передаем адрес картинки

    if img:
        new_window = Toplevel()
        new_window.title("Картинка с котиком")
        new_window.geometry("600x480")
        label = Label(new_window, image=img)  # Создаем метку на которой будет выводиться
        label.pack()
        label.image = img  # Чтобы сборщик мусора не выбросил нашу картинку


def exit(): # Функция закрытия окна
    window.destroy()


window = Tk()
window.title("Cats!")
window.geometry("600x520")



# update_button = Button(text="Обновить", command=set_image) # Кнопка обновления изображения
# update_button.pack()

menu_bar = Menu(window) # Добавляем меню
window.config(menu=menu_bar)

file_menu = Menu(menu_bar, tearoff=0) # Добавляем меню
menu_bar.add_cascade(label="Файл", menu=file_menu)
file_menu.add_command(label="Загрузить фото", command=open_new_window)
file_menu.add_separator()
file_menu.add_command(label="Выход", command=exit)




url = "https://cataas.com/cat"

open_new_window() # Вызываем функцию отображения картинки при первом запуске проекта

window.mainloop()
