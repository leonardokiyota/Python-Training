# -*- coding: utf-8 -*-
"""
    Contagem de questões corretas pag. 90
"""

pontos = 0
question = 1

while question <= 3:
    resp = input("Resposta da questão {} : ".format(question))

    if question == 1 and resp == "b":
        pontos = pontos + 1

    if question == 2 and resp == "a":
        pontos = pontos + 1

    if question == 3 and resp == "d":
        pontos = pontos + 1

    question += 1

print("O aluno fez {} ponto(s)." .format(pontos))