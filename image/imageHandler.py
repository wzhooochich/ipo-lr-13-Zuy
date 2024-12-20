from PIL import Image
from image.imageProcessor import ImageProcessor

class ImageHandler:
    def __init__(self, image_path):
        try:
            self.image = Image.open(image_path)
        except FileNotFoundError:
            print(f"Error: File not found at path: {image_path}")
            self.image = None
        except Exception as e:
            print(f"Error opening image: {e}")
            self.image = None

    def save(self, output_path, format="JPEG"):
        if self.image:
            self.image.save(output_path, format)
        else:
            print("No image to save.")

    def rotate(self, angle=45, save_path="rotated.jpg"):
        """
        Повернуть изображение на указанный угол.
        """
        if self.image:
            self.image = self.image.rotate(angle, expand=True)
            self.save(save_path)
            return self.image
        else:
            print("Изображение не загружено!")
            return None
    
    def apply_sharpen(self):
        processor = ImageProcessor(self.image)
        self.image = processor.sharpen()
        return self.image
    
    def apply_border(self, border_width=15, border_color="black"):
        processor = ImageProcessor(self.image)
        self.image = processor.border(border_width, border_color)
        return self.image
    
    def get_image(self):
      return self.image