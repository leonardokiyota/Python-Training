##############################################################################
# Parte do livro Introdução à Programação com Python
# Autor: Nilo Ney Coutinho Menezes
# Editora Novatec (c) 2010-2014
# Primeira edição - Novembro/2010 - ISBN 978-85-7522-250-8
# Primeira reimpressão - Outubro/2011
# Segunda reimpressão - Novembro/1012
# Terceira reimpressão - Agosto/2013
# Segunda edição - Junho/2014 - ISBN 978-85-7522-408-3
# Site: http://python.nilo.pro.br/
# 
# Arquivo: exercicios_resolvidos\capitulo 06\exercicio-06-13.py
##############################################################################
T=[-10,-8,0,1,2,5,-2,-4]
mínima = T[0] # A escolha do primeiro elemento é arbitrária, poderia ser qualquer elemento válido
máxima = T[0]
soma = 0
for e in T:
    if e < mínima:
        mínima = e
    if e > máxima:
        máxima = e
    soma = soma + e
print("Temperatura máxima: %d °C" % máxima)
print("Temperatura mínima: %d °C" % mínima)
print("Temperatura média: %d °C" % (soma / len(T)))

