import numpy as np
import math
import matplotlib.pyplot as plt
for i in range(1,4):
    i = str(i)
    l = 'boks' + i
    j = '.txt'
    o = l+j
    #o = 'boks1.txt'
    file = open(o, 'r') #  Открываем файл в режиме чтения
    a = 0 # переменная для цикла
    c = 0 # переменная для определения 1 столбца списка
    h = 1 # Переменная для определения 2 столбца списка
    k = 2 # Переменная для определения 3 столбца списка
    sp = [] # Список для внесения данных из файла
    sp_st1 = [] # Список для значений 1 столбца
    sp_st2 = [] # Для значений 2 столбца
    sp_st3 = [] # Для значений 3 столбца
    cout = 0 # Переменная для определения количества строк в файле
    line = file.readline().split()
    while line:
        sp.extend(line)
        line = file.readline().split()
        cout = cout +1
    #print(sp) # Открыть если необходимо просмотреть список из файла txt
    #print(cout) # Открыть, если необходимо посмотреть кол-во строк
    for a in range(a, cout*2, 2):
        st1 = float(sp[c])
        st2 = int(sp[h])
        st3 = int(sp[k])
        #print(st1, st2) # открыть если необходимо посмотреть столбцы файла
        sp_st1.append(st1)
        sp_st2.append(st2)
        sp_st3.append(st3)
        c = c + 3
        h = h + 3
        k = k + 3
    a = 0
    print('   Время', '  Расстояние', 'Прерывание')
    for a in range(cout):
        print(sp_st1[a],sp_st2[a], sp_st3[a])  # Цикл для вывода значений из файла
        a +=1
    # Начинаем расчет трения
    sp_st1 = np.array([sp_st1,sp_st2])
    #sp_st2 = np.array(sp_st2)
    v = np.gradient(sp_st1[0],sp_st1[1]) # Найдем скорость в каждый момент времени
    print('Скорость: ',v)
    A = np.gradient(v,sp_st1[0]) # Найдем ускорение в каждый момент времени
    print('Ускорение: ',A)
    u = 22.0*3.14/180 # Угол наклона поверхности (рад)
    g = 9.8 # Ускорение свободного падения
    m = 0.1 # кг
    DgS = math.cos(u) # Находим косинус угла наклона поверхности
    print(DgS)
    KtsS  = A/g * DgS
    print('Еще один коэффициент трения ',KtsS)
    N = m * g * DgS # Сила реакции опоры
    Norm_sqrt = math.sqrt(N) # Корень из реакции для вычисления через формулу ВНИИЖТа
    KtS = 17/(Norm_sqrt*(v+40)) # Формула ВНИИЖТа
    #print('Трение скольжения: ',KtS,'Н.')
    print('Коэффициент трения скольжения',KtS)
    Fts_Max = max(KtS)*m*g*DgS
    KtSss = KtsS/N
    print('Максимальная сила трения: ',Fts_Max)
    #Ktp = m*g*sin(u)/m*g*cos(u) # Формула коэф.т.покоя
    # Сила трения -  масса на ускорение
    Ftr = m*A - N - m*g
    #print('Сила трения: ',Ftr,'Н.')
    Ktp = math.tan(u) # Коэффициент трения покоя
    print('Коэффициент трения покоя: ',Ktp,'Н.')
    tp = m*g*Ktp*DgS  # Трение покоя
    print('Трение покоя: ',tp,'Н.')
    plt.title('График коэффициента трения скольжения')
    plt.plot(KtS)
    plt.plot(tp)
    plt.show()
