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
# Arquivo: exercicios_resolvidos\capitulo 08\exercicio-08-11.py
##############################################################################
def valida_string(s,mín,máx):
    tamanho = len(s)
    return mín <= tamanho <= máx

print(valida_string("", 1,5))
print(valida_string("ABC", 2,5))
print(valida_string("ABCEFG", 3,5))
print(valida_string("ABCEFG", 1,10))




