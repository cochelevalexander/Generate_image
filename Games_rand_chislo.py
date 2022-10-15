#Игра по определению рандомного числа
def Games_rand_chislo():
    import random
    print('Игра - рандомное число. \n',"Правила игры: \n",'Компьютер загадывает число, ваша задача - его угадать. '+
          'В начале игры дается 50 баллов, за каждую ошибку снимается по 2 баллал, \nза угаданный ответ - дается' +
          ' по 10 баллов. Ваша задача набрать максимальное количество баллов. Удачи!\n')
    sage = 0
    rand = 0
    def main(a):
        print('Игра окончена!\nДля продолжения нажмите \nДля завершения нажмите 0\n')
        a = int(input())
        if a == 1:
            a == 1
        else:
            a == 0
    b = int(input('Для начала игры нажмите 1:\n'))
    try:
        while b ==1:
            summa = 50
            a = b
            while a == 1:
                summa = summa
                if summa ==0:
                    summa = 50
                rand = random.randint(1, 50)
                print('Компьютер загадал число, попробуйте его угадать: \n')
                sage = int(input((': ')))
                while sage <= rand or sage >= rand:
                    if sage < rand - 20:
                        summa -= 2
                        print('Слиишком холодно... ')
                        print('Ваш баланс очков: ',summa)
                        print('***************************************')
                        sage = int(input(('Попробуйте снова: ')))
                    elif sage < rand - 10 and sage > rand - 20:
                        summa -= 2
                        print('Теплее... ')
                        print('Ваш баланс очков: ',summa)
                        print('***************************************')
                        sage = int(input(('Попробуйте снова: ')))
                    elif sage < rand - 5 and sage > rand - 10:
                        summa -= 2
                        print('Горяче... ')
                        print('Ваш баланс очков: ',summa)
                        print('***************************************')
                        sage = int(input(('Попробуйте снова: ')))
                    elif sage < rand and sage > rand - 5:
                        summa -= 2
                        print('Достаточно горяче... ')
                        print('Ваш баланс очков: ',summa)
                        print('***************************************')
                        sage = int(input(('Попробуйте снова: ')))
                    elif sage == rand :
                        summa += 10
                        print('Поздравляю!!! Вы угадали число!!!... ')
                        print('Ваш баланс очков: ',summa)
                        #from cherepacha import cher
                        break
                        main()
                        print('***************************************')
                        sage = int(input(('Попробуйте снова: ')))
                    elif sage > rand and sage < rand + 5:
                        summa -= 2
                        print('Достаточно горяче... ')
                        print('Ваш баланс очков: ',summa)
                        print('***************************************')
                        sage = int(input(('Попробуйте снова: ')))
                    elif sage > rand + 5 and sage < rand + 10:
                        summa -= 2
                        print('Горяче... ')
                        print('Ваш баланс очков: ',summa)
                        print('***************************************')
                        sage = int(input(('Попробуйте снова: ')))
                    elif sage > rand + 10 and sage < rand + 20:
                        summa -= 2
                        print('Теплее... ')
                        print('Ваш баланс очков: ',summa)
                        print('***************************************')
                        sage = int(input(('Попробуйте снова: ')))
                    elif sage > rand + 20:
                        summa -= 2
                        print('Слиишком холодно... ')
                        print('Ваш баланс очков: ',summa)
                        print('***************************************')
                        sage = int(input(('Попробуйте снова: ')))
                    if summa == 0:
                        break
                    elif summa == 100:
                        import File_The_End
                        print('Поздравляю!!! Вы победили!!!')
                a = int(input('Игра окончена!\nДля продолжения нажмите 1\nДля завершения нажмите 0\n'))
            b = a
    except:
        print('Ошибка, попробуйте снова')
        a = int(input('Для продолжения нажмите 1\nДля завершения нажмите 0\n'))
Games_rand_chislo()






#Создадим переменную для ввода в функцию

