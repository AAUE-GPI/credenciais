from PIL import Image as img
im = img.open("image.jpg")
im.rotate(45).show()