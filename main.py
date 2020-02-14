import numpy as np
count = 1                           
number = np.random.randint(1,100)   
print(number)
mass=[]
for i in range(1,101):
    mass+=[i]
while True:
    if len(mass)%2==0:
        predict=mass[int((len(mass)/2))-1]
    else:
        predict=mass[len(mass)//2]
    print(predict) #проверка
    print(count) #проверка
    if number==predict:
        print("Количество попыток -",count)
        break
    else:
        count+=1
        if number<predict:
            mass=mass[:int(len(mass)/2)]
            print(mass) #проверка
        elif number>predict:
            mass=mass[-int(len(mass)/2):]
            print(mass) #проверка
