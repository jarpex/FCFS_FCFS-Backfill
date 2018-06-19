#! /usr/bin/env python3
#Импортируем распределение по Гауссу:
from random import gauss as G
#Функция генерации очереди задач.
problems = []
def gen_problems(max):
    i = 0
    while i < max:
        problems.append([int(G(50,6)),int(G(50,9))])
        i += 1
    return problems
