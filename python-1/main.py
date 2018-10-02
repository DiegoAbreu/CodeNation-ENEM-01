# coding: utf-8

# Todas as perguntas são referentes ao arquivo `data.csv`
# Você ** não ** pode utilizar o pandas e nem o numpy para este desafio.

import csv
from collections import Counter
def ler_coluna(coluna):
    data = []
    with open('data.csv', 'r') as csv_file:
        csv_reader = csv.DictReader(csv_file, delimiter=',')
        for line in csv_reader:
            data.append(line[coluna])
    return data

# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?

def q_1():
    nacionalidade = ler_coluna('nationality')
    return len(set(nacionalidade))
    pass

# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?
def q_2():
    times = ler_coluna('club')
    return len(set(times))
    pass

# **Q3.** Liste o primeiro nome dos 20 primeiros jogadores de acordo com a coluna `full_name`.
def q_3():
    nome_completo = ler_coluna('full_name')
    return nome_completo[0:20]
    pass

# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?
def q_4():
    nome_completo = list(ler_coluna('full_name'))
    salario = list(map(float, ler_coluna('eur_wage')))

    top_10_salarios = sorted(zip(nome_completo, salario), reverse=True, key= lambda k: k[1])[:10]
    nomes = []

    for nome, _ in top_10_salarios:
        nomes.append(nome)
    return nomes
    pass

# **Q5.** Quem são os 10 jogadores mais velhos?
def q_5():
    nome_completo = list(ler_coluna('full_name'))
    idade = list(map(int, ler_coluna('age')))
    top_10_mais_velhos = sorted(zip(nome_completo, idade), reverse=True, key=lambda k: k[1])[:10]
    nomes = []
    for nome, _ in top_10_mais_velhos:
        nomes.append(nome)
    return nomes
    pass

# **Q6.** Conte quantos jogadores existem por idade. Para isso, construa um dicionário onde as chaves são as idades e os valores a contagem.

def q_6():
    idade = list(map(int, ler_coluna('age')))
    return Counter(idade)
    pass

