import tkinter as tk
import time
KNOPON = 0 	# Кнопка включения
KNOPOF = 0	# кнопка выключения
REG = 0	 # режим работы
DAT1 = 0	 # Датчик уровня заготовок
#DOST = 1	# Индикатор достаточного уровня заготовок
VDOST = 0
DOST = VDOST# Вводимое значение достаточного уровня заготовок
OTSUT = 0.0	# Индикатор отсутствия заготовок
M1 = float	# Двигатель конвеера
M3 = 0.0	# Двигатель молоточкового механизма
M2R = 0.0	# Двигатель подачи ножа вправо
M2L = 0.0	# Двигатель подачи ножа влево
DAT2 = 0.0	#Датчик наличия заготовки
DAT3R = 0.0	# Правый концевой выключатель
DAT3L = 0.0	# Левый кольцевой выключатель
COUT = 0	# Счетчик заготовок
X = 0	# Координата ножа
PER = 0 # Движение ножа
SRES = 0.0	# Сброс сигнала
ARES = 0.0	# Сброс аварии
cout = 0 # Бред для проверки работы
N = 0 # Расстояние пройденное заготовкой
U = 0 # Угол поворота механизма подачи заготовки
p = 0 # Скорость поворота механизма подачи
k = 0 # Скорость движения заготовки
L = 0 # Вводимая длинна отрезания заготовки
COU = 0 # счетчик бракованных заготовок

#global N
#global U
def KnopOn():
    global KNOPON
    global cout
    global REG
    KNOPON = True
    KNOPOF = False
    cout = cout +1
    btn['text'] = f'Счетчик: {cout}'
    #REG = 2
def KnopOf():
    global KNOPOF
    global cout
    global REG
    KNOPOF = True
    #REG = 1
    KNOPON = False
    cout = cout - 1
    btn['text'] = f'Счетчик: {cout}'
def Dat1():
    global DAT1
    DAT1 += 10
    btn_dost1['text'] = f'Кол-во заготовок в бункере: {DAT1}'
def VDost():
    global VDOST
    VDOST += 2
    btn_min['text'] = f'Минимальное значение заготовок в бункере: {VDOST}'
root = tk.Tk()
root.title('Окно управления')
root.config(bg = 'yellow')
root.wm_attributes('-alpha',1)
root.geometry('500x600+500+50')
root.resizable(False,False)
label_1 = tk.Label(root, text = 'Окно управления', bg = 'yellow', font = ('Arial',14,'bold')).grid()
label_2 = tk.Button(root, text = f'Брак: {COU}', bg = 'green', font = ('Arial',14,'bold')).grid()
btn_dost= tk.Button(root, text = f'Добавить заготовки в бункер ', bg = 'red', command = Dat1 ).grid()
btn_dost1 = tk.Button(root, text = f'Кол-во заготовок в бункере: {DAT1}', bg = 'yellow', font = ('Arial',14,'bold'), command = DAT1 ).grid()
btn_Vdost= tk.Button(root, text = f'Добавить значение для датчика ', bg = 'red', command = VDost ).grid()
btn_min = tk.Button(root, text = f'Достаточное кол-во заготовок: {VDOST}', bg = 'yellow', font = ('Arial',14,'bold')).grid()
btn_start = tk.Button(root, text = 'ВКЛ', bg = 'green', command = KnopOn ).grid()
btn_start_of = tk.Button(root, text = 'ВЫКЛ', bg = 'red', command = KnopOf ).grid()
btn= tk.Button(root, text = f'ВЫКЛ: {cout}', bg = 'red',command = KnopOf ).grid()

#btn_dost.grid()#raw = 0, column = 0)
#btn_Vdost.grid()
#btn_dost1.grid()
#btn_min.grid()
#btn.grid()
#btn_start.grid()
#btn_start_of.grid()
root.mainloop()
while REG == 1 or REG == 2 or REG == 3 or REG == 4 or REG == 5 or REG == 6 or REG == 7 or REG == 8 or REG == 9  or KNOPOF == True or KNOPON == True:
    if KNOPON == True:
        REG = 2
        print('Сработал режим включения')
        if KNOPOF == True:
            REG = 1
            KNOPON = False
            print('Сработал режим выключения')
    if KNOPOF == True:
        REG = 1
        KNOPON = False
        print('Сработал режим выключения')
    if REG == 1:
        M1 = False
        M3 = False
        M2R = False
        M2L = False
        COUT = 1
        DAT1 = 0
        DAT2 = False
        DAT3R = False
        DAT3R = False
        VDOST = 0
        DOST = False
        OTSUT = False
        X = 0
        print('Сработал режим ', REG)
        exit()
    if REG == 2:
        print('Сработал режим ',REG)
        if DAT1 > VDOST and ARES == False: # если значение датчика уровня заготвок больше чем вводимое значение досточного уровня заготовок и нет аварии, то
            DOST = True
            OTSUT = False
            REG = 3
            M1 = True
            #TRIG = False
            print('Сработало включение двигателя М1 в режиме ', REG)
            print('Сработало условие отсутствия аварии в режиме ', REG)
        if DAT1 <= VDOST:  # если значение датчика уровня заготвок больше чем вводимое значение досточного уровня заготовок
            ARES = True
            DOST = False
            OTSUT = True
            print('Сработало условие наличия аварии в режиме ', REG)
            REG = 7
    if REG == 3:
        if M3 == True: #если двигатель молоточковый механизм работает, то
            p = 5
            U+=p
            print('Сработало условие включенного двигателя М3 в режиме ', REG)
            if U == 360: # если угол равен 360, то
                p = 0
                U = 0
                M4 = False
                print('Сработало условие угла на 360 градусов в режиме ', REG)
        print('Сработал режим ', REG)
        REG = 4
    if REG == 4:
        if DAT2 == True: # если датчик наличия заготовки сработал , то
            print('Сработало условие включенного датчика наличия заготовок в режиме  ', REG)
            if M1 == True: # если двигатель конвейера работает, то
                k = 1
                N +=k
                print('Сработало условие включенного двигателя М1 в режиме ', REG)
            if N ==L: #если расстояние пройденное заготовкой и водимая длина отрезания заготовки совпадают, то
                k = 0
                M1 = False
                PER = math.exp(-1,COUT)
                print('Сработало условие совпадения расстояний заготовки и длинны отрезания заготовки в режиме ', REG)
                REG = 5
        print('Сработал режим ', REG)
        if DAT2 == False and N<=0 or N>0: #если заготовка полностью прошла, то
            COU += 1
            k = 0
            N = 0
            M3 = True
            print('Сработало включение двигателя М3 в режиме ', REG)
            print('Сработало условие полностью пройденной заготовки в режиме ', REG)
            print('Счетчик бракованных заготовок:',COU)
            DAT1 -=1
            print('Остаток заготовок в бункере:',DAT1)
    if REG ==5:
        if PER ==1: #если направление движение ножа должно быть вправо, то
            DAT3L = True
            DAT3R = False
            REG = 6
            print('Сработало условие движения ножа вправо в режиме  ', REG)
        if PER == -1: #если направление движение ножа должно быть влево, то
            DAT3L=False
            DAT3R =True
            REG =6
            print('Сработало условие движения ножа влево в режиме ', REG)
        print('Сработал режим ', REG)
    if REG ==6:
        if DAT3L == True: # если левый концевой датчик зажат,то
            M2R = True
            DAT3L = False
            X +=1
            print('Сработало условие нажатие левого датчика в режиме ', REG)
            if X == 100: #если нож достигает крайнего правого положения, то
                DAT3R == True
                M2R = False
                COUT +=1
                REG = 4
                N =0
                print('Счетчик заготовок:', COUT)
                print('Сработало условие достижения крайнего правого положения ножа в режиме ', REG)
        print('Сработал режим ', REG)
        if DAT3R == True: # если правый концевой датчик зажат, то
            X -= 1
            print('Сработало условие зажатия правого датчика в режиме  ', REG)
            if X <99: # если нож начал двигаться влево, то
                M2L = True
                DAT3R = False
                print('Сработало условие движения ножа влево в режиме ', REG)
            if X == 0: # если нож достиг крайнего левого положения , то
                M2L = False
                DAT3L = True
                COUT += 1
                REG =4
                N =0
                print('Сработало условие если нож достиг крайнего левого положения в режиме ', REG)
    if REG == 7 or REG == 8: # если датчик обнаружил разницу длин отделяемых частей,то
        X -= 1
        print('Сработало условие если датчик обнаружил разницу длин отделяемых частей в режиме', REG)
        if X < 99: # если датчик не обнаружил разницу, то
            M2L = True
            DAT3R = False
            print('Сработало условие отсутствие обнаружения разницы длинны в режиме ', REG)
        DAT3L = True
        COUT +=1
        REG =9
        N =0
        print('Сработал режим ',REG)
    if REG == 9:
        M1 = False
        M3 = False
        print('Сработал режим ', REG)
