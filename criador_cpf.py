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


cpf_gerado = criar_cpf()

resto_1 = gerador_cpf(cpf_gerado, 10)
cpf_dez = cpf_gerado + str(resto_1)

resto_2 = gerador_cpf(cpf_dez, 11)
cpf_novo = cpf_gerado + str(resto_1) + str(resto_2)
print(f'CPF gerado: {cpf_novo[0:3]}.{cpf_novo[3:6]}.{cpf_novo[6:9]}-{cpf_novo[9:]}')
