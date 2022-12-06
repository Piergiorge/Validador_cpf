import random


def criar_cpf():
    """
    Cria um CPF aleatório com 9 dígitos:return:
    """
    string_cpf = ''
    for i in range(9):
        num: int = random.randint(00, 9)
        string_cpf += str(num)
    return string_cpf


def gerador_cpf(cpf, contador):
    """
    Função que cria o décimo e décimo primeiro dígito do CPF
    :param cpf:
    :param contador:
    :return:
    """
    soma = 0
    for num in cpf:
        assert isinstance(num, object)
        soma += contador * int(num)
        contador -= 1
    return soma


cpf_gerado = criar_cpf()

soma_1 = gerador_cpf(cpf_gerado, 10)

resto_1: int = (soma_1 * 10) % 11
resto_1 = 0 if resto_1 > 9 else resto_1

cpf_dez = cpf_gerado + str(resto_1)

soma_2 = gerador_cpf(cpf_dez, 11)

resto_2: int = (soma_2 * 10) % 11
resto_2 = 0 if resto_2 > 9 else resto_2
cpf_novo = cpf_gerado + str(resto_1) + str(resto_2)

print(f'CPF gerado: {cpf_novo[0:3]}.{cpf_novo[3:6]}.{cpf_novo[6:9]}-{cpf_novo[9:]}')
