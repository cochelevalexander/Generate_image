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
ran_coord_rx = [] #Создание нужных массивов
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
delta = 5
for h in range(1, 4): # Цикл для создания папок в основном репозитории
    hh = str(h)
    if not os.path.isdir("traffic"+hh): #Создание папки
        os.mkdir("traffic"+hh)
    os.chdir("traffic"+hh)
    rep = "traffic"+hh
    print(os.getcwd())
    sizeR = 0.5 #Размер точек
    sizeG = 1.5
    ran_red = randint(100, 500) #Количество точек в одной папке
    ran_gray = randint(5, 25)

    filles.append(rep)
    erythrocytes.append(ran_red)
    lymphocytes.append(ran_gray)
    for i in range(0,n_step):

        img = Image.new('RGBA', (112, 112), 'white') # Создание изображение
        idraw = ImageDraw.Draw(img) #Создание объекта изображения
        Wxr.clear() #Обнуление списков
        Wyr.clear()
        Wxg.clear()
        Wyg.clear()
        for m in range(0, ran_red): #Цикл для отображения эретроцитов
            if i == 0:
                ran_coord_rx.append(float(random.uniform(0, 112))) #Генирация начального положения точки на изображении
                ran_coord_ry.append(float(random.uniform(0, 112)))
        print('jjjj', ran_coord_rx)
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
            idraw.ellipse((xr1, yr1, xr2, yr2), 'red') # Отображение точки
            istr = str(i)
            img.save('broun' + istr + '.png') #Сохраннение объекта
        for z in range(0, ran_gray):
            if i == 0:
                ran_coord_gx.append(float(randint(0, 112)))
                ran_coord_gy.append(float(randint(0, 112)))
        print('Rand_xg',ran_coord_gx)
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
            idraw.ellipse((xg1, yg1, xg2, yg2), 'grey')
            istr = str(i)
            img.save('broun' + istr + '.png')
    os.chdir("C:\\GOG Games\\PyCharm\\pythonProject1\\dataset") # Возвращение к исходному репозиторию
data = {'filles', 'erythrocytes', 'lymphocytes'}
frame = pd.DataFrame( {'filles' : filles, 'erythrocytes' : erythrocytes, 'lymphocytes' : lymphocytes})
print(frame)
frame.to_pickle("./DataFrame.csv")

