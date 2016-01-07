# -*- coding: utf-8 -*-
"""
    Faça um Programa que pergunte quanto você ganha por hora e o 
    número de horas trabalhadas no mês. Calcule e mostre o total do 
    seu salário no referido mês.
"""

valor = float(input("Digite o seu valor por hora: "))
hora = float(input("Digite quantas horas você trabalha por mês: "))

print("O seu salário é de: R${:.2f}" .format(valor * hora))