#! /usr/bin/env python3
#Подключение сторонних функций и процедур
from numpy import zeros as array
from prbms import gen_problems as gen
#vars
Curr = 0
CPUs = 1000
Time = 1500
#Gen. problems
problems = gen(1000)
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
                    Curr += 1
                    if mCPUs != CPUs:
                        dCPUs += 1
                    else:
                        dCPUs = 0
                        break
                else:
                    dCPUs += 1
            else:
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