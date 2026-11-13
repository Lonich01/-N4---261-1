# ЗАДАНИЕ 1

summa=0
count=0

while True:
    n=int(input("Введите число: "))
    if n==0:
        break

    a=abs(n)
    s=0

    while a>0:
        s+=a%10
        a//=10

    k=0
    for i in range(1,s+1):
        if s%i==0:
            k+=1

    if k==2:
        summa+=n

    if n>0:
        a=n
        while a>0:
            if a%10==2:
                count+=1
                break
            a//=10

print("Сумма:",summa)
print("Количество:",count)


# ЗАДАНИЕ 2

n=int(input("Введите натуральное число: "))
p=1

while n>0:
    p*=n%10
    n//=10

print("Произведение цифр:",p)


# ЗАДАНИЕ 3

nomer=0
max_chislo=None
max_nomer=0

while True:
    n=int(input("Введите число: "))

    if n==0:
        break

    nomer+=1
    a=abs(n)
    count=0

    while a>0:
        cifra=a%10
        if cifra%2!=0:
            count+=1
        a//=10

    if n<0 and count%2==0:
        if max_chislo is None or n>max_chislo:
            max_chislo=n
            max_nomer=nomer

if max_chislo is None:
    print("Подходящих чисел нет")
else:
    print("Порядковый номер:",max_nomer)
    print("Величина числа:",max_chislo)


# ЗАДАНИЕ 4

count=0
pred=None
tek=None

while True:
    n=float(input("Введите число: "))

    if n<0:
        break

    if pred is None:
        pred=n
    elif tek is None:
        tek=n
    else:
        if tek>pred and tek>n:
            count+=1

        pred=tek
        tek=n

print("Количество чисел:",count)


# ЗАДАНИЕ 5

n=int(input("Введите N: "))
count=0
summa=0

while n>0:
    cifra=n%10
    summa+=cifra
    count+=1
    n//=10

print("Количество цифр:",count)
print("Сумма цифр:",summa)


# ЗАДАНИЕ 6

from math import exp

x=float(input("Введите x: "))
eps=0.00001
y=1
a=1
n=1

while True:
    a=a*x/n

    if abs(a)<eps:
        break

    y+=a
    n+=1

print("Результат ряда:",y)
print("EXP(x):",exp(x))


# ЗАДАНИЕ 7

x=float(input("Введите x: "))
eps=0.00001
y=x
a=x
n=1

while True:
    a=a*(-x*x)/((2*n)*(2*n+1))

    if abs(a)<eps:
        break

    y+=a
    n+=1

print("sin(x)=",y)


# ЗАДАНИЕ 8

from math import cos

x=float(input("Введите x: "))
eps=0.0001
y=1
a=1
n=1

while True:
    a=a*(-x*x)/((2*n-1)*(2*n))

    if abs(a)<eps:
        break

    y+=a
    n+=1

print("Результат ряда:",y)
print("cos(x):",cos(x))


# ЗАДАНИЕ 9

n=int(input("Введите натуральное число: "))
p=1

while n>0:
    p*=n%10
    n//=10

print("Произведение цифр:",p)


# ЗАДАНИЕ 10

nomer=0
max_chislo=None
max_nomer=0

while True:
    n=int(input("Введите число: "))

    if n==0:
        break

    nomer+=1

    if n<0:
        if max_chislo is None or n>max_chislo:
            max_chislo=n
            max_nomer=nomer

if max_chislo is None:
    print("Отрицательных чисел нет")
else:
    print("Порядковый номер:",max_nomer)
    print("Величина числа:",max_chislo)


# ЗАДАНИЕ 11

count=0
pred=None

while True:
    n=int(input("Введите число: "))

    if n==0:
        break

    if pred is not None:
        if (pred<0 and n>0) or (pred>0 and n<0):
            count+=1

    pred=n

print("Количество изменений знака:",count)


# ЗАДАНИЕ 12

a=1
b=1
summa=0

while a<=1000:
    summa+=a
    c=a+b
    a=b
    b=c

print("Сумма чисел Фибоначчи:",summa)


# ЗАДАНИЕ 13

n=int(input("Введите натуральное число: "))
a=n
obratnoe=0

while a>0:
    cifra=a%10
    obratnoe=obratnoe*10+cifra
    a//=10

if n==obratnoe:
    print("Число является палиндромом")
else:
    print("Число не является палиндромом")
