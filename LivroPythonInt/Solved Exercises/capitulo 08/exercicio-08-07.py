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
# Arquivo: exercicios_resolvidos\capitulo 08\exercicio-08-07.py
##############################################################################
def mdc(a,b):
    if b == 0:
        return a
    return mdc(b, a % b)

print("MDC 10 e 5 --> %d" % mdc(10,5))
print("MDC 32 e 24 --> %d" % mdc(32,24))
print("MDC 5 e 3 --> %d" % mdc(5,3))

