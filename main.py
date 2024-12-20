from image.imageHandler import ImageHandler
from image.imageProcessor import ImageProcessor
import os

def main_menu():
    # Функция для отображения меню и получения выбора пользователя
    print()
    print(" Меню работы с изображением ".center(80,"="))
    print("1. Конвертировать изображение в формат PNG")
    print("2. Повернуть изображение на 45 градусов")
    print("3. Применить фильтр резкости")
    print("4. Добавить рамку к изображению")
    print("5. Сохранить изображение")
    print("6. Показать изображение")
    print("7. Выход")
    return input("Выберите действие: ")

def main():
    # Основная функция программы
    # Исходное изображение передаётся в коде
    initial_image_path = "image_5.jpg"  # Укажите путь к вашему изображению
    handler = ImageHandler(initial_image_path)
    try:
        handler.load_image()
        print("Изображение успешно загружено из пути:", initial_image_path)
    except FileNotFoundError:
        print(f"Ошибка: Файл не найден по пути: {initial_image_path}")
        return
    processor = ImageProcessor(handler.get_image())

    # Создаем папку saved_images, если ее нет
    save_dir = "saved_images"
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)


    while True:
        choice = main_menu()  # Отображение меню и получение выбора пользователя

        if choice == "1":
            # Конвертация изображения в формат PNG
            if handler.image:
                filename = os.path.basename(initial_image_path)
                name, ext = os.path.splitext(filename)
                save_path = os.path.join(save_dir, f"{name}.png")
                handler.convert_to_png(save_path)
                print(f"Изображение сохранено в формате PNG по пути {save_path}.")
            else:
                print("Изображение не загружено.")

        elif choice == "2":
            # Поворот изображения на 45 градусов
            if handler.image:
                handler.rotate_image()
                processor.image = handler.get_image()
                print("Изображение повернуто на 45 градусов.")
            else:
                print("Изображение не загружено.")

        elif choice == "3":
             # Применение фильтра резкости
            if handler.image:
                processor.apply_sharpen_filter()
                handler.image = processor.get_image()
                print("Фильтр резкости применён.")
            else:
                 print("Изображение не загружено.")
        elif choice == "4":
            # Добавление рамки к изображению
             if handler.image:
                processor.add_border()
                handler.image = processor.get_image()
                print("Рамка добавлена.")
             else:
                print("Изображение не загружено.")
        elif choice == "5":
           # Сохранение изображения
            if handler.image:
                filename = os.path.basename(initial_image_path)
                name, ext = os.path.splitext(filename)
                save_path = os.path.join(save_dir, f"{name}_processed{ext}")
                handler.save_image(save_path)
                print(f"Изображение сохранено по пути {save_path}.")
            else:
                print("Изображение не загружено.")

        elif choice == "6":
            # Показ изображения
            if handler.image:
                handler.image.show()
            else:
                print("Изображение не загружено.")

        elif choice == "7":
            # Выход из программы
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")


if __name__ == "__main__":
    main()
