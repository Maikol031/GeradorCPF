"""
Calculo do primeiro dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF
multiplicando cada um dos valores por uma
contagem regressiva começando de 10

Ex.:  746.824.890-70 (746824890)
   10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0
   70  36 48 56 12 20 32 27 0

Somar todos os resultados: 
70+36+48+56+12+20+32+27+0 = 301
Multiplicar o resultado anterior por 10
301 * 10 = 3010
Obter o resto da divisão da conta anterior por 11
3010 % 11 = 7
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
"""


"""
Calculo do segundo dígito do CPF
CPF: 746.824.890-70
Colete a soma dos 9 primeiros dígitos do CPF,
MAIS O PRIMEIRO DIGITO,
multiplicando cada um dos valores por uma
contagem regressiva começando de 11
Ex.:  746.824.890-70 (7468248907)
   11 10  9  8  7  6  5  4  3  2
*  7   4  6  8  2  4  8  9  0  7 <-- PRIMEIRO DIGITO
   77 40 54 64 14 24 40 36  0 14
Somar todos os resultados:
77+40+54+64+14+24+40+36+0+14 = 363
Multiplicar o resultado anterior por 10
363 * 10 = 3630
Obter o resto da divisão da conta anterior por 11
3630 % 11 = 0
Se o resultado anterior for maior que 9:
    resultado é 0
contrário disso:
    resultado é o valor da conta
O segundo dígito do CPF é 0
"""

#gerador de cpf

import re
import sys
import random

nove_digitos =''
for i in range(9):
    nove_digitos += str(random.randint(0,9))


# excluir_pontos =  re.sub(r'[^0-9]', '', cpf_usuario)

# sem_sequencia = cpf_usuario==cpf_usuario[0]*len(cpf_usuario)

# if sem_sequencia:
#         print('Seu cpf tem dados sequenciais reptidos')
#         sys.exit()
    

# nove_digitos = excluir_pontos[:9]



regressivo_10 = 10
soma = 0
for digito in nove_digitos:
    soma += int(digito)*regressivo_10
    regressivo_10 -= 1



multdig1 = soma*10
restodig1 = multdig1%11


primeiro_digito = 0 if restodig1 > 9 else restodig1


segundo_cpf = nove_digitos + str(primeiro_digito)


regressivo_11 = 11
soma2 = 0
for digito2 in segundo_cpf:
    soma2 += int(digito2)*regressivo_11
    regressivo_11 -= 1

multdig2 = soma2*10
restodig2 = multdig2%11

segundo_digito = 0 if restodig2 > 9 else restodig2


terceiro_cpf = segundo_cpf + str(segundo_digito)


print(terceiro_cpf)


# if terceiro_cpf == excluir_pontos:
#     print(f'O Cpf {terceiro_cpf} é VALIDO!!!')

# else:
#     print(f'O Cpf {terceiro_cpf} é INVALIDO!!!')