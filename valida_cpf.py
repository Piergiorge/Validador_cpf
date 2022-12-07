"""
Validador de CPF
Usa o algoritmo da receita federal para verificar se um determinado CPF é válido
"""
import re


def gerador_cpf(temp_cpf, contador):
    """
    Função que cria o décimo e décimo primeiro dígito do CPF
    """
    soma = 0
    for num in temp_cpf:
        assert isinstance(num, object)
        soma += contador * int(num)
        contador -= 1
    resto = (soma * 10) % 11
    return resto if resto <= 9 else 0


cpf = input('Digite o CPF: ')
cpf = re.sub(r'[^0-9]',
             '',
             cpf)
entrada_sequencial = cpf[0] * len(cpf)
print('=-' * 40)
if cpf.isnumeric() and len(cpf) == 11 and entrada_sequencial != cpf:
    cpf_nove = cpf[:9]
    resto_1 = gerador_cpf(cpf_nove, 10)
    cpf_dez = cpf[:10]
    resto_2 = gerador_cpf(cpf_dez, 11)
    cpf_novo = cpf_nove + str(resto_1) + str(resto_2)
    print(f'O cpf {cpf} é válido!' if cpf_novo == cpf else f'O cpf {cpf} não é válido --- {cpf_novo}!')
else:
    print('Input inválido! Digite 11 números!')
print('=-' * 40)
