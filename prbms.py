#! /usr/bin/env python3
#Импортируем распределение по Гауссу:
from random import gauss as G
#Импортируем псевдослучайное распределение:
from random import randrange as R
#Функция генерации очереди задач по Гауссу.
problems = []
def gen_problems(max):
    i = 0
    while i < max:
        problems.append([int(G(50,6)),int(G(50,9))])
        i += 1
    return problems
#Функция генерации очереди псевдослучайных задач.
def gen_problemsRnd(max):
    i = 0
    while i < max:
        problems.append([int(R(1,10,1)),int(R(1,100,1))])
        i += 1
    return problems