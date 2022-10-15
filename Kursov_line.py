# Еще одна попытка написать курсач
import time
import threading
import tkinter as tk
import time
import tkinter as tk
import datetime
import TOwen
import MySerial
M1 = 0 # Двигатель М1
M2 = 0 # Двигатель М2
M4 = 0 # Двигатель М4
cout = 0 # Счетчик готовых изделий
ares = 0 # Кнопка выключения аварии
sound = 0 # Кнопка звукового сигнала
Of = 0 # Кнопка выключения
On = 0 # Кнопка включения
dost = 0
dat_otsut = 0 # Датчик отсутствия заготовок в бункере
dat_zag = 0 # Датчик наличия захотовки
data =  datetime.datetime.today() #+ datetime.timedelta(days=21)

#owenDev=Owen.Owen(None,16)
#owenDev=TOwen(0)
COM12 = MySerial.ComPort(port = 0,) #открываем COM12 (нумерация портов начинается с 0)
COM12.LoggingIsOn= M1
COM12 = MySerial.ComPort(port = 0) #открываем COM12 (нумерация портов начинается с 0)
COM12.LoggingIsOn= M1
def Dat_zazg_on():
    global dat_zag
    dat_zag = True
    print('Сработал датчик заготовки')

def Dost():
    global dost
    dost += 5
    btn_dost_1['text'] = f'Кол-во заготовок в бункере: {dost}'
    btn_dost_1['bg'] = 'green'
def OF():
    global Of
    global On
    global M1
    global M2
    global M4
    Of = True
    On = False
    btn_On['bg'] = 'red'
    M1 = False
    M2 = False
    M4 = False
    btn_M2['bg'] = 'red'
    btn_M1['bg'] = 'red'
    btn_M4['bg'] = 'red'
def Ares_of():
    global ares
    global M1
    global M2
    global M4
    ares = False
    btn_ares['text'] = f'Режим аварии ВЫКЛ'
    btn_ares['bg'] = 'green'
    M1 = False
    M2 = False
    M4 = False
    btn_M2['bg'] = 'red'
    btn_M1['bg'] = 'red'
    btn_M4['bg'] = 'red'
def Ares_on():
    global ares
    ares = True
    btn_ares['text'] = f'Режим аварии ВКЛ'
    btn_ares['bg'] = 'red'
def Cout_razn():
    global  dost
    dost-=1
    btn_dost_1['text'] = f'Кол-во заготовок в бункере: {dost}'
def Mus():
    pygame.mixer.music.stop()
def ON():
    global On
    On = True
    btn_On['bg'] = 'green'
    dat_otsut = 0
    
    while On == True:
        global dat_zag
        global dost
        global cout
        global M1
        global M2
        global M4
        global Ares_on
        global playsound
        global ares
        #print('Ошибка, система находится в режиме аварии')
        if ares == True:
            Ares_on()
            print('Ошибка, система находится в режиме аварии')
        elif ares == False:
            if dost > dat_otsut:
                if dat_zag == False:
                    print('Конвеерная лента запущена')
                M1 = True
                #return M1
                btn_M1['bg'] = 'green'
                if dat_zag == False:
                    print('Конвеерная лента в рабочем режиме')
                time.sleep(0.5)
                M4 = True
                #return M4
                btn_M4['bg'] = 'red'
                if dat_zag == False:
                    btn_M4['bg'] = 'green'
                    print('Заготовка спущена на конвеер')
                    time.sleep(0.5)
                    btn_M4['bg'] = 'red'
                #Dat_zag_()
                if dat_zag == True:
                    M2 = True
                    #return M2
                    dost -= 1
                    btn_M2['bg'] = 'green' 
                    cout += 2
                    btn_dost_1['text'] = f'Кол-во заготовок в бункере: {dost}'
                    M2 = False
                    #return M2
                    #btn_M2['bg'] = 'red'
                    time.sleep(1)
                    btn_M2['bg'] = 'red'
                    time.sleep(1.5)
                    print('Заготовка разделена на части')
                    print('Заготовок в бункере: ', dost)
                    print('Готовых изделий: ', cout)
                    btn_cout['text'] = f'Готовых изделий: {cout}'
                    On == True
                    dat_zag = False

                    if dost <= dat_otsut:
                        global btn_ares
                        #global ares
                        ares = True
                        print('В бункере закончились заготовки')
                        print('Срабатывает звуковой сигнал')
                        print('Отключение двигателя M4')
                        btn_ares['text'] = f'Авария ВКЛ'
                        #playsound('Ares.mp3')
                        btn_ares['bg'] = 'red'
                        time.sleep(0.5)
                        M4 = False
                        #return M4
                        btn_M4['bg'] = 'red'
                        time.sleep(0.5)
                        M2 = False
                        #return M2
                        btn_M2['bg'] = 'red'
                        time.sleep(0.5)
                        M1 = False
                        #return M1
                        btn_M1['bg'] = 'red'
                       # a = int(input('Если желаете добавить заготовки в бункер, нажмите 1, в противном случае 0'))
                        if a == 1:
                            dost = int(input('Введите количество заготовок в бункер:'))  # Добавление заготовок в бункер
                            On = True
                            M4 = True
                            #return M4
                        else:
                            print('Работа конвеерной ленты звершена')
                            exit()
                    else:
                        time.sleep(3)
                else:
                    while dat_zag== False:
                        a = 1
                        time.sleep(0.5)
                        #print(a)
root = tk.Tk()

root.title('Окно управления')
root.config(bg = 'yellow')
root.wm_attributes('-alpha',1)
root.geometry('700x800+500+50')
root.resizable(False,False)
label_data = tk.Label(root, text = f'{data}', bg = 'yellow',font = ('Arial',14,'bold'))
btn_dost= tk.Button(root, text = f'Добавить заготовки в бункер ', bg = 'red',font = ('Arial',14,'bold'), command = Dost )
btn_dost_1= tk.Button(root, text = f'Заготовок в бункере: {dost}', bg = 'red', font = ('Arial',14,'bold'))
btn_On= tk.Button(root, text = f'ВКЛ ', bg = 'red',font = ('Arial',14,'bold'), command = lambda: threading.Thread(target = ON, daemon = True).start() )
btn_Of= tk.Button(root, text = f'ВЫКЛ ', bg = 'red',font = ('Arial',14,'bold'), command = lambda: threading.Thread(target = OF, daemon = True).start() )
btn_ares= tk.Button(root, text = f'Режим аварии ВЫКЛ ', bg = 'green',font = ('Arial',14,'bold'), command = Ares_of )
btn_M1= tk.Button(root, text = f'M1 ', bg = 'red',font = ('Arial',14,'bold'))
btn_M2= tk.Button(root, text = f'M2 ', bg = 'red',font = ('Arial',14,'bold'))
btn_M4= tk.Button(root, text = f'M4 ', bg = 'red',font = ('Arial',14,'bold'))
btn_cout= tk.Button(root, text = f'Готовых изделий: {cout} ', bg = 'blue',font = ('Arial',14,'bold'))
btn_mus= tk.Button(root, text = f'Звук выкл ', bg = 'blue',font = ('Arial',14,'bold'), command = Mus)
btn_dat_zag= tk.Button(root, text = f'Датчик заготовки ', bg = 'blue',font = ('Arial',14,'bold'), command = Dat_zazg_on)
label_data. grid(row = 0, column = 0)
btn_dost.grid(row = 1, column = 0)
btn_dost_1.grid(row = 1, column = 1)
btn_On.grid(row = 2, column = 0)
btn_Of.grid(row = 2, column = 1)
btn_ares.grid(row = 3, column = 1)
btn_M1.grid(row = 4, column = 0)
btn_M2.grid(row = 4, column = 1)
btn_M4.grid(row = 4, column = 2)
btn_cout.grid(row = 5, column = 0)
btn_mus.grid(row = 5, column = 1)
btn_dat_zag.grid(row = 6, column = 1)

root.mainloop()
