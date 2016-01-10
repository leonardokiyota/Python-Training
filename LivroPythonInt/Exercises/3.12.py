#!/usr/bin/enc python3
# -*- encoding: utf-8 -*-
'''
   Escreva um programa que calcule o tempo de uma viagem de carro.
   Pergunte a distância a percorrer e a velocidade média esperada para a
   viagem.
'''

dist = float(input("Digite a distância: "))
velo = int(input("Digite a velocidade máxima permitida: "))

print("O tempo de viagem a distância de %.2f Km numa velocidade de %d Km/h é de %d hora(s). "%(dist, velo,(dist / velo)))
