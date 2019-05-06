import matplotlib.pyplot as mt
import random as rd
from random import randint
from math import floor
import numpy as np

MIN = -5.12
MAX = 5.12
CR = 0.7
F = 0.77

def mutacao(schema, geracao):
    new_generation = []
    for cromososmo in geracao:
        for i in range(len(cromososmo)):
            value = rd.random()
            if value < F:
                 cromososmo[i] = randint(1,9)

    if schema == 1:
        new_generation = DE(1, geracao)
    if schema == 2:
        new_generation = DE(2, geracao)
    if schema == 3:
        new_generation = DE(3, geracao)
    return new_generation



def DE(schema, geracao):
    lista_U = []
    if schema == 1: #DE/RAND/1/BIN
        for cromossomos in geracao:
            for genes in range(len(cromossomos)-3):
                alpha = randint(1, len(cromossomos) - 1)
                beta = randint(1, len(cromossomos) - 1)
                gama = randint(1, len(cromossomos) - 1)
                u = abs(get_U(alpha, beta, gama, cromossomos))
                if u <= cromossomos[genes] and u != 0:
                    cromossomos[genes] = u
        return geracao
    elif schema == 2: #DE/RAND/2
        for cromossomos in geracao:
            for genes in range(len(cromossomos)-4):
                u = abs(get_U_schema(genes, genes+2, genes+1, genes+4, genes+3,cromossomos))
                if u <= cromossomos[genes] and u != 0:
                    cromossomos[genes] = u
        return geracao
    elif schema == 3: #DE/BEST/2
        for cromossomos in geracao:
            for genes in range(len(cromossomos)-3):
                best = get_best_value(cromossomos)
                best_pos = get_best_post(best, cromossomos)
                u = abs(get_U_schema(best_pos, genes+1, genes, genes+3, genes+2,cromossomos))
                if u <= cromossomos[genes] and u != 0:
                    cromossomos[genes] = u
        return geracao


def get_best_value(list_cromo):
    best = 0
    for crom in list_cromo:
        if crom > best:
            best = crom
    return best

def get_U(alpha, beta, gama, crom):
    value = crom[beta] - crom[gama]
    valueu = crom[alpha] + F * value
    return int(valueu)

def get_U_schema(alpha, beta, gama, x1, x2, crom):
    valuex = crom[beta] - crom[gama]
    valuey = crom[x1] - crom[x2]
    return int(crom[alpha] + F * valuex + F * valuey)

def get_best_post(best, lista):
    for i in range(len(lista)):
        if lista[i] == best:
            return i
