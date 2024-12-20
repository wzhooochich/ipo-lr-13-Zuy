from image import ImageHandler
from image import ImageProcessor
import os

def main_menu():
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
    images_dir = "images"
    if not os.path.exists(images_dir):
        os.makedirs(images_dir)

    initial_image_path = "input.jpg" 
    handler = ImageHandler(initial_image_path)
    if handler.image is None:
        print("Ошибка: Не удалось загрузить изображение.")
        return
    print("Изображение успешно загружено из пути:", initial_image_path)
    processor = ImageProcessor(handler.image)

    while True:
        choice = main_menu() 

        if choice == "1":
            # Конвертация изображения в формат PNG
            save_path = input("Введите имя файла для сохранения (с расширением .png): ")
            save_path = f"images/{save_path}"
            handler.save(save_path, format="PNG")
            print(f"Изображение сохранено в формате PNG по пути {save_path}.")


        elif choice == "2":
            # Поворот изображения на 45 градусов
            rotated_image = handler.rotate(45)
            if rotated_image is not None:
                handler.image = rotated_image
                processor = ImageProcessor(handler.image)
                print("Изображение повернуто на 45 градусов")
            else:
                print ("Ошибка при повороте изображения.")

        elif choice == "3":
            # Применение фильтра резкости
            if handler.image:
                handler.apply_sharpen()
                processor = ImageProcessor(handler.image)
                print("Фильтр резкости применён.")
            else:
                print("Изображение не загружено.")

        elif choice == "4":
            # Добавление рамки к изображению
             if handler.image:
                handler.apply_border()
                processor = ImageProcessor(handler.image)
                print("Рамка добавлена.")
             else:
                print("Изображение не загружено.")

        elif choice == "5":
            # Сохранение изображения
            save_path = input("Введите имя файла для сохранения (например, output.png): ")
            save_path = f"images/{save_path}"
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
