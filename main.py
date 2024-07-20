from PIL import Image, ImageDraw, ImageFont

tt = input('Генератор мемов запущен!\nВведите верхний текст: ')
bt = input('Введите нижний текст: ')

print("Список картинок:")
print("1. Кот в ресторане")
print("2. Кот в очках")
inm = int(input('Введите номер нужной картинки: '))

if inm == 1:
    image = "Кот в ресторане.png"
elif inm == 2:
    image = 'Кот в очках.png'

imagef = Image.open(image)
dr = ImageDraw.Draw(imagef)
font = ImageFont.truetype('arial.ttf', size=140)

dr.text((400,40), tt, font=font, fill="black")
dr.text((400,1100), bt, font=font, fill="black")
imagef.save('New_Meme.jpg')