from PIL import Image

first_image = Image.open("YourPath/benefit.png")
second_image = Image.open("YourPath/106044_benefit.jpg")
first_image.paste(second_image, (0, 200))
first_image.show()
