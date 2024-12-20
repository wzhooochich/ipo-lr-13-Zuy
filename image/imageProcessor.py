from PIL import ImageFilter, Image, ImageOps

class ImageProcessor:
    def __init__(self, img):
        self.img = img

    def sharpen(self):
        """
        Применить фильтр резкости к изображению.
        """
        if self.img:
            if self.img.mode not in ("RGB", "RGBA"):
                self.img = self.img.convert("RGB")
            self.img = self.img.filter(ImageFilter.SHARPEN)
        else:
            print("Изображение не загружено!")
        return self.img # Возвращаем измененное изображение
    
    def border(self, border_width=15, border_color="black"):
         """
         Добавить рамку вокруг изображения.
         """
         if self.img:
              self.img = ImageOps.expand(self.img, border=border_width, fill=border_color)
         else:
              print("Изображение не загружено!")
         return self.img # Возвращаем измененное изображение

    def save_image(self, save_path):
        """
        Сохранить обработанное изображение.
        """
        if self.img:
            self.img.save(save_path)
        else:
            print("Изображение не загружено!")