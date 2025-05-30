# Crie uma função que calcule a idade de uma pessoa em dias, baseada no ano de nascimento.

import datetime

def calcular_idade_em_dias(ano_nascimento):

    ano_atual = datetime.datetime.now().year
    idade_em_dias = (ano_atual - ano_nascimento) * 365

    print(idade_em_dias)

calcular_idade_em_dias(1998)

# def calcular_idade_em_dias_completo(ano,mes,dia):

#     data_nascimento = datetime.date(ano,mes,dia)
#     data_atual = datetime.date.today()
#     idade_em_dias = (data_atual - data_nascimento).days

#     print(idade_em_dias)

# calcular_idade_em_dias_completo(1998,2,2)