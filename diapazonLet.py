a = int(input('Введите начало отчета високосных лет: '))
b = int(input('Введите конец отчета високосных лет: '))
c = b+1
if a%4==0:
    for a in range(a,c,4):
        print(a)
elif (a+1)%4==0:
    a = a+1
    for a in range(a,c,4):
        print(a)
elif (a+2)%4==0:
    a = a + 2
    for a in range(a,c,4):
        print(a)
elif (a+3)%4==0:
    a = a + 3
    for a in range(a,c,4):
        print(a)
