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
               img = self.img.convert("RGB") 
            else:
               img = self.img
            return img.filter(ImageFilter.SHARPEN)
        else:
            print("Изображение не загружено!")
            return self.img
    
    def border(self, border_width=15, border_color="black"):
         """
         Добавить рамку вокруг изображения.
         """
         if self.img:
             return ImageOps.expand(self.img, border=border_width, fill=border_color)
         else:
              print("Изображение не загружено!")
              return self.img
