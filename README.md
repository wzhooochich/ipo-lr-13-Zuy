- Создать два связанных класса:
    - **ImageHandler** — класс для базовой работы с изображениями (загрузка, сохранение, изменение размеров и форматов).
    - **ImageProcessor** — класс для обработки изображения (применение фильтров, добавление текста, поворот).
- Класс **ImageHandler** должен:
    - Принимать путь к изображению при инициализации.
    - Содержать методы для загрузки изображения, сохранения и изменения его размера.
    - Обеспечивать передачу изображения в класс **ImageProcessor**.
- Класс **ImageProcessor** должен:
    - Принимать изображение, переданное из **ImageHandler**.
    - Содержать методы для применения различных фильтров, добавления текста и других эффектов.
 
      1. В классе **ImageHandler**:
    - Реализовать метод для изменения формата изображения на JPG.
    - Реализовать метод для поворота изображения на 45 градусов.
2. В классе **ImageProcessor**:
    - Применить фильтр повышения резкости (SHARPEN).
    - Добавить рамку вокруг изображения с шириной 15 пикселей.
