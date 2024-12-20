from image import ImageHandler
from image import ImageProcessor

def main_menu():
    # Функция для отображения меню и получения выбора пользователя
    print()
    print(" Меню работы с изображением ".center(80,"="))
    print("1. Конвертировать изображение в формат PNG")
    print("2. Повернуть изображение на 45 градусов")
    print("3. Применить фильтр резкости")
    print("4. Добавить рамку к изображению")
    print("5. Сохранить изображение")
    print("7. Выход")
    return input("Выберите действие: ")

def main():
    # Основная функция программы
    # Исходное изображение передаётся в коде
    initial_image_path = "input.jpg"  # Укажите путь к вашему изображению
    handler = ImageHandler(initial_image_path)
    if handler.image is None:
        print("Ошибка: Не удалось загрузить изображение.")
        return
    print("Изображение успешно загружено из пути:", initial_image_path)
    processor = ImageProcessor(handler.get_image())

    while True:
        choice = main_menu()  # Отображение меню и получение выбора пользователя

        if choice == "1":
            # Конвертация изображения в формат PNG
            save_path = input("Введите путь для сохранения (с расширением .png): ")
            handler.save(save_path, format="PNG")
            print(f"Изображение сохранено в формате PNG по пути {save_path}.")


        elif choice == "2":
            # Поворот изображения на 45 градусов
            rotated_image = handler.rotate(45, "rotated.jpg")
            if rotated_image is not None:
                processor = ImageProcessor(handler.get_image())
                print("Изображение повернуто на 45 градусов и сохранено в rotated.jpg.")
            else:
                print ("Ошибка при повороте изображения.")

        elif choice == "3":
            # Применение фильтра резкости
            if processor.img:
                handler.apply_sharpen()
                print("Фильтр резкости применён.")
            else:
                print("Изображение не загружено.")

        elif choice == "4":
            # Добавление рамки к изображению
             if processor.img:
                handler.apply_border()
                print("Рамка добавлена.")
             else:
                print("Изображение не загружено.")

        elif choice == "5":
            # Сохранение изображения
            save_path = input("Введите путь для сохранения обработанного изображения: ")
            handler.save(save_path)
            print(f"Изображение сохранено по пути {save_path}.")


        elif choice == "7":
            # Выход из программы
            print("Выход из программы.")
            break

        else:
            print("Неверный выбор. Попробуйте снова.")

if __name__ == "__main__":
    main()
