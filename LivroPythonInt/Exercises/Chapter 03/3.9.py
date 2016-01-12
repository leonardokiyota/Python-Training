#!/usr/bin/env python3
# -*- encoding: utf-8 -*-
'''
   Escreva um programa que leia a qtd de dias, horas, min e seg do user.
   Calcule o total em segundos
'''
dia = int(input("Digite quantos dias: "))
horas = int(input("Digite quantas hora: "))
minut = int(input("Digite quantos minutos: "))
seg = int(input("Digite quantos segundos: "))

print("%d dias, %d horas, %d minutos, %d segundos correspondem a %d segundos. "%(dia, horas, minut, seg, (dia * 24 * 3600) + (horas * 3600) + (minut * 60) + seg))
