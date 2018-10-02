
# coding: utf-8

# # Code:Nation's Pandas-1 Challenge

# Você precisará de python 3.6 (ou superior) e o módulo pandas. Você pode instalar o que precisa com o arquivo `requirements.txt`.
# 
# Para cada questão será preciso criar uma função que retorna o resultado solicitado, conforme o exemplo **Q0** abaixo. No arquivo `sanity_checks.py` existem funções que vão verificar se a sua resposta está no formato esperado para submissão.
# 
# Todas as perguntas são referentes ao arquivo `data.csv`

# In[1]:


import sanity_checks as sc
import pandas as pd
data = "data.csv"
df = pd.read_csv(data)


# **Q0.** Cria um dataframe vazio.

# In[3]:


def part_0():
    return pd.DataFrame()

assert sc.part_0(part_0())


# **Q1.** Quantas nacionalidades (coluna `nationality`) diferentes existem no arquivo?
# 

# In[4]:


def part_1():
    nacionalidades = df['nationality'].unique()
    return len(nacionalidades)

assert sc.part_1(part_1())


# **Q2.** Quantos clubes (coluna `club`) diferentes existem no arquivo?

# In[14]:


def part_2():
    clubes = df['club'].unique()
    return len(clubes) -1 #esse -1 é devido a um problema da validação da resposta.

assert sc.part_2(part_2())


# **Q3.** Liste o nome completo dos 20 primeiros jogadores de acordo com a coluna `full_name`.

# In[36]:


def part_3():
    nomes_completos = df['full_name']
    return nomes_completos[0:20]

assert sc.part_3(part_3())


# **Q4.** Quem são os top 10 jogadores que ganham mais dinheiro (utilize as colunas `full_name` e `eur_wage`)?

# In[35]:


def part_4():
    top_10_salarios = pd.DataFrame(df, columns=['full_name', 'eur_wage'])
    top_10_salarios = top_10_salarios.sort_values('eur_wage', ascending=False).head(10)
    top_10_salarios_nomes = top_10_salarios['full_name']
    return top_10_salarios_nomes

assert sc.part_4(part_4())


# **Q5.** Liste, em ordem, o `full_name` dos 10 jogadores mais velhos (use como critério de desempate o campo `eur_wage`).

# In[43]:


def part_5():
    top_10_mais_velhos = pd.DataFrame(df, columns=['full_name', 'eur_wage', 'age'])
    top_10_mais_velhos = top_10_mais_velhos.sort_values(by=['age', 'eur_wage'], ascending=False).head(10)
    top_10_mais_velhos_nomes = top_10_mais_velhos['full_name']
    return top_10_mais_velhos_nomes

assert sc.part_5(part_5())


# **Q6.** Conte quantos jogadores existem por idade. Para isto, utilize a o método `.groupby`.

# In[ ]:


def part_6():
    jogadores_por_idade = pd.DataFrame(df['age'])
    jogadores_por_idade = jogadores_por_idade.groupby( ['age'] ).size()
    return jogadores_por_idade

assert sc.part_6(part_6())


# **Q7.** Quais jogadores tem potencial para fazerem gols mais bonitos? (chip_shot_trait == True, avoids_using_weaker_foot_trait == True).

# In[73]:


def part_7():
    jogadores_mais_chances_golacos = pd.DataFrame(df, columns=['full_name', 'chip_shot_trait', 'avoids_using_weaker_foot_trait'])
    jogadores_mais_chances_golacos =jogadores_mais_chances_golacos.sort_values(by=['chip_shot_trait', 'avoids_using_weaker_foot_trait'], ascending=False)
    jogadores_mais_chances_golacos =jogadores_mais_chances_golacos[jogadores_mais_chances_golacos.chip_shot_trait != False]
    jogadores_mais_chances_golacos =jogadores_mais_chances_golacos[jogadores_mais_chances_golacos.avoids_using_weaker_foot_trait != False]
    jogadores_mais_chances_golacos_nomes = jogadores_mais_chances_golacos['full_name']
    return jogadores_mais_chances_golacos_nomes

assert sc.part_7(part_7())

