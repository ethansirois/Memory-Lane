from PIL import Image

image = Image.open('graphics/images/108.jpg')
image = image.resize((int(image.size[0] * 650 / image.size[1]), 650))
image.save('graphics/images/108.png')
