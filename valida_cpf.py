"""
Validador de CPF
Usa o algoritmo da receita federal para verificar se um determinado CPF é válido
"""
import re
cpf = input('Digite o CPF: ')
cpf = re.sub(r'[^0-9]',
             '',
             cpf)
entrada_sequencial = cpf[0] * len(cpf)
print('=-' * 40)
if cpf.isnumeric() and len(cpf) == 11 and entrada_sequencial != cpf:
    cpf_nove = cpf[:9]
    soma_1 = 0
    multi_1 = 10
    for numero in cpf_nove:
        soma_1 += multi_1 * int(numero)
        multi_1 -= 1
    resto_1: int = (soma_1 * 10) % 11
    resto_1 = 0 if resto_1 > 9 else resto_1
    cpf_dez = cpf[:10]
    soma_2 = 0
    multi_2 = 11
    for numero in cpf_dez:
        soma_2 += multi_2 * int(numero)
        multi_2 -= 1
    resto_2: int = (soma_2 * 10) % 11
    resto_2 = 0 if resto_2 > 9 else resto_2
    cpf_novo = cpf_nove + str(resto_1) + str(resto_2)
    print(f'O cpf {cpf} é válido!' if cpf_novo == cpf else f'O cpf {cpf} não é válido!')
else:
    print('Input inválido! Digite 11 números!')
print('=-' * 40)
