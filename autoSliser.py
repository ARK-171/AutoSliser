import os, sys
from PIL import Image

print("путь к файлу")
put = input()
print("имя файла")
y = input()
name = put+y
im = Image.open(name)

print("ширина спрайта")
width = int(input())
print("высота спрайта")
heigh = int(input())
print("номер строки")
number = int(input())
print("длина строки в спрайтах")
length = int(input())

i=1

print("путь сохранения")
save_put = input()

while i < length+1:
    img = im.crop((width*(i-1), heigh*(number-1), width*i, heigh*number))
    save = save_put + str(i) + ".png"
    img.save(save)
    i += 1
