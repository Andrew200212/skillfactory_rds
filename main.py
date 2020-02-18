import numpy as np
count = 1 #счетчик количества попыток
max_number=100 #максимальное число из диапазона натуральных чисел
max_count=[] #Список количества попыток
#####Количество игр#####
for i in range(0,1000):
    number = np.random.randint(1,max_number)
    #####Список чисел, входящих в диапазон#####
    mass=[]
    for i in range(1,max_number+1):
        mass+=[i]
    #####Нахождение числа путем уменьшения диапазона чисел вдвое#####
    while True:
        predict=mass[len(mass)//2]
        if number==predict:
            max_count+=[count]
            count=1
            break
        else:
            count+=1 #Увеличение количества попыток
            if number<predict:
                mass=mass[:int(len(mass)/2)] #Первая половина диапазона чисел
            elif number>predict:
                mass=mass[-int(len(mass)/2):] #Вторая половина диапазона чисел
print(max_count)
print("Максимальное количество попыток -",max(max_count))
print("Среднее количество попыток -",int(sum(max_count)/len(max_count)))
