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
# Arquivo: exercicios_resolvidos\capitulo 05\exercicio-05-10.py
##############################################################################
pontos = 0
questão = 1
while questão <= 3:
     resposta = input("Resposta da questão %d: " % questão)
     if questão == 1 and (resposta == "b" or resposta == "B"):
         pontos = pontos + 1
     if questão == 2 and (resposta == "a" or resposta == "A"):
         pontos = pontos + 1
     if questão == 3 and (resposta == "d" or resposta == "D"):
         pontos = pontos + 1
     questão += 1
print("O aluno fez %d ponto(s)" % pontos)
