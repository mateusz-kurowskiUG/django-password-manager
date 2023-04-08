from PIL import Image
from PIL import ImageOps
import watchdog

def img_to_gray(img):
    og_image = Image.open(img)    
    gray_image = ImageOps.grayscale(og_image)
    im = gray_image.convert("RGB")
    gray_image.save(f"D:\studia\sem2\Pytong\own\image2.pdf")

img_to_gray("D:\studia\sem2\Pytong\own\wzory_1.png")
