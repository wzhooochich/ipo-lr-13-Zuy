from PIL import ImageFilter, Image, ImageOps

class ImageProcessor:
    def __init__(self, image):
        self.image = image

    def apply_sharpen_filter(self):
        """
        Применить фильтр резкости к изображению.
        """
        if self.image:
             if self.image.mode not in ("RGB", "RGBA"):
                img = self.image.convert("RGB")
             else:
                img = self.image
             self.image = img.filter(ImageFilter.SHARPEN)
        else:
            print("Изображение не загружено!")
    
    def add_border(self):
        """
        Добавить рамку вокруг изображения.
        """
        if self.image:
            self.image = ImageOps.expand(self.image, border=15, fill="black")
        else:
            print("Изображение не загружено!")
    
    def get_image(self):
        """
        Получить текущее изображение.
        """
        if self.image:
            return self.image
        else:
            print("Изображение не загружено!")
            return None
