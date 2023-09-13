from PIL import Image, ImageOps
import os


def resize_photos(folder):
    os.chdir(folder)
    if not os.path.exists('../resized_photos'):
        os.mkdir('../resized_photos')
        for f in os.listdir(os.getcwd()):
            os.chdir(folder)
            if os.path.isdir(f):
                os.chdir(f)
                os.mkdir('../../resized_photos/' + f)
                for img in os.listdir(os.getcwd()):
                    try:
                        image = Image.open(img)
                        image = ImageOps.exif_transpose(image)
                        image = image.resize((int(image.size[0] * 650 / image.size[1]), 650))
                        image.save('../../resized_photos/' + '/' + f + '/' + img)
                    except IOError:
                        print("error with file: " + img)

            else:
                try:
                    image = Image.open(folder + '/' + f)
                    image = ImageOps.exif_transpose(image)
                    image = image.resize((int(image.size[0] * 650 / image.size[1]), 650))
                    image.save('../resized_photos/' + f)
                except IOError:
                    print("error with file: " + f)

    os.chdir(folder)
    os.chdir('../resized_photos')
    return os.getcwd()

