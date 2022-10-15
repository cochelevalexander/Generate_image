# Расчет Просековского курсача
# Определение матриц звена
import math
# from sympy import diff, symbol, cos, sin
import sympy as sym
import numpy as np

def dimens():
    global l1
    global l2
    global l3
    l1 = float(input('Введите длинну', 1, '-го звена'))
    l2 = float(input('Введите длинну', 2, '-го звена'))
    l3 = float(input('Введите длинну', 3, '-го звена'))

zven2 = 0
zven3 = 0
os2 = 0
os3 = 0
# Объявление переменных для символьных вычислений
l1 = sym.Symbol('l1')
l2 = sym.Symbol('l2')
l3 = sym.Symbol('l3')
l1_1 = sym.Symbol('l1_1')
l2_1 = sym.Symbol('l2_1')
l3_1 = sym.Symbol('l3_1')
a = sym.Symbol('a')
#cos = sym.Symbol('cos')
#sin = sym.Symbol('sin')
for i in range(1, 4):

    print('Какое движение у', i, '-го звена? \n 1 - вращающееся \n 2 - поступательное')
    globals()['zven' + str(i)] = int(input())
    print('На какой оси происходит движение ', i, '-го элемента? \n 1 - ось Ох \n 2 - ось Оу \n 3 - ось Оz')
    globals()['os' + str(i)] = int(input())
    print('Звено ',i,' находится на одной оси? \n 1 - Да \n 2 - Нет')
    dop = int(input())
    #if dop == 2:
    #    print('Какая дополнительная ось у ', i, '-го звена? \n 1 - ось Ох \n 2 - ось Оу \n 3 - ось Оz')
    #    globals()['s' + str(i)] = int(input())

    if zven3 == 1 or zven2 ==  1 or zven1 == 1:
        A = int(input('Введите угол вращения\n'))
        A_rad = a * math.pi / 180
        A = A_rad

        if os3 or os2 or os1 == 1:
            globals()['Ma' + str(i)] =np.array( [[1,     0,             0,          0],
                                                 [0, sym.cos(a), (sym.sin(a))*(-1), 0],
                                                 [0, sym.sin(a),    sym.cos(a),     0],
                                                 [0,     0,             0,          1]])
            if dop == 2:
                print('Какая дополнительная ось у ', i, '-го звена? \n 1 - ось Ох \n 2 - ось Оу \n 3 - ось Оz')
                s1 = int(input())
                if s1 == 1:
                    ['Ma' + str(i)][0][3] = l1_1
                elif s1 == 2:
                    ['Ma' + str(i)][1][3] = l1_1
                elif s1 == 3:
                    ['Ma' + str(i)][2][3] = l1_1
                elif s2 == 1:
                    ['Ma' + str(i)][0][3] = l1_2
                elif s2 == 2:
                    ['Ma' + str(i)][1][3] = l1_2
                elif s2 == 3:
                    ['Ma' + str(i)][2][3] = l1_2
                elif s3 == 1:
                    ['Ma' + str(i)][0][3] = l1_3
                elif s3 == 2:
                    ['Ma' + str(i)][1][3] = l1_3
                elif s3 == 3:
                    ['Ma' + str(i)][2][3] = l1_3
        elif os3 == 2:
            globals()['Ma' + str(i)] =np.array( [[sym.cos(a), 0, sym.sin(a), 0],
                                                 [0,          1,     0,      0],
                                                 [sym.sin(a), 0, sym.cos(a), 0],
                                                 [0,          0,     0,      1]])
            if dop == 2:
                print('Какая дополнительная ось у ', i, '-го звена? \n 1 - ось Ох \n 2 - ось Оу \n 3 - ось Оz')
                s1 = int(input())
                if s1 == 1:
                    ['Ma' + str(i)][0][3] = l1_1
                elif s1 == 2:
                    ['Ma' + str(i)][1][3] = l1_1
                elif s1 == 3:
                    ['Ma' + str(i)][2][3] = l1_1
                elif s2 == 1:
                    ['Ma' + str(i)][0][3] = l1_2
                elif s2 == 2:
                    ['Ma' + str(i)][1][3] = l1_2
                elif s2 == 3:
                    ['Ma' + str(i)][2][3] = l1_2
                elif s3 == 1:
                    ['Ma' + str(i)][0][3] = l1_3
                elif s3 == 2:
                    ['Ma' + str(i)][1][3] = l1_3
                elif s3 == 3:
                    ['Ma' + str(i)][2][3] = l1_3
        elif os3 == 3:
            globals()['Ma' + str(i)] =np.array( [[sym.cos(a), (sym.sin(a))*(-1), 0, 0],
                                                 [sym.sin(a),    sym.cos(a),     0, 0],
                                                 [0,                 0,          1, 0],
                                                 [0,                 0,          0, 1]])
            if dop == 2:
                print('Какая дополнительная ось у ', i, '-го звена? \n 1 - ось Ох \n 2 - ось Оу \n 3 - ось Оz')
                s1 = int(input())
                if s1 == 1:
                    ['Ma' + str(i)][0][3] = l1_1
                elif s1 == 2:
                    ['Ma' + str(i)][1][3] = l1_1
                elif s1 == 3:
                    ['Ma' + str(i)][2][3] = l1_1
                elif s2 == 1:
                    ['Ma' + str(i)][0][3] = l1_2
                elif s2 == 2:
                    ['Ma' + str(i)][1][3] = l1_2
                elif s2 == 3:
                    ['Ma' + str(i)][2][3] = l1_2
                elif s3 == 1:
                    ['Ma' + str(i)][0][3] = l1_3
                elif s3 == 2:
                    ['Ma' + str(i)][1][3] = l1_3
                elif s3 == 3:
                    ['Ma' + str(i)][2][3] = l1_3
    elif zven3 == 2:
        if os3 == 1:
            globals()['Ma' + str(i)] =np.array( [[1, 0, 0, l3],
                                                 [0, 1, 0, 0],
                                                 [0, 0, 1, 0],
                                                 [0, 0, 0, 1]])
            if dop == 2:
                print('Какая дополнительная ось у ', i, '-го звена? \n 1 - ось Ох \n 2 - ось Оу \n 3 - ось Оz')
                s1 = int(input())
                if s1 == 1:
                    ['Ma' + str(i)][0][3] = l1_1
                elif s1 == 2:
                    ['Ma' + str(i)][1][3] = l1_1
                elif s1 == 3:
                    ['Ma' + str(i)][2][3] = l1_1
                elif s2 == 1:
                    ['Ma' + str(i)][0][3] = l1_2
                elif s2 == 2:
                    ['Ma' + str(i)][1][3] = l1_2
                elif s2 == 3:
                    ['Ma' + str(i)][2][3] = l1_2
                elif s3 == 1:
                    ['Ma' + str(i)][0][3] = l1_3
                elif s3 == 2:
                    ['Ma' + str(i)][1][3] = l1_3
                elif s3 == 3:
                    ['Ma' + str(i)][2][3] = l1_3
        elif os3 == 2:
            globals()['Ma' + str(i)] =np.array( [[1, 0, 0, 0],
                                                 [0, 1, 0, l3],
                                                 [0, 0, 1, 0],
                                                 [0, 0, 0, 1]])
            if dop == 2:
                print('Какая дополнительная ось у ', i, '-го звена? \n 1 - ось Ох \n 2 - ось Оу \n 3 - ось Оz')
                s1 = int(input())
                if s1 == 1:
                    ['Ma' + str(i)][0][3] = l1_1
                elif s1 == 2:
                    ['Ma' + str(i)][1][3] = l1_1
                elif s1 == 3:
                    ['Ma' + str(i)][2][3] = l1_1
                elif s2 == 1:
                    ['Ma' + str(i)][0][3] = l1_2
                elif s2 == 2:
                    ['Ma' + str(i)][1][3] = l1_2
                elif s2 == 3:
                    ['Ma' + str(i)][2][3] = l1_2
                elif s3 == 1:
                    ['Ma' + str(i)][0][3] = l1_3
                elif s3 == 2:
                    ['Ma' + str(i)][1][3] = l1_3
                elif s3 == 3:
                    ['Ma' + str(i)][2][3] = l1_3
        elif os3 == 3:
            globals()['Ma' + str(i)] =np.array( [[1, 0, 0, 0],
                                                 [0, 1, 0, 0],
                                                 [0, 0, 1, l3],
                                                 [0, 0, 0, 1]])
            if dop == 2:
                print('Какая дополнительная ось у ', i, '-го звена? \n 1 - ось Ох \n 2 - ось Оу \n 3 - ось Оz')
                s1 = int(input())
                if s1 == 1:
                    ['Ma' + str(i)][0][3] = l1_1
                elif s1 == 2:
                    ['Ma' + str(i)][1][3] = l1_1
                elif s1 == 3:
                    ['Ma' + str(i)][2][3] = l1_1
                elif s2 == 1:
                    ['Ma' + str(i)][0][3] = l1_2
                elif s2 == 2:
                    ['Ma' + str(i)][1][3] = l1_2
                elif s2 == 3:
                    ['Ma' + str(i)][2][3] = l1_2
                elif s3 == 1:
                    ['Ma' + str(i)][0][3] = l1_3
                elif s3 == 2:
                    ['Ma' + str(i)][1][3] = l1_3
                elif s3 == 3:
                    ['Ma' + str(i)][2][3] = l1_3
print('Матрица первого звена')
print(Ma1)
print('************************')
print('Матрица второго звена')
print(Ma2)
print('************************')
print('Матрица третьего звена')
print(Ma3)
print('************************')

M41 = int(input('На какой оси расположено последнее звено?\n 1-Ох \n 2-Оу \n 3-Оz'))
if M41 == 1:
    M4 = np.array([[l3],
                    [0],
                    [0],
                    [1]])
elif M41 == 2:
    M4 = np.array([[0],
                   [l3],
                   [0],
                   [1]])
elif M41 == 3:
    M4 = np.array([[0],
                   [0],
                   [l3],
                   [1]])
# Матрицы можно будет заменить, в случае звена с углом
Ma21 = np.dot(Ma1,Ma2)
print(Ma21)
print('Матрица А')
Ma23 = np.dot(Ma21,Ma3)
print('************************')
print(Ma23)
print('Матрица В')
print('************************')
MC = np.dot(Ma23,M4)
print(MC)
print('Матрица С')
print('************************')
