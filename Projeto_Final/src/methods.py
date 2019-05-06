import matplotlib.pyplot as mt
import random as rd
from random import randint
from math import floor
import numpy as np
import Constantes as ct
import DEMethods as dem
import time




VALORES_NECESSARIOS = [1, 2, 3, 4, 5, 6, 7, 8, 9]


def get_sub_matrix(x, y, matriz):
    if y == 0:
        if x == 0:
            return matriz[0:3, 0:3]
        if x == 1:
            return matriz[0:3, 3:6]
        if x == 2:
            return matriz[0:3, 6:9]
    if y == 1:
        if x == 0:
            return matriz[3:6, 0:3]
        if x == 1:
            return matriz[3:6, 3:6]
        if x == 2:
            return matriz[3:6, 6:9]
    if y == 2:
        if x == 0:
            return matriz[6:9, 0:3]
        if x == 1:
            return matriz[6:9, 3:6]
        if x == 2:
            return matriz[6:9, 6:9]


def verificar_valores_sub_matriz(lista):
    valores_faltantes = 0
    for i in range(1,10):
        if i not in lista:
            valores_faltantes = valores_faltantes + 1

    return valores_faltantes


def get_fitness(value):
    if value == 0:
        return 100
    else:
        return (81 * value )/100



def create_chromossome_dificil():
    dificil = ct.DIFICIL
    i = 0
    j = 0
    lista_retorno = []
    lista = matrix_to_array(dificil)
    for values in lista:
        if values == 0:
            lista_retorno.append(randint(1,9))
        else:
            lista_retorno.append(values)
    return lista_retorno



def create_chromossome_medio():
    medio = ct.MEDIO
    i = 0
    j = 0
    lista_retorno = []
    lista = matrix_to_array(medio)
    for values in lista:
        if values == 0:
            lista_retorno.append(randint(1,9))
        else:
            lista_retorno.append(values)
    return lista_retorno


def create_chromossome_facil():
    facil = ct.FACIL
    i = 0
    j = 0
    lista_retorno = []
    lista = matrix_to_array(facil)
    for values in lista:
        if values == 0:
            lista_retorno.append(randint(1,9))
        else:
            lista_retorno.append(values)
    return lista_retorno


def matrix_to_array(matrix):
    i = 0
    j = 0
    lista = []
    for linhas in matrix:
        j = 0
        for colunas in linhas:
            lista.append(matrix[i][j])
            j = j + 1
        i = i + 1
    return lista



def create_generation(value, tamanho):
    if value == 1:
        geracao = []
        for i in range(tamanho):
            geracao.append(create_chromossome_facil())
        return geracao
    if value == 2:
        geracao = []
        for i in range(tamanho):
            matrix = create_chromossome_medio()
            geracao.append(matrix)
        return geracao
    if value == 3:
        geracao = []
        for i in range(tamanho):
            geracao.append(create_chromossome_dificil())
        return geracao



def get_lista_sub_matriz(x, y, matriz): #x e y são as cordenadas do jogo
    lista_valores_sub_matrix = []
    lista_valores_sub_matrix.append(matrix_to_array(get_sub_matrix(x,y,matriz)))
    return lista_valores_sub_matrix

def get_valor_mesma_coluna(coluna, matriz):
    lista_valores_mesma_coluna = []
    if coluna == 0:
        lista_valores_mesma_coluna = matrix_to_array(matriz[0:9, coluna: 1])
    elif coluna == 8:
       lista_valores_mesma_coluna = matrix_to_array(matriz[0:9, 8:9])
    else:
        lista_valores_mesma_coluna = matrix_to_array(matriz[0:9, coluna:coluna+1])

    return lista_valores_mesma_coluna

def cross_over_um_ponto_de_corte(geracao):
    new_generation = []
    for i in range(int(len(geracao)/2)):
        ponto_troca = randint(1, 80)
        individuo1 = torneio(geracao)
        individuo2 = torneio(geracao)
        individuo1[ponto_troca:], individuo2[ponto_troca:] = individuo2[ponto_troca:], individuo1[ponto_troca:]
        new_generation.append(individuo1)
        new_generation.append(individuo2)

    return new_generation


def mutacao_DE(schema, geracao):
    return dem.mutacao(schema, geracao)


def gerarGrafico(fitness,valores):

    mt.title("Valores de Fitness da geração")
    mt.plot(fitness, valores)
    mt.xlabel("Melhor valor na geração")
    mt.ylabel("Numero da geração")
    mt.show()


def torneio(geracao):

    ind1 = geracao[randint(0, len(geracao) - 1)]
    ind2 = geracao[randint(0, len(geracao) - 1)]
    ind3 = geracao[randint(0, len(geracao) - 1)]
    lista_individuos = []
    lista_individuos.append(crom_to_matriz(ind1))
    lista_individuos.append(crom_to_matriz(ind2))
    lista_individuos.append(crom_to_matriz(ind3))
    best = 0
    melhor_individuo = []
    for ind in lista_individuos:
        value = calculo_fitness(ind)
        if value > best:
            best = value
            melhor_individuo = ind
    return matrix_to_array(melhor_individuo)


def calculo_fitness(matriz):
    valor_sub_matrizes = 0
    valor_colunas = 0
    for i in range(3):
        for j in range(3):
            valor_sub_matrizes = valor_sub_matrizes + verificar_valores_sub_matriz(matrix_to_array(get_sub_matrix(i,j, matriz)))
    for i in range(9):
        valor_colunas = valor_colunas + verificar_valores_sub_matriz(get_valor_mesma_coluna(i, matriz))
    return get_fitness(valor_sub_matrizes + valor_colunas)


def crom_to_matriz(crom):
    p = np.array(crom)
    matriz = p.reshape(9, 9)
    return matriz

def get_melhor_valor(lista):
    best = 0
    for i in lista:
        if i > best:
            best = i
    return best

def process_facil_schema1(iter, ger):
    inicio = time.clock()
    todos_fitness = []
    grafic_x_values = []
    grafic_y_values = []
    a = create_generation(1, ger)
    cross = cross_over_um_ponto_de_corte(a)
    mut = mutacao_DE(1, cross)
    for crom in mut:
        todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
    best = get_melhor_valor(todos_fitness)
    grafic_x_values.append(best)
    grafic_y_values.append(1)
    for i in range(iter-1):
        cross = cross_over_um_ponto_de_corte(mut)
        mut = mutacao_DE(1, cross)
        for crom in mut:
            todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
        best = get_melhor_valor(todos_fitness)
        grafic_x_values.append(best)
        grafic_y_values.append(i+1)
    fim = time.clock()
    print("Tempo da execução => ", fim - inicio)
    gerarGrafico(grafic_x_values, grafic_y_values)

def process_medio_schema1(iter, ger):
    inicio = time.clock()
    todos_fitness = []
    grafic_x_values = []
    grafic_y_values = []
    a = create_generation(2, ger)
    cross = cross_over_um_ponto_de_corte(a)
    mut = mutacao_DE(1, cross)
    for crom in mut:
        todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
    best = get_melhor_valor(todos_fitness)
    grafic_x_values.append(best)
    grafic_y_values.append(1)
    for i in range(iter-1):
        cross = cross_over_um_ponto_de_corte(mut)
        mut = mutacao_DE(1, cross)
        for crom in mut:
            todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
        best = get_melhor_valor(todos_fitness)
        grafic_x_values.append(best)
        grafic_y_values.append(i+1)
    fim = time.clock()
    print("Tempo da execução => ", fim - inicio)
    gerarGrafico(grafic_x_values, grafic_y_values)

def process_dificil_schema1(iter, ger):
    inicio = time.clock()
    todos_fitness = []
    grafic_x_values = []
    grafic_y_values = []
    a = create_generation(3, ger)
    cross = cross_over_um_ponto_de_corte(a)
    mut = mutacao_DE(1, cross)
    for crom in mut:
        todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
    best = get_melhor_valor(todos_fitness)
    grafic_x_values.append(best)
    grafic_y_values.append(1)
    for i in range(iter-1):
        cross = cross_over_um_ponto_de_corte(mut)
        mut = mutacao_DE(1, cross)
        for crom in mut:
            todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
        best = get_melhor_valor(todos_fitness)
        grafic_x_values.append(best)
        grafic_y_values.append(i+1)
    fim = time.clock()
    print("Tempo da execução => ", fim - inicio)
    gerarGrafico(grafic_x_values, grafic_y_values)


def process_facil_schema2(iter, ger):
    inicio = time.clock()
    todos_fitness = []
    grafic_x_values = []
    grafic_y_values = []
    a = create_generation(1, ger)
    cross = cross_over_um_ponto_de_corte(a)
    mut = mutacao_DE(2, cross)
    for crom in mut:
        todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
    best = get_melhor_valor(todos_fitness)
    grafic_x_values.append(best)
    grafic_y_values.append(1)
    for i in range(iter-1):
        cross = cross_over_um_ponto_de_corte(mut)
        mut = mutacao_DE(2, cross)
        for crom in mut:
            todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
        best = get_melhor_valor(todos_fitness)
        grafic_x_values.append(best)
        grafic_y_values.append(i+1)
    fim = time.clock()
    print("Tempo da execução => ", fim - inicio)
    gerarGrafico(grafic_x_values, grafic_y_values)


def process_medio_schema2(iter, ger):
    inicio = time.clock()
    todos_fitness = []
    grafic_x_values = []
    grafic_y_values = []
    a = create_generation(2, ger)
    cross = cross_over_um_ponto_de_corte(a)
    mut = mutacao_DE(2, cross)
    for crom in mut:
        todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
    best = get_melhor_valor(todos_fitness)
    grafic_x_values.append(best)
    grafic_y_values.append(1)
    for i in range(iter-1):
        cross = cross_over_um_ponto_de_corte(mut)
        mut = mutacao_DE(2, cross)
        for crom in mut:
            todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
        best = get_melhor_valor(todos_fitness)
        grafic_x_values.append(best)
        grafic_y_values.append(i+1)
    fim = time.clock()
    print("Tempo da execução => ", fim - inicio)
    gerarGrafico(grafic_x_values, grafic_y_values)


def process_dificil_schema2(iter, ger):
    inicio = time.clock()
    todos_fitness = []
    grafic_x_values = []
    grafic_y_values = []
    a = create_generation(3, ger)
    cross = cross_over_um_ponto_de_corte(a)
    mut = mutacao_DE(2, cross)
    for crom in mut:
        todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
    best = get_melhor_valor(todos_fitness)
    grafic_x_values.append(best)
    grafic_y_values.append(1)
    for i in range(iter-1):
        cross = cross_over_um_ponto_de_corte(mut)
        mut = mutacao_DE(2, cross)
        for crom in mut:
            todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
        best = get_melhor_valor(todos_fitness)
        grafic_x_values.append(best)
        grafic_y_values.append(i+1)
    fim = time.clock()
    print("Tempo da execução => ", fim - inicio)
    gerarGrafico(grafic_x_values, grafic_y_values)


def process_facil_schema3(iter, ger):
    inicio = time.clock()
    todos_fitness = []
    grafic_x_values = []
    grafic_y_values = []
    a = create_generation(1, ger)
    cross = cross_over_um_ponto_de_corte(a)
    mut = mutacao_DE(3, cross)
    for crom in mut:
        todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
    best = get_melhor_valor(todos_fitness)
    grafic_x_values.append(best)
    grafic_y_values.append(1)
    for i in range(iter-1):
        cross = cross_over_um_ponto_de_corte(mut)
        mut = mutacao_DE(3, cross)
        for crom in mut:
            todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
        best = get_melhor_valor(todos_fitness)
        grafic_x_values.append(best)
        grafic_y_values.append(i+1)
    fim = time.clock()
    print("Tempo da execução => ", fim - inicio)
    gerarGrafico(grafic_x_values, grafic_y_values)


def process_medio_schema3(iter, ger):
    inicio = time.clock()
    todos_fitness = []
    grafic_x_values = []
    grafic_y_values = []
    a = create_generation(2, ger)
    cross = cross_over_um_ponto_de_corte(a)
    mut = mutacao_DE(3, cross)
    for crom in mut:
        todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
    best = get_melhor_valor(todos_fitness)
    grafic_x_values.append(best)
    grafic_y_values.append(1)
    for i in range(iter-1):
        cross = cross_over_um_ponto_de_corte(mut)
        mut = mutacao_DE(3, cross)
        for crom in mut:
            todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
        best = get_melhor_valor(todos_fitness)
        grafic_x_values.append(best)
        grafic_y_values.append(i+1)
    fim = time.clock()
    print("Tempo da execução => ", fim - inicio)
    gerarGrafico(grafic_x_values, grafic_y_values)


def process_dificil_schema3(iter, ger):
    inicio = time.clock()
    todos_fitness = []
    grafic_x_values = []
    grafic_y_values = []
    a = create_generation(3, ger)
    cross = cross_over_um_ponto_de_corte(a)
    mut = mutacao_DE(3, cross)
    for crom in mut:
        todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
    best = get_melhor_valor(todos_fitness)
    grafic_x_values.append(best)
    grafic_y_values.append(1)
    for i in range(iter-1):
        cross = cross_over_um_ponto_de_corte(mut)
        mut = mutacao_DE(3, cross)
        for crom in mut:
            todos_fitness.append(calculo_fitness(crom_to_matriz(crom)))
        best = get_melhor_valor(todos_fitness)
        grafic_x_values.append(best)
        grafic_y_values.append(i+1)
    fim = time.clock()
    print("Tempo da execução => ", fim - inicio)
    gerarGrafico(grafic_x_values, grafic_y_values)




































