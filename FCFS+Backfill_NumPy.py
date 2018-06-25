#! /usr/bin/env python3
#Подключение сторонних функций и процедур
from numpy import zeros as array                                                            #Функция генерации массива
#Gauss
from prbms import gen_problems as gen                                                       #Функция генерации задач
#Random
#from prbms import gen_problemsRnd as genR
#vars
Curr = 0
CPUs = 1000                                                                                 #Общее количество процессоров
Time = 1500                                                                                 #Время, в рамках которого происходит планирование
LastCPUs = LastTime = 0                                                                     #Последляя позиция, подробнее далее
Backfill = False
'''
Алгоритм FCFS+Backfill подразумевает выполнение следующих шагов:
1) при наличии необходимого количества свободных процессоров для запуска первой
в очереди задачи эта задача удаляется из очереди и запускается на выполнение;
2) если для запуска первой в очереди задачи свободных процессоров не хватает, то
вычисляется момент времени, когда их станет достаточно, и производится резервиро-
вание для данной задачи;
3) продолжается движение по очереди с запуском на выполнение задач, не наруша-
ющих резервирование первой в очереди задачи. 
Фактически, вышесказанное подразумевает планирование текущей задачи на ближайший возможный момент.
Благодаря этому, алгоритм Backfill можно перефразировать:
1) при наличии необходимого количества свободных процессоров для запуска первой
в очереди задачи эта задача удаляется из очереди и запускается на выполнение;
2) если для запуска первой в очереди задачи свободных процессоров не хватает, то
происходит резервирование текущего состояния алгоритма распределения, и задача
размещается на ближайший возможный момент.
3) Разместив текущую задачу, алгоритм возвращается на заранее зарезервированную позицию,
продолжая работать уже со следующей задачей. 
'''
#Gen. problems Gauss
problems = gen(1000)
#Gen. problems Random
#problems = genR(10000)
#Gen. schedule
schedule = array((CPUs,Time))
#FCFS
dTime = 0
while dTime < Time:
    print(round(dTime/Time*100,1),'%')
    dCPUs = 0
    while dCPUs < CPUs:
        if schedule[dCPUs][dTime] == 0:                                                     #Если текущая ячейка свободна
            if  problems[Curr][0] < CPUs - dCPUs:                                           #Если на текущий момент хватает свободных процессоров
                cCPUs = dCPUs                                                               #cCPUs — начальное значение для проверки свободного места
                mCPUs = dCPUs + problems[Curr][0]                                           #mCPUs — конечное значения для проверки свободного места
                sum = 0                                                                     #sum — проверка свободного места
                while cCPUs < mCPUs:                                                        #Цикл, проверяющий свободное место
                    sum = schedule[cCPUs][dTime]
                    cCPUs += 1
                if sum == 0:                                                                #Если сумма = 0, то место свободно.
                    cTime = dTime
                    mTime = dTime + problems[Curr][1]
                    while cTime < mTime:
                        cCPUs = dCPUs
                        while cCPUs <= mCPUs:                                               #Присвоение задачи
                            schedule[cCPUs][cTime] = Curr + 1                               #+1 необходим для проверки на свободное место
                            cCPUs += 1
                        if cTime != Time - 1: 
                            cTime += 1
                        else:
                            break
                    if Backfill == True:                                                    #Если мы имеем зарезервированное место — возвращаемся.
                        print('Backfill')
                        dCPUs = LastCPUs
                        dTime = LastTime
                        Backfill = False
                    Curr += 1
                    if mCPUs != CPUs:
                        dCPUs += 1
                    else:
                        dCPUs = 0
                        break
                else:
                    dCPUs += 1
            else:                                                                           #Backfill
                LastCPUs = dCPUs
                LastTime = dTime
                Backfill = True
                dCPUs = 0
                break
        else:
            dCPUs += 1        
    dTime += 1
print(schedule)
print('Вычисление эффективности распределения')
dTime = 0
sum = 0
while dTime < Time:
    dCPUs = 0
    while dCPUs < CPUs:
        if schedule[dCPUs][dTime] == 0:
            sum += 1
        dCPUs += 1
    dTime += 1
print('Эфективность составила:',100 - round((sum/(CPUs*Time)),2)*100,'%')
print('Всего было распределено',Curr,'задач.')