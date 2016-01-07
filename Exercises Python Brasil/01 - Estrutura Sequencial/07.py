# -*- coding: utf-8 -*-
"""
    Faça um Programa que calcule a área de um quadrado, em seguida mostre o dobro 
    desta área para o usuário.
"""

lado = float(input("Digite o lado do quadrado: "))
print("O quadrado de lado {} possui uma área de {} e o seu dobre é {}"
      .format(lado, lado * lado, lado * lado * 2 ))
