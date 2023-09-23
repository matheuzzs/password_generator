"""
@author matheus dias

---Português---
Script para validar Cadastro de Pessoas Físicas (CPF)

O script avalia os sequintes requisitos:

a. Formatação do CPF (XXX.XXX.XXX-XX)
b. Dígito verificador 1
c. Dígito verificador 2
d. Se o CPF possui todos os números iguais

---English---
Script to validate Individual Taxpayer Registration (CPF)

The script evaluates the following requirements:

The. CPF formatting (XXX.XXX.XXX-XX)
B. Selected digit 1
w. Selected digit 2
d. If the CPF has all the same numbers

"""

import re

def verifica_digito1(cpf):
    """
    Verifica o primeiro dígito de verificação de um CPF brasileiro.

    Argumentos:
        cpf (str): O número do CPF em forma de string.

    Retorna:
        bool: True se o primeiro dígito de verificação for válido, False caso contrário.
    """
    numeros = [int(digito) for digito in cpf if digito.isdigit()]
    soma_produtos = sum(a * b for a, b in zip(numeros[0:9], range(10, 1, -1)))
    digito_esperado = (soma_produtos * 10 % 11) % 10
    return numeros[9] == digito_esperado

def verifica_digito2(cpf):
    """
    Verifica o segundo dígito de verificação de um CPF brasileiro.

    Argumentos:
        cpf (str): O número do CPF em forma de string.

    Retorna:
        bool: True se o segundo dígito de verificação for válido, False caso contrário.
    """
    numeros = [int(digito) for digito in cpf if digito.isdigit()]
    soma_produtos1 = sum(a * b for a, b in zip(numeros[0:10], range(11, 1, -1)))
    digito_esperado1 = (soma_produtos1 * 10 % 11) % 10
    return numeros[10] == digito_esperado1

def verificador_cpf():
    """
    Valida um CPF brasileiro com base no formato e dígitos de verificação.
    """
    cpf = input("Entre com um CPF: > ")

    numeros = [int(digito) for digito in cpf if digito.isdigit()]

    numeros_iguais = len(set(numeros)) == 1
    formatacao = re.match(r'\d{3}\.\d{3}\.\d{3}-\d{2}', cpf)
    quant_digitos = len(numeros) == 11
    validacao1 = verifica_digito1(cpf)
    validacao2 = verifica_digito2(cpf)

    if quant_digitos and formatacao and validacao1 and validacao2 and not numeros_iguais:
        print(f"O CPF {cpf} é válido.")
    else:
        print(f"CPF {cpf} inválido")

verificador_cpf()
