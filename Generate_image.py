import random
from PIL import Image, ImageDraw
import os
from random import randint
import pandas as pd
import numpy as np # Импортируем необходимые библиотеки

if not os.path.isdir("dataset"): #Создаем основной репозиторий
    os.mkdir("dataset")
os.chdir("dataset") # Указываем используемый репозиторий
n_step = 5 # Количество изображений в папке
sizeR = 0.5 #Размер точек
sizeG = 1.5
delta = 5 # Шаг изменения
pack = 4 # Количество папок с изображениями
red_min = 100 # Минимальное количество эритроцитов на изображении
red_max = 500 # Максимальное количество эритроцитов на изображении
gray_min = 5 # Минимальное количество лимфоцитов на изображении
gray_max = 25 # Максимальное количество лимфоцитов на изображении
pix_x = 112 # Размер изображения в пикселях
pix_y = 112
color_f = 'white' # Цвет фона изображения
format_image = '.png' # Формат сохраняемого изображения
name_image = 'broun' # Имя изображения
name_files = "traffic" #Имя папки
color_ery = 'red' # Цвет эритроцитов
color_limf = 'grey' # Цвет лимфоцитов
address = "C:\\GOG Games\\PyCharm\\pythonProject1\\dataset" # Расположение репозитория
ran_coord_rx = [] #Создание используемых массивов
ran_coord_ry = []
ran_coord_gx = []
ran_coord_gy = []
Wxr = []
Wyr = []
Wxg = []
Wyg = []
filles = []
erythrocytes = []
lymphocytes = []

for h in range(1, pack): # Цикл для создания папок в основном репозитории
    hh = str(h)
    if not os.path.isdir(name_files+hh): #Создание папки
        os.mkdir(name_files+hh)
    os.chdir(name_files+hh) # Название папки
    rep = name_files+hh
    print(os.getcwd()) # Проверка репозитория
    ran_red = randint(red_min, red_max) #Количество точек в одной папке
    ran_gray = randint(gray_min, gray_max)
    filles.append(rep)
    erythrocytes.append(ran_red)
    lymphocytes.append(ran_gray)
    for i in range(0,n_step):

        img = Image.new('RGBA', (pix_x, pix_y), color_f) # Создание изображение
        idraw = ImageDraw.Draw(img) #Создание объекта изображения
        Wxr.clear() #Обнуление списков
        Wyr.clear()
        Wxg.clear()
        Wyg.clear()
        for m in range(0, ran_red): #Цикл для отображения эретроцитов
            if i == 0:
                ran_coord_rx.append(float(random.uniform(0, pix_x))) #Генирация начального положения точки на изображении
                ran_coord_ry.append(float(random.uniform(0, pix_y)))
        print('ran_coord_rx', ran_coord_rx)
        for a in range(0, ran_red):
            ran_coord_rx.append(float(random.uniform((ran_coord_rx[0] - delta), (ran_coord_rx[0] + delta)))) #Определение следующей координаты
            ran_coord_ry.append(float(random.uniform((ran_coord_ry[0] - delta), (ran_coord_ry[0] + delta))))
            ran_coord_rx.remove(ran_coord_rx[0])
            ran_coord_ry.remove(ran_coord_ry[0])
            yi = np.random.choice([1, -1])
            Wxr.append(np.ones(n_step) * ran_coord_rx[0])
            Wyr.append(np.ones(n_step) * ran_coord_ry[0])
            Wxr[0] = Wxr[a-1] + (yi / np.sqrt(n_step)) #Уравнение броуновского движения
            Wyr[0] = Wyr[a - 1] + (yi / np.sqrt(n_step))
            wxr1 = Wxr[0]
            wxr = wxr1[0]
            wyr1 = Wyr[0]
            wyr = wyr1[0]
            xr1 = wxr - sizeR
            yr1 = wyr - sizeR
            xr2 = wxr + sizeR
            yr2 = wyr + sizeR
            idraw.ellipse((xr1, yr1, xr2, yr2), color_ery) # Отображение точки
            istr = str(i)
            img.save(name_image + istr + format_image) #Сохраннение объекта
        for z in range(0, ran_gray):
            if i == 0:
                ran_coord_gx.append(float(randint(0, pix_x)))
                ran_coord_gy.append(float(randint(0, pix_y)))
        print('ran_coord_gx',ran_coord_gx)
        for p in range(0, ran_gray):
            ran_coord_gx.append(float(random.uniform((ran_coord_gx[0] - delta), (ran_coord_gx[0] + delta))))
            ran_coord_gy.append(float(random.uniform((ran_coord_gy[0] - delta), (ran_coord_gy[0] + delta))))
            ran_coord_gx.remove(ran_coord_gx[0])
            ran_coord_gy.remove(ran_coord_gy[0])
            yi = np.random.choice([1, -1])
            Wxg.append(np.ones(n_step) * ran_coord_gx[p])
            Wyg.append(np.ones(n_step) * ran_coord_gy[p])
            Wxg[0] = Wxg[p - 1] + (yi / np.sqrt(n_step))
            Wyg[0] = Wyg[p - 1] + (yi / np.sqrt(n_step))
            wxg1 = Wxg[0]
            wxg = wxg1[0]
            wyg1 = Wyg[0]
            wyg = wyg1[0]
            xg1 = wxg - sizeG
            yg1 = wyg - sizeG
            xg2 = wxg + sizeG
            yg2 = wyg + sizeG
            idraw.ellipse((xg1, yg1, xg2, yg2), color_limf)
            istr = str(i)
            img.save(name_image + istr + format_image)
    os.chdir(address) # Возвращение к исходному репозиторию
data = {'filles', 'erythrocytes', 'lymphocytes'}
frame = pd.DataFrame( {'filles' : filles, 'erythrocytes' : erythrocytes, 'lymphocytes' : lymphocytes})
print(frame)
frame.to_pickle("./DataFrame.csv")

