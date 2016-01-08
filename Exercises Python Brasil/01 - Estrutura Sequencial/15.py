# -*- coding: utf-8 -*-
"""
    Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metros 
    quadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litro para 
    cada 3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$ 80,00. 
    Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.
"""

import math

tamanho = float(input("Informe a metragem gradrada a ser pintada: "))
lata = (tamanho / 3) / 18


print("Para pintar {:.2f} mt² precisam de {} lata(s) e sairá por R$ {:.2f} Reais" .format(tamanho, math.ceil(lata),  math.ceil(lata) * 80 ))